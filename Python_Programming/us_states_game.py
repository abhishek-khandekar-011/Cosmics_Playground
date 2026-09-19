import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

# Setup turtle for writing text
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

states_data = {
    "Alabama": (139, -77),
    "Alaska": (-204, -170),
    "Arizona": (-202, -26),
    "Arkansas": (57, -53),
    "California": (-297, 13),
    "Colorado": (-112, 29),
    "Florida": (207, -135),
    "Texas": (-38, -106),
    "New York": (236, 104),
}

guessed_states = []

while len(guessed_states) < len(states_data):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )

    if answer_state is None or answer_state.title() == "Exit":
        break

    answer_formatted = answer_state.title()

    if answer_formatted in states_data and answer_formatted not in guessed_states:
        guessed_states.append(answer_formatted)
        coords = states_data[answer_formatted]
        writer.goto(coords)
        writer.write(answer_formatted)

print(f"Game finished! You guessed: {guessed_states}")
