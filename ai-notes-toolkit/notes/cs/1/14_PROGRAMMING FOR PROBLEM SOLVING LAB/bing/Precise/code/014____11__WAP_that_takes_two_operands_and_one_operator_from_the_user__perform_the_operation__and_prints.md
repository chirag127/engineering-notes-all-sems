## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

Here is an example of a program that takes two operands and one operator from the user, performs the operation, and prints the result using a switch statement:

```c
#include <stdio.h>

int main() {
    double num1, num2;
    char operator;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);

    printf("Enter two operands: ");
    scanf("%lf %lf", &num1, &num2);

    switch(operator) {
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
            printf("Error! operator is not correct");
    }

    return 0;
}
```

This program prompts the user to enter an operator and two operands. The operator is stored in the `operator` variable and the operands are stored in the `num1` and `num2` variables. The program then uses a switch statement to perform the operation specified by the operator and prints the result.

The switch statement checks the value of the `operator` variable and executes the corresponding case. If the operator is `+`, the program adds the two operands and prints the result. If the operator is `-`, the program subtracts the two operands and prints the result. If the operator is `*`, the program multiplies the two operands and prints the result. If the operator is `/`, the program divides the two operands and prints the result. If the operator is not one of these four values, the program prints an error message.

This is an example of how a switch statement can be used to perform different operations based on the value of a variable. In this case, the variable is the operator entered by the user. The switch statement allows the program to perform the correct operation based on the value of the operator. This makes the code more readable and easier to understand than using a series of if-else statements to perform the same task.