import random
from art import logo, vs
from game_data import data

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_it(user_guess, follower_A, follower_B):
    if follower_A > follower_B:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
is_continue = True

print(logo)

account_A = random.choice(data)

while is_continue:
    account_B = random.choice(data)
    
    while account_A == account_B:
        account_B = random.choice(data)
    
    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Against B: {format_data(account_B)}")
    
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    follower_A = account_A["follower_count"]
    follower_B = account_B["follower_count"]
    
    is_correct = check_it(user_guess, follower_A, follower_B)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.\n")
        account_A = account_B
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_continue = False
