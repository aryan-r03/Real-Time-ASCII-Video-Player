# 📺 ASCIImator: Real-Time ASCII Video Player

## 🚀 Overview

**ASCIImator** is a unique Python-based multimedia project that converts video streams into an ASCII art representation, rendering them in real-time within a Pygame window. It includes robust functionality for synchronizing and playing a separate audio file alongside the visual output, offering a complete, retro multimedia experience.

This project showcases expertise in:
* **Computer Vision (OpenCV):** Efficient frame processing, resizing, and grayscale conversion.
* **Multimedia Programming (Pygame):** Window management, display rendering, and precise audio playback synchronization.
* **Algorithm Design:** Implementing the custom pixel-to-ASCII conversion logic for visual accuracy.

## ✨ Key Features

* **Real-Time Conversion:** Converts video frames to an array of ASCII characters frame-by-frame.
* **Audio Synchronization:** Supports loading and playing a separate audio file (e.g., `1.mp3`) alongside the video stream.
* **Configurable Resolution:** The ASCII output width and font size are easily customizable to match various display needs.
* **Grayscale Mapping:** Uses a custom character set (`.:;+=*#@MW$`) to map pixel intensity to ASCII characters.

## 🛠️ Tech Stack

| Category | Tools & Libraries | Purpose |
| :--- | :--- | :--- |
| **Language** | Python | Core logic and execution. |
| **Video Processing** | `opencv-python` (CV2) | Capturing video, reading frames, resizing, and grayscale conversion. |
| **Multimedia/Display** | `pygame` | Window creation, rendering ASCII text, and audio playback. |
| **Numerical** | `numpy` | Efficient array manipulation for image processing. |

## 📁 Project Structure

Assuming your main Python file is named `app.py`:
ASCIImator/ ├── app.py # Main video processing and Pygame execution logic ├── vid6.mp4 # Example Video File (To be supplied by the user) ├── 1.mp3 # Example Audio File (To be supplied by the user) └── README.md # Project documentation (This file) └── requirements.txt # List of required Python dependencies

## ⚙️ Setup and Installation

### 1. Clone the Repository

~~~bash
# Update the URL below with your actual repository link
git clone [https://github.com/aryan-r03/ASCIImator.git](https://github.com/aryan-r03/ASCIImator.git) 
cd ASCIImator
~~~

## Create and Activate a Virtual Environment
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Run the Application
python app.py


## Customization
if __name__ == "__main__":
    VIDEO_PATH = "vid6.mp4"
    AUDIO_PATH = "1.mp3"  # Set to None if no audio is desired
    CHAR_WIDTH = 100       # Controls the ASCII art horizontal resolution
    FONT_SIZE = 10         # Controls the size of the characters in the Pygame window
    
    # ... (function call)
