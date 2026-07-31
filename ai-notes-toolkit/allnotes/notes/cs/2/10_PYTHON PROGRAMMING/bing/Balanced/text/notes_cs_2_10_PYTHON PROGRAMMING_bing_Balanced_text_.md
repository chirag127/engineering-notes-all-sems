

## Unit 1 - Introduction: The Programming Cycle for Python , Python IDE, Interacting with Python Programs , Elements of Python, Type Conversion.

- The programming cycle for Python consists of four steps: writing, testing, debugging, and running the program.
- Writing a Python program involves creating a text file that contains the instructions for the computer to execute. The text file is also called a source code or a script.
- Testing a Python program involves checking if the program works as expected and produces the desired output. Testing can be done by running the program and observing the results, or by using tools such as unit tests or debuggers.
- Debugging a Python program involves finding and fixing the errors or bugs that prevent the program from working correctly. Debugging can be done by using tools such as debuggers, print statements, or breakpoints.
- Running a Python program involves executing the instructions in the source code and obtaining the output. Running can be done by using tools such as interpreters, compilers, or integrated development environments (IDEs).
- A Python IDE is a software application that provides a graphical user interface (GUI) for writing, testing, debugging, and running Python programs. Some examples of Python IDEs are PyCharm, Visual Studio Code, Spyder, and Thonny.
- Interacting with Python programs can be done in two ways: using the interactive mode or using the script mode.
- The interactive mode allows the user to enter Python commands or expressions one by one and see the results immediately. The interactive mode can be accessed by using tools such as the Python shell, the IPython shell, or the Jupyter notebook.
- The script mode allows the user to run a Python program that is stored in a text file. The script mode can be accessed by using tools such as the Python interpreter, the command line, or the IDE.
- Elements of Python are the basic components that make up a Python program. Some examples of elements of Python are keywords, identifiers, literals, operators, expressions, statements, comments, and indentation.
- Keywords are reserved words that have a special meaning and function in Python. They cannot be used as identifiers. Some examples of keywords are `def`, `if`, `for`, `return`, and `import`.
- Identifiers are names that are used to refer to variables, functions, classes, modules, or other objects in Python. They must start with a letter or an underscore and can contain letters, digits, or underscores. They are case-sensitive. Some examples of identifiers are `x`, `sum`, `print`, `math`, and `MyClass`.
- Literals are values that are written directly in the source code. They can be of different types, such as integers, floats, strings, booleans, or None. Some examples of literals are `42`, `3.14`, `"Hello"`, `True`, and `None`.
- Operators are symbols that are used to perform operations on operands, such as arithmetic, comparison, logical, assignment, or membership operations. Some examples of operators are `+`, `-`, `*`, `/`, `==`, `!=`, `and`, `or`, `=`, and `in`.
- Expressions are combinations of operands and operators that produce a value. Some examples of expressions are `x + y`, `a * b`, `x == y`, and `x in y`.
- Statements are instructions that tell the computer what to do. They can be simple or compound. Some examples of statements are `print(x)`, `if x > y:`, `for i in range(10):`, and `return z`.
- Comments are parts of the source code that are ignored by the interpreter and are used to explain or document the program. They start with a `#` symbol and end with a newline. Some examples of comments are `# This is a comment`, `# Calculate the sum of x and y`, and `# TODO: fix this bug`.
- Indentation is the use of whitespace at the beginning of a line to indicate the level of nesting or grouping of statements. Indentation is mandatory and significant in Python. It is usually done by using four spaces or one tab per level. Some examples of indentation are:

```python
# This is a function definition
def add(x, y):
    # This is a function body
    # This is an indented block
    z = x + y # This is a simple statement
    return z # This is another simple statement

# This is a for loop
for i in range(10):
    # This is a for loop body
    # This is another indented block
    print(i) # This is a simple statement
```

- Type conversion is the process of changing the type of a value



### Basics: Expressions for the notes of the Unit 1 - Introduction: The Programming Cycle for Python , Python IDE, Interacting with Python Programs , Elements of Python, Type Conversion.

- Expressions are representations of value that are composed of identifiers, literals, and operators.
- Identifiers are any names that are used to define a class, function, variable, module, or object.
- Literals are language-independent terms in Python that should exist independently in any programming language, such as numbers, strings, booleans, etc.
- Operators are special symbols that designate that some sort of computation should be performed, such as arithmetic, logical, comparison, assignment, etc.
- Expressions are evaluated according to the precedence and associativity of their operators.
- Expressions can be used in statements, assignments, function calls, or conditional expressions.
- Conditional expressions are a way of writing a single line if-else statement, using the syntax `X if condition else Y`.
- Python IDE (Integrated Development Environment) is a software application that provides a comprehensive set of tools for Python programming, such as code editor, debugger, interpreter, etc.
- Interacting with Python programs can be done in two ways: using the interactive mode or the script mode.
- Interactive mode allows the user to enter Python commands one by one and see the results immediately in the console.
- Script mode allows the user to write Python code in a file and execute it as a whole using the interpreter.
- Elements of Python are the basic components of the language, such as keywords, identifiers, literals, operators, expressions, statements, comments, etc.
- Type conversion is the process of changing the data type of a value, either implicitly or explicitly.
- Implicit type conversion is done automatically by Python when it needs to operate on values of different types, such as adding an integer and a float.
- Explicit type conversion is done by the user using built-in functions, such as `int()`, `float()`, `str()`, etc, to convert one type to another.

: https://www.hackerearth.com/practice/python/working-with-data/expressions/tutorial/
: https://note.nkmk.me/en/python-if-conditional-expressions/
: https://docs.python.org/3/reference/expressions.html
: https://www.geeksforgeeks.org/expressions-in-python/
: https://realpython.com/python-operators-expressions/
: https://www.guru99.com/python-ide-code-editor.html
: https://www.tutorialspoint.com/python/python_basic_syntax.htm
: https://www.javatpoint.com/python-tutorial
: https://www.programiz.com/python-programming/type-conversion-and-casting



### Assignment Statement

