### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch.

Conditional branching is a fundamental concept in programming that allows a program to execute specific instructions based on certain conditions. It provides the capability to make decisions based on the current state of the program, user input, or other variables.

One of the most common ways to implement conditional branching is by using if and switch statements. Here are some important points to keep in mind when working with if and switch statements:

#### if Statements:

- An if statement allows a program to execute a set of instructions if a certain condition is met.
- The condition in an if statement is usually evaluated as either true or false.
- The syntax of an if statement is as follows:

  ```
  if (condition) {
      // code to execute if condition is true
  }
  ```

- The code inside the curly braces will only be executed if the condition is true.
- If the condition is false, the code inside the curly braces will be skipped.

#### else Statements:

- An else statement can be used in conjunction with an if statement to execute a different set of instructions if the condition is false.
- The syntax of an if-else statement is as follows:

  ```
  if (condition) {
      // code to execute if condition is true
  } else {
      // code to execute if condition is false
  }
  ```

- If the condition is true, the code inside the first set of curly braces will be executed. If the condition is false, the code inside the second set of curly braces will be executed.

#### Nesting if and Else Statements:

- if and else statements can be nested inside one another to create more complex branching logic.
- Here is an example of nested if-else statements:

  ```
  if (condition1) {
      if (condition2) {
          // code to execute if both conditions are true
      } else {
          // code to execute if condition1 is true and condition2 is false
      }
  } else {
      // code to execute if condition1 is false
  }
  ```

- In this example, the code inside the first set of curly braces will only be executed if condition1 is true. If condition1 is false, the code inside the second set of curly braces will be executed.
- If condition1 is true, the program will evaluate condition2. If condition2 is true, the code inside the third set of curly braces will be executed. If condition2 is false, the code inside the fourth set of curly braces will be executed.

#### Switch Statements:

- A switch statement allows a program to execute different sets of instructions based on the value of a variable.
- The syntax of a switch statement is as follows:

  ```
  switch (variable) {
      case value1:
          // code to execute if variable is equal to value1
          break;
      case value2:
          // code to execute if variable is equal to value2
          break;
      default:
          // code to execute if variable is not equal to any of the cases
          break;
  }
  ```

- The program will evaluate the value of the variable and execute the code inside the corresponding case statement.
- If the variable does not match any of the case values, the code inside the default statement will be executed.

In conclusion, conditional branching is a powerful tool that allows programmers to create dynamic and flexible programs. By using if and switch statements, as well as nesting if and else statements, programmers can create complex branching logic that responds to user input and other variables.