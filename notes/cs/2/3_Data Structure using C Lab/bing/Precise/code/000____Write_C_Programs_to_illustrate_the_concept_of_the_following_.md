## Write C Programs to illustrate the concept of the following:

1. **Input and Output**: In C, input and output operations are performed using the standard library functions `scanf()` and `printf()`. Here is an example program that reads an integer from the user and prints it back to the screen:

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    printf("You entered: %d\n", num);
    return 0;
}
```

2. **Variables and Data Types**: C has several basic data types, including `int` for integers, `float` for floating-point numbers, and `char` for characters. Variables are used to store data and must be declared with a data type before they can be used. Here is an example program that declares and initializes variables of different data types:

```c
#include <stdio.h>

int main() {
    int a = 5;
    float b = 3.14;
    char c = 'A';
    printf("a = %d, b = %f, c = %c\n", a, b, c);
    return 0;
}
```

3. **Conditional Statements**: C has several conditional statements, including `if`, `if-else`, and `switch`. These statements allow the program to make decisions based on certain conditions. Here is an example program that uses an `if-else` statement to check if a number is positive, negative, or zero:

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    if (num > 0) {
        printf("The number is positive.\n");
    } else if (num < 0) {
        printf("The number is negative.\n");
    } else {
        printf("The number is zero.\n");
    }
    return 0;
}
```
