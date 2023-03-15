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
            printf("Error! Invalid operator.");
    }

    return 0;
}
```

This program prompts the user to enter an operator and two operands. It then uses a switch statement to perform the operation based on the operator entered by the user. The result of the operation is then printed to the screen.

Some key points to note about this program:
- The `switch` statement is used to perform different actions based on the value of the `operator` variable.
- The `case` statements within the `switch` statement define the actions to be performed for each possible value of the `operator` variable.
- The `break` statement is used to exit the `switch` statement once the appropriate action has been performed.
- If the value of the `operator` variable does not match any of the `case` statements, the `default` statement is executed, which in this case prints an error message to the screen.

This is just one example of how a program can take two operands and one operator from the user, perform the operation, and print the result using a switch statement. There are many other ways to implement this functionality, and the specific details may vary depending on the requirements of the program and the preferences of the programmer.