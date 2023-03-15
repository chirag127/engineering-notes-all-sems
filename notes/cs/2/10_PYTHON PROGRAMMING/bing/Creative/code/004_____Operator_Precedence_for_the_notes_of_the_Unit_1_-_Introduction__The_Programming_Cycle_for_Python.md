# Operator Precedence for the notes of the Unit 1 - Introduction: The Programming Cycle for Python , Python IDE, Interacting with Python Programs , Elements of Python, Type Conversion.

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
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, membership testing, identity testing |
| `not` | Logical NOT |
| `and` | Logical AND |
| `or` | Logical OR |
| `:=` | Assignment expression |

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

# Example 4: Assignment expression has the lowest precedence
x = 5
y = (z := x + 10) # assigns 15 to z and y
print(x, y, z) # prints 5 15 15
```