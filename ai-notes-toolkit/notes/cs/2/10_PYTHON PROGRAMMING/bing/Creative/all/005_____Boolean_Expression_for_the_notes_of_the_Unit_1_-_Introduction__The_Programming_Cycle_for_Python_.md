# Boolean Expression

A Boolean expression is an expression that evaluates to produce a result which is a Boolean value. A Boolean value is either True or False, and the Python type is bool. For example, the expression 1 <= 2 is True, while the expression 0 == 1 is False.

## Comparison Operators

A Boolean expression often consists of at least two terms separated by a comparison operator, such as:

- `==` equal to
- `!=` not equal to
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to

These operators compare the values on either side of them and return a Boolean value. For example:

- `3 == 4` is False
- `5 != 6` is True
- `7 < 8` is True
- `9 > 10` is False
- `11 <= 11` is True
- `12 >= 13` is False

## Logical Operators

A Boolean expression can also use logical operators to combine multiple comparison expressions. The logical operators are:

- `and` returns True if both expressions are True
- `or` returns True if either expression is True
- `not` returns True if the expression is False

These operators follow the rules of Boolean algebra, which are summarized in the following truth tables:

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

| A | not A |
|---|-------|
| True | False |
| False | True |

For example:

- `(3 < 4) and (5 > 6)` is False
- `(7 != 8) or (9 == 10)` is True
- `not (11 <= 12)` is False

## Precedence Rules

When a Boolean expression contains multiple operators, the order of evaluation depends on the precedence rules. The precedence rules are:

- Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want. 
- Comparison operators have the next highest precedence and are evaluated from left to right.
- Logical operators have the lowest precedence and are evaluated from left to right.

For example:

- `(3 < 4) and (5 > 6) or not (7 == 8)` is equivalent to `((3 < 4) and (5 > 6)) or (not (7 == 8))` and evaluates to True
- `3 < 4 and 5 > 6 or not 7 == 8` is equivalent to `((3 < 4) and (5 > 6)) or (not (7 == 8))` and evaluates to True
- `3 < 4 and (5 > 6 or not 7 == 8)` is equivalent to `(3 < 4) and ((5 > 6) or (not (7 == 8)))` and evaluates to False

## Boolean Expressions in Python Programs

Boolean expressions are often used in Python programs to control the flow of execution. For example, the if statement executes a block of code if a Boolean expression is True, and optionally executes another block of code if the expression is False. The while loop executes a block of code repeatedly as long as a Boolean expression is True. The for loop iterates over a sequence of values and executes a block of code for each value. The in operator can be used to check if a value is in a sequence and returns a Boolean value.

For example:

- `if x > 0: print("x is positive")` prints "x is positive" if x is greater than zero
- `while n > 0: print(n); n = n - 1` prints the numbers from n to 1 in decreasing order
- `for i in range(1, 11): print(i)` prints the numbers from 1 to 10 in increasing order
- `if "a" in "apple": print("a is in apple")` prints "a is in apple"