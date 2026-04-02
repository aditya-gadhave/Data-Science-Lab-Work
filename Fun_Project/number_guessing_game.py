import random

print("🎮 Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed the number.")
        print("Total attempts:", attempts)
        break
