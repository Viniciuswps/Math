#coding: utf-8
'''
@problem: Dados os vlores verdade das proposições p e q, encontre os valores-verdade da conjunção, disjunção, ou exclusivo, sentença condicional e
bicondicional dessa proposições.
@version 21/03/2018    @author: Vinicius Barbosa
'''

# entrando com os valores verdade
print "1: True  0: False"
print ''
p = int(raw_input("Insira o valor verdade de p: "))
q = int(raw_input("Insira o valor verdade de q: "))
print ''

# conjunçao
if p and q:
    print "Conjunçao: True"
else:
    print "Conjunçao: False"

# disjunção
if p or q:
    print "Disjunção: True"
else:
    print "Disjunção: False"

# ou exclusivo
if (p or q) and (not p or not q): # (p or q) and not(p and q)
    print "Ou exclusivo: True"
else:
    print "Ou exclusivo: False"

# sentença condicional
if p and not q:          # p --> q só é falso quando p é verdade e q é falso
    print "p --> q: False"
else:
    print "p --> q: True"
if q and not p:          # q --> p só é falso quando q é verdade e p é falso
    print "q --> p: False"
else:
    print "q --> p: True"

# sentença bicondicional
if (p and q) or (not p and not q):
    print "p <--> q: True"
else:
    print "p <--> q: False"
