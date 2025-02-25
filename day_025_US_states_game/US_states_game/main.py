import turtle
import pandas
import writer

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# use a loop to allow the user to keep guessing
game_is_on == True
while game_is_on == True:

    # Convert the guess to Title Case
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?"
    ).title()

    # Check if the guess is among the 50 states
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()

    # record the correct guesses in a list
    correct_answers = []

    if answer_state in state_list:
        correct_answers.append(answer_state)
        # select the x and y and then pass into the class to write the state on screen.
        position = data[data.x]
        # write correct guess onto the map
        writer(answer_state, position)

        print("true")
    else:
        print("false")

    # keep track of score
    score = len(correct_answers)
