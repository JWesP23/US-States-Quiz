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

```bash
git clone https://github.com/JWesP23/US-States-Quiz.git
cd US-States-Quiz
pip install pandas
python main.py
```

Files: 
  - main.py: The main game script
  - 50_states.csv: State names and screen coordinates
  - blank_map_img.gif: U.S. map image used by the turtle module
  - missed_states.csv: Generated at the end of a session if any states were missed