- An assignment statement is a way of creating, initializing, or updating variables in Python.
- A variable is a name that refers to an object, such as a number, a string, a list, or a function.
- An assignment statement has the form `target = expression`, where `target` is the name of the variable and `expression` is any Python expression that evaluates to an object.
- The assignment statement assigns the object resulting from the expression to the target variable, creating or updating the variable's reference to the object.
- For example, `x = 5` assigns the integer object `5` to the variable `x`, creating or updating `x`'s reference to `5`.
- Python supports multiple assignment, where more than one target variable can be assigned to the same or different objects in a single statement.
- For example, `x, y = 10, 20` assigns the integer object `10` to the variable `x` and the integer object `20` to the variable `y` in one statement.
- Multiple assignment can also be used to swap the values of two variables without using a temporary variable.
- For example, `x, y = y, x` swaps the values of `x` and `y` by assigning the object that `y` refers to `x` and the object that `x` refers to `y`.
- Python also supports augmented assignment, where an operator and an equal sign are combined to perform an arithmetic or bitwise operation and assign the result to the target variable in one statement.
- For example, `x += 5` is equivalent to `x = x + 5`, which adds `5` to the object that `x` refers to and assigns the result to `x`.
- Augmented assignment can be used with any of the following operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
- Augmented assignment can also be used with mutable objects, such as lists or dictionaries, to modify their contents without creating a new object.
- For example, `lst += [4, 5, 6]` appends the list `[4, 5, 6]` to the end of the list that `lst` refers to, modifying `lst` in place.



### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values. They are binary operators, which means they operate on two operands. The following are the arithmetic operators in Python:

- `+` : Addition. It adds the values on either side of the operator. For example, `2 + 3` gives `5`.
- `-` : Subtraction. It subtracts the right operand from the left operand. For example, `5 - 2` gives `3`.
- `*` : Multiplication. It multiplies the values on either side of the operator. For example, `2 * 3` gives `6`.
- `/` : Division. It divides the left operand by the right operand. For example, `6 / 2` gives `3.0`. Note that the result is always a floating-point number, even if the operands are integers.
- `%` : Modulus. It returns the remainder of the division of the left operand by the right operand. For example, `7 % 2` gives `1`.
- `**` : Exponentiation. It raises the left operand to the power of the right operand. For example, `2 ** 3` gives `8`.
- `//` : Floor division. It performs integer division and returns the largest integer less than or equal to the result. For example, `7 // 2` gives `3`. Note that the result is always an integer, even if the operands are floating-point numbers.



### Operator Precedence for the notes of the Unit 1 - Introduction: The Programming Cycle for Python , Python IDE, Interacting with Python Programs , Elements of Python, Type Conversion.

- Operator precedence in Python means the order in which the Python interpreter executes operators.
- It tells the Python interpreter which operator should be evaluated first if a single statement contains more than one operator.
- Therefore, it is essential to understand the order of precedence to avoid the ambiguity in the expressions.
- The following table summarizes the operator precedence in Python, from highest to lowest:

| Operator | Description |
|:--------:|:-----------:|
| `()` | Parentheses |
| `**` | Exponentiation |
| `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT |
| `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo |
| `+`, `-` | Addition, subtraction |
| `<<`, `>>` | Bitwise left shift, bitwise right shift |
| `&` | Bitwise AND |
| `^` | Bitwise XOR |
| `|` | Bitwise OR |
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, membership tests, identity tests |
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
z = x if x > y else y # z is assigned to y, not x
print(z) # prints 10, not 5
```

- Type conversion in Python means changing the data type of a value or variable to another data type.
- There are two types of type conversion in Python: implicit and explicit.
- Implicit type conversion is done automatically by the Python interpreter when it needs to operate on values of different types.
- Explicit type conversion is done by the programmer using built-in functions such as `int()`, `float()`, `str()`, `bool()`, etc.
- Some examples of type conversion in Python are:

```python
# Example 1: Implicit type conversion
x = 10 # x is an integer
y = 3.14 # y is a float
z = x + y # z is a float, because x is converted to a float
print(z) # prints 13.14

# Example 2: Explicit type conversion
x = "10" # x is a string
y = int(x) # y is an integer, because x is converted to an integer
z = y + 5 # z is an integer
print(z) # prints 15
```



### Boolean Expression

- A Boolean expression in Python is a combination of values or values and functions that can be interpreted by the Python compiler to return a value that is either true or false.
- It often consists of at least two terms separated by a comparison operator, such as `price > 0`.
- The comparison operators in Python are: `==` (equal to), `!=` (not equal to), `<` (less than), `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to).
- A Boolean expression can also use logical operators to combine multiple comparison expressions, such as `and`, `or`, and `not`.
- The logical operators in Python follow these rules: `and` returns true if both operands are true, `or` returns true if either operand is true, `not` returns the opposite of the operand.
- A Boolean expression can also use parentheses to group subexpressions and change the order of evaluation.
- For example, the expression `(price > 0) and (quantity > 0)` evaluates to true if both price and quantity are positive numbers.
- A Boolean expression can also use the `in` and `not in` operators to check if a value is or is not in a sequence, such as a string, a list, or a tuple.
- For example, the expression `'a' in 'apple'` evaluates to true, while the expression `'b' not in 'banana'` evaluates to false.
- A Boolean expression can also use the `is` and `is not` operators to check if two variables refer to the same object in memory.
- For example, the expression `x is y` evaluates to true if x and y are the same object, while the expression `x is not y` evaluates to false if they are different objects.
- A Boolean expression can also use the `None` value to check if a variable has no value assigned to it.
- For example, the expression `x is None` evaluates to true if x has no value, while the expression `x is not None` evaluates to false if x has some value.
- A Boolean expression can also use any other value or variable as a truth value, following these rules: any non-zero number is true, any non-empty sequence is true, any other object is true, except for `None` and `False` .
- For example, the expression `bool(1)` evaluates to true, while the expression `bool(0)` evaluates to false .



## Unit 2 - Conditionals

- Conditional statements are used to control the flow of execution of a program based on some conditions.
- In Python, the most common conditional statement is the `if-else` statement, which has the following syntax:

```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False
```

- The `condition` is a boolean expression that evaluates to either `True` or `False`.
- The `if` and `else` keywords are followed by a colon (`:`) and indented blocks of code.
- The indented block of code under the `if` clause is executed only if the condition is `True`, otherwise the indented block of code under the `else` clause is executed.
- For example, the following code prints a message based on the value of a variable `x`:

```python
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative or zero")
```

- The output of this code is:

```
x is positive
```

- Nested-if statement is a conditional statement that contains another conditional statement inside it.
- The nested conditional statement can be either an `if-else` statement or an `elif` statement.
- The `elif` statement is used to check multiple conditions in a sequential manner, and has the following syntax:

```python
if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition1 is False and condition2 is True
elif condition3:
    # block of code to execute if condition1 and condition2 are False and condition3 is True
...
else:
    # block of code to execute if all conditions are False
```

