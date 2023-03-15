Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement. Here is the content in markdown format:

## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

- A switch statement is a control structure that allows us to execute different blocks of code based on the value of a variable or expression.
- We can use a switch statement to implement a simple calculator program that takes two operands and one operator from the user, perform the operation, and prints the result.
- The syntax of a switch statement is:

```c
switch (expression) {
  case value1:
    // statements for value1
    break;
  case value2:
    // statements for value2
    break;
  ...
  default:
    // statements for default case
    break;
}
```

- The expression can be any variable or expression that evaluates to an integer or a character value.
- The case values must be constants or literals that match the type of the expression.
- The break statement is used to exit the switch statement after executing the statements for a matching case.
- The default case is optional and is executed when none of the case values match the expression.

- Here is an example of a program that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement:

```c
#include <stdio.h>

int main() {
  double num1, num2, result;
  char op;

  printf("Enter the first operand: ");
  scanf("%lf", &num1);

  printf("Enter the second operand: ");
  scanf("%lf", &num2);

  printf("Enter the operator (+, -, *, /): ");
  scanf(" %c", &op); // note the space before %c to skip whitespace

  switch (op) {
    case '+':
      result = num1 + num2;
      printf("%.2lf + %.2lf = %.2lf\n", num1, num2, result);
      break;
    case '-':
      result = num1 - num2;
      printf("%.2lf - %.2lf = %.2lf\n", num1, num2, result);
      break;
    case '*':
      result = num1 * num2;
      printf("%.2lf * %.2lf = %.2lf\n", num1, num2, result);
      break;
    case '/':
      if (num2 == 0) {
        printf("Error: division by zero\n");
      } else {
        result = num1 / num2;
        printf("%.2lf / %.2lf = %.2lf\n", num1, num2, result);
      }
      break;
    default:
      printf("Invalid operator\n");
      break;
  }

  return 0;
}
```

- The program uses the scanf function to read the user input and store it in the variables num1, num2, and op.
- The program then uses a switch statement to check the value of op and perform the corresponding operation on num1 and num2.
- The program prints the result with two decimal places using the printf function and the %.2lf format specifier.
- The program also handles the cases of division by zero and invalid operator by printing appropriate error messages.