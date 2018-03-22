/*
@version: 22/03/2018   @author: Vinicius Barbosa
@problem: Dados os valores-verdade das proposições p e q em lógica Fuzzy, encontre os valores verdade da disjunção e da
conjunção de p e q.
*/
import java.util.Scanner;

public class LogicaFuzzy {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double p, q, conjuncao, disjuncao;

        System.out.println("Na lógica Fuzzy, a proprosição tem um valor-verdade que é um número entre [0,1]");
        System.out.println();

        System.out.print("Insira o valor-verdade de p: ");
        p = input.nextDouble();

        System.out.print("Insira o valor-verdade de q: ");
        q = input.nextDouble();

        /* o valor-verdade da conjunção de duas propisições em lógica Fuzzy é o mínimo dos valores-verdade de duas proposições. Já o
        valor-verdade da disjunção é o máximo valor-verdade */

        if (p > q){
            conjuncao = q;
            disjuncao = p;
        } else {
            conjuncao = p;
            disjuncao = q;
        }

        System.out.println("CONJUNÇÃO: " + conjuncao);
        System.out.println("DISJUNÇÃO: " + disjuncao);
    }

}
