# Automated Litter Detection System

A simple Flask web app that detects garbage in uploaded images using Google Gemini, extracts GPS location from image EXIF metadata, and displays detection results on a Leaflet map.

## Features

- Upload an image using a browser form
- Use Gemini API to classify whether the image contains garbage or waste
- Extract GPS coordinates from image EXIF metadata
- Display detection status and location on a Leaflet map

## Project structure

- `code/app.py` - Flask backend application
- `code/index.html` - Frontend page with upload form and Leaflet map
- `code/uploads/` - Folder where uploaded images are saved

## Prerequisites

- Python 3.8 or newer
- Internet access for Gemini API requests and OpenStreetMap tiles
- A Google Gemini API key

## Installation

1. Open a terminal in the project folder:
   ```powershell
   cd "d:/vaibhav gupta/Coding/PROJECTS/Automated Litter Detection/Automated-Litter--detection-System/code"
   ```

2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install required packages:
   ```powershell
   pip install flask google-generativeai pillow exifread
   ```

## Configuration

1. Open `code/app.py`.
2. Replace `YOUR_API_KEY` in the Gemini configuration section with your actual API key:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

## Running the app

From the `code` directory, run:

```powershell
python app.py
```

The app will start in debug mode and listen on `http://127.0.0.1:5000`.

## Using the app

1. Open `http://127.0.0.1:5000` in a browser.
2. Select an image file and click **Upload & Detect**.
3. The app will return JSON with:
   - `status`: whether garbage was detected
   - `description`: Gemini's response
   - `lat` and `lon`: extracted GPS coordinates (if available)
4. If garbage is detected and GPS data exists, the map will center on the photo location and show a marker.

## Notes

- The image must contain GPS EXIF metadata for the map marker to work.
- If the uploaded image has no location data, the app still returns detection results but cannot plot a map marker.
- The app currently uses Gemini to classify images and is not optimized for production usage.

## Troubleshooting

- `No file uploaded` / `No selected file`: ensure you choose a valid image file.
- `alert("No GPS data found in image...")`: the uploaded image has no GPS EXIF metadata.
- Gemini API errors: verify the API key and network connectivity.

## Optional improvement ideas

- Add a `requirements.txt` for dependency management
- Secure the API key via environment variables
- Support multiple image uploads and history tracking
- Deploy with a production-ready WSGI server
