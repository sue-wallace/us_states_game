import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US States Game')

image = 'blank_states_img.gif'

screen.addshape(image)

turtle.shape(image)

turt = turtle.Turtle()

#  check users answer against states to see if it exists in the list, upper and lower

data = pd.read_csv('50_states.csv')

game_is_on = True

score = 0

while game_is_on:

    answer_state = screen.textinput(title=f"{score} /50",
                                    prompt="What is another state name").title()

    if answer_state in data.values:

        score += 1

        get_row = data[data.state == answer_state]

        x = int(get_row['x'])
        y = int(get_row['y'])

        turt.penup()
        turt.color('black')
        turt.goto(x, y)
        turt.write(f'{answer_state}')




