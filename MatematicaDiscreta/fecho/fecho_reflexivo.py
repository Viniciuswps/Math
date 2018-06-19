#-*-coding: utf-8-*-

'''
Recebe como parâmetros um conjunto no qual a relação é aplicada e a própria relação.
'''
def fecho_reflexiva(A, relacao):
    for elemento in A:
        if not (elemento, elemento) in relacao:
            relacao.append((elemento, elemento))
    return relacao

A = [1,2,3,4]

R1 = [(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4)]
R2 = [(1, 1),(1, 2),(2, 1)]
R3 = [(1, 1),(1, 2),(1, 4),(2, 1),(2, 2),(3, 3),(4, 1),(4, 4)]
R4 = [(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3)]
R5 = [(1, 1),(1, 2),(1, 3),(1, 4),(2, 2),(2, 3),(2, 4),(3, 3),(3, 4),(4, 4)]

# Testando ...

assert fecho_reflexiva(A,R1) == [(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4),(3, 3)]
assert fecho_reflexiva(A,R2) == [(1, 1),(1, 2),(2, 1),(2, 2),(3, 3),(4, 4)]
assert fecho_reflexiva(A,R3) == R3
assert fecho_reflexiva(A,R4) == [(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3),(1, 1),(2, 2),(3, 3),(4, 4)]
assert fecho_reflexiva(A,R5) == R5


