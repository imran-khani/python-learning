import random

# Generate random number once
random_num = random.randint(1, 100)

while True:
    try:
        guessed_number = int(input("Enter your guessed number between 1-100: "))
        
        if guessed_number == random_num:
            print(f"🎉 You guessed the correct number: {random_num}")
            break
        elif guessed_number < random_num:
            print("Too low! Try again.")
        elif guessed_number > random_num:
            print("Too high! Try again.")
    except ValueError:
        print("Please enter a valid number.")
