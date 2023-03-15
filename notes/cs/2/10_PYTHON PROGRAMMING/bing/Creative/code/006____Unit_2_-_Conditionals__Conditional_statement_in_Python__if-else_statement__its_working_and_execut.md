Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content in markdown format:

```markdown
## Unit 2 - Conditionals

### Conditional statement in Python (if-else statement, its working and execution)

- A conditional statement is a statement that executes a block of code based on a condition.
- In Python, the syntax of a conditional statement is:

```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False
```

- The condition is an expression that evaluates to a boolean value (True or False).
- The block of code under the if clause is indented by four spaces or a tab.
- The else clause is optional and executes only if the condition is False.
- The if-else statement is executed from top to bottom. If the condition is True, the if block is executed and the else block is skipped. If the condition is False, the if block is skipped and the else block is executed.

### Nested-if statement and Elif statement in Python

- A nested-if statement is a conditional statement that contains another conditional statement inside it.
- The syntax of a nested-if statement is:

```python
if condition1:
    # block of code to execute if condition1 is True
    if condition2:
        # block of code to execute if condition2 is True
    else:
        # block of code to execute if condition2 is False
else:
    # block of code to execute if condition1 is False
```

- The nested-if statement is executed from top to bottom. If condition1 is True, the inner if-else statement is evaluated based on condition2. If condition1 is False, the outer else block is executed.
- An elif statement is a shorthand for else if. It allows us to check multiple conditions in a sequential manner.
- The syntax of an elif statement is:

```python
if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition2 is True
elif condition3:
    # block of code to execute if condition3 is True
...
else:
    # block of code to execute if none of the conditions are True
```

- The elif statement is executed from top to bottom. If condition1 is True, the first block is executed and the rest of the statement is skipped. If condition1 is False, condition2 is checked and so on. If none of the conditions are True, the else block is executed.

### Expression Evaluation & Float Representation

- An expression is a combination of values, variables, operators, and functions that produces a result when evaluated.
- In Python, expressions are evaluated according to the rules of operator precedence and associativity.
- Operator precedence determines the order in which operators are applied in an expression. Operators with higher precedence are applied before operators with lower precedence.
- Associativity determines the order in which operators with the same precedence are applied in an expression. Operators can be either left-associative or right-associative.
- The table below shows the operator precedence and associativity in Python, from highest to lowest:

| Operator | Description | Associativity |
|----------|-------------|---------------|
| ** | Exponentiation | Right |
| +x, -x | Unary plus, unary minus | Right |
| *, /, //, % | Multiplication, division, floor division, modulo | Left |
| +, - | Addition, subtraction | Left |
| <, <=, >, >= | Comparison operators | Left |
| ==, != | Equality operators | Left |
| and | Logical AND | Left |
| or | Logical OR | Left |
| = | Assignment | Right |

- A float is a data type that represents a decimal number with a fractional part.
- In Python, floats are represented using the IEEE 754 standard, which uses 64 bits to store a float value.
- The 64 bits are divided into three parts: sign, exponent, and mantissa.
- The sign bit indicates whether the float is positive or negative. It is 0 for positive and 1 for negative.
- The exponent bits indicate the power of 2 that the mantissa is multiplied by. It is an 11-bit unsigned integer with a bias of 1023. The exponent value is calculated by subtracting the bias from the exponent bits.
- The mantissa bits indicate the fractional part of the float. It is a 52-bit unsigned integer with an implicit leading 1. The mantissa value is calculated by adding the leading 1 and dividing by 2^52.
- The float value is calculated by applying the formula:

```math
float value