- The `elif` keyword is short for `else if`, and is followed by a colon (`:`) and an indented block of code.
- The `elif` clause is executed only if the previous condition is `False` and the current condition is `True`.
- The `else` clause is executed only if all the conditions are `False`.
- For example, the following code prints a message based on the value of a variable `grade`:

```python
grade = 85
if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Good")
elif grade >= 70:
    print("Fair")
elif grade >= 60:
    print("Pass")
else:
    print("Fail")
```

- The output of this code is:

```
Good
```

- Expression evaluation is the process of computing the value of an expression by applying the rules of precedence and associativity of operators and operands.
- In Python, the order of precedence of operators from highest to lowest is:

  - Parentheses `()`
  - Exponentiation `**`
  - Unary operators `+`, `-`, `~`, `not`
  - Multiplication `*`, division `/`, floor division `//`, modulo `%`
  - Addition `+`, subtraction `-`
  - Bitwise operators `<<`, `>>`, `&`, `^`, `|`
  - Comparison operators `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not`, `in`, `not in`
  - Logical operators `and`, `or`

- The associativity of operators determines the order of evaluation of operators with the same precedence level.
- In Python, most operators are left-associative, meaning they are evaluated from left to right, except for the exponentiation operator `**`, which is right-associative, meaning it is evaluated from right to left.
- For example, the following expression is evaluated as:

```python
2 ** 3 ** 2
```

- `(2 ** (3 ** 2))`
- `(2 ** 9)`
- `512`

- Float representation is the way of storing and displaying decimal numbers in a computer system.
- In Python, float numbers are represented using the IEEE 754 standard, which uses a fixed number of bits (usually 64) to store the sign, exponent, and fraction of a decimal number.
- The sign bit indicates whether the number is positive or negative, the exponent bits indicate the magnitude of the number, and the fraction bits indicate the precision of the number.
- For example, the float number `12.34` is represented as:

```
0 10000000010 10001011100011110101110
```

- The sign bit is `0`, indicating the number is positive.
- The exponent bits are `



### Loops: Purpose and working of loops

- A loop is a programming construct that allows a block of code to be executed repeatedly until a certain condition is met.
- The purpose of loops is to automate repetitive tasks, such as processing a list of items, performing calculations, or generating output.
- There are two types of loops in Python: for loops and while loops.
- A for loop iterates over a sequence of values, such as a list, a tuple, a string, or a range object, and executes the block of code for each value in the sequence.
- A while loop executes the block of code as long as a given condition is true, and stops when the condition becomes false.
- The syntax of a for loop is:

```python
for variable in sequence:
    # block of code
```

- The syntax of a while loop is:

```python
while condition:
    # block of code
```

- The block of code inside a loop is indented by four spaces or a tab, and is also called the loop body.
- The loop variable in a for loop takes the value of each element in the sequence, and can be used inside the loop body.
- The condition in a while loop is a boolean expression that evaluates to either True or False, and can use any comparison or logical operators.
- To exit a loop prematurely, the break statement can be used. This will stop the loop execution and jump to the next statement after the loop.
- To skip the current iteration of a loop and continue with the next one, the continue statement can be used. This will skip the loop body and go back to the loop condition.
- To loop through a sequence of values in reverse order, the reversed() function can be used. This will return an iterator that yields the values in reverse order.
- To loop through two or more sequences of values in parallel, the zip() function can be used. This will return an iterator that yields tuples of corresponding values from each sequence.
- To loop through a sequence of values with their indices, the enumerate() function can be used. This will return an iterator that yields pairs of index and value from the sequence.



### While loop

- A while loop is a type of loop that repeats a block of code as long as a given condition is true.
- The syntax of a while loop is:

```python
while condition:
    # block of code
```

- The condition is a boolean expression that evaluates to either True or False.
- The block of code is indented under the while statement and can contain any valid Python statements.
- The while loop checks the condition before each iteration and executes the block of code only if the condition is True.
- The while loop ends when the condition becomes False or when a break statement is encountered inside the loop.
- A while loop can also have an optional else clause that executes after the loop ends normally (without a break statement).

```python
while condition:
    # block of code
else:
    # block of code after the loop
```

- The else clause is useful for performing some final actions after the loop, such as closing a file or displaying a message.
- A while loop can be used to implement various algorithms and tasks, such as counting, searching, validating input, etc.

### Example of a while loop

- The following program uses a while loop to print the numbers from 1 to 10.

```python
# initialize a counter variable
count = 1

# loop until count is greater than 10
while count <= 10:
    # print the current value of count
    print(count)
    # increment count by 1
    count = count + 1

# print a message after the loop
print("The loop is over.")
```

- The output of the program is:

```
1
2
3
4
5
6
7
8
9
10
The loop is over.
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
# print the elements of a list
my_list = [1, 2, 3, 4, 5]
for x in my_list:
    print(x)

# print the characters of a string
my_string = "Hello"
for ch in my_string:
    print(ch)

# print the numbers from 0 to 9 using a range object
for i in range(10):
    print(i)

# print the even numbers from 0 to 10 using a range object with a step argument
for i in range(0, 11, 2):
    print(i)

# print the sum of the elements of a list using a loop variable
my_list = [1, 2, 3, 4, 5]
sum = 0
for x in my_list:
    sum = sum + x
print(sum)

# print the factorial of a number using a loop variable and a break statement
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
    if i == n:
        break
print(factorial)

# print the first 10 Fibonacci numbers using a loop variable and a return statement
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a + b
        if i == n - 1:
            return
fibonacci(10)
```



### Nested Loops

- A nested loop is a loop that is placed inside another loop.
- The inner loop is executed once for each iteration of the outer loop.
- The syntax of a nested loop in Python is:

```python
for i in range(n): # outer loop
  for j in range(m): # inner loop
    # do something with i and j
```

- Nested loops can be used to perform various tasks, such as:
  - Printing patterns or shapes
  - Iterating over multidimensional data structures (such as lists of lists, matrices, etc.)
  - Searching or sorting algorithms
  - Simulating complex scenarios (such as games, simulations, etc.)

- Some examples of nested loops are:

```python
# Printing a square of asterisks
n = 5 # size of the square
for i in range(n):
  for j in range(n):
    print("*", end=" ") # print an asterisk and a space
  print() # print a new line

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
```

```python
# Printing a multiplication table
n = 10 # size of the table
for i in range(1, n+1):
  for j in range(1, n+1):
    print(i*j, end="\t") # print the product and a tab
  print() # print a new line

