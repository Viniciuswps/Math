/*
@problema: Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.

@versao: 28/03/2018   @autor: Vinicius Barbosa
*/

public class ComparacaoDoCrescimentoPopulacionalEmDoisPaises {
    public static void main(String[] args){
        int populacaoA = 80000, populacaoB = 200000;

        int cont = 0;
        while ( populacaoA < populacaoB) {
            cont++;
            populacaoA *= 1.03; // aumento de 3%
            populacaoB *= 1.015; // aumento de 1,5%

        }

        /*  Análise matemática (conferindo a resposta do programa).

        As funções que modelam o problema são A(x) = 80000 * (1.03)^x e B(x) = 200000 * (1.015)^x.
        O ano x onde A iguala B é a solução da equação 80000 * (1.03)^x = 200000 * (1.015)^x
        Após algumas manipulções algébricas (resolvendo a equação) ... x = log(2/5) na base 1015 / 1030
        Logo x = 62.459.... Ou seja A iguala B quando x = 62.49 e supera para qualquer x >62, por exemplo: 63   */

        double x = Math.log(2.0/5) / Math.log(1015.0/1030);

        if (cont * 1.0 ==  Math.ceil(x)) {
            System.out.println("O número de anos necessários é " + cont);
        }
    }
}
