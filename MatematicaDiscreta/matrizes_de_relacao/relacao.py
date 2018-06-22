#-*-coding: utf-8-*-

class Relacao:

    '''
    Constroi uma relação R de A para B a partir de uma propriedade(String), conjunto A e B.
    
    @param propriedade
            propriedade da relação. 
            prop disponiveis : "a = b", "a > b", "a >= b", "a < b", "a <= b" e "".  
    @param A
            conjunto A.
    @param B
            conjunto B.
            parametro opcional, se B nõ for inserido o B passará a ser A e, portanto, a relação sera R de A em A
    '''
    def __init__(self, propriedade, A, B = 0):

        self.A = A
        if B != 0:
            self.B = B
        else:
            self.B = A
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