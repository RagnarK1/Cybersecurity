#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc > 1) {
        printf("%s\n", argv[1]);  // Print the first command-line argument
    } else {
        printf("hello world\n");  // Default to "hello world" if no argument is provided
    }
    return 0;
}
