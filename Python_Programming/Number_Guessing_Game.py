import random

HARD_TURNS = 5
EASY_TURNS = 10
def check(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    
    guess = 0

    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        turns = check(guess, answer, turns)

        if guess == answer:
            break
        elif turns == 0:
            print(f"You've run out of guesses. The number was {answer}. Game over.")
            break
        else:
            print("Guess again.")

game()
while True:
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay == "yes":
        game()
    else:
        print("Thanks for playing!")
        break
