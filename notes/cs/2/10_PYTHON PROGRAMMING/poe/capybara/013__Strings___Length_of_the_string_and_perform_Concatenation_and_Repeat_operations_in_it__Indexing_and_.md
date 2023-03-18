### Strings

A string is a sequence of characters in Python. Strings are immutable, which means that once they are created, they cannot be modified. In this section, we will cover the following topics related to strings in Python:

#### Length of a String

The `len()` function is used to find the length of a string. It returns the number of characters in the string.

```python
string = "Hello, World!"
print(len(string))  # Output: 13
```

#### Concatenation and Repeat Operations on Strings

Strings can be concatenated (joined together) using the `+` operator. Strings can also be repeated using the `*` operator.

```python
string1 = "Hello"
string2 = "World"
string3 = string1 + " " + string2  # Concatenation
print(string3)  # Output: Hello World

string4 = string1 * 3  # Repeat operation
print(string4)  # Output: HelloHelloHello
```

#### Indexing and Slicing of Strings

Strings can be indexed and sliced to access specific characters or substrings within the string. Indexing starts at 0 for the first character and goes up to `len(string)-1` for the last character.

```python
string = "Hello, World!"
print(string[0])  # Output: H
print(string[7])  # Output: W

substring1 = string[0:5]  # Slicing
print(substring1)  # Output: Hello

substring2 = string[7:]  # Slicing
print(substring2)  # Output: World!
```

#### Parts of a Function

A function is a block of code that performs a specific task. Functions help in making the code modular and reusable. The following are the parts of a function:

- Function definition: This is where the function is defined using the `def` keyword.
- Function name: This is the name of the function.
- Parameters: These are the input variables that the function takes.
- Function body: This is where the code inside the function is written.
- Return statement: This is used to return a value from the function.

```python
def add_numbers(num1, num2):
    return num1 + num2
```

#### Execution of a Function

A function is executed by calling its name and passing the required arguments.

```python
result = add_numbers(2, 3)
print(result)  # Output: 5
```

#### Keyword and Default Arguments

Keyword arguments are passed to the function using the parameter name. Default arguments are used when a value is not passed to the function for a specific parameter.

```python
def greet(name, message="Hello"):
    print(message, name)

greet("John")  # Output: Hello John
greet("Mary", message="Hi")  # Output: Hi Mary
```

#### Scope Rules

The scope of a variable is the region of the program where it is defined. Python has two types of scope, global and local. A variable defined outside a function has a global scope, while a variable defined inside a function has a local scope.

```python
global_var = "global"

def print_var():
    local_var = "local"
    print(global_var)
    print(local_var)

print_var()  # Output: global local
```