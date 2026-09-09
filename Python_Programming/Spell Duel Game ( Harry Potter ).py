import random
spells = ["Expelliarmus", "Stupefy", "Protego", "Expecto Patronum", "Avada Kedavra"]
rules = {
    "Expelliarmus": ["Stupefy", "Avada Kedavra"],     # Disarms stun & deadly curses
    "Stupefy": ["Protego", "Expecto Patronum"],       # Stuns shield & weakens Patronus
    "Protego": ["Expelliarmus", "Avada Kedavra"],     # Shields against disarming & curses
    "Expecto Patronum": ["Expelliarmus", "Protego"],  # Patronus outshines shield & disarm
    "Avada Kedavra": ["Stupefy", "Expecto Patronum"]  # Dark curse overpowers stun & Patronus
}

print("Welcome to the Harry Potter Spell Duel!")
print("Choose your spell:")
for i, spell in enumerate(spells, 1):
    print(f"{i}. {spell}")

player_choice = input("\nEnter your spell: ").title()

if player_choice not in spells:
    print(" Invalid spell! Choose carefully, young wizard.")
else:
    computer_choice = random.choice(spells)
    print(f"\nYou cast: {player_choice}")
    print(f"Computer casts: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a draw! Both spells clash in sparks of magic.")
    elif computer_choice in rules[player_choice]:
        print("You win the duel!  Your magic prevails.")
    else:
        print("You lost the duel! The computer's spell was stronger.")
