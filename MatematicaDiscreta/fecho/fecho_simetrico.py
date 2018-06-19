#-*-coding: utf-8-*-

'''
Recebe como parâmetros um conjunto no qual a relação é aplicada e a própria relação.
'''
def fecho_simetrico(A, relacao):
    for a in A:
        for b in A:
            if (a,b) in relacao and not (b,a) in relacao:
                relacao.append((b,a))
    return relacao

A = [1,2,3,4]

R1 = [(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4)]
R2 = [(1, 1),(1, 2),(2, 1)]
R3 = [(1, 1),(1, 2),(1, 4),(2, 1),(2, 2),(3, 3),(4, 1),(4, 4)]
R4 = [(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3)]
R5 = [(1, 1),(1, 2),(1, 3),(1, 4),(2, 2),(2, 3),(2, 4),(3, 3),(3, 4),(4, 4)]

# Testando ...

assert fecho_simetrico(A,R1) == [(1, 1),(1, 2),(2, 1),(2, 2),(3, 4),(4, 1),(4, 4),(4, 3),(1, 4)]
assert fecho_simetrico(A,R2) == R2
assert fecho_simetrico(A,R3) == R3
assert fecho_simetrico(A,R4) == [(2, 1),(3, 1),(3, 2),(4, 1),(4, 2),(4, 3),(1, 2),(1, 3),(2, 3),(1, 4),(2, 4),(3, 4)] 
assert fecho_simetrico(A,R5) == [(1, 1),(1, 2),(1, 3),(1, 4),(2, 2),(2, 3),(2, 4),(3, 3),(3, 4),(4, 4),(2, 1),(3, 1),(4, 1),(3, 2),(4, 2),(4, 3)]

