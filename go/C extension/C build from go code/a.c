#include <stdio.h>
#include "usedByC.h"

int main(int argc, char **argv) {
    GoInt x = 12;
    GoInt y = 23;
    printf("About to call a Go function!\n");
    PrintMessage();
    GoInt m = Multiply(x, y);
    printf("Product: %d\n", (int)m);
    printf("It worked!\n");
    return 0;
}
//  gcc -o a a.c ./usedByC.o