## Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

- A function is a block of code that performs a specific task and can be reused in a program.
- A function has four main parts: name, parameters, body, and return value.
- The name of a function is a unique identifier that is used to call the function.
- The parameters of a function are the variables that are passed to the function when it is called. They are also called arguments.
- The body of a function is the set of statements that define what the function does.
- The return value of a function is the result that the function produces and sends back to the caller.
- To execute a function, we need to call it by using its name and providing the required arguments.
- For example, the following function takes two numbers as parameters and returns their sum:

```python
def add(a, b):
  # This is the body of the function
  c = a + b
  # This is the return value of the function
  return c
```

- To call this function, we can write:

```python
x = 10
y = 20
z = add(x, y) # This is a function call
print(z) # This will print 30
```

- Keyword arguments are arguments that are specified by using the parameter name and an equal sign, such as `add(a=10, b=20)`.
- Keyword arguments can be used to provide the arguments in any order, as long as the parameter names match.
- Keyword arguments can also be used to provide default values for some parameters, in case the caller does not provide them.
- For example, the following function takes two numbers as parameters and returns their product, but has a default value of 1 for the second parameter:

```python
def multiply(a, b=1):
  # This is the body of the function
  c = a * b
  # This is the return value of the function
  return c
```

- To call this function, we can write:

```python
x = 10
y = 2
z = multiply(x, y) # This is a function call with two arguments
print(z) # This will print 20
w = multiply(x) # This is a function call with one argument
print(w) # This will print 10, because the default value of b is 1
```

- Scope rules are the rules that determine where a variable can be accessed and modified in a program.
- A variable has either a global scope or a local scope, depending on where it is defined.
- A global variable is a variable that is defined outside any function and can be accessed and modified by any function in the program.
- A local variable is a variable that is defined inside a function and can only be accessed and modified by that function.
- For example, the following program has two global variables and two local variables:

```python
# These are global variables
x = 10
y = 20

def add():
  # These are local variables
  a = 5
  b = 10
  c = a + b
  return c

def subtract():
  # These are local variables
  a = 15
  b = 5
  c = a - b
  return c

z = add() # This is a function call
w = subtract() # This is another function call
print(x, y, z, w) # This will print 10, 20, 15, 10
```

- In this program, the variables `x` and `y` are global and can be accessed by both `add` and `subtract` functions, but the variables `a`, `b`, and `c` are local and can only be accessed by the function where they are defined.