# -*- coding: utf-8 -*-

'''Seja (S, R) um POSET. onde  x e y ∈ S'''
def eh_predecessor_imediato(x, y, S, relacao):
    
    if not ((x,y) in relacao.__getRelacao__() and x != y):
        return False
    
    for x in S:
        for z in S:
            for y in S:
                if (x,z) in relacao.__getRelacao__() and (z,y) in relacao.__getRelacao__():
                    return False
    
    return True

# METODO COM ERRO - FALTA CORRIGIR
def get_predecessores_imediatos_de_Y(Y, S, relacao):
    predecessores_imediatos = []
    for x in S:
            if eh_predecessor_imediato(x, Y, S, relacao) :
                predecessores_imediatos.append((x,Y))
    return predecessores_imediatos