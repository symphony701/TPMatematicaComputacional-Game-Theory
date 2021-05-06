import numpy as np


class Nash:
    def __init__(self,dimensionx,dimensiony,datos):
        
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
        matrix = np.empty((dimensionx, dimensiony), list)
        a = 0
        b = 1
        for i in range(dimensionx):
            for j in range(dimensiony):
                lista = [datos[a],datos[b]]
                a +=2
                b +=2
                matrix[i, j] = lista

        print(matrix)