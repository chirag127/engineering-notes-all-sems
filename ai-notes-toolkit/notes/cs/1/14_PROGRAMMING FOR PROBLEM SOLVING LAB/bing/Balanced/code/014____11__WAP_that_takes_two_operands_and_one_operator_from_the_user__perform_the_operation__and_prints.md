## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

- A WAP (write a program) is a task that requires the user to write a code in a specific programming language that can perform a certain function or solve a problem.
- In this case, the WAP is to take two operands and one operator from the user, perform the operation, and print the result by using a switch statement.
- An operand is a value or variable that is used in an arithmetic or logical operation, such as 2, x, or y.
- An operator is a symbol that defines the type of operation to be performed on the operands, such as +, -, *, /, or %.
- A switch statement is a control structure that allows the program to execute different blocks of code based on the value of a variable or expression, such as switch (operator) { case '+': ... break; case '-': ... break; ... default: ... break; }
- To write a WAP that takes two operands and one operator from the user, perform the operation, and print the result by using a switch statement, the following steps can be followed:

  - Declare and initialize two variables to store the operands, such as int a = 0; int b = 0;
  - Declare and initialize a variable to store the operator, such as char op = ' ';
  - Declare and initialize a variable to store the result, such as int result = 0;
  - Use the scanf function to take the input from the user and assign it to the variables, such as scanf("%d %c %d", &a, &op, &b);
  - Use a switch statement to check the value of the operator and perform the corresponding operation on the operands, such as switch (op) { case '+': result = a + b; break; case '-': result = a - b; break; case '*': result = a * b; break; case '/': result = a / b; break; case '%': result = a % b; break; default: printf("Invalid operator\n"); break; }
  - Use the printf function to print the result to the standard output, such as printf("%d %c %d = %d\n", a, op, b, result);
  - End the program with a return statement, such as return 0;

- An example of a WAP that takes two operands and one operator from the user, perform the operation, and print the result by using a switch statement in C language is:

```c
#include <stdio.h>

int main()
{
  int a = 0; // first operand
  int b = 0; // second operand
  char op = ' '; // operator
  int result = 0; // result

  // take input from the user
  printf("Enter two operands and one operator: ");
  scanf("%d %c %d", &a, &op, &b);

  // perform the operation based on the operator
  switch (op)
  {
    case '+': // addition
      result = a + b;
      break;
    case '-': // subtraction
      result = a - b;
      break;
    case '*': // multiplication
      result = a * b;
      break;
    case '/': // division
      result = a / b;
      break;
    case '%': // modulo
      result = a % b;
      break;
    default: // invalid operator
      printf("Invalid operator\n");
      break;
  }

  // print the result
  printf("%d %c %d = %d\n", a, op, b, result);

  // end the program
  return 0;
}
```

- The output of the program will depend on the input given by the user, such as:

```
Enter two operands and one operator: 10 + 5
10 + 5 = 15
```

```
Enter two operands and one operator: 20 / 4
20 / 4 = 5
```

```
Enter two operands and one operator: 15 % 2
15 % 2 = 1
```

```
Enter two operands and one operator: 8 ^ 2
Invalid operator
```