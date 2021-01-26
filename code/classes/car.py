import random
from matplotlib import colors 

class Car:
    """
    Class which handles the information from a specific car
    """
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length
        self.colour = str

        # gets a list of colours to choose from and removes red and black
        colourslist = list(colors.cnames.values())
        colourslist.remove('#FF0000')
        colourslist.remove('#000000')
        if self.name == 'X':
                self.colour = 'r'
        else:
            self.colour = random.choice(colourslist)