'''
    Game Borad Placement
'''


import os
from Tile import Tile
import random
import math
from turtle import *
from Counter import Counter
from os import listdir
from os.path import isfile, join
CWD = os.getcwd()
import time
# import class and other modules used in the utility 

def load_tile(filename):
    '''
    Function load_tile is used to open the file\
    and create related tile objects and attach\
    tile image to those tile objects.
    Parameter is a string to show which file to load
    Return a list, an integer and a tile object
    '''
    try:
        with open(CWD + "/" + filename, "r") as in_file:
            content = []
            lines = in_file.readlines()
            for each in lines: 
                nested = each.split()
                nested[0] = nested[0].strip(":")
                if nested[0].isdigit():
                    newtile = Tile(0,0,CWD + "/" + nested[1]) # attach image
                    content.append(newtile)
                elif nested[0] == "size":
                    size = nested[1]
                elif nested[0] == "thumbnail":
                    thumbnail = Tile(300, 415, CWD + "/" + nested[1])
            content[-1].setblank(True) # set the blank tile default
        return content, size, thumbnail
                    
    except IOError: # exception handling
        print("filename not found, please try again")
        with open("5001_puzzle.err", "a") as out_file:
            out_file.write(f"{time.ctime()}:Error: " +\
                           f"Could not find the file"\
                           + f" LOCATION: load_tile()" + "\n")

def load_symbol(symbol_name):
    '''
    Function load_symbol is used to get the path of the symbol
    Parameter is a string
    Return the path
    '''
    symbol = CWD + "/Resources/" + symbol_name + ".gif"
    return symbol
        
            

