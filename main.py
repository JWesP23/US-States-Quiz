import turtle
import pandas
import tkinter

FONT = ("Courier", 10 ,"normal")

states = pandas.read_csv("50_states.csv")   #file contains list of states and coordinates on map
num_states_guessed = 0                      #tracks the number of states which the user has named
states_guessed = []                         #gets filled with names of the states the user has listed
states_missed_dict = {"States Missed" : []} #Filled with names of states the user missed (if any) at the end of the quiz

#Screen using turtle
screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.addshape("blank_map_img.gif")
screen.setup(height=700, width=800)

#Need Access to tk object underlying turtle.Screen()
# noinspection PyProtectedMember
root = screen._root

#Create an Entry widget
entry = tkinter.Entry(root, width= 50, border= True, borderwidth= 2)
entry.place(x= 100, y= 85)

#Create a prompt and a counter
prompt = tkinter.Label(root, text= "Please enter a state name (Enter \"Exit\" to quit): ")
prompt.place(x= 100, y= 60)
counter = tkinter.Label(root, text= f"{num_states_guessed}/50 States Correct")
counter.place(x= 550, y= 85)

#map for background
US_map = turtle.Turtle()
US_map.shape("blank_map_img.gif")

writing_turtle = turtle.Turtle(visible= False)
writing_turtle.penup()
writing_turtle.color("black")

##Used to get coordinates for states, leaving in incase necessary in future
'''def get_click_location(x, y):
    print(x,y)

turtle.onscreenclick(fun= get_click_location)'''


guessing = True
guess = ""

#Format entry input
def get_guess(event):
    global guess
    guess = entry.get().strip().title()
    check_guess(guess)

#check if the entry is a state
def check_guess(state_name):
    if state_name in states.state.values and state_name not in states_guessed:
        states_guessed.append(state_name)

        #clear entry field
        entry.delete(0,tkinter.END)

        #append counter and guessed_states array
        global num_states_guessed
        num_states_guessed += 1
        guessed_state = states[states.state == guess]
        counter.config(text= f"{num_states_guessed}/50 States Correct")
        write_state_name(guessed_state)

    #exit on "Exit" and print to missing states file
    elif guess == "Exit":
        if len(states_guessed) != 50:
            global  states_missed_dict
        states_missed_dict["States Missed"] = [state_name for state_name in states.state if state_name not in states_guessed]

        states_missed = pandas.DataFrame(states_missed_dict)
        states_missed.to_csv(path_or_buf= "missed_states.csv")
        root.destroy()


#Write a state's name at its corresponding coordinates
def write_state_name(state):
    writing_turtle.goto(state.x.iloc[0], state.y.iloc[0])
    writing_turtle.write(arg= state.state.iloc[0], align= "center", font= FONT)

#Check entry on every keystroke
entry.bind("<KeyRelease>", get_guess)

root.mainloop()