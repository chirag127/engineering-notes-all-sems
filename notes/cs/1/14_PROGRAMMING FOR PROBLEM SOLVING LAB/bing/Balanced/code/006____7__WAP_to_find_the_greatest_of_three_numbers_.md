Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to find the greatest of three numbers. Here is the content in markdown format:

## 7. WAP to find the greatest of three numbers.

- To find the greatest of three numbers, we need to compare them using some conditional statements, such as `if`, `else if`, and `else`.
- We can use the `>` operator to check if one number is greater than another.
- We can use the `=` operator to check if two numbers are equal.
- We can use the `&&` operator to combine two conditions with a logical AND.
- We can use the `||` operator to combine two conditions with a logical OR.
- We can use the `!` operator to negate a condition with a logical NOT.
- We can use the `printf` function to print the output to the screen.
- We can use the `scanf` function to read the input from the keyboard.
- We can use the `int` data type to store integer values.
- We can use the `main` function to start the program execution.

- Here is an example of a program to find the greatest of three numbers in C language:

```c
#include <stdio.h>
int main()
{
    int a, b, c; // declare three integer variables
    printf("Enter three numbers: "); // prompt the user to enter three numbers
    scanf("%d %d %d", &a, &b, &c); // read the input from the keyboard and store it in the variables
    if (a > b && a > c) // check if a is greater than both b and c
    {
        printf("%d is the greatest number.\n", a); // print a as the greatest number
    }
    else if (b > a && b > c) // check if b is greater than both a and c
    {
        printf("%d is the greatest number.\n", b); // print b as the greatest number
    }
    else if (c > a && c > b) // check if c is greater than both a and b
    {
        printf("%d is the greatest number.\n", c); // print c as the greatest number
    }
    else if (a == b && a > c) // check if a and b are equal and greater than c
    {
        printf("%d and %d are the greatest numbers.\n", a, b); // print a and b as the greatest numbers
    }
    else if (a == c && a > b) // check if a and c are equal and greater than b
    {
        printf("%d and %d are the greatest numbers.\n", a, c); // print a and c as the greatest numbers
    }
    else if (b == c && b > a) // check if b and c are equal and greater than a
    {
        printf("%d and %d are the greatest numbers.\n", b, c); // print b and c as the greatest numbers
    }
    else // otherwise, all three numbers are equal
    {
        printf("%d, %d and %d are the greatest numbers.\n", a, b, c); // print all three numbers as the greatest numbers
    }
    return 0; // end the program
}
```