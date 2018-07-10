# -*- coding: utf-8 -*-

from base.relacao import Relacao
from predecessorESucessor.predecessor import eh_predecessor
from predecessorESucessor.predecessor import get_predecessores_de_Y
from predecessorESucessor.predecessor_imediato import eh_predecessor_imediato
from predecessorESucessor.predecessor_imediato import get_predecessores_imediatos_de_Y

'''

Considere a relação “x divide y” em {1, 2, 3, 6, 12, 18}

a) Escreva os pares ordenados desta relação.
b) Escreva todos os predecessores de 6.
c) Escreva todos os predecessores imediatos de 6.
'''

A = [1, 2, 3, 6, 12, 18]

relacao = Relacao("a divide b", A, A)
# a)
assert relacao.__getRelacao__() ==  [(1, 1), (1, 2), (2, 2), (1, 3), (3, 3), (1, 6), (2, 6), (3, 6), (6, 6), (1, 12), (2, 12), (3, 12), (6, 12), (12, 12), (1, 18),(2, 18), (3, 18), (6, 18), (18, 18)]

# b)
assert eh_predecessor(1,6,relacao)
assert eh_predecessor(2,6,relacao)
assert eh_predecessor(3,6,relacao)
assert get_predecessores_de_Y(6, A, relacao) == [(1,6), (2,6), (3,6)]

# c)
assert not eh_predecessor_imediato(1,6,A,relacao)
assert eh_predecessor_imediato(2,6,A,relacao)
assert eh_predecessor_imediato(3,6,A,relacao)
assert get_predecessores_imediatos_de_Y(6, A, relacao) == [(2,6), (3,6)]