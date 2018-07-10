# -*- coding: utf-8 -*-

from base.relacao import Relacao
from relacao_de_equivalencia import eh_relacao_de_equivalencia

A = [1, 2, 3]
R = Relacao()
R.__setRelacao__([(1, 1),(2, 2),(3, 3),(1, 2),(2, 1)])
assert eh_relacao_de_equivalencia(A, R)

A = range(30)
R = Relacao("a + b é par", A, A)
assert eh_relacao_de_equivalencia(A, R)

'''
Verifique se a relação binária R = {(x, y)| x divide y} em A = [1,2,3,4,5,6,7,8,9,10]
positivos é uma relação de equivalẽncia.
Sol: não é, pois (2,4) ∈ R mas (4,2) ∈/ R, logo não é simetrica.
'''
A = [1,2,3,4,5,6,7,8,9,10]
R = Relacao("a divide b", A, A)
assert not eh_relacao_de_equivalencia(A, R)