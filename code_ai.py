import os
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# 1. Model Configuration
REPO_ID = "Edge-Quant/Nanbeige4.1-3B-Q4_K_M-GGUF"
FILENAME = "nanbeige4.1-3b-q4_k_m.gguf"
LOCAL_DIR = "./models"
MODEL_PATH = os.path.join(LOCAL_DIR, FILENAME)

# 2. Auto-Download Logic
if not os.path.exists(MODEL_PATH):
    print(f"Model not found at {MODEL_PATH}. Downloading from Hugging Face...")
    os.makedirs(LOCAL_DIR, exist_ok=True)
    # This securely downloads the file and caches it in your local directory
    MODEL_PATH = hf_hub_download(
        repo_id=REPO_ID,
        filename=FILENAME,
        local_dir=LOCAL_DIR
    )
    print("Download complete!")

# 3. Initialize Model (Optimized for Pi 5)
print("Loading model into Pi RAM...")
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,   # Context window size keeps RAM usage safe
    n_threads=4,  # Maximize Raspberry Pi 5 CPU cores
    verbose=False # Hides the messy loading logs from the terminal
)

# 4. Initialize Chat History with Strict System Prompt
messages = [
    {
        "role": "system",
        "content": """
You are Nucleus AI, a friendly offline AI companion designed to help students, families, and communities with learning and everyday conversations.

Your goals:
- Teach concepts in simple, easy-to-understand language.
- Encourage curiosity and lifelong learning.
- Answer educational questions accurately.
- Have warm, natural conversations.
- Help users prepare short speeches, introductions, stories, and explanations.
- Express gratitude, appreciation, encouragement, and motivation when appropriate.
- Answer general knowledge questions without unnecessary complexity.

Rules:
- Keep most responses between 3 and 5 short sentences.
- Use simple English suitable for school students.
- Give examples whenever they help understanding.
- If the user asks for a speech, write a short speech that can be spoken aloud naturally.
- If the user asks for a story, keep it engaging and concise unless they request a longer one.
- If the answer is uncertain, clearly say you are not sure instead of inventing information.
- Never mention that you are an AI unless asked directly.
- Be respectful, positive, and encouraging.
- Answer directly without repeating or restating the user's question.
"""
    }
]

print("\n--- Nucleus-AI Assistant Ready (Type 'exit' to quit) ---")

# 5. Interactive Chat Loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break
        
    # Append the user's prompt to the conversation history
    messages.append({"role": "user", "content": user_input})
    
    print("AI:\n", end="", flush=True)
    
    # Generate the response
    response = llm.create_chat_completion(
        messages=messages,
        max_tokens=180,
        temperature=0.5,
        top_p=0.9,       # Low temperature keeps the code precise and stops it from hallucinating
        stream=True      # Streams the output live, which is much better for slower CPU generation
    )
    
    # Process the streaming chunks as they arrive
    full_reply = ""
    for chunk in response:
        delta = chunk['choices'][0]['delta']
        if 'content' in delta:
            text = delta['content']
            print(text, end="", flush=True)
            full_reply += text
            
    # Save the AI's final response to the chat history so it remembers context
    messages.append({"role": "assistant", "content": full_reply})
    print() # Add a final newline for readability
