### Assignment Statement

- An assignment statement is a way of creating, initializing, or updating variables in Python.
- A variable is a name that refers to an object, such as a number, a string, a list, or a function.
- An assignment statement has the form `target = expression`, where `target` is the name of the variable and `expression` is any Python expression that evaluates to an object.
- The assignment statement assigns the object resulting from the expression to the target variable, creating or updating the variable's reference to the object.
- For example, `x = 5` assigns the integer object `5` to the variable `x`, creating or updating `x`'s reference to `5`.
- Python supports multiple assignment, where more than one target variable can be assigned to the same or different objects in a single statement.
- For example, `x, y = 10, 20` assigns the integer object `10` to the variable `x` and the integer object `20` to the variable `y` in one statement.
- Multiple assignment can also be used to swap the values of two variables without using a temporary variable.
- For example, `x, y = y, x` swaps the values of `x` and `y` by assigning the object that `y` refers to `x` and the object that `x` refers to `y`.
- Python also supports augmented assignment, where an operator and an equal sign are combined to perform an arithmetic or bitwise operation and assign the result to the target variable in one statement.
- For example, `x += 5` is equivalent to `x = x + 5`, which adds `5` to the object that `x` refers to and assigns the result to `x`.
- Augmented assignment can be used with any of the following operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`.
- Augmented assignment can also be used with mutable objects, such as lists or dictionaries, to modify their contents without creating a new object.
- For example, `lst += [4, 5, 6]` appends the list `[4, 5, 6]` to the end of the list that `lst` refers to, modifying `lst` in place.