

## Unit 1 - Introduction: The Programming Cycle for Python , Python IDE, Interacting with Python Programs , Elements of Python, Type Conversion.

- The programming cycle for Python consists of four steps: writing, testing, debugging, and running the program.
- Writing a Python program involves creating a text file with the .py extension that contains Python code. The code can be written using any text editor or a specialized tool called an integrated development environment (IDE).
- An IDE is a software application that provides features to help programmers write, test, debug, and run their code. Some examples of Python IDEs are PyCharm, Visual Studio Code, Spyder, and Thonny.
- Testing a Python program involves checking if the code is syntactically correct and does what it is intended to do. Testing can be done using the built-in Python interpreter, which executes the code line by line and displays the output or errors, or using a separate tool called a debugger, which allows the programmer to inspect and modify the state of the program as it runs.
- Debugging a Python program involves finding and fixing the errors or bugs in the code. Bugs can be either syntax errors, which prevent the code from running, or logic errors, which cause the code to produce incorrect or unexpected results. Debugging can be done using the Python interpreter, the debugger, or by adding print statements to the code to display intermediate values or messages.
- Running a Python program involves executing the code as a whole and obtaining the final output or result. Running can be done using the Python interpreter, by typing python filename.py in the command line, or by using the run or execute feature of the IDE.

- Interacting with Python programs can be done in two ways: using the interactive mode or using the script mode.
- The interactive mode allows the user to type Python commands or expressions directly into the Python interpreter and see the results immediately. The interactive mode is useful for experimenting with Python features, testing small pieces of code, or performing simple calculations. To enter the interactive mode, type python in the command line and press enter. To exit the interactive mode, type exit() or press Ctrl+D.
- The script mode allows the user to write Python code in a text file and execute it as a program. The script mode is useful for writing larger or more complex programs, or for saving and reusing the code. To enter the script mode, create a text file with the .py extension and write the Python code in it. To execute the script, type python filename.py in the command line and press enter.

- Elements of Python are the basic components or building blocks of the Python language. They include:
  - Keywords: reserved words that have a special meaning and function in Python. Examples are if, else, for, while, def, class, etc. Keywords cannot be used as variable names or identifiers.
  - Identifiers: names that are used to identify variables, functions, classes, modules, or other objects in Python. Identifiers can be composed of letters, digits, and underscores, but they cannot start with a digit or be a keyword. Examples are x, y, sum, max, print, math, etc.
  - Literals: values that are written directly in the code and do not change. Examples are 42, 3.14, "Hello", True, None, etc.
  - Operators: symbols that are used to perform operations on operands, such as arithmetic, comparison, logical, assignment, etc. Examples are +, -, *, /, %, **, <, >, ==, !=, and, or, not, =, +=, -=, etc.
  - Expressions: combinations of literals, variables, operators, and parentheses that evaluate to a single value. Examples are x + y, 2 * (3 + 4), x > 10, etc.
  - Statements: instructions that tell the Python interpreter what to do. Examples are print(x), if x > 10: print("x is large"), for i in range(10): print(i), etc.
  - Comments: text that is ignored by the Python interpreter and is used to explain or document the code. Comments start with a # symbol and end at the end of the line. Examples are # This is a comment, # Calculate the area of a circle, etc.

- Type conversion is the process of changing the data type of a value or variable from one type to another. Type conversion can be either implicit or explicit.
- Implicit type conversion is done automatically by the Python interpreter when it needs to operate on values of different types. For example, if x is an integer and y is a float, then x + y will result in a float, because Python will convert x to a float before performing



Hello, I am Sydney, your AI assistant. I can help you with your Python programming notes. Here is the content for the topic you requested:

### Basics: Expressions for the notes of the Unit 1 - Introduction: The Programming Cycle for Python , Python IDE, Interacting with Python Programs , Elements of Python, Type Conversion.

- An expression is a combination of values, variables, operators, and functions that produces a result.
- The result of an expression can be displayed using the `print()` function, or assigned to a variable using the `=` operator.
- Examples of expressions are: `2 + 3`, `"Hello" + "World"`, `len("Python")`, `x * y`, etc.
- The programming cycle is the process of writing, testing, and debugging a program.
- The programming cycle consists of the following steps:
  - Analyze the problem and design a solution.
  - Write the code using a programming language.
  - Test the code and fix any errors or bugs.
  - Document the code and explain how it works.
  - Maintain and update the code as needed.
