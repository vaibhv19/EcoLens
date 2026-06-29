# Automated Litter Detection System

A prototype Flask web app for detecting litter, garbage, and street hazards in uploaded images. The app uses Google Gemini for AI analysis, extracts GPS location from image EXIF metadata, and displays alerts on a Leaflet map.

## Features

- Upload a photo from a browser
- AI-based analysis for garbage / litter / dead animal detection
- Extract GPS from image EXIF metadata
- Store recent alerts in-memory for prototype review
- Live Leaflet map with location markers for detected issues
- Frontend dashboard with alert summary and response details

## Project structure

- `code/app.py` - Flask backend application
- `code/index.html` - Frontend dashboard and map UI
- `code/uploads/` - Saved uploaded image files
- `requirements.txt` - Python dependency list
- `.env` - Environment variables for Gemini API key

## Prerequisites

- Python 3.8 or newer
- Internet access for Gemini API calls and OpenStreetMap tiles
- Google Gemini API key

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

3. Install dependencies:
   ```powershell
   pip install -r ..\requirements.txt
   ```

## Configuration

1. Create a `.env` file in the `code` folder if it does not already exist.
2. Add your Gemini API key to `.env`:
   ```ini
   GEMINI_API_KEY=your_real_api_key_here
   ```

## Running the app

From the `code` directory, start the Flask app:

```powershell
python app.py
```

Open the browser at `http://127.0.0.1:5000`.

## How to use

1. Navigate to the homepage.
2. Upload an image containing street litter, trash, or other hazards.
3. The prototype will analyze the image and return a structured result.
4. If location EXIF data exists, the app will place a marker on the map.
5. Recent alerts appear in the dashboard panel and are available via `/alerts`.

## API endpoints

- `GET /` - Load the frontend dashboard
- `POST /upload` - Upload an image and analyze it
- `GET /alerts` - Get the current in-memory alert list

## Notes

- GPS EXIF metadata is required for map pin placement.
- Alerts are stored only in memory and reset when the server restarts.
- The app is a prototype and not production hardened.
- The frontend uses Leaflet and OpenStreetMap tiles for mapping.

## Troubleshooting

- `RuntimeError: Set GEMINI_API_KEY in .env before starting the app.`
  - Ensure `.env` exists and contains `GEMINI_API_KEY`.
- `No file uploaded` / `No selected file`
  - Make sure you choose a valid image before submitting.
- No marker appears on the map
  - The uploaded photo likely lacks GPS EXIF coordinates.
- Gemini API failures
  - Check the API key and network connectivity.

## Future improvements

- Persist alerts to a database instead of memory
- Add image preview and multiple-upload support
- Add user authentication for cleanup teams
- Improve AI prompt quality and custom training
- Add dark mode and better mobile responsiveness
