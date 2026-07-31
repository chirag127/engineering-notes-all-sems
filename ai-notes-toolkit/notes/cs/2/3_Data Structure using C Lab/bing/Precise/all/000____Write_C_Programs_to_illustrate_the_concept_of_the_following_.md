## Write C Programs to illustrate the concept of the following:

1. **Input and Output:** C provides several functions for input and output operations. For example, `scanf()` and `printf()` functions can be used for reading input from the user and displaying output to the user respectively. Here is an example program that reads an integer from the user and prints it back:

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

2. **Variables and Data Types:** C supports several data types, including `int`, `float`, `double`, and `char`. Variables are used to store data and must be declared with a data type before they can be used. Here is an example program that declares and initializes variables of different data types:

```c
#include <stdio.h>

int main() {
    int a = 5;
    float b = 3.14;
    double c = 2.718;
    char d = 'x';
    printf("a = %d, b = %f, c = %lf, d = %c\n", a, b, c, d);
    return 0;
}
```

3. **Conditional Statements:** C provides several conditional statements, including `if`, `if-else`, and `switch`. These statements allow the program to make decisions based on certain conditions. Here is an example program that uses an `if-else` statement to check if a number is positive or negative:

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    if (num >= 0) {
        printf("%d is positive\n", num);
    } else {
        printf("%d is negative\n", num);
    }
    return 0;
}
```

4. **Loops:** C provides several loop constructs, including `while`, `do-while`, and `for`. These constructs allow the program to repeat a set of statements a certain number of times or until a certain condition is met. Here is an example program that uses a `for` loop to print the first 10 natural numbers:

```c
#include <stdio.h>

int main() {
    int i;
    for (i = 1; i <= 10; i++) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

5. **Functions:** C allows the programmer to define their own functions. A function is a block of code that performs a specific task and can be called by other parts of the program. Here is an example program that defines a function to calculate the factorial of a number and uses it to calculate the factorial of 5:

```c
#include <stdio.h>

int factorial(int n) {
    int result = 1;
    int i;
    for (i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int num = 5;
    printf("Factorial of %d is %d\n", num, factorial(num));
    return 0;
}
```