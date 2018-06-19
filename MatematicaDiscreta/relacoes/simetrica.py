#-*-coding: utf-8-*-

'''
Recebe como parâmetros um conjunto no qual a relação é aplicada e a própria relação.
'''
def simetrica(A, relacao):
    for a in A:
        for b in A:
            if (a,b) in relacao and not (b,a) in relacao:
                return False
    return True


A = [1,2,3,4]

R1 = [(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4)]
R2 = [(1, 1),(1, 2),(2, 1)]
R3 = [(1, 1),(1, 2),(1, 4),(2, 1),(2, 2),(3, 3),(4, 1),(4, 4)]
R4 = [(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3)]
R5 = [(1, 1),(1, 2),(1, 3),(1, 4),(2, 2),(2, 3),(2, 4),(3, 3),(3, 4),(4, 4)]

# Testando ...

assert not simetrica(A,R1)
assert simetrica(A,R2)
assert simetrica(A,R3)
assert not simetrica(A,R4)
assert not simetrica(A,R5)