def set_position(content, size):
    '''
    Function set_position is used to\
    set tile turtle position and attach image\
    to them
    Parameters are a list and an integer 
    Return None
    '''
    index = math.sqrt(len(content)) # see the column and row number
    
    for i in range(len(content)):
        # attach coordinate to each tile and stamp image
        content[i].set_position(-350 + i%index * size, \
                                350 - i//index*size)
        content[i].stamp_image()
    
def set_original(content,size):
    '''
    Function set_original is used to set the tile's orginal coordinate\
    to make it eaiser to reset in later functions
    Parameter is a list and an integer
    Return None
    '''
    for i in range(len(content)):
        index = math.sqrt(len(content))
        content[i].original_position(-350 + i%index * size, \
                                     350 - i//index*size)
        

def load_shuffled(content,size):
    '''
    Function load_shuffled is used to load the tiles onto screen
    Parameter is a list and an integer
    Return None
    '''
    random.shuffle(content)
    set_position(content,size)
    
def find_blank(content):
    '''
    Function find_blank is used to find the blank tile in\
    a list
    Parameter is a list
    Return the blank tile object
    '''
    for i in range(len(content)):
        if content[i].is_blank():
            return content[i]

def get_puzzle_input(screen):
    '''
    Function get_puzzle_input is used to get the .puz
    Parameter is a turtle screen 
    Return a list with .puz file listed in
    '''
    onlyfiles = [f for f in listdir(CWD) if isfile(join(CWD, f))]
    puz_file = []
    for each in onlyfiles :
        if each[-3:] == "puz":
            puz_file.append(each)
    if len(puz_file) > 10: # handling file > 10 
        puz_10 = CWD + "/Resources/file_warning.gif"
        screen.register_shape(puz_10)
        puz_show = Turtle()
        screen.delay(3000)
        puz_show.shape(puz_10)
        screen.delay(0)
        puz_show.hideturtle()
        with open("5001_puzzle.err", "a") as out_file:
            out_file.write(f"{time.ctime()}:Error: " +\
                           f"more than 10 file showing first 10"\
                           + f" LOCATION: screenonclick()" + "\n")
    
    puzfile = puz_file[:10] # only give the first ten .puz file
    return puzfile 
   

def get_new_file(puz_file, screen):
    '''
    Function get_new_file is used to get user input filenames
    Parameter is a list and a turtle screen to pop the message
    Return the input of the user
    '''
    puzstring = "\n".join(puz_file)
    file_name = screen.textinput("Load Puzzle", f"Enter the name of the puzzle "
                                 "you wish to play. ""Choice are: \n"
                                 f"{puzstring}")
    return file_name
    
        
        
                     

def screenclick(content, thumbnail, totalmoves, username, \
                usermoves, size, t_shape, t_moves, screen):
    '''
    Function screenclick is a function to make possible of all \
    the screenclick effect
    Parameter is a list with tile objects in, the thumbnail tile,\
    Count object reflecting usersetting total moves, string username,\
    Count object reflecting user's moves on the screen\
    an integer size, 2 turtle objects t_shape and t_moves\
    screen object screen
    Return None
    '''
    t_shape.hideturtle()
    blank = find_blank(content)
    def getclick(x, y,content=content,blank=blank,\
                 username=username,usermoves=usermoves,\
                 totalmoves=totalmoves,size=size, \
                 t_moves = t_moves,\
                 t_shape=t_shape, screen=screen,\
                 thumbnail=thumbnail):
        '''
        Function getclick is the helper fucntion to make screenclick effect\
        possible. It can do swap, load, reset, quit and check if the user\
        loses or wins the game
        Parameters are the same as screenonclick above
        Return None
        '''
        winning = 0 # winning flag, default not winning
        len_content = len(content)
        # get the number of the tiles
        if abs(x - 30) <=40 and abs(y + 300) <= 40:# reset symbol
            for i in range(len(content)):
                content[i].reset()
                # use tile object to reset
        elif abs(x -130) <=40 and abs(y + 300) <= 38: # load symbol
            puz_file = get_puzzle_input(screen)
            file_name = get_new_file(puz_file, screen)
            flag = 0 # flag to check if pua fileexist
            for each in puz_file:
                if file_name == each:
                    flag = 1 # set flag to 1 to show exist 
            if flag == 1: # if the puz file the user inputs exists
                checkcontent, anothersize, anothumbnail = load_tile(file_name)
                index = math.sqrt(len(checkcontent))
                is_image_exist = 0 # flag to check if image exists 
                for i in range(len(checkcontent)):
                    if os.path.exists(checkcontent[i].get_image()):
                        is_image_exist += 1
                if index.is_integer() == False:
                    t_shape.clear()
                    file_error = load_symbol("file_error") 
                    screen.register_shape(file_error)
                    t_shape.showturtle()
                    screen.delay(3000)
                    t_shape.shape(file_error)
                    screen.delay(0)
                    t_shape.hideturtle() # turtle showing error image
                    with open("5001_puzzle.err", "a") as out_file:
                        out_file.write(f"{time.ctime()}:Error: " +\
                                       f"Could not load the puz Bad Number"\
                                       + f" LOCATION: screenonclick()" + "\n")
                    # load nonvalid number error
                
                elif is_image_exist == len(checkcontent):
                    # if image exists
                    for i in range(len(content)):
                        content[i].hide_turtle()
                        # hide current turtle
                    thumbnail.hide_turtle() 
                    t_moves.clear()
                    t_moves.hideturtle()
                    t_shape.clear()
                    t_shape.hideturtle()
                    content, size, thumbnail = load_tile(file_name)
                    # generate new tile lists based on the new puz file
                    size = int(size)
                    set_original(content,size)
                    load_shuffled(content, size)
                    thumbnail.set_position(275,415) # set thumbnail position
                    thumbnail.stamp_image() # show thumbnail
                    usermoves = Counter()
                    # create a counter object to record user moves
                    
                    screenclick(content, thumbnail, totalmoves, username, \
                                usermoves, size, t_shape, t_moves, \
                                screen)
                    '''
                    to update the content, size, maybe a class object\
                    is better but recursive fucntion works 
                    '''
                    
                else: # if image not exists
                    t_shape.clear()
                    file_error = load_symbol("file_error") 
                    screen.register_shape(file_error)
                    t_shape.showturtle()
                    screen.delay(3000)
                    t_shape.shape(file_error)
                    screen.delay(0)
                    t_shape.hideturtle() # turtle showing error image
                    with open("5001_puzzle.err", "a") as out_file:
                        out_file.write(f"{time.ctime()}:Error: " +\
                                       f"Could not load the puz"\
                                       + f" LOCATION: screenonclick()" + "\n")
                    # load it into the .err file 
            else: # if the input could not be found in the puz file lists
                t_shape.clear()
                file_error = load_symbol("file_error") 
                screen.register_shape(file_error)
                t_shape.showturtle()
                screen.delay(3000)
                t_shape.shape(file_error)
                screen.delay(0)
                t_shape.hideturtle()
                with open("5001_puzzle.err", "a") as out_file:
                    out_file.write(f"{time.ctime()}:Error: " +\
                                   f"Could not find the puz"\
                                   + f" LOCATION: screenonclick()" + "\n")
                # load it into the .err file
        elif abs(x -230) <=40 and abs(y + 300) <= 27: # quit symbol
            quit_ = load_symbol("quitmsg")
            t_shape.clear()
            screen.register_shape(quit_)
            t_shape.showturtle()
            screen.delay(3000)
            t_shape.shape(quit_)
            screen.bye()
        else:
            for i in range(len(content)): # swap
                content[i].check_click(x, y, size)
                if content[i].clicked() and \
                   content[i].is_adjacent(blank, size):
                    content[i].swap(blank)
                    usermoves.increment()
                    # increment usermoves
                    style = ("Times New Roman", 20, "bold")
                    if usermoves.get_moves() <= totalmoves.get_moves():
                        t_moves.clear()
                        t_moves.write("Player Moves: "\
                                      f"{usermoves.get_moves()}", \
                                      font = style, align = "left")
                    # update playermoves
            for i in range(len(content)): # check wining or not 
               if content[i].get_orig_x() == content[i].get_x() and\
                  content[i].get_orig_y() == content[i].get_y():
                   winning +=1
            
            if usermoves.get_moves() > totalmoves.get_moves(): # lose     
                lose = load_symbol("Lose")
                t_shape.clear()
                screen.register_shape(lose)
                t_shape.showturtle()
                screen.delay(3000)
                t_shape.shape(lose)
                screen.delay(0)
                t_shape.clear()
                credit = load_symbol("credits")
                screen.register_shape(credit)
                t_shape.showturtle()
                screen.delay(3000)
                t_shape.shape(credit)
                screen.bye()
            elif winning == len_content: # if win 
                win = load_symbol("winner")
                t_shape.clear()
                screen.register_shape(win)
                t_shape.showturtle()
                screen.delay(3000)
                t_shape.shape(win)
                with open("leaderboard.txt", "a") as out_file:
                    # leaderboard file created or append
                    out_file.write(str(usermoves.get_moves())\
                                   + " : "  + username + "\n")
                screen.bye()
                
    screen.onclick(getclick)


