# U.S. States Map Quiz

A Python-based interactive quiz game where users try to name all 50 U.S. states. When a user correctly guesses a state, its name is written on a blank U.S. map at the appropriate location. The game uses the `turtle` graphics module for the interface and `pandas` for data handling.

## Features

- Displays a blank U.S. map as the background
- Prompts the user to guess state names via text input
- Correct guesses are labeled on the map
- Keeps track of total correct answers out of 50
- Saves a list of missed states to `missed_states.csv` for later review

## Requirements

- Python 3.7 or later
- `pandas` library
- `turtle` (included with Python)

## Setup and Running

1. Clone or download the repository.

2. Make sure the following files are present in the same directory as the Python script:
   - `blank_states_img.gif`: the map image
   - `50_states.csv`: a CSV containing state names and their corresponding x/y coordinates

3. Install pandas if it's not already installed:

```bash
pip install pandas
python us_states_quiz.py
```

Files: 
  - main.py: The main game script
  - 50_states.csv: State names and screen coordinates
  - blank_map_img.gif: U.S. map image used by the turtle module
  - missed_states.csv: Generated at the end of a session if any states were missed
