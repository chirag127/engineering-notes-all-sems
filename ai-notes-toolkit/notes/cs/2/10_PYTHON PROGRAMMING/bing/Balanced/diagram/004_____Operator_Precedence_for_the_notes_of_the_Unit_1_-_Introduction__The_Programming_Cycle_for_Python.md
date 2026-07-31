### Operator Precedence

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
# Parentheses have the highest precedence
print((6 + 3) - (6 + 3)) # prints 0

# Exponentiation has higher precedence than multiplication
print(2 ** 3 * 4) # prints 32, not 64

# Unary operators have higher precedence than binary operators
x = 5
print(-x ** 2) # prints -25, not 25

# Multiplication, division, floor division and modulo have the same precedence and are evaluated from left to right
print(12 / 4 * 3) # prints 9, not 1
print(12 // 4 % 3) # prints 0, not 2

# Addition and subtraction have the same precedence and are evaluated from left to right
print(5 + 3 - 2) # prints 6, not 4
print(5 - 3 + 2) # prints 4, not 0

# Bitwise operators have lower precedence than arithmetic operators
print(5 + 3 & 2) # prints 0, not 7
print(5 - 3 | 2) # prints 3, not 2

# Comparisons have lower precedence than bitwise operators
print(5 & 3 == 1) # prints True, not False
print(5 | 3 > 2) # prints True, not 7

# Logical operators have lower precedence than comparisons
print(not 5 == 3) # prints True, not False
print(5 == 3 or 2) # prints 2, not False

# Conditional expression has lower precedence than logical operators
print(True and False if 5 > 3 else True or False) # prints False, not True
print(True or False if 5 < 3 else True and False) # prints False, not True

# Assignment expression has lower precedence than conditional expression
x = 5
print(x := x + 1 if x > 3 else x - 1) # prints 6, not 4
print(x := x + 1 if x < 3 else x - 1) # prints 5, not 6

# Lambda expression has the lowest precedence
print(lambda x: x + 1 if x > 3 else x - 1) # prints <function <lambda> at 0x000001F9E9E7F1F0>, not a value
```

- To change the order of precedence, parentheses can be used to group the operators and operands as desired.
- For example, if we want to evaluate the addition before the multiplication, we can write:

```python
print((2 + 3) * 4) # prints 20, not 14
```

- This way, we can make the expressions more clear and avoid the confusion caused by the operator precedence.