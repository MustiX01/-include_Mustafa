import sys

# Define colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def greeting_app():
    print("--- AI Greeting App (Type 'exit' to stop) ---")
    
    while True:
        user_input = input("\nYou: ").lower().strip()
        
        if user_input == "exit":
            print("Goodbye! 👋")
            break
        
        elif "hello" in user_input or "hi" in user_input:
            print(f"{GREEN}Hello there! It is wonderful to meet you! 😊{RESET}")
            
        elif "how are you" in user_input:
            print(f"{GREEN}I'm doing fantastic, thank you for asking! 🌟{RESET}")
            
        elif "how old are you" in user_input:
            print(f"{RED}I don't have a birthday, I am just code. 🤖🥀{RESET}")
            
        elif "how is the weather" in user_input:
            # Weather can be tricky, let's assume it's a bit gloomy for the "negative" requirement
            print(f"{RED}It looks a bit cloudy and gray today. ☁️😔{RESET}")
            
        else:
            print(f"{RED}I'm not sure how to answer that yet, but I'm learning! 📚 {RESET}")

if __name__ == "__main__":
    greeting_app()