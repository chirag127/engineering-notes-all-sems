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