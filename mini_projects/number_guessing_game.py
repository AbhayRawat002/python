import random

best_score = None

print("Set the difficulty of the game!")

while True:

    try:
        min_value = int(input("Enter the minimum value for numbers range: "))
        max_value = int(input("Enter the maximum value for numbers range: "))

        if min_value == max_value:
            print("Min and Max values can't be the same.")
        elif min_value > max_value:
            print("Min value can't be greater than max value.")
        else:
            break

    except ValueError:
        print("Invalid input! Please enter a number.")

while True:   # GAME LOOP

    random_number = random.randint(min_value, max_value)

    while True:
        try:
            number_of_guesses = int(input("How many attempts do you want? "))
            if number_of_guesses <= 0:
                print("Attempts must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

    attempts = 0

    while attempts < number_of_guesses:

        try:
            guess = int(input(f"Guess a number between {min_value} and {max_value}: "))
            attempts += 1

            if guess > random_number:
                print("Too high! Guess a lower number.")

            elif guess < random_number:
                print("Too low! Guess a higher number.")

            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts!")

                if best_score is None or attempts < best_score:
                    best_score = attempts

                print(f"Best score: {best_score} attempts")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

    if attempts == number_of_guesses and guess != random_number:
        print(f"Out of attempts! The number was {random_number}.")

    # Ask if user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break
    