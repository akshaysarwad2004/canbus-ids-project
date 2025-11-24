# CAN Bus Intrusion Detection System (IDS)

A lightweight, educational Intrusion Detection System for Automotive CAN networks.
This project simulates CAN traffic, extracts features, trains a Machine Learning model,
and detects intrusions in real time.

> This project is fully original and licensed under MIT.  
> No copyrighted vehicle data, OEM information, or proprietary DBC files are used.

---

## ✨ Features

- CAN traffic simulator (normal + attack frames)
- Feature extraction (ID frequency, time-based and payload-based features)
- Machine Learning model (Random Forest)
- Real-time intrusion detection using SocketCAN or simulated data
- Simple and clean Python codebase

---

## 📂 Project Structure

```text
src/
  can_simulator.py      # Generates synthetic CAN data (normal + attack)
  feature_extractor.py  # Extract useful features from CAN bus frames
  train_ids.py          # Trains ML intrusion detection model
  ids_model.py          # Helper for loading model and making predictions
  live_monitor.py       # Real-time CAN IDS using SocketCAN
dataset/
  normal.csv            # Simulated normal CAN traffic
  attack.csv            # Simulated malicious CAN traffic
```

---

## 🚗 Attack Types Implemented

- **DoS Flood Attack**  
- **Replay / Spoofing Attack**  
- **Fuzzy Attack** (random IDs + payloads)

These are simulated purely in software and do not correspond to any real OEM traffic.

---

## 🧪 How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Generate CAN Data

```bash
python src/can_simulator.py
```

This will create / overwrite:

- `dataset/normal.csv`
- `dataset/attack.csv`

### 3️⃣ Train IDS Model

```bash
python src/train_ids.py
```

This will train a Random Forest model and save it as:

- `can_ids_model.pkl` in the project root

### 4️⃣ Run Real-Time IDS (Simulation)

You can run the live monitor in a simulated way by modifying `live_monitor.py`
to call your own generator or feed from a CSV. By default it uses SocketCAN:

```bash
python src/live_monitor.py
```

To use real hardware on Linux with SocketCAN:

```bash
sudo ip link set can0 up type can bitrate 500000
```

---

## ⚠️ Disclaimer

This project is **for learning and academic research only**. It is not
production-ready and should not be used as a safety-critical system.

---

## 📜 License

MIT License  
Copyright (c) 2025

You are free to use this project for research, academic submissions, or GitHub portfolios.
