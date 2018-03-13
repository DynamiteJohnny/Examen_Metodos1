#include <stdio.h>
#include <math.h>


int main()
{
        float media;
        float desviacion;
        float limsup;
        float liminf;

        float phione;
        float phitwo;

        int opcion;

        while(1){
            printf( "\n   Distribucion Normal.");

            printf("\n   Introduzca el valor medio. ");
            scanf( "%f", &media );
            printf("\n   Introduzca la desviacion estandar. ");
            scanf( "%f", &desviacion );

            printf("\n   1.- Limite sup e inf \n 2.- Probabilidad mayor o igual a x \n 3.- Probabilidad menor o igual a x \n");
            scanf( "%i", &opcion );

            switch(opcion){
                case 1:
                printf("\n   Introduzca el limite inferior. ");
                scanf( "%f", &liminf );
                printf("\n   Introduzca el limite superior. ");
                scanf( "%f", &limsup );

                phione = (limsup - media)/desviacion;
                phitwo = (liminf - media)/desviacion;

                printf("\n   El resultado es: Phi( %f ) - Phi( %f ) \n", phione, phitwo);
                break;

                case 2:
                printf("\n   Introduzca x. ");
                scanf( "%f", &limsup );

                phione = (limsup - media)/desviacion;
                printf("\n   El resultado es: 1 - Phi( %f ) \n", phione);
                break;

                case 3:
                printf("\n   Introduzca x. ");
                scanf( "%f", &liminf );

                phione = (liminf - media)/desviacion;
                printf("\n   El resultado es: Phi( %f ) \n", phione);
                break;

            }



        }



}
