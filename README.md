# Nucleus AI

> **An Offline Voice-First Educational Assistant powered entirely by On-Device AI on Raspberry Pi 5.**

<!-- INSERT: Hero image of the complete Raspberry Pi setup -->

Nucleus AI is an offline educational voice assistant designed for communities with limited or unreliable internet connectivity. Built for Raspberry Pi 5, it combines on-device speech recognition, local Large Language Model (LLM) inference, and offline speech synthesis into a complete voice-first learning companion.

Unlike conventional AI assistants that depend on cloud services, **Nucleus AI performs the entire AI pipeline locally**, preserving user privacy while remaining affordable and accessible for schools, libraries, and community learning centres.

---

# Problem Statement

Millions of students in rural India face limited access to quality educational resources due to unreliable internet connectivity and limited digital infrastructure.

Modern AI assistants are powerful but often require continuous internet access, making them impractical in many low-resource environments.

Nucleus AI addresses this challenge by providing an affordable offline educational assistant capable of answering questions, explaining concepts, encouraging curiosity, and supporting everyday learning without transmitting user data to external servers.

---

# Solution Overview

Nucleus AI integrates multiple open-source AI technologies into a unified edge AI system running completely on Raspberry Pi 5.

The complete interaction pipeline is shown below.

```
                 User

                   │

                   ▼

         Speech Recognition
        (Faster Whisper STT)

                   │

                   ▼

      Prompt Engineering Layer

                   │

                   ▼

   Local LLM Inference (llama.cpp)

                   │

                   ▼

     Educational Response Generation

                   │

                   ▼

     Offline Speech Synthesis (Piper)

                   │

                   ▼

               Speaker Output
```

<!-- INSERT: architecture diagram -->


---

# On-Device AI

Nucleus AI was specifically designed around the principles of Edge AI.

| Component | Implementation |
|------------|----------------|
| Speech Recognition | Faster Whisper |
| Language Model | Edge-Quant Nanbeige4.1 3B Q4_K_M GGUF |
| Inference Engine | llama.cpp |
| Speech Synthesis | Piper TTS |
| Backend | FastAPI |
| Frontend | Electron |
| Hardware | Raspberry Pi 5 |

---

# Engineering Contributions

Although inspired by the open-source Pocket AI project, Nucleus AI was significantly redesigned and adapted into a dedicated educational voice assistant.

The primary engineering contributions focus on **edge deployment, prompt engineering, model optimisation, and system integration** rather than model training.

---

## Model Selection

Original implementation

- Small general-purpose language model

Current implementation

- **Edge-Quant Nanbeige4.1 3B Q4_K_M GGUF**

Reasons for selection:

- Better educational conversations
- Improved reasoning quality
- Efficient CPU inference
- Optimised memory footprint
- Compatible with llama.cpp
- Suitable for Raspberry Pi deployment

---

# Engineering Decisions

The primary engineering challenge of Nucleus AI was not training a new language model, but selecting, integrating, and optimising existing open-source AI components to deliver reliable offline performance on resource-constrained hardware.

Every major design decision was made by considering the trade-offs between response quality, inference speed, memory usage, deployment simplicity, and usability.

| Design Decision | Choice | Engineering Rationale |
|----------------|--------|-----------------------|
| Edge Hardware | Raspberry Pi 5 | Low-cost platform capable of running modern AI models entirely offline |
| Speech Recognition | Faster Whisper | Higher transcription accuracy and robust offline performance compared to lighter alternatives |
| Inference Engine | llama.cpp | Efficient CPU inference with native GGUF support and ARM optimisation |
| Language Model | Edge-Quant Nanbeige4.1 3B Q4_K_M | Strong conversational quality while remaining practical for Raspberry Pi deployment |
| Model Format | GGUF | Optimised for llama.cpp inference and low-overhead loading |
| Quantisation | Q4_K_M | Significantly reduces RAM usage with minimal quality degradation |
| Offline Architecture | Fully Local | Eliminates cloud dependency while improving privacy and accessibility |
| Backend | FastAPI | Lightweight API for coordinating speech and inference pipelines |
| Frontend | Electron | Cross-platform desktop interface with rapid prototyping capability |

---

# Inference Optimisation

The language model was manually tuned to balance response quality, latency, and memory consumption on Raspberry Pi 5.

| Parameter | Value | Engineering Rationale |
|-----------|------:|----------------------|
| Context Window | **2048** | Maintains conversational context while remaining within Raspberry Pi memory constraints |
| CPU Threads | **4** | Utilises all Raspberry Pi CPU cores for inference |
| Temperature | **0.5** | Produces consistent educational responses while reducing hallucinations |
| Top-p | **0.9** | Maintains natural conversational diversity without sacrificing stability |
| Maximum Tokens | **180** | Keeps spoken responses concise and reduces inference time |
| Streaming Output | **Enabled** | Reduces perceived latency by displaying generated tokens immediately |
| Automatic Model Download | **Enabled** | Simplifies deployment and avoids bundling large model files in the repository |

These parameters were selected through iterative testing to optimise the balance between:

- Response quality
- Conversational consistency
- CPU utilisation
- Memory footprint
- Deployment simplicity
- User experience

---

## Educational Prompt

The original coding-assistant behaviour was completely replaced.

A new system prompt was engineered to:

