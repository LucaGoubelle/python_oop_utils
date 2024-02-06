""" scatter plot drawer """
from typing import List
from matplotlib import pyplot
import numpy

class ScatterPlotDrawer:
    """ scatter plot drawer """
    def __init__(self, x:List[int], y:List[int]):
        self.x = numpy.array(x)
        self.y = numpy.array(y)
    
    def gen_more_scatter(self, x:List[int],y:List[int]):
        """ gen scatter plot """
        pyplot.scatter(x,y)
    
    def draw(self):
        pyplot.scatter(self.x,self.y)
        pyplot.show()
