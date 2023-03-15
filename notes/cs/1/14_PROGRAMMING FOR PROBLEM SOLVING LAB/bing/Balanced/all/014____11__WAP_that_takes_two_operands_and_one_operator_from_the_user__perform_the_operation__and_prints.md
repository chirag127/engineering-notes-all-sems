## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

- WAP stands for Write A Program.
- A switch statement is a control structure that allows a program to execute different blocks of code based on the value of a variable or expression.
- The syntax of a switch statement in C is:

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

- The expression can be any integer or character value. The case values must be constant and unique. The break statement is used to exit the switch statement after executing a case. The default case is optional and is executed when none of the case values match the expression.
- To write a program that takes two operands and one operator from the user, perform the operation, and prints the result by using switch statement, we can follow these steps:

  - Declare three variables to store the operands, the operator, and the result.
  - Prompt the user to enter the first operand and read it using scanf function.
  - Prompt the user to enter the second operand and read it using scanf function.
  - Prompt the user to enter the operator and read it using scanf function.
  - Use a switch statement to check the value of the operator and perform the corresponding operation on the operands. Store the result in the result variable.
  - Print the result using printf function.
  - Handle the possible errors such as division by zero, invalid operator, etc. using default case or if-else statements.

- An example of such a program in C is:

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

  // Use a switch statement to check the value of the operator and perform the corresponding operation on the operands. Store the result in the result variable
  switch (operator) {
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
      // Handle the possible error of division by zero using if-else statement
      if (operand2 == 0) {
        printf("Error: Division by zero.\n");
        return 1; // Exit the program with an error code
      }
      result = operand1 / operand2;
      break;
    default:
      // Handle the possible error of invalid operator using default case
      printf("Error: Invalid operator.\n");
      return 1; // Exit the program with an error code
  }

  // Print the result using printf function
  printf("%.2lf %c %.2lf = %.2lf\n", operand1, operator, operand2, result);

  return 0; // Exit the program with a success code
}
```

- The output of the program may look like:

```
Enter the first operand: 10
Enter the second operand: 5
Enter the operator (+, -, *, /): +
10.00 + 5.00 = 15.00
```

```
Enter the first operand: 20
Enter the second operand: 0
Enter the operator (+, -, *, /): /
Error: Division by zero.
```

```
Enter the first operand: 15
Enter the second operand: 3
Enter the operator (+, -, *, /): %
Error: Invalid operator.
```