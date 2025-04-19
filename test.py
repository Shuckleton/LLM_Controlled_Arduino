from llama_cpp import Llama

# Path to your model
model_path = "DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored.Q4_K_M.gguf"

# Ensure CUDA is being used
llm = Llama(
    model_path=model_path,
    n_ctx=512,
    n_threads=8,           # Number of CPU threads
    n_gpu_layers=-1,       # Specify how many layers to run on the GPU
    chat_format="llama-3"  # Ensure you use the correct format
)

output = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's 3 + 5?"}
    ],
    max_tokens=20
)

print("Assistant:", output["choices"][0]["message"]["content"])