# Output:
# 1	2	3	4	5	6	7	8	9	10
# 2	4	6	8	10	12	14	16	18	20
# 3	6	9	12	15	18	21	24	27	30
# 4	8	12	16	20	24	28	32	36	40
# 5	10	15	20	25	30	35	40	45	50
# 6	12	18	24	30	36	42	48	54	60
# 7	14	21	28	35	42	49	56	63	70
# 8	16	24	32	40	48	56	64	72	80
# 9	18	27	36	45	54	63	72	81	90
# 10	20	30	40	50	60	70	80	90	100
```

```python
# Finding the maximum element in a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # a 3x3 matrix
max_element = matrix[0][0] # initialize the maximum element to the first element
for i in range(len(matrix)): # iterate over the rows
  for j in range(len(matrix[i])): # iterate over the columns
    if matrix[i][j] > max_element: # compare the current element with the maximum element
      max_element = matrix[i][j] # update the maximum element if needed
print("The maximum element is", max_element) # print the result

# Output:
# The maximum element is 9
```



### Break and Continue

- Break and continue are two keywords that can be used to alter the flow of a loop in Python.
- Break is used to exit the loop prematurely, while continue is used to skip the current iteration and move on to the next one.
- Break and continue can be used with both for and while loops, but they have different effects depending on the type of loop.

#### Break with for loop

- A break statement inside a for loop will terminate the loop and execute the code after the loop.
- For example, the following code will print the numbers from 1 to 10, but stop when it reaches 5:

```python
for i in range(1, 11):
  print(i)
  if i == 5:
    break
print("Loop ended")
```

- The output will be:

```text
1
2
3
4
5
Loop ended
```

#### Break with while loop

- A break statement inside a while loop will also terminate the loop and execute the code after the loop.
- For example, the following code will print the numbers from 1 to 10, but stop when it reaches 5:

```python
i = 1
while i < 11:
  print(i)
  if i == 5:
    break
  i += 1
print("Loop ended")
```

- The output will be the same as the previous example.

#### Continue with for loop

- A continue statement inside a for loop will skip the current iteration and continue with the next one.
- For example, the following code will print the odd numbers from 1 to 10:

```python
for i in range(1, 11):
  if i % 2 == 0:
    continue
  print(i)
```

- The output will be:

```text
1
3
5
7
9
```

#### Continue with while loop

- A continue statement inside a while loop will also skip the current iteration and continue with the next one.
- For example, the following code will print the odd numbers from 1 to 10:

```python
i = 1
while i < 11:
  if i % 2 == 0:
    i += 1
    continue
  print(i)
  i += 1
```

- The output will be the same as the previous example.



## Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

- A function is a block of code that performs a specific task, such as printing a message, calculating a value, or sorting a list.
- A function can be defined using the `def` keyword, followed by the function name and a pair of parentheses that may contain some parameters.
- A function can be called by using the function name followed by a pair of parentheses that may contain some arguments.
- A function can return a value to the caller using the `return` statement, or return `None` by default if there is no `return` statement.
- A function can have four types of parameters: positional, keyword, default, and variable-length.
- Positional parameters are the ones that are specified in the function definition and must be passed in the same order by the caller.
- Keyword parameters are the ones that are specified in the function definition and can be passed by using the parameter name and an equal sign, regardless of the order.
- Default parameters are the ones that are specified in the function definition and have a default value assigned to them, which is used if the caller does not provide a value for that parameter.
- Variable-length parameters are the ones that are prefixed with an asterisk (*) or a double asterisk (**), and can accept any number of arguments from the caller. The single asterisk (*) creates a tuple of positional arguments, while the double asterisk (**) creates a dictionary of keyword arguments.
- A function can have a docstring, which is a string literal that appears as the first statement in the function body, and describes the purpose and usage of the function.
- A function can have local and global variables. Local variables are the ones that are defined inside the function body and are only accessible within the function. Global variables are the ones that are defined outside the function body and are accessible throughout the program.
- A function can modify a global variable by using the `global` keyword inside the function body, which tells the interpreter that the variable is not local but global.
- A function can also have nonlocal variables, which are the ones that are defined in the enclosing function, and are accessible by the nested function. A nested function can modify a nonlocal variable by using the `nonlocal` keyword inside the function body, which tells the interpreter that the variable is not local but nonlocal.



### Strings : Length of the string and perform Concatenation and Repeat operations in it. Indexing and Slicing of Strings.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or 'Python'.
- The length of a string is the number of characters in it, which can be obtained by using the `len()` function, such as `len("Hello")` returns 5.
- Concatenation is the operation of joining two or more strings together, using the `+` operator, such as `"Hello" + "World"` returns "HelloWorld".
- Repeat is the operation of repeating a string a certain number of times, using the `*` operator, such as `"Hello" * 3` returns "HelloHelloHello".
- Indexing is the operation of accessing a single character from a string, using square brackets and an integer index, such as `"Hello"[0]` returns "H". The index starts from 0 for the first character and goes up to `len(string) - 1` for the last character. Negative indexes can also be used to access characters from the end of the string, such as `"Hello"[-1]` returns "o". The index -1 corresponds to the last character and goes down to `-len(string)` for the first character.
- Slicing is the operation of accessing a substring, or a part of a string, using square brackets and a colon, such as `"Hello"[1:3]` returns "el". The syntax for slicing is `[start:stop:step]`, where `start` is the index of the first character to include, `stop` is the index of the first character to exclude, and `step` is the number of characters to skip between each character in the slice. If `start` is omitted, it defaults to 0. If `stop` is omitted, it defaults to `len(string)`. If `step` is omitted, it defaults to 1. Negative values can also be used for `start`, `stop`, and `step`, to indicate counting from the end of the string. For example, `"Hello"[-3:-1]` returns "ll", and `"Hello"[::-1]` returns "olleH", which is the reverse of the string.



### Python Data Structure : Tuples , Unpacking Sequences , Lists , Mutable Sequences , List Comprehension , Sets , Dictionaries

- A data structure is a way of organizing and storing data in a computer memory.
- Python provides several built-in data structures, such as tuples, lists, sets, and dictionaries.
- Each data structure has its own characteristics and operations.

#### Tuples
- A tuple is an ordered and immutable sequence of values, separated by commas and enclosed in parentheses.
- A tuple can store any type of data, such as numbers, strings, booleans, or other tuples.
- A tuple can be indexed and sliced using square brackets, similar to strings.
- A tuple can be iterated over using a for loop or a while loop.
- A tuple can be compared, concatenated, and repeated using operators, such as ==, +, and *.
- A tuple can be converted to a list using the list() function, or to a set using the set() function.
- A tuple can be created with or without parentheses, or with a single element and a trailing comma.
- Example:

```python
# Creating a tuple
t = (1, 2, 3, 4, 5)
t = 1, 2, 3, 4, 5 # without parentheses
t = (1,) # with a single element and a trailing comma

