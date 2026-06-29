import os
import re
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from PIL import Image
import exifread
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Flask app
app = Flask(__name__)

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Set GEMINI_API_KEY in .env before starting the app.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# In-memory alert store for prototype
alerts = []

SUMMARY_PROMPT = (
    "Examine the attached image for garbage, litter, waste, or a dead animal. "
    "If you find a problem, answer with a short structured response using these fields:\n"
    "Found: yes/no\n"
    "Type: garbage / dead animal / none\n"
    "Severity: low / medium / high\n"
    "Alert: yes/no\n"
    "Description: Briefly describe what you see."
)


def get_exif_location(filepath):
    """Extract GPS coordinates from image EXIF metadata."""
    with open(filepath, 'rb') as f:
        tags = exifread.process_file(f)

    def get_decimal_from_dms(dms, ref):
        degrees = float(dms[0].num) / float(dms[0].den)
        minutes = float(dms[1].num) / float(dms[1].den)
        seconds = float(dms[2].num) / float(dms[2].den)
        dec = degrees + minutes / 60 + seconds / 3600
        if ref in ['S', 'W']:
            dec = -dec
        return dec

    try:
        lat = get_decimal_from_dms(tags['GPS GPSLatitude'].values,
                                   tags['GPS GPSLatitudeRef'].values)
        lon = get_decimal_from_dms(tags['GPS GPSLongitude'].values,
                                   tags['GPS GPSLongitudeRef'].values)
        return lat, lon
    except Exception:
        return None, None


def parse_response(text):
    """Parse Gemini response into structured prototype fields."""
    lower = text.lower()

    def field(name, default):
        match = re.search(rf"{name}:\s*(.+)", text, flags=re.IGNORECASE)
        return match.group(1).strip() if match else default

    found = field("Found", "no").lower().startswith("y")
    type_value = field("Type", "none").lower()
    severity = field("Severity", "low").lower()
    alert = field("Alert", "no").lower().startswith("y")
    description = field("Description", text).strip()

    if type_value == "none" and found:
        if "dead animal" in lower:
            type_value = "dead animal"
        elif any(k in lower for k in ["garbage", "litter", "trash", "waste"]):
            type_value = "garbage"

    if severity not in ["low", "medium", "high"]:
        if "high" in lower:
            severity = "high"
        elif "medium" in lower or "moderate" in lower:
            severity = "medium"
        else:
            severity = "low"

    return {
        "found": found,
        "type": type_value,
        "severity": severity,
        "alert": alert or (found and severity in ["medium", "high"]),
        "description": description,
        "raw": text
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    img = Image.open(filepath)
    response = model.generate_content([SUMMARY_PROMPT, img])
    analysis = parse_response(response.text.strip())

    lat, lon = get_exif_location(filepath)
    timestamp = datetime.utcnow().isoformat() + "Z"

    alert_record = {
        "id": len(alerts) + 1,
        "timestamp": timestamp,
        "filename": filename,
        "status": "Alert" if analysis["alert"] else "Review",
        "type": analysis["type"],
        "severity": analysis["severity"],
        "description": analysis["description"],
        "lat": lat,
        "lon": lon,
        "alert": analysis["alert"],
        "raw_response": analysis["raw"]
    }

    if analysis["alert"]:
        alerts.insert(0, alert_record)
        alerts[:] = alerts[:20]

    return jsonify({
        "result": alert_record,
        "alerts": alerts,
        "message": "Alert generated" if analysis["alert"] else "No urgent alert",
    })


@app.route("/alerts")
def get_alerts():
    return jsonify({"alerts": alerts})


if __name__ == "__main__":
    app.run(debug=True)
