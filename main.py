import turtle
import pandas as pd
import numpy as np

screen = turtle.Screen()
screen.title('US States Game')

image = 'blank_states_img.gif'

screen.addshape(image)

turtle.shape(image)

#  check users answer against states to see if it exists in the list, upper and lower

data = pd.read_csv('50_states.csv')

guessed_states = []
all_states = data['state'].tolist()

score = 0

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{score} /50",
                                    prompt="What is another state name").title()
    if answer_state == 'Exit':

        missed_states = np.setdiff1d(all_states, guessed_states)
        #  need to convert the np array back to pandas before saving as csv
        pd.DataFrame(missed_states).to_csv('states_to_learn.csv')
        break

    if answer_state in data.values:

        guessed_states.append(answer_state)

        score += 1

        get_row = data[data.state == answer_state]

        x = int(get_row['x'])
        y = int(get_row['y'])

        turtle_point = turtle.Turtle()
        turtle_point.hideturtle()
        turtle_point.penup()
        turtle_point.color('black')
        turtle_point.goto(x, y)
        turtle_point.write(f'{answer_state}')



