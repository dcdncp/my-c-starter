#include "stdio.h"
#include "add.h"

int main() {
    int a = 5;
    int b = 3;
    int sum = add(a, b);
    printf("%d + %d = %d\n", a, b, sum);
    return 0;
}