import numpy as np


class Nash:
    def __init__(self,dimensionx,dimensiony):
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
        matrix = np.empty((dimensionx, dimensiony), list)
        