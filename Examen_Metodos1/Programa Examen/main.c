#include <math.h>
#include <stdio.h>

int main()
{
    int opcion;

    do
    {
        printf( "\n   1. Formulas generales (media, varianza y desviacion estandar).");
        printf( "\n   2. Calcular la mitad de un n%cmero entero.", 163 );
        printf( "\n   3. Calcular el cuadrado de un n%cmero entero.", 163 );
        printf( "\n   4. Salir." );
        printf( "\n\n   Introduzca opci%cn (1-4): ", 162 );

        scanf( "%d", &opcion );

        switch ( opcion )
        {
            case 1: printf( "\n   Introduzca el número de x's " );
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
                break;

            //case 2: //printf( "\n   Introduzca un n%cmero entero: ", 163 );
                    //scanf( "%d", &n );
                    //printf( "\n   La mitad de %d es %f\n\n", n, ( float ) n / 2 );
                   // break;

           //case 3: //printf( "\n   Introduzca un n%cmero entero: ", 163 );
                    //scanf( "%d", &n );
                    //printf( "\n   El cuadrado de %d es %d\n\n", n, ( int ) pow( n, 2 ) );
                    //break;
         }

    } while ( opcion != 4 );

    return 0;
}
