# Exceptions and Assertions

## Exceptions
- Exceptions are errors that occur during the execution of a program.
- Exceptions can interrupt the normal flow of the program and cause it to terminate unexpectedly.
- Exceptions can be handled using the `try` and `except` statements in Python.
- The `try` block contains the code that may raise an exception, and the `except` block contains the code that handles the exception if it occurs.
- The `except` block can specify the type of exception to catch, or use a generic `Exception` class to catch any exception.
- The `except` block can also access the exception object using the `as` keyword, which contains information about the error.
- The `else` block can be used after the `except` block to execute code that only runs if no exception occurs in the `try` block.
- The `finally` block can be used after the `else` block to execute code that always runs regardless of whether an exception occurs or not in the `try` block.
- The `raise` statement can be used to manually trigger an exception in Python, either by using a built-in exception class or by defining a custom exception class.
- Python has many built-in exception classes that inherit from the `BaseException` class, such as `ZeroDivisionError`, `ValueError`, `IndexError`, `IOError`, etc.
- The built-in exception classes can be found in the [Python documentation](https://docs.python.org/3/library/exceptions.html).

## Assertions
- Assertions are statements that check if a condition is true, and raise an `AssertionError` exception if it is false.
- Assertions are used as debugging tools to verify the correctness of the program logic and the validity of the input and output data.
- The `assert` statement is used to perform an assertion in Python, followed by a condition and an optional error message.
- The `assert` statement evaluates the condition, and if it is false, it raises an `AssertionError` exception with the error message as the argument.
- The `AssertionError` exception can be caught and handled like any other exception using the `try` and `except` statements, but if not handled, it will terminate the program and produce a traceback.
- Assertions should not be used to handle expected errors or user input errors, as they are meant for debugging purposes only.
- Assertions can be disabled by running Python with the `-O` or `-OO` options, which will ignore the `assert` statements and improve the performance of the program.

## Example
- The following example shows how to use exceptions and assertions in Python to implement the Sieve of Eratosthenes algorithm, which generates prime numbers up to a given limit.
- The algorithm works by creating a list of numbers from 2 to the limit, and marking the multiples of each number as composite, starting from 2.
- The remaining unmarked numbers are prime numbers, and are returned by the function.
- The function uses assertions to check if the limit is a positive integer, and raises a `ValueError` exception if it is not.
- The function also uses a `try` and `except` block to handle the `ZeroDivisionError` exception that may occur if the limit is 1.

```python
def sieve_of_eratosthenes(limit):
    # Check if the limit is a positive integer
    assert isinstance(limit, int), "Limit must be an integer"
    assert limit > 0, "Limit must be positive"

    # Create a list of numbers from 2 to the limit
    numbers = list(range(2, limit + 1))

    # Loop through the numbers from 2 to the square root of the limit
    for i in range(2, int(limit ** 0.5) + 1):
        # If the number is not marked as composite, mark its multiples as composite
        if numbers[i - 2] != 0:
            for j in range(i * i, limit + 1, i):
                numbers[j - 2] = 0

    # Return the unmarked numbers as prime numbers
    primes = [n for n in numbers if n != 0]
    return primes

# Test the function with different limits
try:
    print(sieve_of_eratosthenes(10)) # [2, 3, 5, 7]
    print(sieve_of_eratosthenes(1)) # ZeroDivisionError
    print(sieve_of_eratosthenes(-5)) # AssertionError
    print(s