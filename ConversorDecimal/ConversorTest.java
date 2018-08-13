package ConversorDecimal;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class ConversorTest {

	@Test(expected = IllegalArgumentException.class)
	public void testBaseInvalidaNegativa() {
		Conversor.converteBase(25, -1);
	}

	@Test(expected = IllegalArgumentException.class)
	public void testBaseInvalidaMaiorQue16() {
		Conversor.converteBase(25, 17);
	}

	@Test
	public void testConverteQualquerBase() {
		assertEquals("19", Conversor.converteBase(25, 16));
		assertEquals("23463", Conversor.converteBase(10035, 8));
		assertEquals("2733", Conversor.converteBase(10035, 16));
		assertEquals("3E7", Conversor.converteBase(999, 16));
	}

}
