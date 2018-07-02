# -*- coding: utf-8 -*-

# recebe uma relação como parâmetro e retorna a relação inversa.
def inversal(relacao):
    inversal = []
    for tupla in relacao. __getRelacao__():
        inversal.append((tupla[1], tupla[0]))
    relacao.__setRelacao__(inversal)
    return relacao