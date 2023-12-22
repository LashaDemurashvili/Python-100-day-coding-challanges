import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. - States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


# find coordinates in turtle screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# use pandas module
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()  # convert all state to list
guessed_states = []

while len(guessed_states) < 50:
    prompt = turtle.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Enter the state's name").title()
    if prompt in states_list:  # check if prompt is in list
        guessed_states.append(prompt)

        answer = data[data['state'] == prompt]
        x = data[data['state'] == prompt].x
        y = data[data['state'] == prompt].y

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(x), int(y))
        t.write(prompt)

    # break code and save missing states as a .csv file
    elif prompt == "Exit":
        missing_states = []
        all_states = states_list
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                # appended only missing states

        # create new csv file with new list
        new_dict = {"Missing states": [missing_states]}
        data = pandas.DataFrame(new_dict)
        data.to_csv('Missing states.csv')
        break




# screen.exitonclick()

