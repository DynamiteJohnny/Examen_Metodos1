#include <math.h>
#include <stdio.h>

unsigned factorial(unsigned n)
{
    if (n == 1 || n == 0) {
        return 1;
    }
    else{
        return n * factorial(n - 1);
    }
}

int main()
{
    int opcion = 0;

    do
    {
        printf( "\n   Distribucion Binomial(Probabilidad, Media, Varianza, Desviacion y acumulativas).");
        printf( "\n\nElija una opcion\n1)Normal\n2)Acumulativa");
        int opcion;
        float p = 0;
        float q = 0;
        float n = 0;
        scanf( "%i", &opcion );

        switch(opcion) {
            case 1:
                printf( "\n   Introduzca la probabilidad de exito (p) " );
                scanf( "%f", &p );
                printf( "\n   Introduzca la probabilidad de fracaso (q) " );
                scanf( "%f", &q );
                printf( "\n   Introduzca el numero de pruebas (n) " );
                scanf( "%f", &n );
                printf( "\n   Introduzca el numero de exitos (k) " );
                float k = 0;
                scanf( "%f", &k );

                float res = ((factorial(n))/(factorial(k)*factorial(n - k))*(pow(p,k)*pow(q,n - k)));

                printf( "\n   La probabilidad es: %f",res );
                printf( "\n   El valor de la media es: %f",n*p );
                printf( "\n   El valor de la varianza es: %f",n*p*q );
                printf( "\n   El valor de la desviacion  es: %f \n\n",sqrt(n*p*q) );
            break;
            case 2:
                printf( "\n   Introduzca la probabilidad de exito (p) " );
                scanf( "%f", &p );
                printf( "\n   Introduzca la probabilidad de fracaso (q) " );
                scanf( "%f", &q );
                printf( "\n   Introduzca el numero de pruebas (n) " );
                scanf( "%f", &n );
                printf( "\n   Dame el limite inferior para hacer las pruebas (k0) " );
                float k0 = 0;
                scanf( "%f", &k0 );
                printf( "\n   Dame el limite superior para hacer las pruebas (kn) " );
                float kn = 0;
                scanf( "%f", &kn );

                float resvarios = 0;
                float i = 0;
                float aux;
                for (i = k0; i <= kn; i++) {
                    aux = (((factorial(n))/(factorial(i)*factorial(n - i)))*(pow(p,i)*pow(q,n - i)));
                    printf( "\n   La probabilidad de %f es: %f",i,aux );
                    resvarios += aux;
                }

                printf( "\n\n   La probabilidad total es: %f",resvarios );
                printf( "\n   El valor de la media es: %f",n*p );
                printf( "\n   El valor de la varianza es: %f",n*p*q );
                printf( "\n   El valor de la desviacion  es: %f \n\n",sqrt(n*p*q) );

            break;
            default:
                printf( "\nElija otra opcion.");
            break;
        }

    } while (opcion == 0);

    return 0;
}
