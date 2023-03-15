# Exceptions and Assertions

Exceptions and assertions are two mechanisms in Python that allow you to handle errors and unexpected behavior in your code.

## Exceptions

An exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions. When an exception occurs, the program stops executing and an error message is displayed.

In Python, exceptions are raised using the `raise` statement. For example, if you want to raise an exception when a certain condition is not met, you can use the following code:

```python
if not condition:
    raise Exception("Condition not met")
```

You can also define your own exceptions by creating a new class that inherits from the `Exception` class. This allows you to create custom error messages and handle specific types of errors in your code.

```python
class MyException(Exception):
    pass

raise MyException("My custom error message")
```

When an exception is raised, you can use a `try`...`except` block to catch the exception and handle it gracefully. The `try` block contains the code that might raise an exception, and the `except` block contains the code that will be executed if an exception is raised.

```python
try:
    # code that might raise an exception
except MyException as e:
    # handle the exception
    print(e)
```

## Assertions

An assertion is a statement that checks if a condition is true. If the condition is not true, an `AssertionError` is raised. Assertions are used to ensure that the code is working as expected and to catch errors early in the development process.

In Python, you can use the `assert` statement to perform an assertion. The `assert` statement takes a condition and an optional error message as arguments. If the condition is not true, an `AssertionError` is raised with the error message.

```python
assert condition, "Error message"
```

Assertions are commonly used in testing and debugging to ensure that the code is working correctly. However, they should not be used to handle runtime errors, as they can be disabled globally in the Python interpreter.

In summary, exceptions and assertions are two powerful tools that allow you to handle errors and unexpected behavior in your Python code. By using these mechanisms, you can write more robust and reliable code.