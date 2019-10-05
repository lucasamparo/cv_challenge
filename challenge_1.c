#include <stdio.h>

// Montei as equações dos circulos para o par de pontos e subtraí as duas
// Apliquei substituições para encontrar as constantes A, B e C
// Montei um sistema de equação com duas equações e as duas incognitas que representam o centro dos circulos
// Resolvi o sistema de equações aplicando substituições
// Imprimi o resultado com 2 casas decimais
int main() {
    int i, n;
    float ax1, ax2, ay1, ay2, bx1, bx2, by1, by2;
    float A1, B1, C1, A2, B2, C2; 
    float x, y;

    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        scanf("%f %f", &ax1, &ay1);
        scanf("%f %f", &bx1, &by1);

        scanf("%f %f", &ax2, &ay2);
        scanf("%f %f", &bx2, &by2);

        //(x1 - x)^2 + (y1 - y)^2 = r^2
        //(x2 - x)^2 + (y2 - y)^2 = r^2
        //Subtraindo... Expandindo...
        // x*(2*(ax2 - ax1)) + y*(2*(ay2 - ay1)) + (x1^2 - x2^2 + y1^2 - y2^2) = 0
        // A*x + B*y + C = 0

        //Constantes para o primeiro par de pontos
        A1 = 2 * (ax2 - ax1);
        B1 = 2 * (ay2 - ay1);
        C1 = ax1*ax1 - ax2*ax2 + ay1*ay1 - ay2*ay2;

        //Constantes para o segundo par de pontos
        A2 = 2 * (bx2 - bx1);
        B2 = 2 * (by2 - by1);
        C2 = bx1*bx1 - bx2*bx2 + by1*by1 - by2*by2;

        //Resolvendo o sistema de equações 
        // A1x + B1y + C1 = 0
        // A2x + B2y + C2 = 0
        y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1);
        x = - (y*B1 + C1) / A1;

        printf("Caso #%d: %.2f %.2f\n", i+1, x, y);
    }
}