import turtle
import pandas

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()


# record the correct guesses in a list
correct_answers = []


# use a loop to allow the user to keep guessing
while len(correct_answers) < 50:
    # keep track of score
    score = len(correct_answers)

    # Convert the guess to Title Case
    answer_state = screen.textinput(
        title=f"{score}/50 Guess the State", prompt="What's another state's name?"
    ).title()

    # Check if the guess is among the 50 states
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        correct_answers.append(answer_state)
        state_data = data[data.state == answer_state]
        # select the x and y and then pass into the class to write the state on screen.
        position = (state_data.x.item(), state_data.y.item())
        # write correct guess onto the map
        writer.goto(position)
        writer.write(answer_state)

# states_to_learn
states_to_learn = []
for state in state_list:
    if state not in answer_state:
        states_to_learn.append(state)

print(states_to_learn)
