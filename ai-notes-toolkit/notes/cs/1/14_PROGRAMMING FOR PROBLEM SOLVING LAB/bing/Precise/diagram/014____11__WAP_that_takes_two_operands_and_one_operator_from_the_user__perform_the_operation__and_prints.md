## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

A switch statement is a control structure that allows us to choose which statement to execute next. It can be used to replace multiple if-else statements. Here is an example of a program that takes two operands and one operator from the user, performs the operation, and prints the result using a switch statement:

```c
#include <stdio.h>

int main() {
    double num1, num2;
    char operator;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);

    printf("Enter two operands: ");
    scanf("%lf %lf", &num1, &num2);

    switch (operator) {
        case '+':
            printf("%.1lf + %.1lf = %.1lf", num1, num2, num1 + num2);
            break;
        case '-':
            printf("%.1lf - %.1lf = %.1lf", num1, num2, num1 - num2);
            break;
        case '*':
            printf("%.1lf * %.1lf = %.1lf", num1, num2, num1 * num2);
            break;
        case '/':
            printf("%.1lf / %.1lf = %.1lf", num1, num2, num1 / num2);
            break;
        default:
            printf("Error! Invalid operator.");
    }

    return 0;
}
```

This program prompts the user to enter an operator and two operands. The operator is stored in the `operator` variable and the operands are stored in the `num1` and `num2` variables. The `switch` statement then checks the value of the `operator` variable and executes the corresponding case. If the operator is `+`, the program adds the two operands and prints the result. If the operator is `-`, the program subtracts the two operands and prints the result. If the operator is `*`, the program multiplies the two operands and prints the result. If the operator is `/`, the program divides the two operands and prints the result. If the operator is not one of the four valid operators, the program prints an error message.