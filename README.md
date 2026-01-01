# 📺 ASCIImator — Real-Time ASCII Video Player

**ASCIImator** is a Python-based multimedia application that converts video frames into **real-time ASCII art** and renders them inside a Pygame window, with optional **synchronized audio playback**.

This project demonstrates practical skills in **computer vision**, **multimedia systems**, and **real-time rendering**, packaged as a clean, self-contained application.

---

## 🚀 Overview

ASCIImator reads a video file frame-by-frame, converts each frame into grayscale, maps pixel intensities to ASCII characters, and displays the result live. Audio can be played alongside the video to create a complete retro-style viewing experience.

This project focuses on:
- Real-time performance
- Clear algorithmic design
- Practical use of Python multimedia libraries

---

## ✨ Features

- 🎞 **Real-time video-to-ASCII conversion**
- 🔊 **Optional audio synchronization**
- 🖥 **Live rendering using Pygame**
- ⚙️ **Configurable resolution and font size**
- 🎨 Custom grayscale-to-ASCII character mapping

---

## 🛠 Tech Stack

- **Language:** Python 3  
- **Libraries:**
  - `opencv-python` – video capture and frame processing  
  - `pygame` – window rendering and audio playback  
  - `numpy` – efficient numerical operations  

---

## 📁 Project Structure
```
ASCIImator/
│
├── app.py # Main application logic
├── vid6.mp4 # Sample video file (user-provided)
├── 1.mp3 # Sample audio file (user-provided)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/aryan-r03/ASCIImator.git
cd ASCIImator
```
---

##(Optional) Create a virtual environment
### Linux / macOS
```
python3 -m venv venv
source venv/bin/activate
```

### Windows
python -m venv venv
venv\Scripts\activate

---

## Install dependencies
```
pip install -r requirements.txt
```

---

## Running the Application
```
python app.py
```
---

## Customization
###You can control output quality and behavior directly from the configuration section in app.py:
```
VIDEO_PATH = "vid6.mp4"
AUDIO_PATH = "1.mp3"     # Set to None to disable audio
CHAR_WIDTH = 100         # ASCII output width (higher = more detail)
FONT_SIZE = 10           # Font size for rendering

```
---
### 🧠 How It Works (High-Level)
```
Capture video frames using OpenCV
Resize and convert frames to grayscale
Map pixel intensity to ASCII characters
Render ASCII text in a Pygame window
Synchronize audio playback (if enabled)
```
### 🔮 Future Improvements
```
Frame-rate adaptive rendering
Terminal-based (CLI) ASCII output
Color ASCII mode
Performance optimizations for large videos
Unit tests and CI integration
```
### 📌 Learning Outcomes
```
Real-time video processing with OpenCV
ASCII rendering algorithms
Multimedia synchronization
Structuring Python projects for GitHub
```
### 📜 License
```
Licensed under the MIT License.
```
Free to use, modify, and distribute.
