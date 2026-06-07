# 🧠🚀 AI-Based Smart Garbage Detection & Mapping System

> An intelligent waste monitoring system using **AI + Geolocation + Interactive Maps** to make cities cleaner and smarter 🌍✨

---

## 📌 Project Overview

This project automates garbage detection using **AI (Gemini Vision)** and maps its exact location using **Leaflet.js**.
It helps municipal authorities identify waste hotspots and respond quickly.

---

## ✨ Key Features

* 🖼️ **AI Garbage Detection** – Detect waste from images using Gemini AI
* 📍 **Auto Location Detection** – Extract GPS via EXIF or browser geolocation
* 🗺️ **Interactive Map** – Visualize garbage locations with Leaflet
* 🚨 **Alert System** – Notify authorities instantly
* ⚡ **Real-Time Processing** – Fast and efficient detection
* 📊 **Scalable System** – Ready for smart city integration

---

## 🏗️ System Architecture

```
Image Input → AI Detection → Location Extraction → Backend Processing → Map Visualization → Alerts
```

---

## 🛠️ Tech Stack

### 🔹 Backend

* Python (Flask)
* Gemini AI (Google Generative AI)

### 🔹 Frontend

* HTML, CSS, JavaScript
* Leaflet.js (Map visualization)

### 🔹 Tools & APIs

* EXIF Metadata Extraction
* REST APIs

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/vaibhv19/
Automated-Litter--detection-System.git
cd garbage-detection-system
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your Gemini API key

```python
genai.configure(api_key="YOUR_API_KEY")
```

### 4️⃣ Run the backend

```bash
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
├── app.py
├── templates/
│   └── index.html
├── static/
├── uploads/
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow

1. User uploads an image
2. System sends image to Gemini AI
3. AI detects garbage
4. Location is extracted (EXIF / GPS)
5. Result is plotted on map
6. Alert is generated

---

## 📸 Screenshots

> Add your screenshots here:

* Upload Interface
* Detection Result
* Map with Pin
* Alert Dashboard

---

## ⚠️ Limitations

* Depends on image quality
* GPS metadata may not always be available
* Requires internet connection

---

## 🚀 Future Enhancements

* 📡 CCTV integration
* 🚁 Drone-based monitoring
* 📱 Mobile application
* 📊 Predictive analytics
* 🧠 Custom-trained AI models

---

## 🌍 Use Cases

* Smart Cities 🏙️
* Municipal Corporations 🏛️
* Public Spaces (parks, roads, stations)
* Large Events & Gatherings 🎪

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Vaibhav Gupta**
B.Tech CSE
Greater Noida Institute of Technology

