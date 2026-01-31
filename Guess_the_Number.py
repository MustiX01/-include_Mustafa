import random

# Color Codes
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"

def play_game():
    secret_number = random.randint(1, 100)
    print("🌡️  I am thinking of a number between 1 and 100.")
    print("Can you guess it? I'll tell you how 'hot' or 'cold' you are!")
    
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            diff = abs(secret_number - guess) # Calculate the distance
            
            if guess == secret_number:
                print(f"{GREEN}🎯 BOOM! You got it in {attempts} tries! 🥳{RESET}")
                break
            
            # Temperature Logic
            if diff <= 2:
                print(f"{RED}🔥 SWELTERING! You're right next to it!{RESET}")
            elif diff <= 5:
                print(f"{RED}♨️  VERY HOT! So close!{RESET}")
            elif diff <= 10:
                print(f"{YELLOW}☀️  Hot! You're getting there.{RESET}")
            elif diff <= 20:
                print(f"{RESET}🌤️  Normal. Not too far, not too close.{RESET}")
            elif diff <= 30:
                print(f"{CYAN}🌬️  A little bit cold.{RESET}")
            elif diff <= 50:
                print(f"{BLUE}❄️  Cold. Keep looking.{RESET}")
            else:
                print(f"{BLUE}🧊 FREEZING! You're miles away.{RESET}")
                
        except ValueError:
            print("Please enter a valid whole number!")

if __name__ == "__main__":
    play_game()