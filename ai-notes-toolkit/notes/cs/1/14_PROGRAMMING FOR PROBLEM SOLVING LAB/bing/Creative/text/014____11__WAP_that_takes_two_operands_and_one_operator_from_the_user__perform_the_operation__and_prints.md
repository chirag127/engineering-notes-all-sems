## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to achieve a certain goal or output.
- A switch statement is a control structure that allows a program to execute different blocks of code based on the value of a variable or expression.
- An operand is a value or variable that is used in an arithmetic or logical operation, such as addition, subtraction, multiplication, division, etc.
- An operator is a symbol or keyword that specifies the type of operation to be performed on the operands, such as +, -, *, /, etc.
- To write a WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using switch statement, we need to follow these steps:

  - Declare and initialize three variables: op1, op2, and op to store the first operand, second operand, and operator respectively.
  - Use the input() function to prompt the user to enter the values for op1, op2, and op, and assign them to the corresponding variables.
  - Use the switch statement to check the value of op, and execute the appropriate block of code to perform the operation and print the result.
  - Use the break keyword to exit the switch statement after each case.
  - Use the default case to handle the situation when the user enters an invalid operator, and print an error message.

- Here is an example of a WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using switch statement in Python:

```python
# Declare and initialize three variables
op1 = 0
op2 = 0
op = ""

# Prompt the user to enter the values for op1, op2, and op
op1 = int(input("Enter the first operand: "))
op2 = int(input("Enter the second operand: "))
op = input("Enter the operator: ")

# Use the switch statement to check the value of op
switch(op):
  # If op is "+", perform addition and print the result
  case "+":
    print(f"{op1} + {op2} = {op1 + op2}")
    break
  # If op is "-", perform subtraction and print the result
  case "-":
    print(f"{op1} - {op2} = {op1 - op2}")
    break
  # If op is "*", perform multiplication and print the result
  case "*":
    print(f"{op1} * {op2} = {op1 * op2}")
    break
  # If op is "/", perform division and print the result
  case "/":
    # Check if op2 is not zero to avoid division by zero error
    if op2 != 0:
      print(f"{op1} / {op2} = {op1 / op2}")
    else:
      print("Error: Cannot divide by zero")
    break
  # If op is not any of the above, print an error message
  default:
    print("Error: Invalid operator")
```