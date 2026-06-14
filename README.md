# 🔐 Prodigy InfoTech — Cyber Security Internship

**Intern:** Veer Nagadwala
**Domain:** Cyber Security
**Duration:** 1 June 2026 – 30 June 2026

---

## 👋 About This Repository

This repository contains all the tasks I completed during my Cyber Security internship at Prodigy InfoTech.

Each task is a mini project that helped me understand a real concept in cybersecurity — from basic encryption and password security to keylogging and network traffic analysis. All projects are written in Python and are meant for learning purposes.

---

## 📁 Tasks

| # | File | What it does |
|---|------|--------------|
| Task 1 | [PRODIGY_CS_01_Caesar_Cipher.py](./PRODIGY_CS_01_Caesar_Cipher.py) | Encrypt and decrypt messages using the classic Caesar Cipher |
| Task 2 | [PRODIGY_CS_02_Image_Encryption.py](./PRODIGY_CS_02_Image_Encryption.py) | Encrypt and decrypt images by manipulating pixel values |
| Task 3 | [PRODIGY_CS_03_Password_Strength_Checker.py](./PRODIGY_CS_03_Password_Strength_Checker.py) | Check how strong a password is and get tips to improve it |
| Task 4 | [PRODIGY_CS_04_Keylogger.py](./PRODIGY_CS_04_Keylogger.py) | A basic keylogger that records keystrokes to understand how they work |
| Task 5 | [PRODIGY_CS_05_Network_Packet_Analyzer.py](./PRODIGY_CS_05_Network_Packet_Analyzer.py) | Capture and display live network packets on your machine |

---

## ⚙️ Setup & Requirements

Make sure you have Python installed, then install the required libraries:

```bash
pip install pillow pynput scapy
```

| Library | Used in |
|---------|---------|
| `pillow` | Task 2 — Image processing |
| `pynput` | Task 4 — Keyboard listener |
| `scapy` | Task 5 — Packet capturing |

Tasks 1 and 3 use only built-in Python libraries — no installation needed!

---

## ▶️ How to Run Each Task

**Task 1 — Caesar Cipher**
```bash
python PRODIGY_CS_01_Caesar_Cipher.py
```
Enter a message and a shift number to encrypt or decrypt.

---

**Task 2 — Image Encryption**
```bash
python PRODIGY_CS_02_Image_Encryption.py
```
Choose to encrypt or decrypt, provide your image path, and enter a key (0–255).
Use the same key to get your original image back!

---

**Task 3 — Password Strength Checker**
```bash
python PRODIGY_CS_03_Password_Strength_Checker.py
```
Type any password and get an instant strength score (out of 5) with feedback on how to improve it.

---

**Task 4 — Keylogger**
```bash
python PRODIGY_CS_04_Keylogger.py
```
Starts recording keystrokes and saves them to `keylog.txt`.
Press **ESC** to stop the logger.

---

**Task 5 — Network Packet Analyzer**
```bash
# Windows: Run as Administrator
# Linux/Mac: use sudo
sudo python PRODIGY_CS_05_Network_Packet_Analyzer.py
```
Captures live IP packets and saves details to `packet_log.txt`.
Press **CTRL+C** to stop.

---

## ⚠️ Ethical Disclaimer

Tasks 4 and 5 involve sensitive techniques (keylogging and packet sniffing). These are built **purely for educational purposes** as part of this internship curriculum.

- Only run these on your **own devices and networks**
- Never use them on someone else's device or network without permission
- Unauthorized use of these tools is **illegal**

Understanding how attacks work is the first step to defending against them. That's the whole point of studying cybersecurity!

---

## 🏢 About the Internship

This internship was offered by **Prodigy InfoTech**.
Visit: [https://prodigyinfotech.dev](https://prodigyinfotech.dev)
