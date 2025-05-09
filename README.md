# Rock-Paper-Scissors-Game

A classic Rock-Paper-Scissors game available in multiple implementations - from simple command-line to graphical interfaces with images. Challenge the computer to this timeless game of chance and strategy.

## Demonstration

[![Rock-Paper-Scissors Demo](https://img.youtube.com/vi/oZ5eidRpXmg/0.jpg)](https://www.youtube.com/watch?v=oZ5eidRpXmg)

## Overview

This project offers four versions of the Rock-Paper-Scissors game with increasing complexity and features:

1. **Command-Line Version** (Rock-Paper-Scissors-v1.py): Text-based interface
2. **Basic GUI Version** (Rock-Paper-Scissors-v2.py): Simple Tkinter interface with buttons
3. **Enhanced GUI with Images** (Rock-Paper-Scissors-v3.py): Adds visual representation of choices
4. **Advanced GUI with User/Computer Images** (Rock-Paper-Scissors-v4.py): Distinct images for player vs computer

## Features

- Player vs Computer gameplay
- Random computer choice selection
- Win/lose/tie determination
- Multiple interface options
- Visual feedback (in GUI versions)
- Replay functionality (in command-line version)

## Game Versions

### Command-Line Version (Rock-Paper-Scissors-v1.py)

A simple text-based implementation where players type their choices.

- **Features:**
  - Text-based interface
  - Input validation
  - Play again option
  - Clear result display

### Basic GUI Version (Rock-Paper-Scissors-v2.py)

A graphical implementation using Tkinter with button-based interaction.

- **Features:**
  - Button interface for selection
  - Real-time result display
  - Clean layout

### Enhanced GUI with Images (Rock-Paper-Scissors-v3.py)

Adds visual representations of rock, paper, and scissors choices.

- **Features:**
  - All features of the basic GUI
  - Visual display of chosen items
  - Requires image files (rock.png, paper.png, scissors.png)

### Advanced GUI with User/Computer Images (Rock-Paper-Scissors-v4.py)

Uses distinct images for player and computer choices for better visual distinction.

- **Features:**
  - Separate image sets for player and computer
  - Clearer visual feedback
  - Requires 6 image files (user_rock.png, computer_rock.png, etc.)

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)
- PIL/Pillow (for GUI versions with images)
  ```
  pip install pillow
  ```

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```
   pip install pillow
   ```
3. For versions with images (sps3.py, sps4.py), ensure image files are in the same directory as the script

## How to Run

### Command-Line Version
```
python Rock-Paper-Scissors-v1.py
```

### GUI Versions
```
python Rock-Paper-Scissors-v2.py
# or
python Rock-Paper-Scissors-v3.py
# or
python Rock-Paper-Scissors-v4.py
```

## Image Requirements

### For Rock-Paper-Scissors-v3.py
- rock.png
- paper.png
- scissors.png

### For Rock-Paper-Scissors-v4.py
- user_rock.png
- user_paper.png
- user_scissors.png
- computer_rock.png
- computer_paper.png
- computer_scissors.png

## Game Rules

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

## Future Improvements

- Score tracking
- Best of N games option
- Additional choices (Rock-Paper-Scissors-Lizard-Spock)
- Animation effects
- Sound effects
