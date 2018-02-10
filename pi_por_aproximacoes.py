# coding: utf-8
'''
Na segunda metade do século XVII, Leibniz descobriu, através do método infinitesimal, uma soma
infinita que lentamente converge para o valor de pi. A série é a seguinte:

pi = 4 x ( 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15 + ... )

Além dessa série, várias outras foram descobertas que permitem calcular o valor de pi e outros
números irracionais de interesse. Por convergerem muito lentamente para o valor de pi, contudo,
são necessárias muitas iterações para calcular pi com significativa precisão.

Pede-se que você escreva um programa que permite calcular uma aproximação de pi, usando a série
descrita, com uma precisão arbitrária. O programa deve imprimir os valores aproximados de pi
calculados a cada passo, até o valor final.
'''

precisao = float(raw_input("Insira uma precisão: "))
i, somatorio, ultimo_somatorio  = 0, 0, 0
while True:
	# Soma dos termos da sequência pi (linha 6)
	somatorio += 4 * (-1) ** i * (1 / (2.0 * i + 1))
	i += 1
	print '%.6f' % somatorio
	if abs(somatorio - ultimo_somatorio ) < precisao:
		break
	ultimo_somatorio = somatorio
