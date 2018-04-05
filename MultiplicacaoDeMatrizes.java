/*
@versao: 05/04/2018   @autor: Vinicius Barbosa
:::::::: Programa que recebe duas matrizes(A e B) e imprime, quando possível, o produto matricial A x B.
*/
import java.util.Scanner;

public class MultiplicacaoDeMatrizes {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // MATRIZ A
        System.out.println("| -- Matriz A -- |");
        System.out.print("Insira o número de linhas: ");
        int linhasA = input.nextInt();
        System.out.print("Insira o número de colunas: ");
        int colunasA = input.nextInt();

        int[][] A = new int[linhasA][colunasA];

        for (int i = 0; i < linhasA ; i++) {
            for (int j = 0; j < colunasA; j++) {
                System.out.printf("Insira o elemento da %d° linhas e %d° coluna: ", i + 1, j + 1);
                A[i][j] = input.nextInt();
            }
        }

        // MATRIZ B
        System.out.println("| -- Matriz B -- |");
        System.out.print("Insira o número de linhas: ");
        int linhasB = input.nextInt();
        System.out.print("Insira o número de colunas: ");
        int colunasB = input.nextInt();

        int[][] B = new int[linhasB][colunasB];

        for (int i = 0; i < linhasB ; i++) {
            for (int j = 0; j < colunasB; j++) {
                System.out.printf("Insira o elemento da %d° linhas e %d° coluna: ", i + 1, j + 1);
                B[i][j] = input.nextInt();
            }
        }

        // imprimindo A
        System.out.println();
        System.out.println("A: ");
        for (int i = 0; i < linhasA ; i++) {
            for (int j = 0; j < colunasA; j++) {
                System.out.printf("|%d| ", A[i][j]);
            }
            System.out.println();
        }

        System.out.println();

        // imprimindo B
        System.out.println();
        System.out.println("B: ");
        for (int i = 0; i < linhasB ; i++) {
            for (int j = 0; j < colunasB; j++) {
                System.out.printf("|%d| ", B[i][j]);
            }
            System.out.println();
        }

        
        if (colunasA == linhasB) {
            int ordem = linhasA; // == colunasB
            int[][] AB = new int[ordem][ordem];

            for (int i = 0; i < ordem ; i++) {
                for (int j = 0; j < ordem; j++) {

                    for (int k = 0; k < colunasA ; k++) {
                        AB[i][j] += A[i][k] * B[k][j] ;
                    }
                    
                }
            }

            // imprimindo AB
            System.out.println();
            System.out.println("AB: ");
            for (int i = 0; i < AB.length ; i++) {
                for (int j = 0; j < AB[i].length; j++) {
                    System.out.printf("|%d| ", AB[i][j]);
                }
                System.out.println();
            }
        }

    }
}
