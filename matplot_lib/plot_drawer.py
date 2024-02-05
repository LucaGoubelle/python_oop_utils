""" plot drawer """
from matplotlib import pyplot
import numpy
from typing import List

class PlotDrawer:
    """ plot drawer """
    def __init__(self, x:List[int], y:List[int]):
        self.xpoints = numpy.array(x)
        self.ypoints = numpy.array(y)
        
    def draw(self, scatter=''):
        """ draw plot """
        pyplot.plot(self.xpoints, self.ypoints, scatter)
        pyplot.show()
