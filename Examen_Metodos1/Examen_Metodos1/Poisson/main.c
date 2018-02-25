#include <stdio.h>
#include <math.h>

long long int factorial(int N)
{
    long long ans = 1;
    int i;
    for(i=1; i <= N; i++)
        ans *= i;
    return ans;
}

int main() {
    int opcion, opcion2;

    do
    {
        printf( "\n --------------------------------------------------\n   Poisson (Probabilidad, Media, Varianza, Desviacion y acumulativas).");
        printf( "\n\nElije que operacion de Poisson deseas hacer: \n\t1) Distribucion de poisson \n\t2) Procesos de Poisson (Probabilidad en un tiempo dado)\n\t3) Salir\n");
        float lambda, tiempo, prob, x1, x2, alpha = 0;
        scanf( "%i", &opcion );

        switch(opcion) {
            case 1:
                printf( "\n Desea calcular:  \n\t1) Normal\n\t2) Acumulativa\nOpcion =");
                scanf("%i", &opcion2);
                if (opcion2 == 1){
                    printf("Introduce el valor de lambda:\n\t NOTA: Si tienes n > 50 y n*p < 5 (Siendo n el numero de pruebas y p la probabilidad de exito) lambda = n*P\n\nlambda = ");
                    scanf("%f", &lambda);
                    printf("\nIntroduce el valor de x =");
                    scanf("%f", &x1);
                    prob = ( exp(lambda * -1) * pow(lambda ,x1) )/factorial(x1);

                    printf("Probabilidad es: %f \nMedia y Varianza es: %f \nDesviacion Estandar: %f\n", prob, lambda, sqrt(lambda));

                } else if (opcion2 == 2) {
                    printf("Introduce el valor de lambda:\n\t NOTA: Si tienes n > 50 y n*p < 5 (Siendo n el numero de pruebas y p la probabilidad de exito) lambda = n*P\n\nlambda = ");
                    scanf("%f", &lambda);
                    printf("Introduce el valor del limite inferior =\n");
                    scanf("%f", &x1);
                    printf("Introduce el valor del limite superior =\n");
                    scanf("%f", &x2);
                    prob = 0;
                    for (int i = x1; i < (x2 + 1); i++) {
                        prob += (exp(lambda * -1) * pow(lambda, i)) / factorial(i);
                    }
                    printf("Probabilidad es: %f \nMedia y Varianza es: %f \nDesviacion Estandar: %f\n", prob, lambda,sqrt(lambda));
                }
                break;
            case 2:
                printf( "\n Desea calcular:  \n\t1) Normal\n\t2) Acumulativa\n");
                scanf("%i", &opcion2);
                if (opcion2 == 1){
                    printf("Introduce el valor de alpha =\n");
                    scanf("%f", &alpha);
                    printf("Introduce el tiempo =\n");
                    scanf("%f", &tiempo);
                    printf("Introduce el valor de x\n");
                    scanf("%f", &x1);

                    lambda = alpha * tiempo;
                    prob = ( exp(lambda * -1) * pow(lambda ,x1) )/factorial(x1);
                    printf("\nProbabilidad es: %f \nMedia y Varianza es: %f \nDesviacion Estandar: %f\n", prob, lambda, sqrt(lambda));

                } else if (opcion2 == 2) {
                    printf("Introduce el valor de alpha =\n");
                    scanf("%f", &alpha);
                    printf("Introduce el tiempo =\n");
                    scanf("%f", &tiempo);
                    printf("Introduce el limite inferior\n");
                    scanf("%f", &x1);
                    printf("Introduce el limite superior\n");
                    scanf("%f", &x2);

                    lambda = alpha * tiempo;

                    prob = 0;
                    for (int i = x1; i < (x2 + 1); i++) {
                        prob += (exp(lambda * -1) * pow(lambda, i)) / factorial(i);

                    }
                    printf("Probabilidad es: %f \nMedia y Varianza es: %f \nDesviacion Estandar: %f\n", prob, lambda, sqrt(lambda));
                }
                break;
            default:
                printf( "\nElija otra opcion.");
                break;
        }

    } while (opcion != 3);

    return 0;
}