# -*- coding: utf-8 -*-

from base.relacao import Relacao
from inversaisEDuais.inversal import inversal
from relacao_de_ordem import eh_relacao_de_ordem

'''
Considere a relação “x divide y” em {1, 2, 3, 6, 12, 18}
'''
A = [1, 2, 3, 6, 12, 18]
relacao = Relacao("a divide b", A, A)

assert eh_relacao_de_ordem(A, relacao)
relacao_inversa = inversal(relacao)
assert eh_relacao_de_ordem(A, relacao_inversa)