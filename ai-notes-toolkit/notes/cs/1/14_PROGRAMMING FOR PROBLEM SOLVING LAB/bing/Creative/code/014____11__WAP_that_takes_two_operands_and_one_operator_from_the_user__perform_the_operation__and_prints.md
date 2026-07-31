Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a content on the topic: 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement. Here is the content I have written for you:

## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

A switch statement is a control structure that allows us to execute different blocks of code based on the value of a variable or expression. It is often used to implement multiple choices or alternatives in a program.

In this problem, we want to write a program that takes two operands and one operator from the user, perform the operation, and prints the result by using switch statement. The operands are numbers and the operator can be one of the following: +, -, *, /, or %. The program should also handle invalid inputs and display appropriate messages.

Here is the algorithm for the program:

- Declare three variables: num1, num2, and op to store the operands and the operator.
- Prompt the user to enter the first operand and store it in num1.
- Prompt the user to enter the second operand and store it in num2.
- Prompt the user to enter the operator and store it in op.
- Use a switch statement to check the value of op and perform the corresponding operation on num1 and num2.
- In each case, print the result of the operation and break the switch statement.
- If the value of op is not one of the valid operators, print an error message and break the switch statement.
- If the value of op is / or % and the value of num2 is zero, print a message that division by zero is not possible and break the switch statement.

Here is the pseudocode for the program:

```
num1 <- 0
num2 <- 0
op <- ' '

INPUT "Enter the first operand: " num1
INPUT "Enter the second operand: " num2
INPUT "Enter the operator: " op

SWITCH op
  CASE '+':
    PRINT num1 + num2
    BREAK
  CASE '-':
    PRINT num1 - num2
    BREAK
  CASE '*':
    PRINT num1 * num2
    BREAK
  CASE '/':
    IF num2 == 0 THEN
      PRINT "Division by zero is not possible"
    ELSE
      PRINT num1 / num2
    END IF
    BREAK
  CASE '%':
    IF num2 == 0 THEN
      PRINT "Division by zero is not possible"
    ELSE
      PRINT num1 % num2
    END IF
    BREAK
  DEFAULT:
    PRINT "Invalid operator"
    BREAK
END SWITCH
```

Here is an example of the program output:

```
Enter the first operand: 10
Enter the second operand: 5
Enter the operator: +
15
```

```
Enter the first operand: 10
Enter the second operand: 5
Enter the operator: /
2
```

```
Enter the first operand: 10
Enter the second operand: 0
Enter the operator: /
Division by zero is not possible
```

```
Enter the first operand: 10
Enter the second operand: 5
Enter the operator: ^
Invalid operator
```
