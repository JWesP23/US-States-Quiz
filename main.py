import turtle
import pandas

FONT = ("Courier", 10 ,"normal")

screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.addshape("blank_map_img.gif")
screen.setup(height=600, width=800)

US_map = turtle.Turtle()
US_map.shape("blank_map_img.gif")

writing_turtle = turtle.Turtle(visible= False)
writing_turtle.penup()
writing_turtle.color("black")

'''def get_click_location(x, y):
    print(x,y)

turtle.onscreenclick(fun= get_click_location)'''

states = pandas.read_csv("50_states.csv")
num_states_guessed = 0
states_guessed = []
guessing = True

def get_guess():
    #Take and format input
    answer = screen.textinput(title= f"{num_states_guessed}/50 States Correct", prompt= "Please enter a state name (Enter \"Exit\" to quit): ").strip()
    return answer.title()

def check_guess(state_name):
    if state_name in states.state.values and state_name not in states_guessed:
        states_guessed.append(state_name)
        return True
    return False

def write_state_name(state):
    writing_turtle.goto(state.x.iloc[0], state.y.iloc[0])
    writing_turtle.write(arg= state.state.iloc[0], align= "center", font= FONT)

while guessing:

    guess = get_guess()

    if guess == "Exit":
        break

    if check_guess(guess) is True:
        guessed_state = states[states.state == guess]
        num_states_guessed += 1
        write_state_name(guessed_state)


    if num_states_guessed >= 50:
        guessing = False

states_missed_dict = {"States Missed" : []}

if len(states_guessed) != 50:
    states_missed_dict["States Missed"] = [state_name for state_name in states.state if state_name not in states_guessed]

    states_missed = pandas.DataFrame(states_missed_dict)
    states_missed.to_csv(path_or_buf= "missed_states.csv")

turtle.mainloop()