Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a content on the topic: ## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

Here is the content I have written in markdown format:

## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

- A switch statement is a control structure that allows us to execute different blocks of code based on the value of a variable or expression.
- A switch statement has the following syntax:

```c
switch (expression) {
  case value1:
    // statements to execute when expression is equal to value1
    break;
  case value2:
    // statements to execute when expression is equal to value2
    break;
  ...
  default:
    // statements to execute when expression does not match any of the cases
    break;
}
```

- The expression can be any valid C expression that evaluates to an integer or a character value.
- The cases are labels that represent the possible values of the expression. Each case is followed by a colon (:).
- The statements inside each case are the actions to be performed when the expression matches the case value. Each case should end with a break statement, which exits the switch statement and prevents the execution of the following cases.
- The default case is optional and it is executed when the expression does not match any of the cases. It should also end with a break statement.
- The switch statement evaluates the expression once and compares it with each case value in order. If a match is found, it executes the corresponding statements and exits the switch statement. If no match is found, it executes the default case if present, or skips the switch statement otherwise.

- To write a program that takes two operands and one operator from the user, perform the operation, and prints the result by using switch statement, we can follow these steps:

  - Declare three variables to store the operands, the operator, and the result. For example, we can use `double num1, num2, result;` and `char op;`.
  - Prompt the user to enter the first operand and store it in `num1`. For example, we can use `printf("Enter the first operand: ");` and `scanf("%lf", &num1);`.
  - Prompt the user to enter the second operand and store it in `num2`. For example, we can use `printf("Enter the second operand: ");` and `scanf("%lf", &num2);`.
  - Prompt the user to enter the operator and store it in `op`. For example, we can use `printf("Enter the operator (+, -, *, /): ");` and `scanf(" %c", &op);`. Note the space before the `%c` to skip any whitespace characters.
  - Use a switch statement to evaluate the operator and perform the corresponding operation on the operands. Store the result in `result`. For example, we can use:

```c
switch (op) {
  case '+':
    // perform addition
    result = num1 + num2;
    break;
  case '-':
    // perform subtraction
    result = num1 - num2;
    break;
  case '*':
    // perform multiplication
    result = num1 * num2;
    break;
  case '/':
    // perform division
    // check if the second operand is zero and print an error message if so
    if (num2 == 0) {
      printf("Error: division by zero\n");
      break;
    }
    result = num1 / num2;
    break;
  default:
    // print an error message for invalid operator
    printf("Error: invalid operator\n");
    break;
}
```

  - Print the result if the operation was successful. For example, we can use `printf("The result is: %lf\n", result);`.
  - End the program.

- Here is an example of the complete program:

```c
#include <stdio.h>

int main() {
  // declare variables
  double num1, num2, result;
  char op;

  // prompt the user to enter the first operand
  printf("Enter the first operand: ");
  scanf("%lf", &num1);

  // prompt the user to enter the second operand
  printf("Enter the second operand: ");
  scanf("%lf", &num2);

  // prompt the user to enter the operator
  printf("Enter the operator (+, -, *, /): ");
  scanf(" %c", &op);

  //

```
