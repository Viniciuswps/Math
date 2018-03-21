# coding: utf-8
'''
@problem: Dadas duas sequências de bits de comprimento n, encontre as sequências resultantes das operações AND,OR e XOR dessas
operações.
@version 21/03/2018    @author: Vinicius Barbosa
'''
print "Insira duas sequências de comprimento n"
sequencia1 = raw_input("Sequência1: ")
sequencia2 = raw_input("Sequência2: ")
print ""

# AND
conjuncao = ""
for i in range(len(sequencia1)):
    if int(sequencia1[i]) and int(sequencia2[i]):
        conjuncao += '1'
    else:
        conjuncao += '0'

# OR
disjuncao = ""
for i in range(len(sequencia1)):
    if int(sequencia1[i]) or int(sequencia2[i]):
        disjuncao += '1'
    else:
        disjuncao += '0'

# XOR
ouExclusivo = ""
for i in range(len(sequencia1)):
    if int(sequencia1[i]) or int(sequencia2[i]) and (not int(sequencia1[i]) or not int(sequencia2[i])):
        ouExclusivo += '1'
    else:
        ouExclusivo += '0'
        
print "AND: %s" % conjuncao
print "OR : %s" % disjuncao
print "XOR: %s" % ouExclusivo
