# Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

A function is a block of code that performs a specific task and can be reused in a program. Functions can make the code more modular, readable, and maintainable.

## Parts of a Function

A function has four main parts:

- The function name, which identifies the function and can be used to call it.
- The parameter list, which specifies the names and types of the arguments that the function can accept. Parameters are optional and can be omitted if the function does not need any input.
- The function body, which contains the statements that define the logic and behavior of the function. The function body is indented under the function header.
- The return statement, which specifies the value or expression that the function returns to the caller. The return statement is optional and can be omitted if the function does not need to return anything.

The general syntax of a function definition in Python is:

```python
def function_name(parameter_list):
    function_body
    return value_or_expression
```

For example, the following function takes two numbers as parameters and returns their sum:

```python
def add(x, y):
    result = x + y
    return result
```

## Execution of a Function

A function can be executed or called by using its name followed by parentheses. If the function has parameters, the arguments that match the parameters must be passed inside the parentheses. The arguments can be literals, variables, expressions, or other functions.

The general syntax of a function call in Python is:

```python
function_name(argument_list)
```

For example, the following statement calls the add function defined above and prints the returned value:

```python
print(add(3, 5)) # prints 8
```

## Keyword and Default Arguments

When calling a function, the arguments can be passed by position or by keyword. Positional arguments are matched with the parameters in the order they appear in the function definition. Keyword arguments are matched with the parameters by name, regardless of the order. Keyword arguments are specified by using the parameter name followed by an equal sign and the argument value.

The general syntax of a function call with keyword arguments in Python is:

```python
function_name(parameter1=value1, parameter2=value2, ...)
```

For example, the following statement calls the add function with keyword arguments:

```python
print(add(y=5, x=3)) # prints 8
```

When defining a function, the parameters can have default values that are used if the caller does not provide an argument for them. Default arguments are specified by using the parameter name followed by an equal sign and the default value in the function definition.

The general syntax of a function definition with default arguments in Python is:

```python
def function_name(parameter1=default1, parameter2=default2, ...):
    function_body
    return value_or_expression
```

For example, the following function takes two numbers as parameters and returns their product, but has a default value of 1 for the second parameter:

```python
def multiply(x, y=1):
    result = x * y
    return result
```

The following statement calls the multiply function with only one argument, which is matched with the first parameter, and the second parameter uses the default value of 1:

```python
print(multiply(4)) # prints 4
```

## Scope Rules

The scope of a variable is the region of the code where the variable can be accessed and modified. In Python, there are two types of scopes: global and local.

- A global scope is the outermost scope of a program, where variables that are not defined inside any function or class are located. Global variables can be accessed and modified from any part of the program, unless they are shadowed by a local variable with the same name.
- A local scope is the innermost scope of a function or a class, where variables that are defined inside the function or class are located. Local variables can only be accessed and modified within the function or class where they are defined, and they are destroyed when the function or class ends.

The general rule of scope in Python is: a variable can be accessed from the scope where it is defined and from any inner scope, but not from any outer scope.

For example, consider the following code:

```python
x = 10 # global variable

def foo():
    y = 20 # local variable
    print(x) # prints 10, can access global variable
    print(y) # prints 20, can access local variable

def bar():
    z = 30 # local variable
    print(x) # prints 10, can access global variable

```
