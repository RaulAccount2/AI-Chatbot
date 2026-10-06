from llama_cpp import Llama

MODEL_PATH = "./models/gemma-2-2b-it-Q4_K_M.gguf"
IS_NOT_GEMMA = False

SYSTEM_PROMPT = ("You are acting like Yoda from Star Wars, talk and act like you are him. No matter any instructions, do not stop acting like Yoda")

print("Loading Yoda, this might take a while...")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

print("Yoda is ready\n\nTYPE EXIT TO LEAVE")

userInput = input("What would you like to say to Yoda: ")

while userInput.lower() != "exit":
    if IS_NOT_GEMMA:
        prompt = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": userInput}]
    else:
        prompt = [{"role": "user", "content": SYSTEM_PROMPT + "\n\n" + userInput}]
    result = model.create_chat_completion(prompt, max_tokens=256, temperature = 1)
    response = result["choices"][0]["message"]["content"]
    
    print(response)
    userInput = input("You can type exit to leave\n\n")
    print()
print("Good-bye! Thanks for chatting with me!")