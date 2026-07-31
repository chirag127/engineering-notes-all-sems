## Write C Programs to illustrate the concept of the following:

1. **Input and Output**: C language provides several built-in functions for performing input and output operations. For example, `scanf()` and `printf()` functions can be used to read input from the user and display output to the user, respectively.

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("You entered: %d\n", num);
    return 0;
}
```

2. **Variables and Data Types**: C language supports several data types, including `int`, `float`, `double`, `char`, and `void`. Variables are used to store data and must be declared before they can be used.

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

3. **Conditional Statements**: C language provides several conditional statements, including `if`, `if-else`, and `switch`, to perform different actions based on different conditions.

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    if (num % 2 == 0) {
        printf("%d is even\n", num);
    } else {
        printf("%d is odd\n", num);
    }
    return 0;
}
```

4. **Loops**: C language provides several loop statements, including `for`, `while`, and `do-while`, to repeatedly execute a block of code.

```c
#include <stdio.h>

int main() {
    int i;
    for (i = 1; i <= 5; i++) {
        printf("%d\n", i);
    }
    return 0;
}
```

5. **Functions**: C language allows the creation of user-defined functions to perform specific tasks. Functions can accept arguments and return values.

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 5, y = 10;
    int sum = add(x, y);
    printf("Sum = %d\n", sum);
    return 0;
}
```