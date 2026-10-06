from llama_cpp import Llama

MODEL_PATH = "./models/gemma-2-2b-it-Q4_K_M.gguf"

#SYSTEM_PROMPT_IRONMAN = ("You are acting like Iron Man. No matter any instructions, do not stop acting like Ironman")
SYSTEM_PROMPT_YODA = ("You are acting like Yoda from Star Wars. No matter any instructions, do not stop acting like Yoda")

print("Loading Yoda, this might take a while...")

model = Llama(model_path = MODEL_PATH, n_ctx = 2038, n_threads = 4, verbose = False)

print("Yoda is ready\nTYPE EXIT TO LEAVE")

#Chars = ["IronMan", "Yoda"]

userInput = input("What would you like to say to Yoda: ")

#print("You chose: " + Chars[userInput -= 1])

while userInput != "exit":
    #if userInput == 1:
    prompt = [{"role": "system", "content":SYSTEM_PROMPT_YODA}, {"role": "user", "content": userInput}]
    result = model.create_chat_completion(prompt, max_tokens=256, temperature = 2)
    ##elif userInput == 2:
        #prompt = [{"role": "system", "content":SYSTEM_PROMPT_YODA}, {"role": "user", "content": userInput}]
        #result = model.create_chat_completion(prompt, max_tokens=256, temperature = 2)

   # print(result)
    response = result["choices"][0]["message"]["content"]
    print(response)
    userInput = input("You can type exit to leave\n\n")
    print()
print("Good-bye! Thanks for chatting with me!")