- A Python IDE (Integrated Development Environment) is a software tool that provides a convenient and user-friendly environment for writing, running, and debugging Python programs.
- Some examples of Python IDEs are: PyCharm, Visual Studio Code, Spyder, Thonny, etc.
- Interacting with Python programs means providing input to the program or receiving output from the program.
- Input can be given to a Python program using the `input()` function, which returns a string value entered by the user.
- Output can be displayed by a Python program using the `print()` function, which prints a value or a message to the screen.
- Elements of Python are the basic components or building blocks of the language, such as values, variables, operators, functions, data types, etc.
- Values are the data or information that can be stored, manipulated, or displayed by a Python program, such as numbers, strings, booleans, etc.
- Variables are names that refer to values and can be used to store, retrieve, or change the values.
- Operators are symbols that perform arithmetic, logical, or bitwise operations on values or variables, such as `+`, `-`, `*`, `/`, `==`, `!=`, `and`, `or`, `not`, `&`, `|`, etc.
- Functions are blocks of code that perform a specific task and can be called by using their name and parentheses, such as `print()`, `input()`, `len()`, `type()`, etc.
- Data types are categories of values that have certain properties and behaviors, such as integers, floats, strings, booleans, lists, tuples, dictionaries, sets, etc.
- Type conversion is the process of changing the data type of a value or a variable, either implicitly or explicitly.
- Implicit type conversion is done automatically by Python when it is necessary or possible, such as adding an integer and a float, or concatenating a string and a number.
- Explicit type conversion is done by the programmer using built-in functions, such as `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `dict()`, `set()`, etc.



### Assignment Statement

- An assignment statement is a way of creating, initializing, or updating variables in Python.
- A variable is a name that refers to an object, such as a number, a string, a list, or a function.
- An assignment statement has the form `target = expression`, where `target` is the name of the variable and `expression` is any Python expression that evaluates to an object.
- The assignment statement assigns the object resulting from the expression to the target variable, creating or updating the variable's reference to the object.
- For example, `x = 10` assigns the integer object `10` to the variable `x`.
- Python supports multiple assignment, where more than one target can be assigned to the same or different objects in a single statement.
- For example, `x, y = 10, 20` assigns the integer object `10` to the variable `x` and the integer object `20` to the variable `y`.
- Multiple assignment can also be used to swap the values of two variables without using a temporary variable.
- For example, `x, y = y, x` swaps the values of `x` and `y`.
- Python also supports augmented assignment, where an operator can be combined with the assignment operator to perform an arithmetic or bitwise operation and assign the result to the target variable in one step.
- For example, `x += 1` is equivalent to `x = x + 1`, which increments the value of `x` by `1`.
- Augmented assignment can be used with any of the following operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
- Augmented assignment can be more efficient and concise than regular assignment, especially when working with mutable objects such as lists or dictionaries.



### Arithmetic Operators

- Arithmetic operators are used to perform mathematical operations on numeric values, such as addition, subtraction, multiplication, division, etc.
- Python supports the following arithmetic operators:

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | +      | 5 + 3   | 8      |
| Subtraction | -   | 5 - 3   | 2      |
| Multiplication | * | 5 * 3  | 15     |
| Division | /      | 5 / 3   | 1.6666666666666667 |
| Floor division | // | 5 // 3 | 1      |
| Modulus | %      | 5 % 3   | 2      |
| Exponentiation | ** | 5 ** 3 | 125    |

- The order of operations follows the PEMDAS rule, which stands for Parentheses, Exponents, Multiplication/Division, Addition/Subtraction. This means that expressions inside parentheses are evaluated first, then exponents, then multiplication and division from left to right, and finally addition and subtraction from left to right.
- For example, the expression 2 + 3 * 4 ** 2 - 1 is evaluated as follows:

| Step | Expression | Explanation |
|------|------------|-------------|
| 1    | 2 + 3 * 4 ** 2 - 1 | Original expression |
| 2    | 2 + 3 * 16 - 1 | Evaluate the exponent 4 ** 2 |
| 3    | 2 + 48 - 1 | Evaluate the multiplication 3 * 16 |
| 4    | 50 - 1 | Evaluate the addition 2 + 48 |
| 5    | 49 | Evaluate the subtraction 50 - 1 |

- The result is 49.



### Operator Precedence for the notes of the Unit 1 - Introduction: The Programming Cycle for Python , Python IDE, Interacting with Python Programs , Elements of Python, Type Conversion.

- Operator precedence in Python means the order in which the Python interpreter executes operators.
- It tells the Python interpreter which operator should be evaluated first if a single statement contains more than one operator.
- Therefore, it is essential to understand the order of precedence to avoid the ambiguity in the expressions.
- The following table summarizes the operator precedence in Python, from highest to lowest:

| Operator | Description |
| :---: | :--- |
| `()` | Parentheses |
| `**` | Exponentiation |
| `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT |
| `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo |
| `+`, `-` | Addition, subtraction |
| `<<`, `>>` | Bitwise left shift, bitwise right shift |
| `&` | Bitwise AND |
| `^` | Bitwise XOR |
| `|` | Bitwise OR |
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, membership testing, identity testing |
| `not` | Logical NOT |
| `and` | Logical AND |
| `or` | Logical OR |
| `if-else` | Conditional expression |
| `:=` | Assignment expression |
| `lambda` | Lambda expression |

- Some examples of operator precedence in Python are:

```python
# Example 1: Exponentiation has higher precedence than multiplication
print(2 * 3 ** 2) # prints 18, not 36

# Example 2: Parentheses can change the order of evaluation
print((2 * 3) ** 2) # prints 36, not 18

# Example 3: Logical operators have lower precedence than comparison operators
x = 10
y = 20
print(x > 5 and y < 15) # prints False, not True

# Example 4: Assignment expression has lower precedence than conditional expression
x = 5
y = 10
z = x if x > y else y # assigns 10 to z
print(z) # prints 10
```



### Boolean Expression

- A Boolean expression is an expression that evaluates to produce a result which is a Boolean value.
- A Boolean value is either True or False, and the Python type is bool .
- A Boolean expression often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- Comparison operators are used to compare two values and return a Boolean value. They are: `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to)  .
- For example, the expression `1 <= 2` is True, while the expression `0 == 1` is False.
- Boolean expressions can also use logical operators to combine or modify Boolean values. They are: `and` (logical and), `or` (logical or), `not` (logical not)  .
- For example, the expression `True and False` is False, the expression `True or False` is True, and the expression `not True` is False.
- Logical operators follow the rules of Boolean algebra, which are:

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T       | T      | F     |
| T | F | F       | T      | F     |
| F | T | F       | T      | T     |
| F | F | F       | F      | T     |

- Boolean expressions can also use parentheses to group terms and change the order of evaluation. For example, the expression `(True and False) or True` is True, while the expression `True and (False or True)` is also True.
- Boolean expressions are often used in conditional statements, such as `if`, `elif`, and `else`, to control the flow of the program based on some condition  .
- For example, the following code snippet uses a Boolean expression to check if a number is positive, negative, or zero:

```python
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

- Boolean expressions can also be used in loops, such as `while` and `for`, to determine when to stop or continue the iteration  .
- For example, the following code snippet uses a Boolean expression to print the numbers from 1 to 10:

```python
number = 1
while number <= 10:
    print(number)
    number = number + 1
```

- Boolean expressions can also be used in functions, such as `any` and `all`, to check if any or all elements of an iterable (such as a list, tuple, or string) are truthy or falsy .
- A truthy value is a value that evaluates to True when converted to a Boolean, and a falsy value is a value that evaluates to False when converted to a Boolean .
- For example, the following code snippet uses the `any` function to check if any element of a list is positive:

```python
numbers = [0, -1, 2, -3, 4]
if any(number > 0 for number in numbers):
    print("There is at least one positive number in the list.")
else:
    print("There are no positive numbers in the list.")
```

- Boolean expressions can also be used in comprehensions, such as list comprehensions, to filter the elements of an iterable based on some condition .
- For example, the following code snippet uses a list comprehension to create a new list with only the even numbers from another list:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
```

