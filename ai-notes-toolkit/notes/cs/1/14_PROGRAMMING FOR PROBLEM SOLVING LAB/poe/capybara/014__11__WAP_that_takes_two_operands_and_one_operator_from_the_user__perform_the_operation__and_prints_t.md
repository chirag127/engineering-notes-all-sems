## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

Here are the steps to perform this operation:

1. First, we will take input from the user in the form of two operands and one operator.
2. We will then use a switch statement to determine which operation needs to be performed based on the operator entered by the user.
3. We will perform the operation based on the operator entered by the user and the two operands entered by the user.
4. Finally, we will print the result of the operation performed.

Here is the code snippet for the same:

```
#include <stdio.h>

int main() {
    float operand1, operand2, result;
    char operator;

    printf("Enter two operands: ");
    scanf("%f %f", &operand1, &operand2);

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator);

    switch(operator) {
        case '+':
            result = operand1 + operand2;
            break;
        case '-':
            result = operand1 - operand2;
            break;
        case '*':
            result = operand1 * operand2;
            break;
        case '/':
            result = operand1 / operand2;
            break;
        default:
            printf("Error! operator is not correct");
            break;
    }

    printf("%.2f %c %.2f = %.2f", operand1, operator, operand2, result);
    return 0;
}
```

This code will take two operands and one operator as input from the user and perform the operation based on the operator entered by the user. It will then print the result of the operation performed.