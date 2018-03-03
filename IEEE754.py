# coding: utf-8
'''
@disciplina: Introdução à Computação;
@objetivo: Esse programa converte números para o padrão IEEE754;
@author: Vinicius Barbosa da Silva;
@version 03/mar/2018
'''




def conversor_decimal_p_binario(numero):
    numero = numero.split('.')
    saida = ''
    if len(numero) > 1: # Se há parte fracionária
        p_inteira = ''
        parte_inteira = numero[0]
        parte_fracionaria = numero[1]

        while parte_inteira >= 2:
            saida += str(parte_inteira%2)
            parte_inteira /= 2
        else:
            if parte_inteira != 0:
                p_inteira += str(1)
            else: p_inteira = '0'
        # invertendo a ordem da lista
        aux = ''
        for i in range(len(p_inteira)-1, -1, -1):
            aux += list[i]
        saida = aux
        saida += '.' # separando a parte inteira da fracionária


        '''15.75'''
        # parte_fracionaria /= 1.0 * 10 ** len(parte_fracionada)
        p_fracionaria = ''
        while 2 * parte_fracionaria != 100:
            if 2 * parte_fracionaria > 100:
                p_fracionaria += '1'
                parte_fracionaria = 2 * parte_fracionaria - 100
            else:
                parte_fracionaria += '0'
                parte_fracionaria = 2 * parte_fracionaria

        saida += parte_fracionaria
        return saida






    elif len(numero) == 1: # Se é um número inteiro
        parte_inteira = numero[0]





    # invertendo a ordem da list
    saida = ''
    for i in range(len(list)-1, -1, -1):
        saida += list[i]
    return int(saida)

while True:
    entrada = raw_input('digite um inteiro: ')
    if entrada == 'a': break
    print conversor_decimal_p_binario(entrada)


def main():
    while True:
        print '| ---------- Conversor IEEE-754 ---------- |'
        print ''
        print '1) N° decimal ==>> N° binário'
        print '2) N° binário ==>> N° decimal'
        print 's) Sair'
        entrada = raw_input()

        if entrada == '1':
            print ''
            print 'Digite um número decimal(ex: 15.75): '
            entrada = raw_input().split(',')

            if len(entrada) > 1: # Se o número é do tipo ploat
                parte_inteira = entrada[0]
                parte_fracionada = entrada[1]
                p_inteira_em_binario = conversor_decimal_p_binario(parte_inteira)


        elif entrada == '2':
            pass

        elif entrada == 's':
            break

        else:
            print 'Código inválido'
