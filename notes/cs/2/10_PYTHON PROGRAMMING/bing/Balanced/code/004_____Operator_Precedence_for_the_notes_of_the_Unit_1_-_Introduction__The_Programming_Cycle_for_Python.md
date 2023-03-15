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
y = 5
print(x > y and x < 20) # prints True
print(x > y and x < 20 or x > 15) # prints True
print(x > y and (x < 20 or x > 15)) # prints True
print((x > y and x < 20) or x > 15) # prints True
```

- Type conversion in Python means changing the data type of a value or variable.
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
print(type(z)) # prints <class 'float'>

# Example 2: Explicit type conversion
a = "100" # a is a string
b = int(a) # b is an integer, because a is converted to an integer
print(b) # prints 100
print(type(b)) # prints <class 'int'>
```
