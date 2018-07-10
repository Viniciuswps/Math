# -*- coding: utf-8 -*-

from base.relacao import Relacao
from relacao_de_ordem import eh_relacao_de_ordem

A = range(40)
B = range(1,40)

relacao = Relacao("a <= b", A, A)
assert eh_relacao_de_ordem(A, relacao)

relacao = Relacao("a divide b", B, B)
assert eh_relacao_de_ordem(B, relacao)

relacao = Relacao("a < b", B, B)
assert not eh_relacao_de_ordem(B, relacao)
