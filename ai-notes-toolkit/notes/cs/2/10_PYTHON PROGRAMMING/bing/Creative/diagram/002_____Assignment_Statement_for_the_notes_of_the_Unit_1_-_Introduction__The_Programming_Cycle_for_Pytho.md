### Assignment Statement

- An assignment statement is a way of creating, initializing, or updating variables in Python.
- A variable is a name that refers to an object, such as a number, a string, a list, or a function.
- An assignment statement has the form `target = expression`, where `target` is the name of the variable and `expression` is any Python expression that evaluates to an object.
- The assignment statement assigns the object resulting from the expression to the target variable, creating or updating the variable's reference to the object.
- For example, `x = 10` assigns the integer object `10` to the variable `x`.
- Python supports multiple assignment, where more than one target can be assigned to the same or different objects in a single statement.
- For example, `x, y = 10, 20` assigns the integer object `10` to the variable `x` and the integer object `20` to the variable `y`.
- Multiple assignment can also be used to swap the values of two variables without using a temporary variable.
- For example, `x, y = y, x` swaps the values of `x` and `y`.
- Python also supports augmented assignment, where an operator can be combined with the assignment operator to perform an arithmetic or bitwise operation and assign the result to the target variable in one step.
- For example, `x += 5` is equivalent to `x = x + 5`, which adds `5` to the value of `x` and assigns the result back to `x`.
- Augmented assignment can be used with any of the following operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
- Augmented assignment can also be used with custom objects that define special methods for the corresponding operators, such as `__add__`, `__sub__`, `__mul__`, etc.