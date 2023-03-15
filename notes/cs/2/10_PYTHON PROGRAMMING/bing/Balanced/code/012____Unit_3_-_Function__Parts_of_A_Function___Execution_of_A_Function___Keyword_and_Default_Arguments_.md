## Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

- A function is a block of code that performs a specific task, such as printing a message, calculating a value, or sorting a list.
- A function can be defined using the `def` keyword, followed by the function name and a pair of parentheses. Inside the parentheses, we can specify zero or more parameters that the function can accept as input. After the parentheses, we write a colon and then indent the function body.
- For example, the following code defines a function named `greet` that takes one parameter named `name` and prints a greeting message:

```python
def greet(name):
    print("Hello, " + name + "!")
```

- To execute a function, we need to call it by using its name and passing the appropriate arguments inside parentheses. Arguments are the actual values that we pass to the function when we call it. They must match the number and order of the parameters defined in the function header.
- For example, the following code calls the `greet` function with the argument `"Alice"`:

```python
greet("Alice")
```

- The output of this code is:

```
Hello, Alice!
```

- We can also use keyword arguments to pass arguments to a function by specifying the parameter name and the value. Keyword arguments can be used in any order and can improve the readability of the code.
- For example, the following code calls the `greet` function with the keyword argument `name="Bob"`:

```python
greet(name="Bob")
```

- The output of this code is:

```
Hello, Bob!
```

- We can also define default arguments for the parameters of a function. Default arguments are the values that are used if no arguments are passed when the function is called. We can specify default arguments by assigning them to the parameters in the function header using the equal sign.
- For example, the following code defines a function named `add` that takes two parameters named `x` and `y` and returns their sum. The parameter `y` has a default argument of `0`, which means that if no value is passed for `y`, it will be assumed to be `0`.

```python
def add(x, y=0):
    return x + y
```

- The following code calls the `add` function with different arguments:

```python
print(add(3, 4)) # prints 7
print(add(5)) # prints 5, since y is 0 by default
print(add(x=2, y=3)) # prints 5, using keyword arguments
print(add(y=6, x=1)) # prints 7, using keyword arguments in different order
```

- The scope of a variable is the region of the code where the variable can be accessed or modified. Variables defined inside a function have a local scope, which means that they can only be accessed or modified within the function. Variables defined outside any function have a global scope, which means that they can be accessed or modified anywhere in the code.
- For example, the following code defines a global variable named `a` and a local variable named `b` inside a function named `foo`:

```python
a = 10 # global variable

def foo():
    b = 20 # local variable
    print(a) # prints 10, accessing the global variable
    print(b) # prints 20, accessing the local variable
```

- The following code calls the `foo` function and tries to access the variables `a` and `b`:

```python
foo() # prints 10 and 20
print(a) # prints 10, accessing the global variable
print(b) # causes an error, since b is not defined in the global scope
```