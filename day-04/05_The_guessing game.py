
secret_number = 12
attempts = 0
guessed_correctly = False

while attempts < 5 and not guessed_correctly:

    guess = input("Enter your guess (1 to 20): ")

    # Check whether the input contains digits only
    if not guess.isdigit():
        print("Invalid input! Enter numeric digits only.")

    else:
        # Convert the guess to a whole number
        guess = int(guess)

        # Check whether the number is within range
        if guess < 1 or guess > 20:
            print("Invalid input! Enter a number from 1 to 20.")

        else:
            # Count a valid attempt
            attempts = attempts + 1

            if guess == secret_number:
                print("Correct! You guessed the secret number.")
                guessed_correctly = True

            elif guess < secret_number:
                print("Too low!")

            else:
                print("Too high!")

# Display the result
if not guessed_correctly:
    print("You did not guess correctly.")
    print("The secret number was:", secret_number)

print("Valid attempts used:", attempts)
