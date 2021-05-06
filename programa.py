import numpy as np


class Nash:
    def __init__(self,dimensionx,dimensiony,datos):
        
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
        self.matrix = np.empty((dimensionx, dimensiony), list)
        a = 0
        b = 1
        for i in range(dimensionx):
            for j in range(dimensiony):
                lista = [datos[a],datos[b]]
                a +=2
                b +=2
                self.matrix[i, j] = lista

    def justpuras():
            #jugador 1
        conjunto1 = []
        for j in range(dimensionx):
            mayor = [0,0] 
            for i in range(dimensiony):
                if mayor[0]<= matrix[i,j][0] :
                    mayor = matrix[i,j]
            #conjunto1.append([mayor,[j,i]])
            for k in range(dimensiony):
                if mayor[0] == matrix[k,j][0]:
                    conjunto1.append([matrix[k,j],[k,j]])

        print(conjunto1)
        conjunto2 = []
        #jugador 2
        for i in range(dimensionx):
            mayor = [0,0]
            for j in range(dimensiony):
               if mayor[1] <= matrix[i,j][1]:
                mayor = matrix[i,j]
            for k in range(dimensiony):
             if mayor[1] == matrix[i,k][1]:
                conjunto2.append([matrix[i,k],[i,k]])
                
        print(conjunto2)

        NashPuras = []

        for i in range(len(conjunto1)):
            for j in range(len(conjunto2)):
              if conjunto1[i][1] == conjunto2[j][1]:
                NashPuras.append(conjunto1[i])

        print(NashPuras)