# Accessing a tuple element
t[0] # returns 1
t[-1] # returns 5
t[1:3] # returns (2, 3)

# Iterating over a tuple
for x in t:
  print(x)

i = 0
while i < len(t):
  print(t[i])
  i += 1

# Comparing tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1 == t2 # returns False
t1 < t2 # returns True

# Concatenating and repeating tuples
t3 = t1 + t2 # returns (1, 2, 3, 4, 5, 6)
t4 = t1 * 2 # returns (1, 2, 3, 1, 2, 3)

# Converting a tuple to a list or a set
l = list(t) # returns [1, 2, 3, 4, 5]
s = set(t) # returns {1, 2, 3, 4, 5}
```

#### Unpacking Sequences
- Unpacking sequences is a way of assigning multiple values from a sequence, such as a tuple or a list, to multiple variables in one line of code.
- The number of variables must match the number of elements in the sequence, otherwise a ValueError will be raised.
- The variables can be enclosed in parentheses or not, depending on the style preference.
- The unpacking can also be done with nested sequences, such as tuples of tuples or lists of lists.
- Example:

```python
# Unpacking a tuple
t = (1, 2, 3)
a, b, c = t # a = 1, b = 2, c = 3
(a, b, c) = t # same as above

# Unpacking a list
l = [4, 5, 6]
x, y, z = l # x = 4, y = 5, z = 6
[x, y, z] = l # same as above

# Unpacking a nested sequence
t = ((1, 2), (3, 4))
(a, b), (c, d) = t # a = 1, b = 2, c = 3, d = 4
```

#### Lists
- A list is an ordered and mutable sequence of values, separated by commas and enclosed in square brackets.
- A list can store any type of data, such as numbers, strings, booleans, or other lists.
- A list can be indexed and sliced using square brackets, similar to strings and tuples.
- A list can be iterated over using a for loop or a while loop.
- A list can be compared, concatenated, and repeated using operators, such as ==, +, and *.
- A list can be converted to a tuple using the tuple() function, or to a set using the set() function.
- A list can be modified using methods, such as append(), insert(), remove(), pop(), sort(), reverse(), and clear().
- A list can be created with or without square brackets, or with a single element and a trailing



### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- Higher order functions (HOFs) are functions that can take other functions as arguments or return functions as results.
- In Python, functions are first class objects, which means they can be assigned to variables, passed as parameters, returned from other functions, and stored in data structures.
- Some examples of built-in higher order functions in Python are `map`, `filter`, `sorted`, and `reduce`.
- `map` applies a function to each element of an iterable and returns a new iterable with the results.
- `filter` returns a new iterable with only the elements that satisfy a predicate function.
- `sorted` returns a new sorted list from an iterable, optionally using a key function or a reverse flag.
- `reduce` applies a binary function to the elements of an iterable, from left to right, and returns a single value.
- Lambda expressions are anonymous functions that can be created using the `lambda` keyword. They can be used as arguments to higher order functions or assigned to variables.
- Lambda expressions have the syntax `lambda parameters: expression`, where parameters are optional and expression is a single statement that returns a value.
- Lambda expressions can access variables from the enclosing scope, but they cannot modify them.
- Lambda expressions are useful for creating simple functions that are only used once or for a short time.

Here is an example of using higher order functions and lambda expressions in Python:

```python
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to square each number and print the result
squared = map(lambda x: x**2, numbers)
print(list(squared)) # [1, 4, 9, 16, 25]

# Use filter to keep only the even numbers and print the result
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even)) # [2, 4]

# Use sorted to sort the numbers in descending order and print the result
descending = sorted(numbers, reverse=True)
print(descending) # [5, 4, 3, 2, 1]

# Use reduce to sum up the numbers and print the result
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total) # 15
```



## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 are prime numbers.
- A composite number is a natural number that has more than two positive divisors. For example, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18 are composite numbers.
- The Sieve of Eratosthenes is an algorithm that can be used to generate all the prime numbers up to a given limit. It was invented by Eratosthenes, a Greek mathematician and astronomer, who lived in the 3rd century BC.
- The algorithm works as follows:
  - Start with a list of all the natural numbers from 2 to the limit. For example, if the limit is 20, the list is [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
  - Mark the first number in the list as prime, and cross out all its multiples in the list. For example, the first number is 2, so mark it as prime, and cross out 4, 6, 8, 10, 12, 14, 16, 18, 20. The list becomes [2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, 9, ~~10~~, 11, ~~12~~, 13, ~~14~~, 15, ~~16~~, 17, ~~18~~, 19, ~~20~~].
  - Move to the next number in the list that is not crossed out, and repeat the previous step. For example, the next number is 3, so mark it as prime, and cross out 9 and 15. The list becomes [2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~].
  - Continue this process until you reach the end of the list or the square root of the limit, whichever is smaller. For example, the square root of 20 is about 4.47, so we stop after checking 3. The list becomes [2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~].
  - The numbers that are not crossed out in the list are the prime numbers up to the limit. For example, the prime numbers up to 20 are [2, 3, 5, 7, 11, 13, 17, 19].
- The Sieve of Eratosthenes is an efficient and simple way to generate prime numbers, as it only requires basic arithmetic operations and a list of natural numbers. It can be implemented using various programming languages, such as Python, Java, C++, etc.



### File I/O : File input and output operations in Python Programming

- File I/O is the process of reading data from or writing data to a file using a programming language such as Python.
- Python provides built-in functions and modules to handle various types of files, such as text files, binary files, CSV files, JSON files, etc.
- To perform file I/O operations in Python, we need to follow these steps:
  - Open the file using the `open()` function, which returns a file object.
  - Perform the desired read or write operations on the file object using methods such as `read()`, `write()`, `readline()`, `writelines()`, etc.
  - Close the file using the `close()` method of the file object, or use the `with` statement to automatically close the file when the block ends.
- The `open()` function takes two parameters: the file name and the mode. The mode specifies how the file is opened, such as `'r'` for reading, `'w'` for writing, `'a'` for appending, `'b'` for binary mode, etc.
- The file object has various attributes and methods to access and manipulate the file data, such as `name`, `mode`, `closed`, `seek()`, `tell()`, `flush()`, etc.

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- The Sieve of Eratosthenes is a simple and efficient algorithm to find all the prime numbers up to a given limit n.
- The algorithm works by creating a list of numbers from 2 to n, and marking the multiples of each prime number as composite, starting from 2. The remaining unmarked numbers are prime.
- The steps of the algorithm are as follows:
  - Create a boolean array of size n+1, and initialize all the elements to True, except for 0 and 1, which are False.
  - Loop from 2 to the square root of n, and for each number i, check if it is True in the array.
  - If i is True, it means it is a prime number, so loop from i*i to n, and mark every multiple of i as False in the array, using a step size of i.
  - After the loop ends, the array will contain True for the prime numbers and False for the composite numbers.
  - Return the list of indices of the array that are True, which are the prime numbers up to n.
- The following is a Python implementation of the Sieve of Eratosthenes algorithm:

```python
def sieve_of_eratosthenes(n):
  # create a boolean array of size n+1
  is_prime = [True] * (n+1)
  # mark 0 and 1 as False
  is_prime[0] = is_prime[1] = False
  # loop from 2 to the square root of n
  for i in range(2, int(n**0.5) + 1):
    # check if i is True in the array
    if is_prime[i]:
      # mark every multiple of i as False in the array
      for j in range(i*i, n+1, i):
        is_prime[j] = False
  # return the list of indices that are True, which are the prime numbers
  return [i for i in range(n+1) if is_prime[i]]
