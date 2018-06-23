# -*- coding: utf-8 -*-

from base.relacao import Relacao

def eh_relacao_de_equivalencia(A, relacao):

    # verificando a propriedade reflexiva
    for elemento in A:
        if not (elemento, elemento) in relacao. __getRelacao__():
            return False

    # verificando a propriedade transitiva
    for a in A:
        for b in A:
            for c in A:
                if (a,b) in relacao. __getRelacao__() and (b,c) in relacao. __getRelacao__() and not (a,c) in relacao. __getRelacao__():
                    return False

    # verificando a propriedade simétrica
    for a in A:
        for b in A:
            if (a,b) in relacao. __getRelacao__() and not (b,a) in relacao. __getRelacao__():
                return False
                
    return True
