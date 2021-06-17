/*Leia dois valores inteiros, no caso para variáveis A e B.
 A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.*/
 #include<stdio.h>

 int main()
 {
     int A, B, SOMA;
     scanf("%d", &A);
     scanf("%d", &B);
     SOMA = A + B;
     printf("SOMA = %i", SOMA);
     printf("\n");
     return 0;
 }