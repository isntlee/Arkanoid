# Arkanoid
 Play a game or two on my Atari arkanoid/breakout clone 

# Features
- Paddle and a ball where the ball can destroy the bricks in a wall
- Simple level and scoring system
- 5 lives initially and 1 life is lost when the ball touches the bottom of the screen
- Game is played with the arrow keys, it ends when lives reach 0

# Requirements
- Created on Python 3.8
- Created using Python library - PyGame
- Developed on Windows 10, so should run on most Windows systems

## Installing instructions for Windows 10
### Python 3.8
1) Locate the appropriate version of Python here:
- https://www.python.org/downloads/

2) Add the file to a known directory of your choice and execute the file. ((C:) drive most accessible)

3) Run the command prompt and access the directory you chose in the previous step.

4) Type ```python``` in to the terminal to check your version.

### PyGame

1) Locate the appropriate version of PyGame here:
- https://bitbucket.org/pygame/pygame/downloads/

2) Copy the PyGame file into the same directory as the Arkanoid game and access this directory in the command prompt, then enter:
```
python3 -m pip install pygame
```

# Usage
## Running the game
Access the directory of the Arkanoid file through the command prompt and simply execute by typing:
```
python3 arkanoid.py
```
### or 

1) Load python files into a python IDE (easiest with PyCharm) with pygame installed


2) To start the game, run:
```
arkanoid.py
```

# Components
See the relevant files for more detailed annotations. My project is made up of:

- arkanoid.py - Executable code to run the game is located here
- png files - Contains the images used as the paddle and bricks.

## Exiting the game
You can exit the game by clicking the 'X' button at the top right, or you can press 'Q' at anytime.

# Testing
When building this game I wasn't familar with the means of unit-testing PyGame, and so resorted to manual testing. Through a relatively laborious process I had ironed out as many bugs as I could find. I was sure the game was solid.   


## Preview

![](images/arkanoid.gif?raw=true)

![](images/arkanoid(47fps-21ms).gif?raw=true)

![](images/arkanoid(60fps-16ms).gif?raw=true)