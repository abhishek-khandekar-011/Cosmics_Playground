import random


def deal_cards():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} & current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_input = input("Enter y to draw another card or n to pass: ").lower()
            if user_input == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    def compare(uscore, cscore):
        if uscore == cscore:
            return "Draw"
        elif uscore == 0:
            return "Blackjack! You win"
        elif cscore == 0:
            return "Computer wins with Blackjack"
        elif uscore > 21:
            return "You went over. You lose"
        elif cscore > 21:
            return "Computer went over. You win"
        else:
            return "You lose" if uscore < cscore else "You win"

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))



play_game()

while input("Do you want to play again? Enter y: ").lower() == "y":
    print("\n" * 20)
    play_game()

