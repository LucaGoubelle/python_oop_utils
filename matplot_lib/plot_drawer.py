""" plot drawer """
from matplotlib import pyplot
import numpy
from typing import List

class PlotDrawer:
    """ plot drawer """
    def __init__(self, x:List[int], y:List[int], title:str="", xlabel:str="", ylabel:str=""):
        self.xpoints = numpy.array(x)
        self.ypoints = numpy.array(y)
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        
    def draw(self, scatter='', title_pos:str='center', grid:bool=False):
        """ draw plot """
        pyplot.plot(self.xpoints, self.ypoints, scatter)
        pyplot.title(self.title, loc=title_pos)
        pyplot.xlabel(self.xlabel)
        pyplot.ylabel(self.ylabel)
        if grid: pyplot.grid(axis='y')
        pyplot.show()
