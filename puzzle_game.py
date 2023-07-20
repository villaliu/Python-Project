'''
5001 Final Project Puzzle Game
Ruochen Liu
Prof K
'''
from turtle import *
from Tile import Tile 
import os
import math
from Utility import *
from Counter import Counter
from os import listdir
from os.path import isfile, join
import time
# import modules and classes
t = Turtle() # set turtle to draw board
screen = Screen() # set screen 
CWD = os.getcwd() # get directory of the file


def setup():
    '''
    Function setup() is used to show the splash screen\
    and the username and the moves user sets
    Parameter not needed
    Return two strings, username and moves
    '''
    screen.screensize(970,970)
    '''
    on my screen if I use screen.setup, the turtle screen will move\
    to the top of my computer screen.
    After discussing it in the lab session with 2 TAs, I was suggested\
    to use screensize instead. It may result to scrolling all the time\
    But at least it works.
    '''
    splash = CWD + "/Resources/splash_screen.gif"
    screen.register_shape(splash)
    screen.delay(3000)
    t.shape(splash)
    screen.clear()
    t.clear()
    username = get_user_name()
    moves = get_steps()
    return username, moves

def puzzleboard():
    '''
    Function puzzleboard is used to create three boards\
    and load symbols
    Parameter not needed
    Return None
    '''
    t.up() # hide the turtle's motion
    t.goto(-415, 415) # make sure the retangle is on the left 
    t.down()# reshow the turtle
    t.color('black') # set the color
    t.pensize(3) # line thickness
    t.forward(430)  # side 1
    t.right(90) 
    t.forward(550)  # side 2
    t.right(90)
    t.forward(430)  # side 3
    t.right(90)
    t.forward(550)  # side 4
    t.right(90)
    t.up() # hide the turtle's motion
    t.goto(30, 415)
    t.down()# reshow the turtle
    t.color('blue') # set the color
    t.pensize(3) # line thickness
    t.forward(300)  # side 1
    t.right(90) 
    t.forward(550)  # side 2
    t.right(90)
    t.forward(300)  # side 3
    t.right(90)
    t.forward(550)  # side 4
    t.right(90)
    t.up() # hide the turtle's motion
    t.goto(-415, -250) # make sure the retangle is on the left 
    t.down()# reshow the turtle
    t.color('black') # set the color
    t.pensize(3) # line thickness
    t.forward(745)  # side 1
    t.right(90) 
    t.forward(100)  # side 2
    t.right(90)
    t.forward(745)  # side 3
    t.right(90)
    t.forward(100)  # side 4
    t.right(90)
    leader() 
    load_winners()
    reset_symbol()
    load_symbol()
    quit_symbol()
    

def get_user_name():
    '''
    Function get_user_name is used to get username
    Parameter not needed
    Return user name
    '''
    return screen.textinput("CS5001 Puzzle Slider", "Your Name: ")
    
def get_steps():
    '''
    Function get_steps is used to get max moves the user wants
    Parameter not needed
    Return moves the user sets
    '''
    return screen.numinput("CS5001 Puzzle Slider-Moves", "Enter the moves(5 to 200): ",\
                    5, minval=5, maxval=200)
    

def leader():
    '''
    Function leader is used to write leaders
    Parameter not needed
    Return None
    '''
    t.pencolor("black")
    t.pensize(3)
    t.up()
    t.goto(50, 390)
    style = ("Times New Roman", 15, "bold")
    t.write("Leaders: ", font = style, align = "left")
    t.down()
    
    
def quit_symbol():
    '''
    Function quit_symbol is used to load quit button
    Parameter not needed
    Return None
    '''
    quit_symbol = CWD + "/Resources/quitbutton.gif"
    screen.register_shape(quit_symbol)
    quit_t = Turtle()
    quit_t.up()
    quit_t.goto(230, -300)
    quit_t.shape(quit_symbol)
    quit_t.down()

def load_symbol():
    '''
    Function load_symbol is used to load load button
    Parameter not needed
    Return None
    '''
    load_symbol = CWD + "/Resources/loadbutton.gif"
    screen.register_shape(load_symbol)
    load_t = Turtle()
    load_t.up()
    load_t.goto(130, -300)
    load_t.shape(load_symbol)
    load_t.down()

def reset_symbol():
    '''
    Function reset_symbol is used to load reset button
    Parameter not needed
    Return None
    '''
    reset_symbol = CWD + "/Resources/resetbutton.gif"
    screen.register_shape(reset_symbol)
    reset_t = Turtle()
    reset_t.up()
    reset_t.goto(30, -300)
    reset_t.shape(reset_symbol)
    reset_t.down()
        
def load_winners():
    '''
    Function load_winners is used to load winner name\
    and their moves. It will only load the latest 4 winners
    '''
    t.up()
    t.goto(50, 330)
    t.down()
    style = ("Times New Roman", 15, "bold")
    content = []
    try:
        with open("leaderboard.txt", "r") as in_file:
            for each in in_file:
                content.append(each)
        for i in content[-4:]:
            t.write(i, font = style, align = "left")
            t.up()
            t.right(90)
            t.forward(30)
            t.left(90)
            t.down()
        t.hideturtle()
    except IOError: # exception handling 
        lead_error = CWD + "/Resources/leaderboard_error.gif"
        screen.register_shape(lead_error)
        leadturtle = Turtle()
        screen.delay(3000)
        leadturtle.shape(lead_error)
        screen.delay(0)
        leadturtle.hideturtle()
        with open("5001_puzzle.err", "a") as out_file:
            # err file create or append to it 
            out_file.write(f"{time.ctime()}:Error: " +\
                           f"Could not open leaderboard.txt"\
                           + f" LOCATION: load_winners()" + "\n")
        
        
    
def main():
    username, moves = setup() # set up username and moves
    puzzleboard()# set up game board
    content, size, thumbnail = load_tile("mario.puz")
    # load in puzzles
    size = int(size)
    set_original(content,size)
    # set tile original coordinates
    load_shuffled(content, size)
    # load tiles onto turtle screen
    thumbnail.set_position(275,415)
    # load thumbnail tiles
    thumbnail.stamp_image()
    totalmoves = Counter(moves) # create counters for totalmoves
    usermoves = Counter() # create usermoves counter
    t_shape = Turtle()
    t_moves = Turtle()
    t_moves.hideturtle()
    t_moves.up()
    t_moves.goto(-400, -317)# set turtle to the player move position
    t_moves.down()
    screenclick(content, thumbnail, totalmoves, username, \
                usermoves, size, t_shape, t_moves, screen)
    # pull in screenclick effect
if __name__ == "__main__":
    main()
    
    
