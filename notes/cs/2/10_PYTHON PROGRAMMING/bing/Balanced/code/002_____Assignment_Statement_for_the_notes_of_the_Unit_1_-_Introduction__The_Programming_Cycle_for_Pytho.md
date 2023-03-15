### Assignment Statement

- An assignment statement is a way of creating, initializing, or updating variables in Python.
- A variable is a name that refers to an object, such as a number, a string, a list, or a function.
- An assignment statement has the form `target = expression`, where `target` is the name of the variable and `expression` is any Python expression that evaluates to an object.
- The assignment statement assigns the object resulting from the expression to the target variable, creating or updating the variable's reference to the object.
- For example, `x = 5` assigns the integer object `5` to the variable `x`, creating or updating `x`'s reference to `5`.
- Python supports multiple assignment, where more than one target variable can be assigned to the same or different objects in a single statement.
- For example, `x, y = 10, 20` assigns the integer object `10` to `x` and the integer object `20` to `y` in one statement.
- Multiple assignment can also use tuples or lists as targets, where each element of the tuple or list is assigned to the corresponding element of the expression.
- For example, `x, y = (1, 2)` assigns the integer object `1` to `x` and the integer object `2` to `y` in one statement, using a tuple as the target.
- Similarly, `x, y = [3, 4]` assigns the integer object `3` to `x` and the integer object `4` to `y` in one statement, using a list as the target.
- Python also supports augmented assignment, where an operator can be combined with the assignment operator to perform an arithmetic or bitwise operation and assign the result to the target variable in one statement.
- For example, `x += 5` is equivalent to `x = x + 5`, which adds `5` to the current value of `x` and assigns the result back to `x`.
- Similarly, `x &= 3` is equivalent to `x = x & 3`, which performs a bitwise and operation between `x` and `3` and assigns the result back to `x`.
- Augmented assignment can be used with any of the following operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
- Assignment statements are fundamental to Python programming, as they allow you to create and manipulate variables throughout your code.