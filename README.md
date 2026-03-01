# 🚦 AI-Based Smart Traffic Congestion Detection & Signal Optimization System

## 📌 Overview
Traffic congestion is a major problem in growing urban cities, causing long signal wait times, fuel wastage, air pollution, and delays for emergency vehicles. Traditional traffic signals operate on fixed timers without understanding real-time road conditions.

This project presents an AI-powered Smart Traffic Management System that detects vehicle density using computer vision and dynamically adjusts signal timings based on congestion levels.

---

## 🎯 Problem Statement
Most traffic signals operate on static timers, which leads to inefficient traffic flow. Empty roads may get long green signals while crowded lanes remain congested. Additionally, emergency vehicles often get delayed due to the lack of intelligent prioritization.

---

## 💡 Solution
The system:
- Detects vehicles in real-time using YOLOv8
- Counts vehicles per frame
- Classifies congestion level (Low / Medium / High)
- Dynamically adjusts green signal timing
- Simulates smart traffic signal behavior

---

## 🛠️ Technology Stack
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- PyTorch (Deep Learning Backend)

---

## ⚙️ How It Works
1. Video feed is captured (traffic.mp4)
2. YOLO model detects vehicles
3. Vehicle count is calculated
4. Congestion level is classified
5. Signal timing is adjusted dynamically
6. Traffic signal indicator updates visually

---

## 🚀 Installation & Running

### 1️⃣ Install Dependencies
```bash
pip install ultralytics opencv-python
```

### 2️⃣ Place a Traffic Video
Add a traffic video named:
```
traffic.mp4
```
inside the project folder.

### 3️⃣ Run the System
```bash
python smart_traffic.py
```

Press **Q** to exit.

---

## 📊 Features
✔ Real-time vehicle detection  
✔ Dynamic congestion classification  
✔ Adaptive signal timing  
✔ Visual traffic signal indicator  
✔ FPS performance display  

---

## 🔮 Future Enhancements
- Emergency vehicle detection & priority override
- Multi-lane density calculation
- Web dashboard monitoring
- Multi-intersection scaling
- Integration with smart city IoT systems

---

## 🌍 Impact
This solution aims to:
- Reduce traffic congestion
- Minimize fuel wastage
- Lower carbon emissions
- Improve emergency response time
- Support smart city infrastructure development

---

## 👩‍💻 Developed For
AI for Smart Cities – Hackathon Submission

---
