#-*-coding: utf-8-*-

class Matriz:
   
    '''
    Constroi uma matriz a partir da quantidade de linhas e colunas
    
    @param Nlinhas
            qtd de linhas da matriz.
    @param Ncolunas
            qtd de colunas da matriz.
    @param matriz
            array onde será armazenado os elementos da matriz.
    '''
    def __init__(self, Nlinhas, Ncolunas, array_matriz=0):
        self.Nlinhas = Nlinhas
        self.Ncolunas = Ncolunas
        if array_matriz != 0:
            self.array_matriz = array_matriz
        else:
            self.array_matriz = []
            for i in range(self.Nlinhas):
                self.array_matriz.append([])

    def __addElemento__(self, i, elemento):
        self.array_matriz[i].append(elemento)

    def __getNlinhas__(self):
        return self.Nlinhas

    def __getNcolunas__(self):
        return self.Ncolunas

    def __get_array_matriz__(self):
        return self.array_matriz

    def __str__(self):
        msg = "Matriz:\n"
        for i in range(self.Nlinhas):
            for j in range(self.Ncolunas): 
                msg += "| " + str(self.array_matriz[i][j]) + " |"
            msg += "\n"
        return msg