- explain concepts using simple English
- encourage curiosity-driven learning
- provide concise spoken responses
- generate speeches and educational content
- reduce hallucinations by explicitly admitting uncertainty
- avoid unnecessary technical complexity
- maintain a friendly conversational personality

This optimisation improves response quality for voice interaction and educational use.

---

## Raspberry Pi Optimisation

The inference pipeline was tuned specifically for Raspberry Pi 5.

| Parameter | Value | Engineering Rationale |
|-----------|------:|----------------------|
| Model | Nanbeige4.1 3B Q4_K_M | Improved educational response quality |
| Quantisation | Q4_K_M | Reduced memory usage while maintaining quality |
| Context Window | 2048 | Balances conversational memory with RAM constraints |
| CPU Threads | 4 | Utilises all Raspberry Pi CPU cores |
| Temperature | 0.5 | Improves consistency and reduces hallucinations |
| Top-p | 0.9 | Maintains natural conversational diversity |
| Max Tokens | 180 | Produces concise spoken responses |
| Streaming | Enabled | Improves perceived responsiveness on CPU inference |

---

## Deployment Optimisations

Several engineering improvements were introduced to simplify deployment and improve usability.

- Automatic model download using Hugging Face Hub
- Local GGUF model loading
- Streaming token generation for reduced perceived latency
- Offline speech recognition
- Offline speech synthesis
- Unified FastAPI backend
- Electron desktop interface

These changes reduce installation complexity while maintaining complete offline functionality after setup.

---

## System Integration

The project combines several independent AI components into a single end-to-end application.

- Faster Whisper
- llama.cpp
- Quantized GGUF model
- Piper TTS
- FastAPI
- Electron
- Raspberry Pi hardware

The engineering challenge focused on integrating these components into a seamless voice-first interaction pipeline suitable for low-resource hardware.

---

# Features

- Fully offline AI assistant
- Voice-first interaction
- Educational explanations
- General knowledge assistance
- Story generation
- Speech preparation
- Gratitude message generation
- Natural conversations
- Privacy-first architecture
- Raspberry Pi deployment
- Low-cost edge AI solution

---

# Hardware

Current hardware

- Raspberry Pi 5
- USB Headset (Microphone + Speaker)
- HDMI Display
- Keyboard & Mouse
- microSD Card

Planned hardware

- Push-to-Talk GPIO Button
- Camera Module
- Battery Pack
- Portable Enclosure

<!-- INSERT: Raspberry Pi hardware image -->

---

# Software Stack

- Python
- FastAPI
- Electron
- llama.cpp
- Faster Whisper
- Piper
- Hugging Face Hub
- GGUF Quantized Models
- Raspberry Pi OS

---

# Repository Structure

```
Nucleus-AI/

├── app.py
├── chat_ai.py
├── stt_whisper.py
├── tts_piper.py
├── requirements.txt
├── architecture.md
├── design.md
├── roadmap.md
├── README.md
├── chat-gui/
└── images/
```

---

# Setup

## Clone Repository

```bash
git clone https://github.com/AnushkaLal/Nucleus-AI.git

cd Nucleus-AI
```

## Create Virtual Environment

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
python app.py
```

---

## Launch Electron Frontend

```bash
cd chat-gui

npm install

npm run dev
```

---

# Usage

1. Launch the backend.
2. Open the Electron application.
3. Speak naturally into the microphone.
4. Whisper converts speech into text.
5. The local LLM generates an educational response.
6. Piper converts the response into speech.
7. The spoken response is played through the speaker.

---

# Demonstration

Demo Video

**(Insert YouTube / Google Drive / Loom link after recording)**

---

# Screenshots

## Raspberry Pi Prototype

<!-- INSERT IMAGE -->

---

## Electron Interface

<!-- INSERT IMAGE -->

---

## Voice Conversation

<!-- INSERT IMAGE -->

---

## System Architecture

<!-- INSERT IMAGE -->

---

# Use Cases

Nucleus AI can support learning in various environments including:

- Rural schools
- Village libraries
- Community learning centres
- Home learning
- STEM education
- Digital literacy initiatives
- Offline educational assistance

---

# Future Scope

- GPIO Push-to-Talk button
- Camera-assisted visual learning
- Image understanding
- Subject-specific tutoring
- Multi-language support
- Conversation memory optimisation
- Portable battery-powered deployment

---

# Known Limitations

- Current prototype primarily supports English interactions.
- CPU inference on Raspberry Pi is slower than GPU-based cloud inference.
- Response quality depends on the selected language model.
- Camera-assisted learning remains under active development.

---

# Why Nucleus AI?

Nucleus AI demonstrates that modern AI assistants do not need expensive cloud infrastructure to provide meaningful educational assistance.

By combining efficient open-source speech recognition, quantized language models, prompt engineering, and offline speech synthesis, the project delivers a privacy-preserving educational assistant capable of running entirely on affordable edge hardware.

---

# Documentation

Additional documentation:

- [architecture.md](architecture.md)
- [design.md](design.md)
- [roadmap.md](roadmap.md)

---

# Acknowledgements

This project was initially based on the open-source **Pocket AI** project.

Nucleus AI significantly extends and adapts the original work by:

- redesigning the assistant for educational use
- engineering a new educational system prompt
- replacing the original language model
- tuning inference parameters for Raspberry Pi deployment
- integrating an offline speech pipeline
- optimising deployment for edge hardware
- focusing on low-cost, privacy-preserving AI for education

---

# License

MIT License
