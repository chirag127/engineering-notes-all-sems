### Assignment Statement

- An assignment statement is a way of creating, initializing, or updating variables in Python.
- A variable is a name that refers to an object, such as a number, a string, a list, or a function.
- An assignment statement has the form `target = expression`, where `target` is the name of the variable and `expression` is any Python expression that evaluates to an object.
- The assignment statement assigns the object resulting from the expression to the target variable, creating or updating the variable's reference to the object.
- For example, `x = 10` assigns the integer object `10` to the variable `x`.
- Python supports multiple assignment, where more than one variable can be assigned at the same time, using a comma-separated list of targets and expressions.
- For example, `x, y = 10, 20` assigns the integer object `10` to the variable `x` and the integer object `20` to the variable `y`.
- Multiple assignment can also be used to swap the values of two variables, without using a temporary variable.
- For example, `x, y = y, x` swaps the values of `x` and `y`.
- Python also supports augmented assignment, where an operator can be combined with the assignment operator to perform an arithmetic or bitwise operation and assign the result to the same variable.
- For example, `x += 1` is equivalent to `x = x + 1`, which increments the value of `x` by `1`.
- Augmented assignment can be used with any of the following operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
- Augmented assignment can be more efficient and concise than regular assignment, especially when working with mutable objects such as lists or dictionaries.
- For example, `lst.append(5)` can be written as `lst += [5]`, which appends the list `[5]` to the list `lst`.