#-*-coding: utf-8-*-

import matriz_reflexiva
from matrizes_de_relacao.relacao import Relacao
from  matriz_reflexiva import eh_reflexiva
from  matriz_simetrica import eh_simetrica
from matriz_antisimetrica import eh_antisimetrica


A = [1,2,3]
relacao = Relacao("a > b", A, A)
print "EXEMPLO 1:"
print relacao
print relacao.__matriz_relacao__()
assert relacao.__getRelacao__() == [(2, 1), (3, 1), (3, 2)]
assert not eh_reflexiva(relacao)
assert not eh_simetrica(relacao)
assert eh_antisimetrica(relacao)


A = [8,9,3]
relacao = Relacao("a > b", A, A)
print "EXEMPLO 2:"
print relacao
print relacao.__matriz_relacao__()
assert not eh_reflexiva(relacao)
assert not eh_simetrica(relacao)
assert eh_antisimetrica(relacao)


A = [1,2,3]
relacao = Relacao("a >= b", A, A)
print "EXEMPLO 3:"
print relacao
print relacao.__matriz_relacao__()
assert eh_reflexiva(relacao)
assert not eh_simetrica(relacao)
assert eh_antisimetrica(relacao)


A = [1,2,3]
relacao = Relacao("a = b", A, A)
print "EXEMPLO 4:"
print relacao
print relacao.__matriz_relacao__()
assert eh_reflexiva(relacao)
assert eh_simetrica(relacao)
assert not eh_antisimetrica(relacao)