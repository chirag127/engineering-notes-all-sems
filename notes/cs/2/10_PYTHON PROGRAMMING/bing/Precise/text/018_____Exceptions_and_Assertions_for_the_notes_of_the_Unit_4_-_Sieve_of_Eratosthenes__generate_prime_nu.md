### Exceptions and Assertions

Exceptions and assertions are two mechanisms in Python that allow you to handle errors and unexpected behavior in your code.

#### Exceptions

- Exceptions are events that occur during the execution of a program that disrupt the normal flow of the program's instructions.
- When an exception occurs, the program stops executing at that point and Python looks for a way to handle the exception.
- If an appropriate exception handler is found, the program continues executing from that point. If no handler is found, the program terminates and an error message is displayed.
- Exceptions can be raised by the Python interpreter or by the code you write.
- To handle exceptions, you can use a `try`...`except` block. The code that might raise an exception is placed in the `try` block, and the code that handles the exception is placed in the `except` block.
- You can also use the `else` and `finally` clauses with the `try`...`except` block. The `else` clause is executed if no exception is raised, and the `finally` clause is always executed, regardless of whether an exception is raised or not.

#### Assertions

- Assertions are statements that check if a condition is true.
- If the condition is not true, an `AssertionError` is raised.
- Assertions are used to ensure that the code is working as expected and to catch errors early in the development process.
- Assertions are not meant to be used to handle runtime errors or to validate user input.
- To use assertions, you can use the `assert` statement. The `assert` statement takes a condition and an optional error message. If the condition is not true, an `AssertionError` is raised with the error message.
