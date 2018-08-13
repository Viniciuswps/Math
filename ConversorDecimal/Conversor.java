package ConversorDecimal;

import java.util.Stack;

/**
 * Converte um número decimal para qualquer base entre 1 e 16
 * 
 */
public class Conversor {

	public static String converteBase(int decimal, int base) {

		if (base < 1 || base > 16) {
			throw new IllegalArgumentException("base inválida");
		}

		Stack<Integer> pilha = new Stack<Integer>();
		String binario = "";

		String bases = "0123456789ABCDEF";

		while (decimal > 0) {
			pilha.add(decimal % base);
			decimal /= base;
		}

		while (!pilha.isEmpty()) {
			binario += "" + bases.charAt(pilha.pop());
		}
		return binario;
	}
}
