#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc > 1) {
        printf("%s", argv[1]);  // Print the first command-line argument
    } else {
        printf("01");  // Default to "01" if no argument is provided
    }
    return 0;
}