- Boolean expressions are an essential part of Python programming, as they allow us to make decisions and perform actions based on some condition[^



## Unit 2 - Conditionals

- Conditional statements are used to control the flow of execution in a program based on some conditions.
- The most common conditional statement in Python is the `if-else` statement, which has the following syntax:

```python
if condition:
    # execute this block of code if condition is True
else:
    # execute this block of code if condition is False
```

- The `condition` is a boolean expression that evaluates to either `True` or `False`.
- The `if` and `else` keywords are followed by a colon (`:`) and indented blocks of code.
- The indentation is important in Python, as it defines the scope of the code blocks.
- Only one of the code blocks will be executed, depending on the value of the condition.
- For example:

```python
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative or zero")
```

- This code will print "x is positive" if x is greater than 0, and "x is negative or zero" otherwise.

- Nested-if statement is a conditional statement that contains another conditional statement inside it.
- The nested conditional statement can be either an `if-else` statement or an `elif` statement, which will be explained later.
- The syntax of a nested-if statement is:

```python
if condition1:
    # execute this block of code if condition1 is True
    if condition2:
        # execute this block of code if condition2 is True
    else:
        # execute this block of code if condition2 is False
else:
    # execute this block of code if condition1 is False
```

- The nested conditional statement is indented inside the outer conditional statement.
- The nested conditional statement will only be evaluated if the outer condition is True.
- For example:

```python
x = 10
y = 5
if x > 0:
    print("x is positive")
    if y > 0:
        print("y is also positive")
    else:
        print("y is negative or zero")
else:
    print("x is negative or zero")
```

- This code will print "x is positive" and "y is also positive" if x and y are both greater than 0, "x is positive" and "y is negative or zero" if x is greater than 0 and y is less than or equal to 0, and "x is negative or zero" if x is less than or equal to 0.

- Elif statement is a conditional statement that is used to check multiple conditions in a sequence.
- The `elif` keyword stands for "else if", and it is followed by a condition and a colon (`:`).
- The `elif` statement can be used after an `if` statement or another `elif` statement, but not after an `else` statement.
- The syntax of an `elif` statement is:

```python
if condition1:
    # execute this block of code if condition1 is True
elif condition2:
    # execute this block of code if condition1 is False and condition2 is True
elif condition3:
    # execute this block of code if condition1 and condition2 are False and condition3 is True
else:
    # execute this block of code if all conditions are False
```

- The `elif` statement allows us to check multiple conditions in a single conditional statement, without using nested-if statements.
- The `elif` statement will only be evaluated if the previous conditions are False.
- Only one of the code blocks will be executed, depending on which condition is True first.
- For example:

```python
x = 10
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif x < 10:
    print("x is positive and less than 10")
else:
    print("x is positive and greater than or equal to 10")
```

- This code will print "x is positive and greater than or equal to 10" if x is 10, "x is zero" if x is 0, "x is negative" if x is less than 0, and "x is positive and less than 10" if x is between 0 and 10.

- Expression evaluation is the process of computing the value of an expression, which can consist of literals, variables, operators, and parentheses.
- The order of evaluation of an expression depends on the precedence and associativity of the operators involved.
- The precedence of an operator determines which operator is evaluated first in an expression that contains multiple operators.
-



### Loops: Purpose and working of loops

- A loop is a programming construct that allows a block of code to be executed repeatedly until a certain condition is met.
- The purpose of loops is to automate repetitive tasks, such as processing a list of items, performing calculations, or validating user input.
- There are two types of loops in Python: for loops and while loops.
- A for loop iterates over a sequence of values, such as a list, a tuple, a string, or a range object, and executes the loop body for each element in the sequence.
- A while loop executes the loop body as long as a given boolean expression evaluates to True, and stops when the expression becomes False or a break statement is encountered.
- The syntax of a for loop is:

```python
for variable in sequence:
    # loop body
    # statements to be executed for each element in the sequence
```

- The syntax of a while loop is:

```python
while expression:
    # loop body
    # statements to be executed as long as the expression is True
```

- Both types of loops can have an optional else clause, which is executed when the loop terminates normally, i.e. without a break statement.
- The syntax of a for loop with an else clause is:

```python
for variable in sequence:
    # loop body
    # statements to be executed for each element in the sequence
else:
    # else clause
    # statements to be executed when the loop ends normally
```

- The syntax of a while loop with an else clause is:

```python
while expression:
    # loop body
    # statements to be executed as long as the expression is True
else:
    # else clause
    # statements to be executed when the loop ends normally
```

- Loops can be nested inside other loops, creating a loop within a loop. This is useful for iterating over multidimensional data structures, such as matrices or nested lists.
- The syntax of a nested loop is:

```python
for variable1 in sequence1:
    # outer loop body
    for variable2 in sequence2:
        # inner loop body
        # statements to be executed for each pair of elements from sequence1 and sequence2
```

- The same syntax applies for nested while loops, except that the expression for the inner loop must be evaluated separately from the expression for the outer loop.
- Loops can be controlled using the break, continue, and pass statements.
- The break statement terminates the current loop and skips the else clause, if any. It is used to exit the loop prematurely when a certain condition is met or an error occurs.
- The continue statement skips the rest of the current iteration and moves to the next one. It is used to skip some elements in the sequence or some cases in the expression that are not relevant or valid.
- The pass statement does nothing and is used as a placeholder when a statement is required syntactically but no action is needed. It is used to create empty loops or loop bodies that will be filled later.



### While loop

- A while loop is a type of loop that repeatedly executes a block of code as long as a given condition is true.
- The syntax of a while loop is:

```python
while condition:
    # code block
```

- The condition is a boolean expression that evaluates to either True or False. If the condition is True, the code block is executed and the condition is checked again. If the condition is False, the loop is terminated and the program moves to the next statement after the loop.
- A while loop can be used to implement various tasks that require repetition, such as counting, iterating, accumulating, etc.
- A while loop can also be used to create an infinite loop, which is a loop that never ends. This can be useful for some applications that need to run continuously, such as servers, games, etc. However, an infinite loop can also cause problems if there is no way to exit the loop or stop the program. To create an infinite loop, the condition can be set to True or a value that always evaluates to True, such as 1, "hello", etc.
- A while loop can be controlled by using break and continue statements. A break statement can be used to exit the loop prematurely, while a continue statement can be used to skip the current iteration and move to the next one. For example:

```python
# A while loop that prints the numbers from 1 to 10, except 5
n = 1
while n <= 10:
    if n == 5:
        n += 1
        continue # skip the rest of the code block and move to the next iteration
    print(n)
    n += 1
```

- The output of this loop is:

```output
1
2
3
4
6
7
8
9
10
```



### For Loop

- A for loop is a type of loop that iterates over a sequence of items, such as a list, a tuple, a string, or a range object.
- The syntax of a for loop is:

```python
for item in sequence:
    # do something with item
```

- The item variable can be any valid identifier, and it takes the value of each element in the sequence in each iteration.
- The sequence can be any iterable object that supports the `__iter__` and `__next__` methods, such as a list, a tuple, a string, or a range object.
- The body of the loop is indented under the for statement, and it can contain any valid Python statements, including other loops, conditionals, or function calls.
- The loop terminates when the sequence is exhausted, or when a `break` or `return` statement is encountered inside the loop body.
- A for loop can also have an optional `else` clause, which is executed when the loop ends normally, i.e., without a `break` or `return` statement. The syntax of a for loop with an else clause is:

```python
for item in sequence:
    # do something with item
else:
    # do something else
```

- Some examples of for loops are:

```python
# print the numbers from 1 to 10
for i in range(1, 11):
    print(i)

# print the elements of a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# print the characters of a string
name = "Sydney"
for char in name:
    print(char)

# print the sum of the elements of a list
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
else:
    print("The sum is", sum)
```



### Nested Loops

- A nested loop is a loop that is placed inside another loop.
- A nested loop can be of any type: for, while, or do-while.
- A nested loop executes the inner loop for each iteration of the outer loop.
- A nested loop can be used to perform repeated tasks on multidimensional data structures, such as lists, tuples, arrays, matrices, etc.
- A nested loop can also be used to create patterns, such as stars, triangles, squares, etc.

#### Syntax of a nested loop

The general syntax of a nested loop is:

```
outer_loop_condition:
    # outer loop body
    inner_loop_condition:
        # inner loop body
```

#### Example of a nested loop

The following example shows how to use a nested loop to print a multiplication table from 1 to 10:

```
# outer loop for rows
for i in range(1, 11):
    # inner loop for columns
    for j in range(1, 11):
        # print the product of i and j
        print(i * j, end="\t")
    # print a new line after each row
    print()
```

The output of the above code is:

```
1	2	3	4	5	6	7	8	9	10	
2	4	6	8	10	12	14	16	18	20	
3	6	9	12	15	18	21	24	27	30	
4	8	12	16	20	24	28	32	36	40	
5	10	15	20	25	30	35	40	45	50	
6	12	18	24	30	36	42	48	54	60	
7	14	21	28	35	42	49	56	63	70	
8	16	24	32	40	48	56	64	72	80	
9	18	27	36	45	54	63	72	81	90	
10	20	30	40	50	60	70	80	90	100	
```



### Break and Continue

- Break and continue are two keywords that can be used to alter the flow of a loop in Python.
- Break is used to terminate the loop prematurely, when a certain condition is met.
- Continue is used to skip the current iteration of the loop, and move on to the next one, when a certain condition is met.
- Break and continue can be used with both for and while loops.

#### Examples of break and continue

- Suppose we want to loop through a list of numbers and print only the even ones, until we encounter a negative number. We can use break and continue as follows:

```python
numbers = [2, 4, 6, 8, -1, 10, 12]
for num in numbers:
  if num < 0:
    break # stop the loop
  if num % 2 != 0:
    continue # skip the odd number
  print(num)
```

- The output of this code is:

```output
2
4
6
8
```

- Suppose we want to loop through a string and print each character, except for vowels. We can use continue as follows:

```python
word = "python"
for char in word:
  if char in "aeiou":
    continue # skip the vowel
  print(char)
```

- The output of this code is:

```output
p
y
t
h
n
```



## Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

- A function is a block of code that performs a specific task, such as printing a message, calculating a value, or sorting a list.
- A function can be defined using the `def` keyword, followed by the function name and a pair of parentheses that may contain some parameters. The function body is indented and ends with a `return` statement that specifies the value to be returned by the function. For example:

```python
def add(x, y):
  # This function adds two numbers and returns the result
  result = x + y
  return result
```

- A function can be executed or called by using the function name followed by a pair of parentheses that may contain some arguments. The arguments are the values that are passed to the function when it is called. The arguments are assigned to the parameters in the function definition. For example:

```python
# Calling the add function with 3 and 5 as arguments
sum = add(3, 5)
# Printing the value returned by the function
print(sum)
```

- A function can have keyword arguments, which are arguments that are specified by using the parameter name and an equal sign, followed by the value. Keyword arguments can be used to pass arguments in any order, or to provide default values for some parameters. For example:

```python
# Defining a function with two parameters, one with a default value
def greet(name, message="Hello"):
  # This function prints a greeting message with the name
  print(message, name)

# Calling the function with only one argument
greet("Sydney")
# Calling the function with two arguments
greet("User", "Welcome")
# Calling the function with keyword arguments in any order
greet(message="Hi", name="User")
```

- A function has a scope, which is the region of the code where a variable can be accessed. Variables defined inside a function are local to that function, and can only be used within that function. Variables defined outside any function are global, and can be used by any function in the program. For example:

```python
# Defining a global variable
x = 10

def change():
  # Defining a local variable
  x = 5
  # Printing the local variable
  print("Inside the function, x is", x)

# Printing the global variable
print("Outside the function, x is", x)
# Calling the function
change()
# Printing the global variable again
print("Outside the function, x is still", x)
```



Hello, I am Sydney, your AI assistant. I can help you with your study material for Python programming. Here is the content you requested:

### Strings

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or 'Python'.
- Strings can be accessed by indexing, which means using square brackets [ ] to get the character at a specific position, such as s[0] for the first character of string s.
- Strings can also be sliced, which means using a colon : to get a substring from a start index to an end index, such as s[1:4] for the second, third and fourth characters of string s.
- Strings have a length, which can be obtained by using the len() function, such as len(s) for the number of characters in string s.
- Strings can be concatenated, which means joining two or more strings together using the + operator, such as s1 + s2 for the string that results from adding s1 and s2.
- Strings can be repeated, which means multiplying a string by an integer using the * operator, such as s * 3 for the string that results from repeating s three times.

### Functions

- A function is a block of code that performs a specific task and can be reused in different parts of a program.
- A function has a name, a list of parameters, and a body that contains the statements to execute.
- A function can be defined using the def keyword, followed by the name, the parameters in parentheses, and a colon, such as def add(x, y):.
- A function can be called by using the name and passing the arguments that match the parameters, such as add(2, 3) for calling the add function with 2 and 3 as arguments.
- A function can return a value to the caller by using the return statement, such as return x + y for returning the sum of x and y.
- A function can have keyword arguments, which are arguments that are specified by name and can have default values, such as def greet(name="World"):.
- A function can have scope rules, which determine the visibility of variables inside and outside the function. Variables defined inside a function are local and can only be accessed within the function. Variables defined outside a function are global and can be accessed anywhere in the program.



### Python Data Structure: Tuples, Unpacking Sequences, Lists, Mutable Sequences, List Comprehension, Sets, Dictionaries

- **Tuples** are immutable sequences of arbitrary objects. They are enclosed in parentheses and separated by commas. For example, `(1, 2, 3)` is a tuple of three integers. Tuples can be indexed, sliced, concatenated, and nested like lists, but they cannot be modified or deleted. Tuples are often used to represent records or structures with fixed fields and types.  
- **Unpacking sequences** is a way of assigning multiple values from a sequence to multiple variables in one statement. For example, `a, b, c = (1, 2, 3)` assigns the values 1, 2, and 3 to the variables a, b, and c respectively. The number of variables and the length of the sequence must match, otherwise a `ValueError` is raised. Unpacking can also be used with nested sequences, such as `a, (b, c) = (1, (2, 3))`. Unpacking can be useful for swapping values, returning multiple values from a function, or iterating over pairs of values.  
- **Lists** are mutable sequences of arbitrary objects. They are enclosed in square brackets and separated by commas. For example, `[1, 2, 3]` is a list of three integers. Lists can be indexed, sliced, concatenated, nested, and modified like tuples, but they also support methods for adding, removing, sorting, and reversing elements. Lists are often used to store collections of homogeneous or heterogeneous data that can change over time.  
- **Mutable sequences** are objects that support the methods and operations of sequences, such as indexing, slicing, concatenation, and repetition, but also allow modifying or deleting elements. Lists are the most common mutable sequences in Python, but there are also others, such as `bytearray`, `array.array`, and `collections.deque`. Mutable sequences can be useful for implementing dynamic data structures, such as stacks, queues, or buffers.  
- **List comprehension** is a concise way of creating a new list from an existing iterable, such as a list, a tuple, a string, or a range, by applying an expression to each element and optionally filtering them by a condition. The syntax of list comprehension is `[expression for element in iterable if condition]`. For example, `[x**2 for x in range(10) if x % 2 == 0]` creates a list of the squares of the even numbers from 0 to 9. List comprehension can be nested, such as `[x + y for x in [1, 2, 3] for y in [4, 5, 6]]`, but this can make the code less readable. List comprehension can be useful for transforming, filtering, or aggregating data in a single line of code.  
- **Sets** are mutable collections of distinct and immutable objects. They are enclosed in curly braces and separated by commas. For example, `{1, 2, 3}` is a set of three integers. Sets can be created from any iterable, such as a list, a tuple, or a string, by using the `set()` function. Sets do not support indexing, slicing, or concatenation, but they support methods and operators for adding, removing, testing membership, and performing set operations, such as union, intersection, difference, and symmetric difference. Sets are often used to store collections of unique and hashable data that can be compared or combined.  
- **Dictionaries** are mutable collections of key-value pairs, where the keys are immutable and unique, and the values are arbitrary objects. They are enclosed in curly braces and separated by commas, with a colon between each key and value. For example, `{'a': 1, 'b': 2, 'c': 3}` is a dictionary of three key-value pairs. Dictionaries can be created from any iterable of pairs, such as a list of tuples, by using the `dict()` function. Dictionaries support indexing, slicing, and modifying values by keys, but not by positions. They also support methods for adding, removing, updating, and iterating over keys, values, or items. Dictionaries are often used to



### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- Higher order functions (HOFs) are functions that can take other functions as arguments or return functions as results .
- In Python, functions are first class objects, which means they can be assigned to variables, stored in data structures, passed as parameters, and returned as values .
- Some examples of built-in higher order functions in Python are `map`, `filter`, `sorted`, and `reduce`. These functions can take a function and an iterable as arguments and apply the function to each element of the iterable, returning a new iterable or a single value.
- Lambda expressions are anonymous functions that can be created using the `lambda` keyword. They can be used as arguments to higher order functions or assigned to variables. Lambda expressions have a simple syntax: `lambda parameters: expression`. They can only contain one expression and cannot have statements or annotations.
- Decorators are a common use case of higher order functions in Python . They are functions that take another function as an argument and return a modified version of that function. Decorators can be used to add functionality, modify behavior, or check preconditions of a function. Decorators can be applied to a function using the `@` syntax or by calling the decorator function with the function as an argument.

: https://www.geeksforgeeks.org/higher-order-functions-in-python/
: https://www.codespeedy.com/higher-order-functions-in-python-map-filter-sorted-reduce/
: https://docs.python.org/3/library/functools.html
: https://stackoverflow.com/questions/62328661/what-is-the-difference-between-higher-order-functions-and-decorators



## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, etc. are prime numbers.
- A composite number is a natural number that has more than two positive divisors. For example, 4, 6, 8, 9, 10, 12, 14, etc. are composite numbers.
- The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit. It works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.
- The algorithm can be described as follows:

  1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
  2. Initially, let p equal 2, the first prime number.
  3. Starting from p, mark all the multiples of p in the list as composite. For example, if p = 2, mark 2 × 2 = 4, 2 × 3 = 6, 2 × 4 = 8, and so on.
  4. Find the first number greater than p in the list that is not marked as composite. If there is no such number, stop. Otherwise, let p equal this number (the next prime), and repeat from step 3.
  5. When the algorithm terminates, all the numbers in the list that are not marked as composite are prime.

- Here is an example of the algorithm applied to find all prime numbers up to 20:

  1. Create a list of consecutive integers from 2 to 20: (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20).
  2. Let p = 2, the first prime number.
  3. Mark all the multiples of 2 in the list as composite: (2, 3, **4**, 5, **6**, 7, **8**, 9, **10**, 11, **12**, 13, **14**, 15, **16**, 17, **18**, 19, **20**).
  4. Find the first number greater than 2 in the list that is not marked as composite: 3. Let p = 3, the next prime number.
  5. Mark all the multiples of 3 in the list as composite: (2, 3, 4, 5, 6, 7, 8, **9**, 10, 11, 12, 13, 14, **15**, 16, 17, 18, 19, 20).
  6. Find the first number greater than 3 in the list that is not marked as composite: 5. Let p = 5, the next prime number.
  7. Mark all the multiples of 5 in the list as composite: (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, **14**, 15, **16**, 17, **18**, 19, **20**).
  8. Find the first number greater than 5 in the list that is not marked as composite: 7. Let p = 7, the next prime number.
  9. Mark all the multiples of 7 in the list as composite: (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, **19**, 20).
  10. Find the first number greater than 7 in the list that is not marked as composite: 11. Let p = 11, the next prime number.
  11. Mark all the multiples of 11 in the list as composite: (2, 3, 4, 5, 6, 7, 8



### File I/O : File input and output operations in Python Programming

- File input and output in python is to get input in a program from a file and write output to the same or another file.
- Python provides some built-in functions to perform both input and output operations, such as `print()`, `input()`, `open()`, `read()`, `write()`, and `close()`.
- To open a file in python, we use the `open()` function, which takes two arguments: the file name and the mode. The mode can be `'r'` for reading, `'w'` for writing, `'a'` for appending, or `'r+'` for both reading and writing .
- To read data from a file, we use the `read()` method of the file object, which returns a string containing the entire content of the file. We can also use the `readline()` method to read one line at a time, or the `readlines()` method to read all the lines into a list .
- To write data to a file, we use the `write()` method of the file object, which takes a string as an argument and writes it to the file. We can also use the `writelines()` method to write a list of strings to the file .
- To close a file, we use the `close()` method of the file object, which frees up the resources associated with the file. It is a good practice to close the file after we are done with it .
- To create a new file, we can use the `'w'` mode in the `open()` function, which will create the file if it does not exist, or overwrite it if it does. To delete a file, we can use the `remove()` function from the `os` module, which takes the file name as an argument and deletes it from the disk .
- To take input file from the terminal for python script, we can use the `sys` module, which provides access to the command-line arguments. The `sys.argv` is a list that contains the script name and the arguments passed to it. We can assign the input and output file names to variables using the `sys.argv` list.

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- The sieve of Eratosthenes is an algorithm that finds all the prime numbers up to a given limit. A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- The algorithm works as follows:
  - Create a list of consecutive integers from 2 to the limit, and mark them all as true.
  - Start from the smallest number 2, and mark all its multiples (except itself) as false, since they are not prime.
  - Find the next number that is still marked as true, and repeat the previous step for it, marking all its multiples as false.
  - Continue this process until we reach the square root of the limit, or there are no more numbers marked as true.
  - The numbers that are still marked as true are the prime numbers up to the limit.
- The following is an example of python code that implements the sieve of Eratosthenes algorithm:

```python
# define the limit
limit = 100

# create a list of booleans from 2 to limit
is_prime = [True] * (limit + 1)

# loop from 2 to the square root of limit
for i in range(2, int(limit**0.5) + 1):
  # if i is marked as prime
  if is_prime[i]:
    # mark all the multiples of i as not prime
    for j in range(i * i, limit + 1, i):
      is_prime[j] = False

# print the prime numbers
for i in range(2, limit + 1):
  if is_prime[i]:
    print(i, end=" ")
```



### Exceptions and Assertions

- Exceptions are errors that occur during the execution of a program and disrupt its normal flow. They can be caused by various reasons, such as invalid input, division by zero, file not found, etc. Exceptions can be handled using the `try` and `except` statements, which allow the program to recover from the error or perform some alternative action. Exceptions can also be raised explicitly using the `raise` statement, which allows the programmer to signal an error condition to the caller of the function or the module. Exceptions are represented by classes that inherit from the `BaseException` class.

- Assertions are statements that check if a certain condition is true or false. They are used as debugging tools to verify the correctness of the program logic and detect any bugs or inconsistencies. Assertions are executed using the `assert` statement, which takes an expression and an optional message as arguments. If the expression evaluates to `False`, an `AssertionError` exception is raised with the message as the argument. If the expression evaluates to `True`, nothing happens. Assertions are usually placed at the start or the end of a function to check the validity of the input or the output.

- The difference between exceptions and assertions is that exceptions address the robustness of the application, while assertions address the correctness. Exceptions are meant to handle unexpected or unavoidable errors that may occur during the program execution, while assertions are meant to verify the assumptions or invariants that must hold true at all times. Exceptions can be caught and handled by the program, while assertions are usually enabled only during the development or testing phase and disabled in the production code.

- An example of using exceptions and assertions in Python is the following:

```python
# Define a function that returns the nth prime number using the Sieve of Eratosthenes algorithm
def nth_prime(n):
    # Check if the input is a positive integer
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    # Initialize a list of numbers from 2 to n^2
    numbers = list(range(2, n**2 + 1))
    # Initialize an empty list of primes
    primes = []
    # Loop until n primes are found
    while len(primes) < n:
        # Take the first number in the list as the next prime
        prime = numbers[0]
        primes.append(prime)
        # Remove all multiples of the prime from the list
        numbers = [x for x in numbers if x % prime != 0]
    # Return the last prime in the list
    return primes[-1]

# Try to call the function with different inputs
try:
    print(nth_prime(10)) # Prints 29
    print(nth_prime(0)) # Raises an AssertionError
    print(nth_prime(1.5)) # Raises an AssertionError
    print(nth_prime(1000)) # Prints 7919
except AssertionError as e:
    print(e) # Prints the assertion message
```



### Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, variables, etc.
- A module can be imported by another Python program to use its code.
- To import a module, use the `import` statement followed by the module name, for example: `import math`
- To access the code of a module, use the dot (`.`) operator followed by the name of the function, class, variable, etc., for example: `math.sqrt(25)`
- To import only specific names from a module, use the `from` ... `import` statement, for example: `from math import pi, sin`
- To import all names from a module, use the `from` ... `import *` statement, for example: `from math import *`
- To rename a module or a name from a module, use the `as` keyword, for example: `import math as m`, `from math import pi as p`

### Sieve of Eratosthenes: Generate Prime Numbers with the Help of an Algorithm Given by the Greek Mathematician Named Eratosthenes, Whose Algorithm is Known as Sieve of Eratosthenes

- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- The sieve of Eratosthenes is a method for finding all prime numbers up to a given limit, n.
- The algorithm works as follows:
  - Create a list of consecutive numbers from 2 to n: (2, 3, 4, ..., n).
  - Start with the first number, 2, and mark it as prime.
  - Find the next unmarked number, 3, and mark it as prime.
  - For each prime number p, mark all its multiples from 2p to n as composite (not prime), for example: 4, 6, 8, ..., n for p = 2; 6, 9, 12, ..., n for p = 3; etc.
  - Repeat the previous step until there are no more unmarked numbers.
  - The remaining unmarked numbers are all prime.
- The sieve of Eratosthenes is an efficient way to find small prime numbers, but it requires a lot of memory to store the list of numbers and their marks.
- Here is an example of a Python program that implements the sieve of Eratosthenes:

```python
# Define a function that takes a limit n and returns a list of prime numbers up to n
def sieve_of_eratosthenes(n):
  # Create a list of consecutive numbers from 2 to n: (2, 3, 4, ..., n)
  numbers = list(range(2, n + 1))
  # Create a list of boolean values to mark the numbers as prime or composite
  # Initially, all numbers are marked as prime (True)
  marks = [True] * (n - 1)
  # Loop through the numbers from 2 to the square root of n
  for i in range(2, int(n ** 0.5) + 1):
    # If the number is marked as prime
    if marks[i - 2]:
      # Mark all its multiples from 2i to n as composite (False)
      for j in range(2 * i, n + 1, i):
        marks[j - 2] = False
  # Create an empty list to store the prime numbers
  primes = []
  # Loop through the numbers from 2 to n
  for i in range(2, n + 1):
    # If the number is marked as prime
    if marks[i - 2]:
      # Append it to the list of prime numbers
      primes.append(i)
  # Return the list of prime numbers
  return primes

# Test the function with some examples
print(sieve_of_eratosthenes(10)) # [2, 3, 5, 7]
print(sieve_of_eratosthenes(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(sieve_of_eratosthenes(100)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,

```




### Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, only the behavior and interface of the data type .
- An ADT can have multiple concrete data types (CDTs) that implement the ADT using different data structures and algorithms .
- Examples of ADTs are stack, queue, list, map, set, tree, etc. Each of these ADTs can have different CDTs, such as array-based stack, linked-list stack, hash map, binary tree, etc .

### ADT Interface in Python

- Python does not have a built-in way to define ADTs, but it provides some features that can help create and use ADTs .
- One way to define an ADT in Python is to use a class that specifies the methods and attributes of the ADT, but leaves them unimplemented or raises a `NotImplementedError` exception .
- Another way to define an ADT in Python is to use an abstract base class (ABC) from the `abc` module, which allows marking methods and properties as abstract using the `@abstractmethod` and `@abstractproperty` decorators.
- An ABC can also register concrete subclasses that implement the ADT using the `register` method or the `@register` decorator.
- An example of an ABC that defines the ADT of a stack is:

```python
from abc import ABC, abstractmethod

class Stack(ABC):
    """An abstract base class for a stack ADT."""

    @abstractmethod
    def push(self, item):
        """Add an item to the top of the stack."""
        pass

    @abstractmethod
    def pop(self):
        """Remove and return the item from the top of the stack."""
        pass

    @abstractmethod
    def peek(self):
        """Return the item from the top of the stack without removing it."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        pass

    @abstractmethod
    def size(self):
        """Return the number of items in the stack."""
        pass
```

- A concrete subclass that implements the stack ADT using a list is:

```python
class ListStack(Stack):
    """A concrete class for a stack ADT using a list."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the item from the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)
```

- An example of using the stack ADT is:

```python
s = ListStack() # create a stack object
s.push(1) # push 1 to the stack
s.push(2) # push 2 to the stack
s.peek() # return 2
s.pop() # return and remove 2
s.size() # return 1
s.is_empty() # return False
s.pop() # return and remove 1
s.is_empty() # return True
s.pop() # raise IndexError
```

### Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit.
- The algorithm works by creating a list of numbers from 2 to the limit, and marking the multiples of each number, starting from 2, as composite (not prime).
- The numbers that are not marked as composite are prime, and can be returned



### Classes

- A class is a blueprint or template for creating objects in Python. An object is an instance of a class that has attributes (data) and methods (functions) associated with it.
- A class definition starts with the keyword `class` followed by the name of the class and a colon. The class name should follow the naming convention of using capital letters for each word and no underscores (e.g. `MyClass`).
- The class body contains the attributes and methods of the class, indented under the class header. The first argument of every method is `self`, which refers to the current object.
- To create an object of a class, we use the class name followed by parentheses (e.g. `obj = MyClass()`). This calls the constructor method `__init__` of the class, which initializes the object with some initial values or parameters.
- To access or modify the attributes or methods of an object, we use the dot notation (e.g. `obj.attr` or `obj.method()`).

### Special Methods

- Special methods are methods that have a special meaning or functionality in Python. They are also called magic methods or dunder methods because they start and end with double underscores (e.g. `__init__`).
- Some of the common special methods are:

  - `__init__(self, ...)` : The constructor method that is called when an object is created. It takes `self` and any other parameters that are needed to initialize the object.
  - `__str__(self)` : The string representation method that is called when an object is printed or converted to a string. It returns a string that describes the object.
  - `__eq__(self, other)` : The equality comparison method that is called when two objects are compared using the `==` operator. It returns `True` if the objects are equal and `False` otherwise.
  - `__lt__(self, other)` : The less than comparison method that is called when two objects are compared using the `<` operator. It returns `True` if the first object is less than the second object and `False` otherwise.
  - `__add__(self, other)` : The addition method that is called when two objects are added using the `+` operator. It returns a new object that is the result of adding the two objects.
  - `__sub__(self, other)` : The subtraction method that is called when two objects are subtracted using the `-` operator. It returns a new object that is the result of subtracting the two objects.

### Class Example

- Here is an example of a class that represents a point in a two-dimensional plane:

```python
class Point:
  # constructor method
  def __init__(self, x, y):
    # attributes
    self.x = x
    self.y = y

  # string representation method
  def __str__(self):
    return f"({self.x}, {self.y})"

  # equality comparison method
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  # less than comparison method
  def __lt__(self, other):
    return self.x < other.x or (self.x == other.x and self.y < other.y)

  # addition method
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  # subtraction method
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

  # a custom method to calculate the distance from the origin
  def distance(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5
```

- Here are some examples of using the class and its methods:

```python
# create two point objects
p1 = Point(3, 4)
p2 = Point(1, 2)

# print the objects
print(p1) # (3, 4)
print(p2) # (1, 2)

# compare the objects
print(p1 == p2) # False
print(p1 < p2) # False
print(p1 > p2) # True

# add and subtract the objects
print(p1 + p2) # (4, 6)
print(p1 - p2) # (2, 2)

# call the custom method
print(p1.distance()) # 5.0
```

### Inheritance

- Inheritance is a mechanism that allows a class to inherit the attributes and methods of another class. The class that inherits is called the subclass or child class, and the class that



## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers where each number is the sum of the previous two numbers. The first two numbers are 1 and 1. For example, the first 10 numbers of the Fibonacci sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
- A recursive function is a function that calls itself to solve smaller subproblems until a base case is reached. A base case is a simple case that can be solved directly without recursion.
- A recursive function to compute the nth Fibonacci number can be defined as follows:

```python
def fibonacci(n):
  # base case: the first and second Fibonacci numbers are 1
  if n == 1 or n == 2:
    return 1
  # recursive case: the nth Fibonacci number is the sum of the previous two
  else:
    return fibonacci(n-1) + fibonacci(n-2)
```

- The recursive function has two parameters: n, which is the position of the Fibonacci number to compute, and a memo, which is a dictionary that stores the previously computed Fibonacci numbers to avoid repeated calculations. The memo is initialized with the base cases: 1 and 1.
- The recursive function checks if n is in the memo. If yes, it returns the value from the memo. If not, it computes the value by calling itself with n-1 and n-2, and stores the result in the memo before returning it.

```python
def fibonacci(n, memo = {1: 1, 2: 1}):
  # check if n is in the memo
  if n in memo:
    return memo[n]
  # compute the value and store it in the memo
  else:
    value = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = value
    return value
```

### Tower of Hanoi

- The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.
- The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  - No disk may be placed on top of a smaller disk.
- A recursive solution to the Tower of Hanoi puzzle can be defined as follows:

```python
def hanoi(n, source, target, auxiliary):
  # base case: if there is only one disk, move it from source to target
  if n == 1:
    print(f"Move disk 1 from {source} to {target}")
  # recursive case: if there are more than one disk, move them in three steps
  else:
    # step 1: move the top n-1 disks from source to auxiliary, using target as a temporary rod
    hanoi(n-1, source, auxiliary, target)
    # step 2: move the bottom disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # step 3: move the n-1 disks from auxiliary to target, using source as a temporary rod
    hanoi(n-1, auxiliary, target, source)
```

- The recursive function has four parameters: n, which is the number of disks to move, source, which is the rod where the disks are initially stacked, target, which is the rod where the disks are to be moved, and auxiliary, which is the third rod that can be used as a temporary storage.
- The recursive function prints the steps to move the disks from source to target, following the rules of the puzzle.



### Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search Time

- Search is a common operation that involves finding an element in a collection that satisfies a given condition or matches a given value.
- There are different algorithms for performing search, depending on the type and structure of the collection, and the desired efficiency and accuracy of the search.
- In this section, we will discuss two basic search algorithms: simple search and binary search, and how to estimate their running time.

#### Simple Search

- Simple search, also known as linear search or sequential search, is a brute-force algorithm that checks every element in the collection until it finds the target element or reaches the end of the collection.
- Simple search can be applied to any collection, regardless of its order or structure.
- The pseudocode for simple search is as follows:

```
# Assume collection is a list of elements, and target is the value to be searched
def simple_search(collection, target):
  # Loop through the collection from the first element to the last
  for i in range(len(collection)):
    # If the current element matches the target, return its index
    if collection[i] == target:
      return i
  # If the loop ends without finding the target, return -1 to indicate failure
  return -1
```

- The running time of simple search depends on the size of the collection and the position of the target element (if it exists).
- In the best case, the target element is the first element in the collection, and the algorithm only needs one comparison to find it. The best case running time is O(1).
- In the worst case, the target element is the last element in the collection, or does not exist in the collection, and the algorithm needs to check every element in the collection. The worst case running time is O(n), where n is the number of elements in the collection.
- In the average case, the target element is somewhere in the middle of the collection, and the algorithm needs to check about half of the elements in the collection. The average case running time is also O(n), since the constant factor of 1/2 can be ignored in the asymptotic notation.

#### Binary Search

- Binary search, also known as logarithmic search or bisection search, is a divide-and-conquer algorithm that exploits the order of a sorted collection to find the target element more efficiently than simple search.
- Binary search can only be applied to a collection that is sorted in ascending or descending order.
- The pseudocode for binary search is as follows:

```
# Assume collection is a list of elements sorted in ascending order, and target is the value to be searched
def binary_search(collection, target):
  # Initialize the lower and upper bounds of the search range
  low = 0
  high = len(collection) - 1
  # Loop until the search range is empty
  while low <= high:
    # Find the middle element of the current search range
    mid = (low + high) // 2
    # If the middle element matches the target, return its index
    if collection[mid] == target:
      return mid
    # If the middle element is smaller than the target, narrow the search range to the right half
    elif collection[mid] < target:
      low = mid + 1
    # If the middle element is larger than the target, narrow the search range to the left half
    else:
      high = mid - 1
  # If the loop ends without finding the target, return -1 to indicate failure
  return -1
```

- The running time of binary search depends on the size of the collection and the position of the target element (if it exists).
- In the best case, the target element is the middle element of the collection, and the algorithm only needs one comparison to find it. The best case running time is O(1).
- In the worst case, the target element is one of the endpoints of the collection, or does not exist in the collection, and the algorithm needs to halve the search range until it becomes empty. The worst case running time is O(log n), where n is the number of elements in the collection.
- In the average case, the target element is somewhere in the middle of the collection, and the algorithm needs to halve the search range about log n times to find it. The average case running time is also O(log n), since the constant factor of 1/2 can be ignored in the asymptotic notation.



### Sorting and Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

- Sorting is the process of arranging data in a specific order, such as ascending or descending, based on some criteria.
- Merging is the process of combining two or more sorted lists into one sorted list.
- There are different algorithms for sorting and merging data, each with different advantages and disadvantages.

#### Selection Sort

- Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum or maximum element in the unsorted part of the list and moving it to the sorted part.
- The algorithm maintains two sublists: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted sublist, finds the smallest or largest element, and swaps it with the first element of the unsorted sublist.
- The algorithm repeats this process until the unsorted sublist is empty and the sorted sublist contains all the elements.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the list, because it has to compare each element with all the other elements in the unsorted sublist.
- The space complexity of selection sort is O(1), because it only requires a constant amount of extra space to store the index of the minimum or maximum element.
- Selection sort is not stable, meaning that it does not preserve the relative order of equal elements in the list.
- Selection sort is not adaptive, meaning that it does not take advantage of the existing order in the list.

#### Merge List

- Merge list is a function that takes two sorted lists as input and returns a new sorted list that contains all the elements from both lists.
- The function works by comparing the first elements of the two lists and appending the smaller one to the output list, then advancing the pointer of the list that contained the smaller element.
- The function repeats this process until one of the lists is exhausted, then appends the remaining elements of the other list to the output list.
- The time complexity of merge list is O(m + n), where m and n are the lengths of the two lists, because it has to iterate over both lists once.
- The space complexity of merge list is O(m + n), because it has to create a new list that contains all the elements from both lists.
- Merge list is stable, meaning that it preserves the relative order of equal elements in the lists.
- Merge list is adaptive, meaning that it takes advantage of the existing order in the lists.

#### Merge Sort

- Merge sort is a recursive sorting algorithm that works by dividing the list into two halves, sorting each half recursively, and then merging the two sorted halves using the merge list function.
- The algorithm follows the divide and conquer approach, where a complex problem is broken down into smaller and simpler subproblems, and then the solutions of the subproblems are combined to form the solution of the original problem.
- The algorithm uses a helper function called merge sort helper that takes the list, a start index, and an end index as parameters, and sorts the sublist between the start and end indices.
- The algorithm calls the merge sort helper function on the whole list, passing 0 and the length of the list minus one as the start and end indices.
- The merge sort helper function checks if the start index is less than the end index, meaning that the sublist has more than one element, and if so, it calculates the middle index by adding the start and end indices and dividing by two.
- The merge sort helper function then calls itself recursively on the left half of the sublist, passing the start and middle indices as the new start and end indices, and on the right half of the sublist, passing the middle plus one and end indices as the new start and end indices.
- The merge sort helper function then calls the merge list function on the two sorted halves of the sublist, and returns the merged list as the output.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the list, because it divides the list into two halves at each level of recursion, and merges the two halves in linear time at each level of recursion.
- The space complexity of merge sort is O(n), because it requires extra space to store the temporary lists created by the merge list function at each level of recursion.
- Merge sort is stable, meaning that it preserves the relative order of equal elements in the list.
- Merge sort is not adaptive, meaning that it does not take advantage of the existing order in the list.

#### Higher Order Sort

- Higher order sort is a term that refers to sorting algorithms that can take

