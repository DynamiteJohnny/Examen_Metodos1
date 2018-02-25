#include <math.h>
#include <stdio.h>

int main()
{
        printf( "\n   Distribución uniforme. ");
        printf( "\n   Introduzca el numero de x's " );
        int n = 0;
        float media = 0;
        scanf( "%i", &n );
        float valores[n];
        int i;
        for (i = 0; i < n; i++) {
            printf( "\n   Introduzca valor de x%i ",i +1 );
            scanf( "%f", &valores[i] );
            media += (valores[i]/n);
        }

        float varianza = 0;
        for (i = 0; i < n; i++) {
            varianza += ((pow((valores[i] - media),2))/n);
        }


        printf("\n    La media es: %f", media);
        printf("\n    La varianza es: %f", varianza);
        printf( "\n   El valor de la desviacion  es: %f \n\n",sqrt(varianza) );

        return 0;

}
