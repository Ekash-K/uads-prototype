# Unauthorized Access Detection System (Prototype)

## Overview

This project is a Computer Vision–based prototype designed to simulate an **unauthorized access monitoring system**. It uses a webcam to detect human faces in real time and automatically captures an image whenever a face is detected, labeling it as a potential intruder.

The system demonstrates how basic vision-based surveillance can be implemented and extended into real-world security applications.

---

## Problem Statement

Unauthorized access to personal computers or workstations poses a security risk. Traditional systems rely on passwords or authentication, but they do not provide visual evidence of access attempts.

---

## Proposed Solution

This project implements a **real-time face detection system** that:

* Monitors the webcam feed continuously
* Detects human faces using a pre-trained model
* Labels detected faces as **"Unknown User"**
* Captures and stores images as evidence

---

## Features

* Real-time face detection using OpenCV
* Automatic intruder image capture
* Cooldown mechanism to avoid repeated captures
* Timestamp-based file naming
* On-screen status display (face count, alerts)
* Organized storage in a dedicated folder

---

## Technologies Used

* Python
* OpenCV (Computer Vision library)
* Haar Cascade Classifier (pre-trained model)

---

## Project Structure

```
project/
│
├── main.py              # Main application file
├── captures/            # Folder storing captured images
└── README.md            # Project documentation
```

---

## Installation & Setup

### Step 1: Create environment (Anaconda)

```
conda create -n cv_project python=3.9
conda activate cv_project
```

### Step 2: Install dependencies

```
pip install opencv-python
```

---

## How to Run

```
python main.py
```

* The webcam will start automatically
* Detected faces will be highlighted
* Images will be saved in the `captures/` folder
* Press **ESC** to exit

---

## Output

* Images are saved in the format:

```
captures/intruder_<timestamp>.jpg
```

* Terminal logs display alerts:

```
[ALERT] Intruder detected. Image saved: captures/intruder_XXXXXXXX.jpg
```

---

## Key Concepts Used

* Image preprocessing (grayscale conversion)
* Object detection (face detection using Haar Cascade)
* Event-triggered automation
* File handling and timestamping

---

## Limitations

* All detected faces are treated as "unknown"
* No actual face recognition or user verification
* Runs as a standalone application (not integrated with OS events like system wake or login)

---

## Future Improvements

* Integrate face recognition to distinguish authorized users
* Connect with system login/wake triggers
* Add email/SMS alerts
* Store logs in a database
* Improve detection using deep learning models

---

## Conclusion

This project demonstrates a simple yet effective application of Computer Vision in security systems. While implemented as a prototype, it provides a foundation for building more advanced surveillance and authentication solutions.

---
