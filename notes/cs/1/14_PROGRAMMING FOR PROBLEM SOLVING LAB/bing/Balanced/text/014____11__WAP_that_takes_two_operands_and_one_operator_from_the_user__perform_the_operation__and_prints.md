## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

- WAP stands for Write a Program.
- A switch statement is a control structure that allows a program to choose different actions based on a value or expression.
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

- The expression can be any valid C expression that evaluates to an integer or a character value.
- The case values must be constants or literals that match the type of the expression.
- The break statement is used to exit the switch statement and prevent the execution of the following cases.
- The default case is optional and is executed when none of the case values match the expression.

- To write a program that takes two operands and one operator from the user, perform the operation, and prints the result by using switch statement, we can follow these steps:

  - Declare three variables to store the operands, the operator, and the result.
  - Prompt the user to enter the first operand and read it using scanf function.
  - Prompt the user to enter the second operand and read it using scanf function.
  - Prompt the user to enter the operator and read it using scanf function.
  - Use a switch statement to check the value of the operator and perform the corresponding operation on the operands.
  - Store the result of the operation in the result variable.
  - Print the result using printf function.
  - Use a default case to handle invalid operators and print an error message.

- An example of the program in C language is:

```c
#include <stdio.h>

int main() {
  // Declare three variables to store the operands, the operator, and the result
  double operand1, operand2, result;
  char operator;

  // Prompt the user to enter the first operand and read it using scanf function
  printf("Enter the first operand: ");
  scanf("%lf", &operand1);

  // Prompt the user to enter the second operand and read it using scanf function
  printf("Enter the second operand: ");
  scanf("%lf", &operand2);

  // Prompt the user to enter the operator and read it using scanf function
  printf("Enter the operator (+, -, *, /): ");
  scanf(" %c", &operator); // Note the space before %c to skip any whitespace

  // Use a switch statement to check the value of the operator and perform the corresponding operation on the operands
  switch (operator) {
    case '+':
      // Add the operands and store the result
      result = operand1 + operand2;
      break;
    case '-':
      // Subtract the operands and store the result
      result = operand1 - operand2;
      break;
    case '*':
      // Multiply the operands and store the result
      result = operand1 * operand2;
      break;
    case '/':
      // Divide the operands and store the result
      // Check if the second operand is zero and print an error message if so
      if (operand2 == 0) {
        printf("Error: Cannot divide by zero.\n");
        return 0; // Exit the program
      }
      result = operand1 / operand2;
      break;
    default:
      // Handle invalid operators and print an error message
      printf("Error: Invalid operator.\n");
      return 0; // Exit the program
  }

  // Print the result using printf function
  printf("%.2lf %c %.2lf = %.2lf\n", operand1, operator, operand2, result);

  return 0; // End the program
}
```

- An example of the output of the program is:

```
Enter the first operand: 10
Enter the second operand: 5
Enter the operator (+, -, *, /): *
10.00 * 5.00 = 50.00
```