import turtle
import pandas
counter = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
pic = "blank_states_img.gif"
state_name = "50_states.csv"
data = pandas.read_csv(state_name)
# print(data)
all_state = data["state"].to_list()
# print(all_state)
screen.addshape(pic)
screen.setup(height=491, width=725)
user_guess = []
turtle.shape(pic)
flag = True
# data["state"] = data["state"].str.lower()
# print(data)
# while flag:
#     answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name")
while flag:
    answer_state = screen.textinput(title=f"{counter}/50 Guess the State",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        flag = False
    state = data["state"]
    list_state = data["state"].to_list()
    if answer_state in data["state"].values and answer_state not in user_guess:
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        x_value = data.loc[data["state"] == answer_state, "x"]
        y_value = data.loc[data["state"] == answer_state, "y"]
        new_turtle.goto(int(x_value), int(y_value))
        new_turtle.write(answer_state)
        user_guess.append(answer_state)
        counter += 1


not_guessed = []
for state in all_state:
    if state not in user_guess:
        not_guessed.append(state)

new_data = pandas.DataFrame(not_guessed)

new_data.to_csv("state_to_learn.csv")
