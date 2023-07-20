'''
Class Tile
'''
from turtle import *

class Tile:
    '''
    class Tile is used to create tile object, record its coordinate\
    set its image, show whether it is blank or not, create its turtle\
    screen, stamp image. 
    '''
    
    def __init__(self, x=0, y=0, image=None):
        self.x = x
        self.y = y
        self.turtle = Turtle()
        self.turtle.up()
        self.screen = Screen()
        self.image = image
        self.blank = False # set default blank to False
        self.click = False # set default click to False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_position(self, newx, newy):
        self.x = newx
        self.y = newy
        self.turtle.setposition(self.x, self.y)

    def show_turtle(self):
        self.turtle.showturtle()
        

    def hide_turtle(self):
        self.turtle.hideturtle()

    def stamp_image(self):
        self.turtle.clear()
        self.screen.register_shape(self.image)
        self.turtle.shape(self.image)
        
    def get_image(self):
        return self.image
        
    def check_click(self, x, y, size): # size is the tile size
        if abs(x - self.x) <= size/2 and \
           abs(y - self.y) <= size/2:
            self.click = True
        else:
            self.click = False

    def clicked(self):
        return self.click
        

    def original_position(self, x, y):
        self.orig_x = x
        self.orig_y = y

    def get_orig_x(self):
        return self.orig_x

    def get_orig_y(self):
        return self.orig_y

    def is_blank(self):
        return self.blank
    
    def setblank(self, blank):
        self.blank = blank

    def is_adjacent(self, other, size): # check if adjacent to blank tile
        if abs(self.x - other.x) == 0 and \
           abs(self.y - other.y) == size:
            return True
        elif abs(self.y - other.y) == 0 and \
           abs(self.x - other.x) == size:
            return True
        else:
            return False
            
        
    def swap(self, other):
        tempx = self.x
        tempy = self.y
        self.set_position(other.x, other.y)
        other.set_position(tempx, tempy)
           
             
    def reset(self):
        self.set_position(self.orig_x, self.orig_y)
        
    def __str__(self):
        return f"Tile with image{self.image}"
        

    