```



### Exceptions and Assertions

- Exceptions are events that occur during the execution of a program that disrupt the normal flow of control. They are usually caused by errors or unexpected situations that the program cannot handle by itself.
- Assertions are statements that check if a certain condition is true or false. They are used as debugging tools to verify the correctness of the program logic and to detect potential bugs or errors.
- The difference between exceptions and assertions is that exceptions address the robustness of the application, while assertions address the correctness. Exceptions are meant to be handled by the program or the user, while assertions are meant to halt the program at the point where an error occurs.
- In Python, exceptions are represented by classes that derive from the BaseException class. There are many built-in exceptions that cover different types of errors, such as ValueError, IndexError, ZeroDivisionError, etc. Custom exceptions can also be defined by creating subclasses of Exception.
- Exceptions can be raised by using the raise statement, which takes an exception object as an argument. For example, raise ValueError("Invalid input") will raise a ValueError exception with the message "Invalid input".
- Exceptions can be caught and handled by using the try and except statements, which create a block of code that is executed normally until an exception occurs. The except clause specifies which exceptions to catch and what to do with them. For example, try: x = int(input("Enter a number: ")) except ValueError: print("That was not a valid number") will prompt the user to enter a number and print an error message if the input is not a valid integer .
- Assertions can be made by using the assert statement, which takes an expression and an optional message as arguments. The assert statement evaluates the expression and if it is false, it raises an AssertionError exception with the message. For example, assert x > 0, "x must be positive" will raise an AssertionError exception with the message "x must be positive" if x is not greater than zero.
- Assertions can be caught and handled like any other exception using the try and except statements, but if not handled, they will terminate the program and produce a traceback. Assertions are usually disabled when the program is run in optimized mode, so they should not be used for error handling or input validation.



### Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, and variables.
- Modules can be used to organize and reuse code, as well as to avoid name conflicts between different parts of a program.
- To use a module in another Python file, we need to import it using the `import` statement.
- The `import` statement can take different forms, such as:

  - `import module_name`: This imports the entire module and makes its contents available under the module name. For example, `import math` allows us to access the `math` module and use its functions like `math.sqrt()`.
  - `from module_name import name1, name2, ...`: This imports specific names from a module and makes them available without the module name prefix. For example, `from math import pi, sin` allows us to use `pi` and `sin` directly, without writing `math.pi` or `math.sin`.
  - `from module_name import *`: This imports all names from a module and makes them available without the module name prefix. This is not recommended, as it can cause name conflicts and make the code less readable.
  - `import module_name as alias`: This imports a module and gives it an alias, which can be used instead of the module name. For example, `import numpy as np` allows us to use `np` instead of `numpy` to access the `numpy` module.

- Modules can also be nested, meaning that a module can contain other modules. To access a nested module, we need to use the dot notation, such as `module1.module2.name`.

### Sieve of Eratosthenes: Generate Prime Numbers with the Help of an Algorithm Given by the Greek Mathematician Named Eratosthenes, Whose Algorithm is Known as Sieve of Eratosthenes

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, etc. are prime numbers.
- The sieve of Eratosthenes is a method for finding all prime numbers up to a given limit. It works by creating a list of all natural numbers from 2 to the limit, and then marking the multiples of each prime number as composite (not prime), starting from the first prime number, 2.
- The algorithm can be implemented in Python as follows:

  - Create a list of boolean values, where the index represents the number and the value represents whether it is prime or not. Initially, all values are set to True, except for 0 and 1, which are set to False.
  - Loop over the list from 2 to the square root of the limit, and check if the current number is prime (i.e., its value is True). If it is, then mark all its multiples (starting from its square) as False, as they are composite.
  - Return the list of prime numbers, which are the indices of the True values in the list.

- Here is an example of the code in Python:

```python
def sieve_of_eratosthenes(limit):
  # Create a list of boolean values, where the index represents the number and the value represents whether it is prime or not
  is_prime = [False, False] + [True] * (limit - 1)

  # Loop over the list from 2 to the square root of the limit
  for i in range(2, int(limit**0.5) + 1):
    # Check if the current number is prime
    if is_prime[i]:
      # Mark all its multiples (starting from its square) as False
      for j in range(i * i, limit + 1, i):
        is_prime[j] = False

  # Return the list of prime numbers, which are the indices of the True values in the list
  return [i for i, prime in enumerate(is_prime) if prime]
