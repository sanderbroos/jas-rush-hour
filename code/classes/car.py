from random import choice
from matplotlib import colors


class Car:
    """
    Class which handles the information of a specific car.
    """
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length

        if self.name == 'X':
            self.color = 'r'
        else:
            # gets a list of colors to choose from and removes red and black
            colors_list = list(set(colors.cnames.values()) - {'#FF0000', '#000000'})
            self.color = choice(colors_list)