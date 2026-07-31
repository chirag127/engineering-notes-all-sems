## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

A switch statement is a control structure that allows us to choose which statement to execute next. It is an alternative to the if-else-if ladder statement. The switch statement evaluates an expression and executes the corresponding case that matches the expression's value.

Here is an example of a program that takes two operands and one operator from the user, performs the operation, and prints the result by using a switch statement:

```c
#include <stdio.h>

int main()
{
    double num1, num2;
    char operator;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);

    printf("Enter two operands: ");
    scanf("%lf %lf", &num1, &num2);

    switch(operator)
    {
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

In this program, the user is prompted to enter an operator and two operands. The operator is stored in the `operator` variable and the operands are stored in the `num1` and `num2` variables.

The switch statement then evaluates the `operator` variable and executes the corresponding case that matches the value of the `operator` variable. If the `operator` variable is `'+'`, the case `case '+'` is executed and the result of the addition of `num1` and `num2` is printed. Similarly, if the `operator` variable is `'-'`, the case `case '-'` is executed and the result of the subtraction of `num1` and `num2` is printed.

If the `operator` variable does not match any of the cases, the `default` case is executed and an error message is printed.

This is how you can use a switch statement to take two operands and one operator from the user, perform the operation, and print the result. You can modify the code to add more cases and operators as per your requirements.