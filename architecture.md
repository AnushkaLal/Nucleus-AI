# Nucleus AI Architecture

## System Overview

Nucleus AI is an offline voice-first educational assistant designed to operate entirely on a Raspberry Pi 5. The system processes speech locally, performs inference using a quantized language model, and generates spoken responses without requiring internet connectivity.

The architecture prioritizes:

- Low latency
- Low memory footprint
- Privacy
- Cost effectiveness
- Ease of deployment

---

# High-Level Architecture

```
                 User
                   │
                   ▼
           Voice Recording
                   │
                   ▼
        Faster Whisper (STT)
                   │
                   ▼
        Prompt Construction
                   │
                   ▼
      Quantized Local LLM
         (llama.cpp)
                   │
                   ▼
       Response Generation
                   │
                   ▼
         Piper Text-to-Speech
                   │
                   ▼
               Speaker
```

---

# Component Selection

## Speech Recognition

Engine:
- Faster Whisper

Reason:

- Fully offline
- Faster inference than OpenAI Whisper implementation
- Suitable for ARM processors
- Accurate enough for conversational interaction

---

## Language Model

Model:

Nanbeige 4.1 3B (Q4_K_M GGUF)

Reason for selection:

- Fits Raspberry Pi memory limitations
- Good conversational capability
- Quantized for CPU inference
- Compatible with llama.cpp

Alternative models evaluated:

- Qwen 3 0.6B
- TinyLlama
- Phi-2

Nanbeige produced better educational and conversational responses while remaining lightweight enough for edge deployment.

---

## Inference Engine

Framework:

llama.cpp

Reason:

- Optimized for CPU inference
- Native GGUF support
- Efficient memory management
- Raspberry Pi compatible
- No GPU dependency

---

## Text-to-Speech

Engine:

Piper TTS

Reason:

- Fully offline
- Fast synthesis
- Natural sounding voices
- Low CPU utilization

---

# Engineering Parameters

## Context Window

```
n_ctx = 2048
```

Reason:

Provides enough conversational history while maintaining acceptable RAM usage.

Increasing the context window significantly increases memory consumption and inference latency.

---

## Threads

```
n_threads = 4
```

Reason:

The Raspberry Pi 5 contains four high-performance Cortex-A76 cores.

Using four threads maximizes CPU utilization without excessive scheduling overhead.

---

## Temperature

```
temperature = 0.5
```

Purpose:

Controls randomness during generation.

Engineering decision:

Lower temperatures produce more deterministic educational responses while still allowing natural conversation.

---

## Top-p Sampling

```
top_p = 0.9
```

Purpose:

Restricts token sampling to the most probable candidates.

Benefits:

- Improved fluency
- Reduced hallucinations
- More stable responses

---

## Maximum Tokens

```
max_tokens = 150
```

Reason:

Voice assistants should produce concise responses.

Shorter generations improve:

- Response latency
- User experience
- Audio synthesis time

---

# Prompt Engineering

The system prompt defines the assistant's behaviour.

Design goals:

- Educational
- Friendly
- Encourages curiosity
- Simple language
- Short responses
- Suitable for students

Rather than modifying model weights, behaviour is controlled through prompt engineering, allowing rapid iteration without retraining.

---

# Memory Strategy

Conversation history is stored in a rolling message buffer.

Benefits:

- Maintains conversational context
- Supports follow-up questions
- Low implementation complexity

Future work:

Sliding-window context management.

---

# Performance Goals

Target Hardware:

Raspberry Pi 5 (8 GB)

Expected performance:

| Metric | Target |
|---------|---------|
| STT latency | <2 s |
| LLM response | 3–6 s |
| TTS latency | <1 s |
| Internet dependency | None |

---

# Design Decisions

Why quantization?

Using Q4_K_M quantization reduces memory usage while preserving conversational quality.

This enables deployment on inexpensive hardware without dedicated AI accelerators.

---

Why offline inference?

- Privacy
- No recurring API costs
- Works without internet
- Suitable for rural environments

---

# Future Improvements

- Push-to-talk GPIO button
- Camera-assisted educational mode
- Local knowledge base
- Subject-specific tutoring modes
- Adaptive response complexity based on learner age

---

# Engineering Contribution

The primary engineering effort focuses on adapting modern LLM inference to resource-constrained edge hardware.

This includes:

- Selecting an appropriate quantized model
- Optimizing inference parameters
- Prompt engineering for educational dialogue
- Integrating offline speech recognition and synthesis
- Building an end-to-end voice interaction pipeline suitable for Raspberry Pi deployment
