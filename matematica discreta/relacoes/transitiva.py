#-*-coding: utf-8-*-

'''
Recebe como parâmetros um conjunto no qual a relação é aplicada e a própria relação.
'''
def transitiva(A, relacao):
    for a in A:
        for b in A:
            for c in A:
                if (a,b) in relacao and (b,c) in relacao and not (a,c) in relacao:
                    return False
    return True


A = [1,2,3,4]

R1 = [(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4)]
R2 = [(1, 1),(1, 2),(2, 1)]
R3 = [(1, 1),(1, 2),(1, 4),(2, 1),(2, 2),(3, 3),(4, 1),(4, 4)]
R4 = [(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3)]
R5 = [(1, 1),(1, 2),(1, 3),(1, 4),(2, 2),(2, 3),(2, 4),(3, 3),(3, 4),(4, 4)]
R6 = [(3,4)]

# Testando ...

assert not transitiva(A,R1)
assert not transitiva(A,R2)
assert not transitiva(A,R3)
assert transitiva(A,R4)
assert transitiva(A,R5)
assert transitiva(A,R6)


