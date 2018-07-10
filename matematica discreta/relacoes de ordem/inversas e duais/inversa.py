# -*- coding: utf-8 -*-

# recebe uma relação como parâmetro e retorna a relação inversa.
def inversa(relacao):
    inversa = []
    for tupla in relacao. __getRelacao__():
        inversa.append((tupla[1], tupla[0]))
    relacao.__setRelacao__(inversa)
    return relacao