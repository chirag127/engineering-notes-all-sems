### Loops: Purpose and working of loops for the notes of the Unit 2 - Conditionals: Conditional statement in Python (if-else statement, its working and execution), Nested-if statement and Elif statement in Python, Expression Evaluation & Float Representation.

Loops are an essential part of any programming language, including Python. A loop is a control structure that enables you to execute a block of code repeatedly. Loops are used when you need to perform a task multiple times, such as iterating over a list of items or performing a calculation until a certain condition is met.

Python has two types of loops: for loops and while loops. Here's how they work:

#### For Loops:
- For loops are used to iterate over a sequence of values, such as a list or a tuple.
- The basic syntax for a for loop is:
  ```python
  for variable in sequence:
      # code to be executed
  ```
- The `variable` takes on the value of each item in the `sequence` one at a time, and the code inside the loop is executed for each value.
- For example, if you wanted to print each item in a list of numbers, you could use a for loop like this:
  ```python
  numbers = [1, 2, 3, 4, 5]
  for num in numbers:
      print(num)
  ```
- This would output:
  ```
  1
  2
  3
  4
  5
  ```

#### While Loops:
- While loops are used to execute a block of code repeatedly as long as a certain condition is true.
- The basic syntax for a while loop is:
  ```python
  while condition:
      # code to be executed
  ```
- The `condition` is checked at the start of each iteration, and the code inside the loop is executed only if the condition is true.
- For example, if you wanted to print the numbers from 1 to 5 using a while loop, you could use code like this:
  ```python
  num = 1
  while num <= 5:
      print(num)
      num += 1
  ```
- This would output:
  ```
  1
  2
  3
  4
  5
  ```

#### Nested If Statements:
- Nested if statements are used when you need to check multiple conditions in a specific order.
- The basic syntax for a nested if statement is:
  ```python
  if condition1:
      # code to be executed if condition1 is true
      if condition2:
          # code to be executed if condition2 is true
      elif condition3:
          # code to be executed if condition3 is true
      else:
          # code to be executed if none of the conditions are true
  ```
- The `elif` statement is short for "else if" and is used to check another condition if the previous conditions were false.
- For example, if you wanted to check if a number is positive, negative, or zero using a nested if statement, you could use code like this:
  ```python
  num = 5
  if num > 0:
      print("Positive")
  elif num < 0:
      print("Negative")
  else:
      print("Zero")
  ```
- This would output:
  ```
  Positive
  ```

#### Expression Evaluation and Float Representation:
- In Python, expressions are evaluated using a set of rules known as operator precedence.
- Operator precedence determines the order in which operators are evaluated in an expression.
- For example, in the expression `2 + 3 * 4`, the multiplication operator has higher precedence than the addition operator, so the expression is evaluated as `2 + (3 * 4)`, which equals 14.
- Python also has built-in support for floating-point numbers, which are numbers with a decimal point.
- However, because of the way floating-point numbers are represented in computer memory, they may not always be exact.
- For example, the expression `0.1 + 0.2` should equal `0.3`, but due to floating-point rounding errors, it actually equals `0.30000000000000004`.
- To avoid these issues, you can use the built-in `decimal` module in Python to perform exact decimal arithmetic.