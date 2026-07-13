# Nucleus AI Design

## Design Objectives

The system is designed around the following engineering principles:

- Offline-first operation
- Modular architecture
- Low resource utilization
- Maintainability
- Extensibility
- Fast voice interaction

Each subsystem performs a single responsibility and communicates through well-defined interfaces, allowing components to be replaced independently.

---

# Software Architecture

```
┌────────────────────────────────────────────┐
│                 Main Loop                  │
└────────────────────────────────────────────┘
                    │
                    ▼
          Audio Input Module
                    │
                    ▼
        Speech Recognition Module
                    │
                    ▼
          Prompt Builder Module
                    │
                    ▼
          LLM Inference Module
                    │
                    ▼
       Response Processing Module
                    │
                    ▼
          Text-to-Speech Module
                    │
                    ▼
             Audio Output Module
```

---

# Module Responsibilities

## Audio Input

Responsibilities:

- Capture microphone input
- Normalize audio
- Store temporary recordings
- Trigger speech recognition

Input:
- User speech

Output:
- WAV audio stream

---

## Speech Recognition

Responsibilities:

- Convert speech to text
- Handle transcription errors
- Return cleaned transcript

Input:
- Audio recording

Output:
- Plain text query

---

## Prompt Builder

Responsibilities:

- Combine system prompt
- Append conversation history
- Insert latest user message
- Format prompts for llama.cpp

Output:

```
System Prompt

Conversation History

Current User Query
```

---

## Inference Module

Responsibilities:

- Load quantized GGUF model
- Execute token generation
- Apply sampling parameters
- Return generated response

This module remains isolated from user interface logic.

---

## Response Processor

Responsibilities:

- Remove unnecessary whitespace
- Limit excessively long outputs
- Prepare text for speech synthesis

This stage ensures responses remain concise for spoken interaction.

---

## Text-to-Speech

Responsibilities:

- Receive generated response
- Generate speech waveform
- Return playable audio

---

## Audio Output

Responsibilities:

- Play synthesized speech
- Release temporary resources
- Return system to listening state

---

# Control Flow

The application follows a sequential processing pipeline.

1. Capture speech
2. Transcribe speech
3. Construct prompt
4. Generate response
5. Convert response to speech
6. Play audio
7. Wait for next interaction

This design minimizes synchronization complexity and simplifies debugging.

---

# Configuration

Runtime parameters are separated from application logic.

Example configuration values include:

- Model path
- Whisper model
- Piper voice
- Context length
- Temperature
- Thread count
- Maximum generation length

Centralizing configuration simplifies tuning without modifying source code.

---

# Error Handling

Each module validates its input before execution.

Typical failure scenarios include:

- Microphone unavailable
- Empty transcription
- Model loading failure
- Audio playback failure

Errors are handled locally where possible to prevent complete application termination.

---

# Scalability

The modular structure supports future extensions without major architectural changes.

Potential additions include:

- Wake-word detection
- Camera input
- Local document retrieval
- Multiple language support
- Plugin-based educational tools

---

# Design Considerations

The application favors predictable execution over maximum throughput.

Trade-offs include:

- Sequential processing instead of concurrent pipelines
- Smaller language model for reduced memory usage
- Short responses to improve interaction speed
- Local execution in place of cloud services

These choices align with the project's deployment target of Raspberry Pi 5.
