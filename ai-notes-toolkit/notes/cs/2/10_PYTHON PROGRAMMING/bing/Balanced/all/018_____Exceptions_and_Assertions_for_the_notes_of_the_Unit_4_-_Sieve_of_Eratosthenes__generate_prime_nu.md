# Exceptions and Assertions

## Exceptions
- Exceptions are errors that occur during the execution of a program and disrupt its normal flow.
- Exceptions can be caused by various reasons, such as invalid input, division by zero, file not found, etc.
- Exceptions can be handled using the `try` and `except` statements in Python, which allow the program to continue or perform some alternative action instead of terminating abruptly.
- The `try` block contains the code that may raise an exception, and the `except` block contains the code that handles the exception if it occurs.
- The `except` block can specify the type of exception to handle, or use a generic `Exception` class to handle any exception.
- The `except` block can also access the exception object using the `as` keyword, which contains information about the error, such as its type, message, and traceback.
- The `try` and `except` statements can be nested to handle different exceptions at different levels of the program.
- The `try` statement can also have an optional `else` block, which executes if no exception occurs in the `try` block, and a `finally` block, which executes in any case, whether an exception occurs or not.
- The `raise` statement can be used to explicitly raise an exception in the program, either by using an existing exception class or by creating a custom exception class that inherits from `BaseException` or one of its subclasses.
- The `assert` statement can also be used to raise an `AssertionError` exception if a condition is not met, which is useful for debugging and testing purposes.

## Assertions
- Assertions are statements that check if a condition is true, and raise an exception if it is false.
- Assertions are used to ensure the correctness and validity of the program logic, such as checking the input, output, or intermediate results of a function or a block of code.
- Assertions are carried out by the `assert` statement, which takes a condition and an optional message as arguments, and raises an `AssertionError` exception with the message if the condition is false.
- Assertions can be enabled or disabled by using the `-O` or `-OO` flags when running the Python interpreter, which can improve the performance of the program by skipping the assertion checks.
- Assertions should not be used to handle expected errors or user input, as they are meant for debugging and testing purposes only. Exceptions should be used instead for those cases.