```



### Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, but only the interface or behavior of the data type .
- An ADT can be implemented using different concrete data types (CDTs), such as arrays, lists, maps, queues, sets, stacks, tables, trees, vectors, etc .
- An ADT can be viewed as a concept or a specification, rather than a data type .
- In Python, an ADT can be defined using abstract base classes (ABCs), which are classes that cannot be instantiated, but can be subclassed by concrete classes that provide implementations for the abstract methods and properties.
- Some examples of ADTs in Python are collections.abc.Sequence, collections.abc.Mapping, collections.abc.Set, etc.

### ADT Interface in Python

- An ADT interface in Python is a set of abstract methods and properties that define the behavior of the ADT.
- An ADT interface can be created using the abc module, which provides the infrastructure for defining ABCs in Python.
- An ADT interface can be declared using the @abc.abstractmethod and @abc.abstractproperty decorators, which indicate that the method or property must be overridden by a concrete subclass.
- An ADT interface can also specify some concrete methods and properties that provide default or common functionality for the ADT, but can be overridden by a concrete subclass if needed.
- An ADT interface can be inherited by multiple concrete classes that provide different implementations for the ADT.
- An example of an ADT interface in Python is collections.abc.Container, which defines the abstract method __contains__ and the concrete method __iter__ for checking membership and iterating over the elements of a container.

### Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit.
- The algorithm was devised by the Greek mathematician Eratosthenes in the 3rd century BC.
- The algorithm works by creating a list of consecutive integers from 2 to the limit, and marking off multiples of each prime, starting from 2.
- The numbers that are not marked off are the prime numbers.
- The algorithm can be implemented in Python using the following steps:

  - Create a list of booleans of length limit + 1, initialized to True, except for the first two elements, which are False.
  - Loop over the list from 2 to the square root of the limit, and for each element that is True, mark off its multiples as False, starting from its square.
  - Loop over the list again and collect the indices that are True into a new list, which are the prime numbers.

- An example of the sieve of Eratosthenes in Python is:

```python
def sieve_of_eratosthenes(limit):
  # Create a list of booleans of length limit + 1
  is_prime = [False, False] + [True] * (limit - 1)

  # Loop over the list from 2 to the square root of the limit
  for i in range(2, int(limit**0.5) + 1):
    # If the element is True, mark off its multiples as False
    if is_prime[i]:
      for j in range(i*i, limit + 1, i):
        is_prime[j] = False

  # Loop over the list again and collect the indices that are True
  primes = []
  for i in range(2, limit + 1):
    if is_prime[i]:
      primes.append(i)

  # Return the list of prime numbers
  return primes
```



Hello, I am Sydney, your AI assistant. I can help you with your study material for Python programming. Here are some notes on the topic of classes and inheritance.

### Classes
- A class is a blueprint or template for creating objects in Python. An object is an instance of a class that has attributes (data) and methods (functions) associated with it.
- A class definition starts with the keyword `class` followed by the name of the class and a colon. The class name should follow the naming convention of capitalizing the first letter of each word.
- The class body contains the attributes and methods of the class, indented under the class header. The first argument of every method is `self`, which refers to the current object.
- To create an object of a class, we use the class name followed by parentheses. We can assign the object to a variable and access its attributes and methods using the dot operator.
- For example, here is a class definition for a `Point` class that represents a point in a two-dimensional plane:

```python
class Point:
    # A class attribute that is shared by all instances of the class
    dimension = 2

    # A special method that is called when an object is created
    def __init__(self, x, y):
        # Assign the parameters to instance attributes
        self.x = x
        self.y = y

    # A method that returns the distance of the point from the origin
    def distance(self):
        # Use the built-in function sqrt to calculate the square root
        return sqrt(self.x**2 + self.y**2)

    # A special method that returns a string representation of the object
    def __str__(self):
        # Use the format method to create a formatted string
        return "Point({}, {})".format(self.x, self.y)
```

- To create a `Point` object and use its methods, we can do the following:

```python
# Create a Point object with x = 3 and y = 4
p = Point(3, 4)

# Print the dimension of the point
print(p.dimension) # 2

# Print the distance of the point from the origin
print(p.distance()) # 5.0

# Print the string representation of the point
print(p) # Point(3, 4)
```

### Special Methods
- Special methods are methods that have a special meaning in Python. They are also called magic methods or dunder methods because they start and end with double underscores, such as `__init__` or `__str__`.
- Some of the common special methods are:

  - `__init__(self, ...)` : This method is called when an object is created. It is used to initialize the instance attributes of the object. It can take any number of parameters, but the first one must be `self`.
  - `__str__(self)` : This method is called when the `str` function is applied to an object. It should return a string representation of the object. It is also used when the `print` function is called on the object.
  - `__repr__(self)` : This method is called when the `repr` function is applied to an object. It should return a string that can be used to recreate the object. It is also used when the object is displayed in an interactive shell or a debugger.
  - `__eq__(self, other)` : This method is called when the `==` operator is used to compare two objects. It should return `True` if the objects are equal, and `False` otherwise. It can also be used to implement other comparison methods, such as `__ne__` (not equal), `__lt__` (less than), `__gt__` (greater than), `__le__` (less than or equal), and `__ge__` (greater than or equal).
  - `__add__(self, other)` : This method is called when the `+` operator is used to add two objects. It should return a new object that is the result of the addition. It can also be used to implement other arithmetic methods, such as `__sub__` (subtraction), `__mul__` (multiplication), `__truediv__` (true division), `__floordiv__` (floor division), `__mod__` (modulo), `__pow__` (power), and `__neg__` (negation).

- For example, here is a class definition for a `Fraction` class that represents a fraction with a numerator and a denominator. It implements some of the special methods to allow arithmetic and comparison operations on fractions:

```python

```




## Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

- In this unit, we will learn about two important concepts in computer science: iterators and recursion.
- Iterators are objects that allow us to traverse through a collection of elements, such as a list, a string, or a file, in a sequential and uniform way.
- Recursion is a technique of defining a problem in terms of smaller instances of the same problem, and solving it by using a base case and a recursive step.
- We will see how these concepts can be applied to solve some classic problems, such as the Fibonacci sequence and the Tower of Hanoi puzzle.

### Recursive Fibonacci

- The Fibonacci sequence is a series of numbers that starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. For example, the first 10 numbers of the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
- We can define the Fibonacci sequence recursively as follows:

  - Base case: F(0) = 0, F(1) = 1
  - Recursive step: F(n) = F(n-1) + F(n-2) for n > 1

- This means that to find the nth Fibonacci number, we need to find the (n-1)th and the (n-2)th Fibonacci numbers, and add them together. We can implement this definition in Python using a recursive function:

```python
def fibonacci(n):
  # base case
  if n == 0:
    return 0
  elif n == 1:
    return 1
  # recursive step
  else:
    return fibonacci(n-1) + fibonacci(n-2)
```

- This function will return the nth Fibonacci number for any non-negative integer n. For example, fibonacci(5) will return 5, and fibonacci(10) will return 34.
- However, this function is not very efficient, because it repeats a lot of calculations. For example, to find fibonacci(5), we need to find fibonacci(4) and fibonacci(3), but to find fibonacci(4), we also need to find fibonacci(3) and fibonacci(2), and so on. This leads to an exponential growth in the number of function calls, which can slow down the program significantly.
- A better way to implement the Fibonacci sequence is to use an iterative approach, where we use a loop to keep track of the previous two Fibonacci numbers, and update them as we go along. For example, we can use a while loop to implement the Fibonacci sequence in Python:

```python
def fibonacci(n):
  # initialize the first two Fibonacci numbers
  a = 0
  b = 1
  # loop until we reach the nth Fibonacci number
  while n > 0:
    # update the next Fibonacci number as the sum of the previous two
    c = a + b
    # update the previous two Fibonacci numbers
    a = b
    b = c
    # decrement n by 1
    n -= 1
  # return the last Fibonacci number
  return a
