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

    def justpuras(self):
            #jugador 1
        conjunto1 = []
        for i in range(self.dimensiony):
            mayor = [0,0] 
            for j in range(self.dimensionx):
                if mayor[0]<= self.matrix[j,i][0] :
                    mayor = self.matrix[j,i]
            for k in range(self.dimensionx):
                if mayor[0] == self.matrix[k,i][0]:
                    conjunto1.append([self.matrix[k,i],[k,i]])
        

        conjunto2 = []
        #jugador 2
        for i in range(self.dimensionx):
            mayor = [0,0]
            for j in range(self.dimensiony):
                if mayor[1] <= self.matrix[i,j][1]:
                    mayor = self.matrix[i,j]
            for k in range(self.dimensiony):
                if mayor[1] == self.matrix[i,k][1]:
                    conjunto2.append([self.matrix[i,k],[i,k]])
                
        NashPuras = []

        for i in range(len(conjunto1)):
            for j in range(len(conjunto2)):
                if conjunto1[i][1] == conjunto2[j][1]:
                    NashPuras.append(conjunto1[i])


        
        return self.matrix,NashPuras
    
    
    def mixtas(self):
        self.matrix = self.eliminarDominadas()
        if self.dimensionx == 2 and self.dimensiony == 2:
            resultado= "{(",self.calcularP(),"A )(",1-self.calcularP(),"B )(",self.calcularQ(),"X )(",1-self.calcularQ(),"Y)}"
            return self.matrix,resultado
        else: return
    
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
        return self.matrix , [],self.dimensionx,self.dimensiony
    
    def dominacionY(self):
        eCol = False
        for y in range(self.dimensiony - 1):
            conty = 1

            while y + conty < self.dimensiony and eCol == False:
                conjuntoDominacion = [[], []]
                #[[],[],y,y+n]
                conjuntoDominacion.append(y)
                conjuntoDominacion.append(y + conty)
                for x in range(self.dimensionx):
                    # matrix[x,y] [x,y][]
                    if self.matrix[x, y][1] <= self.matrix[x, y + conty][1]:

                        conjuntoDominacion[1].append(1)

                    else:

                        conjuntoDominacion[0].append(1)

                if len(conjuntoDominacion[0]) == 0:

                    eCol = True
                    self.matrix = np.delete(self.matrix, conjuntoDominacion[2], axis=1)
                    self.dimensiony -= 1
                elif len(conjuntoDominacion[1]) == 0:

                    eCol = True
                    self.matrix = np.delete(self.matrix, conjuntoDominacion[3], axis=1)
                    self.dimensiony -= 1
                else:

                    eCol = False

                conty += 1
            if eCol:
                break

        return eCol
    
    def dominacionX(self):
        eFil=False
        for x in range(self.dimensionx - 1):
            contx = 1

            while x + contx < self.dimensionx and eFil == False:
                prueba = [[], []]
                prueba.append(x)
                prueba.append(x + contx)
                for y in range(self.dimensiony):

                    if self.matrix[x, y][0] <= self.matrix[x + contx, y][0]:

                        prueba[1].append(1)
                    else:

                        prueba[0].append(1)
                if len(prueba[0]) == 0:

                    eFil = True
                    self.matrix = np.delete(self.matrix, prueba[2], axis=0)
                    self.dimensionx -= 1
                elif len(prueba[1]) == 0:

                    eFil = True
                    self.matrix = np.delete(self.matrix, prueba[3], axis=0)
                    self.dimensionx -= 1
                else:

                    eFil = False

                contx += 1
            if eFil:
                break
        return eFil
        