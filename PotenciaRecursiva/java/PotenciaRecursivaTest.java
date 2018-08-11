package PotenciaRecursiva.java;

import static org.junit.Assert.assertEquals;

public class PotenciaRecursivaTest {

	@org.junit.Test
	public void testComBaseNula() {
		assertEquals(0, PotenciaRecursiva.potencia(0, 1), 00000001);
		assertEquals(0, PotenciaRecursiva.potencia(0, 10), 00000001);
	}

	@org.junit.Test(expected = IllegalArgumentException.class)
	public void testIndeterminacaoZeroElevadoAZero() {
		assertEquals(1, PotenciaRecursiva.potencia(0, 0), 00000001);
	}

	@org.junit.Test(expected = IllegalArgumentException.class)
	public void testIndeterminacaoDivisaoPorZero() {
		assertEquals(1, PotenciaRecursiva.potencia(0, -1), 00000001);
	}

	@org.junit.Test
	public void testComExpoenteNulo() {
		assertEquals(1, PotenciaRecursiva.potencia(1, 0), 00000001);
		assertEquals(1, PotenciaRecursiva.potencia(2, 0), 00000001);
		assertEquals(1, PotenciaRecursiva.potencia(100, 0), 00000001);
	}

	@org.junit.Test
	public void testComCasosNormais() {
		assertEquals(2, PotenciaRecursiva.potencia(2, 1), 00000001);
		assertEquals(9, PotenciaRecursiva.potencia(3, 2), 00000001);
		assertEquals(27, PotenciaRecursiva.potencia(3, 3), 00000001);
	}

	@org.junit.Test
	public void testComExpoenteNegativo() {
		assertEquals(1 / 3, PotenciaRecursiva.potencia(3, -1), 00000001);
		assertEquals(1 / 27, PotenciaRecursiva.potencia(3, -3), 00000001);
		assertEquals(1 / 9, PotenciaRecursiva.potencia(-3, -2), 00000001);
		assertEquals(1, PotenciaRecursiva.potencia(1, -100), 00000001);
	}

}
