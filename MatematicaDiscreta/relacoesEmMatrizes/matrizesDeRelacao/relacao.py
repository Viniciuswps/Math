#-*-coding: utf-8-*-

from matriz import Matriz

class Relacao:

    '''
    Constroi uma relação R de A para B a partir de uma propriedade(String), conjunto A e B.
    
    @param propriedade
            propriedade da relação. 
            prop disponiveis : "a = b", "a > b", "a >= b", "a < b", "a <= b", a + b é par", "a + b é impar", "a divide b" e "".  
    @param A
            conjunto A.
    @param B
            conjunto B.
    '''
    def __init__(self, propriedade, A, B):

        self.A = A
        self.B = B
        self.propriedade = propriedade
        self.relacao = []

        if self.propriedade == "a = b":   
            for a in A:
                for b in B:
                    if a == b:
                        self.relacao.append((a,b))  

        elif self.propriedade == "a > b":   
            for a in A:
                for b in B:
                    if a > b:
                        self.relacao.append((a,b))       

        elif self.propriedade == "a >= b":   
            for a in A:
                for b in B:
                    if a >= b:
                        self.relacao.append((a,b))

        elif self.propriedade == "a < b":   
            for a in A:
                for b in B:
                    if a < b:
                        self.relacao.append((a,b))

        elif self.propriedade == "a <= b":   
            for a in A:
                for b in B:
                    if a <= b:
                        self.relacao.append((a,b))
        
        elif self.propriedade == "a + b é par":   
            for a in A:
                for b in B:
                    if (a + b) % 2 == 0:
                        self.relacao.append((a,b))

        elif self.propriedade == "a + b é impar":   
            for a in A:
                for b in B:
                    if (a + b) % 2 == 1:
                        self.relacao.append((a,b))
                        
        elif self.propriedade == "a divide b":   
                for a in A:
                    for b in B:
                        if a % b == 0:
                            self.relacao.append((a,b))

        # relacao simples
        elif self.propriedade == "":
            relacao = []
            for a in A:
                for b in B:
                    self.relacao.append((a,b))

    def __getRelacao__(self):
        return self.relacao

    def __str__(self):
        msg  = "A = " + str(self.A) + "\n"
        msg += "B = " + str(self.B) + "\n"
        msg += "R = " + str(self.relacao)
        return msg

    # retorna a matriz de relação da relaçao R
    def __matriz_relacao__(self):
        matriz = Matriz(len(self.A), len(self.B))
        for i in range(matriz.__getNlinhas__()):
            for j in range(matriz.__getNcolunas__()):
                if (self.A[i], self.B[j]) in self.relacao:
                    matriz.__addElemento__(i, 1)
                else:
                    matriz.__addElemento__(i, 0)
        return matriz
    
    