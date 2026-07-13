# Nucleus AI

**An offline AI voice companion for rural education and curiosity-driven learning.**

Nucleus AI is a cost-effective offline voice assistant designed for communities with limited or unreliable internet access. Running entirely on a Raspberry Pi 5, it enables students and families to ask questions naturally and receive educational, conversational, and practical responses without relying on cloud services.

---

## Problem Statement

Millions of students in rural India have limited access to quality educational resources due to unreliable internet connectivity and limited digital infrastructure.

Nucleus AI aims to bridge this gap by providing an affordable offline AI companion that can:
- Answer educational questions.
- Encourage curiosity and exploration.
- Explain concepts in simple language.
- Assist with short speeches, gratitude messages, and everyday conversations.
- Operate locally without sending user data to external servers.

---

## Vision

Our goal is to make AI accessible beyond urban classrooms.

Instead of replacing teachers, Nucleus AI serves as an always-available learning companion that encourages curiosity, self-learning, and confidence while remaining affordable enough to be deployed in schools, libraries, and community learning centers.

---

# Features

- Offline speech-to-text using Whisper
- Offline local LLM inference
- Offline text-to-speech
- Voice-first interaction
- Educational explanations
- General knowledge assistance
- Short speeches and conversational responses
- Privacy-first (no cloud dependency)

---

# Current Hardware

- Raspberry Pi 5
- HDMI Display
- USB Audio (Headset / Microphone)
- Speaker / Earphones
- Power Supply
- microSD Card

### Planned Hardware

- Push Button (Push-to-Talk)
- Camera Module
- GPIO Integration
- Battery-powered portable enclosure

---

# Software Stack

- Python
- llama.cpp
- Local Quantized Language Model
- Faster Whisper
- Piper TTS
- FastAPI
- Electron
- Raspberry Pi OS

---

# System Workflow

```
User
   │
   ▼
Voice Input
   │
   ▼
Whisper Speech-to-Text
   │
   ▼
Local Language Model
   │
   ▼
Educational Response
   │
   ▼
Piper Text-to-Speech
   │
   ▼
Speaker
```

---

# Progress So Far

- ✅ Raspberry Pi environment configured
- ✅ Offline LLM successfully running
- ✅ Whisper speech recognition integrated
- ✅ Piper offline speech synthesis integrated
- ✅ Voice interaction pipeline functional
- ✅ Initial Raspberry Pi deployment completed
- 🔄 Hardware integration in progress

---

# Next Steps

- Integrate push-to-talk hardware button
- Optimize response latency on Raspberry Pi
- Add educational conversation modes
- Build a cleaner user interface
- Add camera-based learning assistance
- Package into a portable classroom-ready device

---

# Project Goals

Nucleus AI is designed around four principles:

- **Offline First** – Works without internet.
- **Affordable** – Built using low-cost hardware.
- **Educational** – Encourages curiosity through conversation.
- **Accessible** – Simple voice interaction for all age groups.

---

# Raspberry Pi Prototype

[Hardware](image.png)


---

# Future Applications

- Rural schools
- Village libraries
- Community learning centers
- STEM education
- Self-learning companion
- Digital literacy initiatives

---

# Team

**Nucleus AI**
An offline AI companion built to make learning more accessible, affordable, and curiosity-driven.

Check out the [Design Specifications](design.md) and [Project Architecture](architecture.md).


## Acknowledgements
This prototype builds upon the open-source Pocket AI project and has been adapted for the Nucleus AI educational voice assistant prototype.
