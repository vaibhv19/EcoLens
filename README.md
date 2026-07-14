# EcoLens

A prototype Flask application that detects litter, waste, or dead-animal hazards in uploaded images using Google Gemini. The app extracts GPS metadata from images, displays detected issues on a Leaflet map, and shows a dashboard of recent alerts.

## Features

- Upload an image from a browser
- AI-based detection for garbage, litter, and dead animals
- Structured alert generation with severity and status
- Extract GPS coordinates from EXIF metadata
- Live Leaflet map with detected issue markers
- In-memory alert history for prototype review
- Responsive dashboard with latest analysis output

## Repository structure

- `code/app.py` - Flask backend and Gemini integration
- `code/index.html` - Frontend dashboard, upload form, and map UI
- `code/uploads/` - Stored uploaded images
- `requirements.txt` - Python dependencies
- `.env` - Local environment variables for API keys

## Getting started

### Prerequisites

- Python 3.8 or newer
- Internet access for Google Gemini API and OpenStreetMap tiles
- Google Gemini API key

### Install dependencies

Open a terminal in the repository root and run:

```powershell
cd code
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r ..\requirements.txt
```

### Configure environment

Create a `.env` file inside the `code/` folder with:

```ini
GEMINI_API_KEY=your_real_api_key_here
```

### Run locally

From the `code/` directory:

```powershell
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

## Usage

1. Open the homepage.
2. Select an image file.
3. Click **Analyze Image**.
4. Review the generated alert output and map marker.
5. Recent alerts appear in the dashboard and are available at `/alerts`.

## API endpoints

- `GET /` — Load the frontend dashboard
- `POST /upload` — Upload an image and receive detection results
- `GET /alerts` — Retrieve current in-memory alerts

## Notes

- The location map marker is only available when the uploaded image includes GPS EXIF metadata.
- Alerts are stored in memory and will be reset if the server restarts.
- This repository is intended as a prototype, not a production system.

## Troubleshooting

- `RuntimeError: Set GEMINI_API_KEY in .env before starting the app.`
  - Add `GEMINI_API_KEY` to the `code/.env` file.
- `No file uploaded` / `No selected file`
  - Ensure you choose a valid image before submitting.
- No marker is displayed on the map
  - The image likely does not contain GPS EXIF location data.
- Gemini API request errors
  - Verify your Gemini API key and network connectivity.

## Improvements

- Persist alerts using SQLite or another database
- Add an image preview before upload
- Improve upload validation and duplicate filename handling
- Add a dark theme and better mobile responsiveness
- Add unit tests and CI validation

## License

This project is released under the MIT License.
