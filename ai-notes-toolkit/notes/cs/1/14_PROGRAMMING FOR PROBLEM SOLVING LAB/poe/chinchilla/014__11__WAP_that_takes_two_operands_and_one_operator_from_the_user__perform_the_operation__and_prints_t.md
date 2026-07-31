## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

When writing a computer program, it is often necessary to perform mathematical operations. One common way to do this is by using operators such as addition, subtraction, multiplication, and division. In this program, we will create a calculator that takes two operands and one operator from the user and performs the operation using a switch statement.

Here are the steps to create the program:

1. First, we need to declare three variables: two operands and one operator. We can use the `float` data type to allow for decimal values.

2. Next, we need to prompt the user to enter the two operands and the operator. We can use the `scanf()` function to read in the user's input.

3. After we have the user's input, we can use a switch statement to determine which mathematical operation to perform based on the operator entered. We can use the following cases for the different operators:

   - Case '+': Add the two operands together and print the result.
   - Case '-': Subtract the second operand from the first operand and print the result.
   - Case '*': Multiply the two operands together and print the result.
   - Case '/': Divide the first operand by the second operand and print the result. It is important to check for a divide-by-zero error.

4. Finally, we can use the `printf()` function to display the result to the user.

Here is an example code for the program:

```c
#include <stdio.h>

int main() {
    float operand1, operand2;
    char operator;

    printf("Enter the first operand: ");
    scanf("%f", &operand1);

    printf("Enter the operator (+, -, *, /): ");
    scanf(" %c", &operator);

    printf("Enter the second operand: ");
    scanf("%f", &operand2);

    switch(operator) {
        case '+':
            printf("%.2f + %.2f = %.2f\n", operand1, operand2, operand1 + operand2);
            break;
        case '-':
            printf("%.2f - %.2f = %.2f\n", operand1, operand2, operand1 - operand2);
            break;
        case '*':
            printf("%.2f * %.2f = %.2f\n", operand1, operand2, operand1 * operand2);
            break;
        case '/':
            if(operand2 == 0) {
                printf("Error: Cannot divide by zero\n");
                break;
            }
            printf("%.2f / %.2f = %.2f\n", operand1, operand2, operand1 / operand2);
            break;
        default:
            printf("Error: Invalid operator\n");
            break;
    }

    return 0;
}
```

In conclusion, by following the above steps, we can create a program that takes two operands and one operator from the user, performs the operation, and prints the result using a switch statement. This program can be a useful tool for performing basic mathematical calculations.