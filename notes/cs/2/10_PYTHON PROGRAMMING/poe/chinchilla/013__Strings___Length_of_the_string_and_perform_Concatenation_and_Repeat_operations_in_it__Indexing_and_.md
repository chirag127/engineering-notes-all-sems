### Strings: Length, Concatenation, and Repeat Operations

Strings are a sequence of characters enclosed in quotes, single or double. A string can be of any length and can include letters, numbers, and symbols. In Python, strings are immutable, which means that the contents of a string cannot be changed once it is created.

#### Length of a String

The length of a string can be determined using the `len()` function. The `len()` function returns the number of characters in the string, including spaces and punctuation marks.

```python
string = "Hello, World!"
print(len(string)) # Output: 13
```

#### Concatenation and Repeat Operations

Concatenation is the process of combining two or more strings into one. In Python, concatenation can be performed using the `+` operator.

```python
string1 = "Hello"
string2 = "World"
string3 = string1 + " " + string2
print(string3) # Output: Hello World
```

Repeat operation can be performed using the `*` operator.

```python
string4 = "Hello" * 3
print(string4) # Output: HelloHelloHello
```

#### Indexing and Slicing of Strings

Indexing and slicing are two essential operations for working with strings in Python.

Indexing is used to access a specific character in a string. In Python, indexing starts from 0, which means that the first character in a string has an index of 0.

```python
string = "Hello, World!"
print(string[0]) # Output: H
print(string[7]) # Output: W
```

Slicing is used to extract a substring from a string. The syntax for slicing is `string[start:end:step]`, where `start` is the index of the first character to be included, `end` is the index of the last character to be included (not inclusive), and `step` is the number of characters to skip between each character.

```python
string = "Hello, World!"
print(string[0:5]) # Output: Hello
print(string[7:12]) # Output: World
print(string[::2]) # Output: Hlo ol!
```

### Functions: Parts of a Function, Execution of a Function, Keyword and Default Arguments, Scope Rules

Functions are a set of instructions that perform a specific task. Functions in Python are defined using the `def` keyword followed by the function name and parentheses.

#### Parts of a Function

A function in Python consists of four parts:

1. **Function Header:** The function header is the first line of a function that includes the `def` keyword, the function name, and the parameter list enclosed in parentheses.

2. **Function Body:** The function body contains the set of instructions that perform a specific task. The function body is indented and must be aligned with the `def` keyword.

3. **Return Statement:** The return statement is used to return a value from a function. It is optional, and if it is not included, the function will return `None` by default.

4. **Function Call:** The function call is used to execute a function. It includes the function name followed by parentheses enclosing the arguments (if any).

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result) # Output: 8
```

#### Execution of a Function

The execution of a function involves calling the function and passing the required arguments (if any). When a function is called, the interpreter jumps to the function definition, executes the instructions in the function body, and returns the result (if any) to the calling statement.

#### Keyword and Default Arguments

Keyword arguments are used to specify the parameter names when calling a function. It helps to avoid confusion in the order of the arguments.

```python
def greet(name, message):
    print("Hello", name + ",", message)

greet(message="How are you?", name="John") # Output: Hello John, How are you?
```

Default arguments are used to set a default value for a parameter in a function. If the argument is not passed, the default value is used.

```python
def greet(name, message="Welcome"):
    print("Hello", name + ",", message)

greet("John") # Output: Hello John, Welcome
greet("John", "How are you?") # Output: Hello John, How are you?
```

#### Scope Rules

The scope of a variable determines where it can be accessed within a program. In Python, there are two types of scopes: global scope and local scope.

A variable declared outside a function has a global scope and can be accessed from anywhere in the program. A variable declared inside a function has a local scope and can only be accessed within that function.

```python
x = 10 # Global variable

def my_function():
    y = 20 # Local