import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

# print(answer_state)


# print(data["state"])
# print(data["x"])
# print(data["y"])

while len(guessed_states) < len(all_states) :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct" , 
                                    prompt="What's another state's name?").title()

    #print(answer_state)

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        # another way instead the 4 lines of code above
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        #print("Your're right")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(answer_state) #t.write(state_data.state.item())
        guessed_states.append(answer_state)
    






# for state in all_states:
#     if answer_state == state:
#         print("Your're right")


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()



