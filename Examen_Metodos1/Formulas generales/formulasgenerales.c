#include <math.h>
#include <stdio.h>

int main()
{
    int opcion = 0;

    do
    {
        printf( "\n   Formulas generales (media, varianza y desviacion estandar).");
        printf( "\n   Introduzca el numero de x's " );
        int n = 0;
        scanf( "%i", &n );
        float probequis[n];
        int i;
        for (i = 0; i < n; i++) {
            printf( "\n   Introduzca probabilidad de x%i ",i +1 );
            scanf( "%f", &probequis[i] );
        }
        float media = 0;
        for (i = 0; i < n; i++) {
            media += (1 + i) * probequis[i];
        }
        float varianza = 0;
        for (i = 0; i < n; i++) {
            varianza += pow((1 + i - media),2) * probequis[i];
        }
        printf( "\n   El valor de la media es: %f",media );
        printf( "\n   El valor de la varianza es: %f",varianza );
        printf( "\n   El valor de la desviacion  es: %f \n\n",sqrt(varianza) );

    } while (opcion == 0);

    return 0;
}
