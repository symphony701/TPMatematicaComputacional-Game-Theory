import numpy as np
import math


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

    def justpuras(self):
       
        posmaxg1 = []
        for i in range(self.dimensionx):
            biggestJ1 = [0,0]
            for j in range(self.dimensiony):
                if self.matrix[i][j][1] > biggestJ1[1]:
                    biggestJ1 = self.matrix[i][j]
                    pos1 = (i, j)
            posmaxg1.append(pos1)
        #print(posmaxg1)

        #Jugador 2
        posmaxg2 = []
        for j in range(self.dimensiony):
            biggestJ2 = [0,0]
            for i in range(self.dimensionx):
                if self.matrix[i][j][0] > biggestJ2[0]:
                    biggestJ2 = self.matrix[i][j]
                    print(self.matrix[i][j])
                    pos2 = (i, j)
            posmaxg2.append(pos2)
        #print(posmaxg2)

        balNash = []

        for i in range(len(posmaxg1)):
            for j in range(len(posmaxg2)):
                if posmaxg1[i] == posmaxg2[j]:
                    balNash.append(self.matrix[posmaxg1[i][0]][posmaxg1[i][1]])
            
            
        
        return self.matrix,balNash
    
    
    def mixtas(self):
        self.eliminarDominadas()
        
        if self.dimensionx == 2 and self.dimensiony == 2:
            
            resultado=""
            resultado += "("
            resultado += str(round(self.calcularP(),3))+ "A )(" +str(round(1-self.calcularP(),3)) + "B )(" +str(round(self.calcularQ(),3)) + "X )(" +str(round(1-self.calcularQ(),3))+"Y)"
            
            return self.matrix,resultado,self.dimensionx,self.dimensiony
        else: 
            print("em nani)?!")
    
    def calcularQ(self):
        n = self.matrix[1,1][0] - self.matrix[0,0][0]
        d = (self.matrix[0,0][0]-self.matrix[0,1][0])-(self.matrix[1,0][0]-self.matrix[1,1][0])
        return n/d    
    def calcularP(self):
        n= self.matrix[1,1][1]-self.matrix[1,0][1]
        d=(self.matrix[0,0][1]-self.matrix[1,0][1])-(self.matrix[0,1][1]-self.matrix[1,1][1])
        return n/d

    
    def eliminarDominadas(self):
        eFil = True
        eCol = True
        while eFil or eCol:
            
            eCol = self.dominacionY()
            eFil = self.dominacionX()
        
        if self.dimensionx == 1 and self.dimensiony ==1:
            
            return self.matrix , [self.matrix[0,0]],self.dimensionx,self.dimensiony
        else:
            return self.matrix , [],self.dimensionx,self.dimensiony
    
    def dominacionY(self):
       
        todelCol=False
        for j in range(self.dimensiony - 1):
            for j2 in range(j + 1, self.dimensiony):
                domination_score = [[],[]]
                for i in range(self.dimensionx):
                    if self.matrix[i][j][1] < self.matrix[i][j2][1]:
                        domination_score[1].append(1)
                    elif self.matrix[i][j][1] > self.matrix[i][j2][1]:
                        domination_score[0].append(1)

                if not len(domination_score[0]):
                    print(self.dimensiony, j)
                    todelCol = True
                    pos_dc = j
                    self.matrix = np.delete(self.matrix, pos_dc, axis = 1)
                    self.dimensiony -= 1
                    return todelCol
                elif not len(domination_score[1]):
                    print(self.dimensiony, j2)
                    todelCol = True
                    pos_dc = j2
                    self.matrix = np.delete(self.matrix, pos_dc, axis = 1)
                    self.dimensiony -= 1
                    return todelCol 
        return todelCol
    
    
    
    def dominacionX(self):
        
        todelRow = False
        for i in range(self.dimensionx - 1):
            for i2 in range(i + 1, self.dimensionx):
                domination_score = [[],[]]
                for j in range(self.dimensiony):
                    if self.matrix[i][j][0] < self.matrix[i2][j][0]:
                        domination_score[1].append(1)
                    elif self.matrix[i][j][0] > self.matrix[i2][j][0]:
                        domination_score[0].append(1)
                if not len(domination_score[0]):
                    todelRow = True
                    pos_dr = i
                    self.matrix = np.delete(self.matrix, pos_dr, axis = 0)
                    self.dimensionx -=1
                    return todelRow
                elif not len(domination_score[1]):
                    todelRow = True
                    pos_dr = i2
                    self.matrix = np.delete(self.matrix, pos_dr, axis = 0)
                    self.dimensionx -=1
                    return todelRow
        return todelRow        
        
    