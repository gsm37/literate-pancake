import pandas
import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"

screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
count = 0
correct_states = []
missing_states = []


def check_answer(answer,count):
    if answer in data["state"].values:
        x = data[data["state"] == answer]["x"].values[0]
        y = data[data["state"] == answer]["y"].values[0]
        coord = (x,y)
        return answer,coord, True
    else:
        print("answer not correct")
        return None, None, False

def write_state(name,coord):
    turtle.up()
    turtle.goto(coord)
    turtle.down()
    turtle.write(name, align="center")
    turtle.hideturtle()

while count < 50:
    answer = screen.textinput(title=f"{count}/50 States Correct",prompt="What's another state's name?")
    if answer == None:
        exit()

    if answer == "exit":
        for x in data["state"].values:
            if x not in correct_states:
                missing_states.append(x)
                print(missing_states)
                missed = {
                    "states": missing_states
                }
                miss = pd.DataFrame(missed)
                miss.to_csv("Missing_states.csv")
        break
    answer = answer.title()

    state, coord, is_correct = check_answer(answer,count)

    if is_correct and state not in correct_states:
        count+=1
        write_state(state,coord)
        correct_states.append(state)

    print(correct_states)

if count == 50:
    print("You Win")
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.write("You Win!", align="center", font=("Verdana",
                                    40, "normal"))



screen.exitonclick()
