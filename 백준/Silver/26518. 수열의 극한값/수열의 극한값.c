#pragma warning (disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


/*int compare(const void* a, const void* b) {
	return(*(int*)a - *(int*)b);
}*/
int main() {
	long double n1, n2, n3, n4;
	scanf("%Lf %Lf %Lf %Lf", &n1, &n2, &n3, &n4);
	printf("%.9Lf",(n1 + sqrt(n1 * n1 + 4 * n2)) / 2);
}