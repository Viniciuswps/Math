#-*-coding: utf-8-*-

'''
Considere as relações abaixo no conjunto A = {1, 2, 3, 4}:

R1 = {(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4)}
R2 = {(1, 1),(1, 2),(2, 1)}
R3 = {(1, 1),(1, 2),(1, 4),(2, 1),(2, 2),(3, 3),(4, 1),(4, 4)}
R4 = {(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3)}
R5 = {(1, 1),(1, 2),(1, 3),(1, 4),(2, 2),(2, 3),(2, 4),(3, 3),(3, 4),(4, 4)}

Quais dessas relações são reflexivas ?
'''

A = [1,2,3,4]

R1 = [(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4)]
R2 = [(1, 1),(1, 2),(2, 1)]
R3 = [(1, 1),(1, 2),(1, 4),(2, 1),(2, 2),(3, 3),(4, 1),(4, 4)]
R4 = [(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3)]
R5 = [(1, 1),(1, 2),(1, 3),(1, 4),(2, 2),(2, 3),(2, 4),(3, 3),(3, 4),(4, 4)]

'''
Recebe como parâmetros um conjunto no qual a relação é aplicada e a própria relação.
'''
def reflexiva(A, relacao):
    for elemento in A:
        if not (elemento, elemento) in relacao:
            return False
    return True


# Testando ...

assert not reflexiva(A,R1)
assert not reflexiva(A,R2)
assert reflexiva(A,R3)
assert not reflexiva(A,R4)
assert reflexiva(A,R5)


