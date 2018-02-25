#include <math.h>
#include <stdio.h>

int main()
{
    float media = 0;
    float lambda = 0;
    int opcion = 0;

    printf( "\n   Introduzca el valor medio de la distribucion exponencial. ");
    scanf( "%f", &media );

    lambda = 1/media;

    printf("\n   El valor de lambda es: %f", lambda);

    printf("\n   Seleccione que desea calcular: ");
    printf("\n   1. Calcular probabilidad entre 'x' y 'y' ");
    printf("\n   2. Calcular la probabilidad sea a lo más de 'x' ");
    printf("\n   Introduzca una opcion:  ");
    scanf( "%i", &opcion );

    float resultado = 0;
    float limin = 0;
    float limsup = 0;
    float probin = 0;
    float probsup = 0;

    switch(opcion){
        case 1:

            printf("\n Introduzca el limite inferior:  ");
            scanf( "%f", &limin );

            printf("\n Introduzca el limite superior:  ");
            scanf( "%f", &limsup );


            probin = (1 - (exp(-(lambda*limin))));
            probsup = (1 - (exp(-(lambda*limsup))));

            resultado = probsup - probin;

            printf("\n El resultado es: %f ", resultado);


        break;

        case 2:
            printf("\n Introduzca el limite superior:  ");
            scanf( "%f", &limsup );

            resultado = (1 - (exp(-(lambda*limsup))));

            printf("\n El resultado es: %f ", resultado);
        break;
    }

}
