# -*- coding: utf-8 -*-

'''
Seja (S, R) um POSET. onde  x e y ∈ S.
'''

def eh_predecessor(x, y, relacao):

    if (x,y) in relacao.__getRelacao__() and x != y:
        return True

    return False

def get_predecessores_de_Y(Y, S, relacao):
    predecessores = []
    for x in S:
            if eh_predecessor(x, Y, relacao) :
                predecessores.append((x,Y))
    return predecessores