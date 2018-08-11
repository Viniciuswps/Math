#-*-coding: utf-8-*-

from relacao import Relacao


''' ---------------------------------- EXEMPLOS --------------------------------------------- '''

print "Exemplo1: "

A = [1,2,3]
B = [1,2]

relacao = Relacao("a > b", A, B)

print relacao.__str__()
print
print relacao.__matriz_relacao__()
assert relacao.__matriz_relacao__().__get_array_matriz__() == [[0,0], [1,0], [1,1]]


print "Exemplo2: "

A = [8,9,3]
B = [4,10,2]

relacao = Relacao("a > b", A, B)

print "Matriz de Relação:\n"
print relacao.__str__()
print
print relacao.__matriz_relacao__()
assert relacao.__matriz_relacao__().__get_array_matriz__() == [[1,0,1], [1,0,1], [0,0,1]]