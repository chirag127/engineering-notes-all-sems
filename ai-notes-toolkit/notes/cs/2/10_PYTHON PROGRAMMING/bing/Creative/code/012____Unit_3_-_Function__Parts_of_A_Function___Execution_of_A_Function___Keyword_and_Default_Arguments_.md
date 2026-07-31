Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 3 - Function:

## Unit 3 - Function

A function is a block of code that performs a specific task. Functions are useful for organizing and reusing code, as well as making the code more readable and modular.

### Parts of a Function

A function has four main parts:

- The function name: This is the identifier that is used to call the function. It should be descriptive and follow the naming conventions of the programming language.
- The parameters: These are the variables that are passed to the function when it is called. They are also called arguments. Parameters are optional, and a function can have zero or more parameters.
- The body: This is the block of code that contains the statements that define what the function does. The body is indented and enclosed by curly braces or other symbols depending on the programming language.
- The return value: This is the value that the function produces as a result of its execution. The return value is optional, and a function can return zero or one value. The return value is specified by using the return keyword or other syntax depending on the programming language.

### Execution of a Function

A function is executed when it is called by using its name and passing the appropriate arguments. The function call is an expression that evaluates to the return value of the function. The function call can be used as a statement or as part of another expression.

For example, in Python, a function can be defined and called as follows:

```python
# Define a function that takes two parameters and returns their sum
def add(x, y):
  return x + y

# Call the function and print the result
result = add(3, 5)
print(result) # 8

# Call the function and use the result in another expression
print(add(2, 4) * 10) # 60
```

### Keyword and Default Arguments

Some programming languages allow the use of keyword and default arguments in function calls. Keyword arguments are arguments that are specified by using the parameter name and an equal sign, rather than by their position. Default arguments are arguments that have a predefined value that is used if the argument is not provided in the function call.

For example, in Python, a function can be defined and called with keyword and default arguments as follows:

```python
# Define a function that takes three parameters and prints a message
def greet(name, age, message="Hello"):
  print(message, name, "You are", age, "years old.")

# Call the function with positional arguments
greet("Alice", 20) # Hello Alice You are 20 years old.

# Call the function with keyword arguments
greet(message="Hi", age=25, name="Bob") # Hi Bob You are 25 years old.

# Call the function with a mix of positional and keyword arguments
greet("Charlie", message="Hey", age=30) # Hey Charlie You are 30 years old.

# Call the function with some default arguments
greet("David", 35) # Hello David You are 35 years old.
```

### Scope Rules

Scope is the region of code where a variable or a function is defined and can be accessed. Scope rules determine the visibility and lifetime of variables and functions in a program. There are two main types of scope: global and local.

- Global scope: This is the scope that is outside of any function or block. Variables and functions that are defined in the global scope can be accessed from anywhere in the program, unless they are shadowed by a local definition.
- Local scope: This is the scope that is inside a function or a block. Variables and functions that are defined in the local scope can only be accessed from within that function or block, and they are destroyed when the function or block ends.

For example, in Python, the scope rules can be illustrated as follows:

```python
# Define a global variable
x = 10

# Define a global function
def foo():
  # Define a local variable
  y = 20
  # Access the global variable
  print(x) # 10
  # Access the local variable
  print(y) # 20

# Call the global function
foo()

# Access the global variable
print(x) # 10

# Access the local variable
print(y) # NameError: name 'y' is not defined
```