```

- This function will also return the nth Fibonacci number for any non-negative integer n, but it will do so much faster, because it does not repeat any calculations. For example, fibonacci(5) will return 5, and fibonacci(10) will return 34, but it will only use one loop iteration for each n, instead of many recursive calls.

### Tower of Hanoi

- The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks stacked on one rod in order of decreasing size, such that the smallest disk is on top and the largest disk is on the bottom. The objective of the puzzle is to move the entire stack of disks from the first rod to the last rod, following these rules:

  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the rods and sliding it onto another rod, on top of the other disks that may already be present on that rod.
  - No disk may be placed on top of a smaller disk.

- For example, if we have three disks, labeled A, B, and C, from smallest to largest, and three rods, labeled 1, 2, and 3, from left to right, the puzzle starts with the disks stacked on rod 1 as follows:

```
  A
  B
  C

```




### Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search Time

- Searching algorithms are implemented to search for elements and retrieve their values from any data structure.
- Based on the search operation, searching algorithms can be classified into two categories:
  - Sequential Search: In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.
  - Interval Search: These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. For Example: Binary Search, Jump Search, Interpolation Search.
- Simple Search or Linear Search is a method for finding an element within a list or array. It sequentially checks each element of the list until a match is found or the whole list has been searched.
- The time complexity of Linear Search is O(n), where n is the number of elements in the list. This means that the worst case scenario is that the algorithm has to check every element in the list to find the target or conclude that it is not present.
- Binary Search is a searching algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful or the remaining half is empty.
- The time complexity of Binary Search is O(log n), where n is the number of elements in the array. This means that the algorithm divides the search space in half at each step, reducing the number of comparisons needed to find the target or conclude that it is not present.
- To implement Binary Search in Python, we need to use a recursive function that takes the sorted array, the target value, and the left and right indices as parameters. The base case is when the left index is greater than the right index, which means the target is not in the array. The recursive case is when the left index is less than or equal to the right index, which means the target may be in the array. In this case, we calculate the middle index and compare the value at that index with the target. If they are equal, we return the middle index. If the target is smaller than the value at the middle index, we call the function again with the right index as the middle index minus one. If the target is larger than the value at the middle index, we call the function again with the left index as the middle index plus one.
- Here is an example of Binary Search in Python:

```python
# Define a recursive function for binary search
def binary_search(array, target, left, right):
  # Base case: left index is greater than right index
  if left > right:
    return -1 # Target not found
  # Recursive case: left index is less than or equal to right index
  else:
    # Calculate the middle index
    middle = (left + right) // 2
    # Compare the value at the middle index with the target
    if array[middle] == target:
      return middle # Target found
    elif target < array[middle]:
      # Call the function again with the right index as the middle index minus one
      return binary_search(array, target, left, middle - 1)
    else:
      # Call the function again with the left index as the middle index plus one
      return binary_search(array, target, middle + 1, right)

# Test the function on a sorted array
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = binary_search(array, target, 0, len(array) - 1)
print(result) # Output: 6
```



### Sorting and Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

- Sorting is the process of arranging data in a specific order, such as ascending or descending, based on some criteria.
- Merging is the process of combining two or more sorted lists into one sorted list.
- There are different algorithms for sorting and merging data, each with different advantages and disadvantages.

#### Selection Sort

- Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum or maximum element in the unsorted part of the list and moving it to the sorted part.
- The algorithm maintains two sublists: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted sublist, finds the smallest or largest element, and swaps it with the first element of the unsorted sublist.
- The algorithm repeats this process until the unsorted sublist is empty and the sorted sublist contains all the elements.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the list, because it requires n iterations to sort the list and each iteration requires n comparisons to find the minimum or maximum element.
- The space complexity of selection sort is O(1), because it only requires a constant amount of extra space to store the index of the minimum or maximum element.
- Selection sort is not a stable sorting algorithm, meaning that it does not preserve the relative order of equal elements in the list.
- Selection sort is not an adaptive sorting algorithm, meaning that it does not take advantage of the existing order in the list and performs the same number of operations regardless of the initial order of the elements.
- Selection sort is suitable for small lists or lists that are already nearly sorted, because it has a low overhead and performs fewer swaps than other algorithms.

#### Merge List

- Merge list is a simple merging algorithm that works by comparing the first elements of two sorted lists and appending the smaller or larger one to the output list, until one of the lists is exhausted.
- The algorithm then appends the remaining elements of the non-empty list to the output list.
- The time complexity of merge list is O(m + n), where m and n are the number of elements in the two lists, because it requires at most m + n comparisons to merge the lists.
- The space complexity of merge list is O(m + n), because it requires a new list of size m + n to store the output.
- Merge list is a stable merging algorithm, meaning that it preserves the relative order of equal elements in the lists.
- Merge list is not an adaptive merging algorithm, meaning that it does not take advantage of the existing order in the lists and performs the same number of operations regardless of the initial order of the elements.
- Merge list is suitable for merging two sorted lists of any size, because it has a linear time complexity and a simple implementation.

#### Merge Sort

- Merge sort is a recursive sorting algorithm that works by dividing the list into two halves, sorting each half recursively, and then merging the two sorted halves using the merge list algorithm.
- The algorithm follows the divide and conquer paradigm, where a complex problem is broken down into smaller and simpler subproblems, which are then solved and combined to obtain the final solution.
- The algorithm uses a recursive function that takes the list and two indices, start and end, as parameters.
- The base case of the recursion is when the list has one or zero elements, in which case the list is already sorted and returned as it is.
- The recursive case of the recursion is when the list has more than one element, in which case the list is split into two halves by finding the middle index, mid, as the average of start and end.
- The algorithm then calls itself recursively on the left half, from start to mid, and on the right half, from mid + 1 to end, and obtains the sorted halves as the return values.
- The algorithm then merges the two sorted halves using the merge list algorithm and returns the merged list as the final output.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the list, because it requires log n levels of recursion to divide the list into sublists of size one, and each level requires n comparisons to merge the sublists.
- The space complexity of merge sort is O(n), because it requires a new list of size n to store the output at each level of recursion.
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the list.
- Merge sort is not an adaptive sorting algorithm, meaning that it does not

