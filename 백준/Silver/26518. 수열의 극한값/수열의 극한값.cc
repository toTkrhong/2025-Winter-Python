#include <stdio.h>
#include <math.h>

int main() {
    double b, c;
    scanf("%lf %lf", &b, &c);

    double result = (b + sqrt(b * b + 4 * c)) / 2.0;

    printf("%.9lf\n", result);

    return 0;
}
