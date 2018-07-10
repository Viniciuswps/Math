import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class MultiplicacaoDeMatrizesTest {

	/**
	 * primeira multiplicação.
	 */
	private int[][] matA = { { 3, 5, -2 }, { 2, 8, -6 } };
	private int[][] matB = { { 2, 3, 1 }, { 5, -7, -2 }, { 9, 0, -3 } };
	private int[][] matAB = { { 13, -26, -1 }, { -10, -50, 4 } };
	private Matriz A;
	private Matriz B;
	private Matriz AB;

	/**
	 * segunda multiplicação.
	 */
	private int[][] matC = { { 1, 5, 2 }, { -1, 4, 7 } };
	private int[][] matD = { { 1, -1 }, { 2, 3 }, { -3, 0 } };
	private int[][] matCD = { { 5, 14 }, { -14, 13 } };
	private Matriz C;
	private Matriz D;
	private Matriz CD;

	@Before
	public void primeiraMatriz() {
		A = new Matriz(matA, "A");
		B = new Matriz(matB, "B");
	}

	@Before
	public void segundaMatriz() {
		C = new Matriz(matC, "C");
		D = new Matriz(matD, "D");
	}

	/**
	 * Testa o método multiplicaMatrizes.
	 */
	@Test
	public void testMultiplicaMatrizes() {
		AB = new Matriz(matAB, "AB");
		assertEquals(AB, A.multiplicaMatriz(B));

		CD = new Matriz(matCD, "CD");
		assertEquals(CD, C.multiplicaMatriz(D));
	}

}
