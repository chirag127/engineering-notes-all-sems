### Exceptions and Assertions

- Exceptions are errors that occur during the execution of a program and disrupt its normal flow. They can be caused by various reasons, such as invalid input, division by zero, file not found, etc. Exceptions can be handled using the `try` and `except` statements, which allow the program to recover from the error or perform some alternative action. Exceptions can also be raised explicitly using the `raise` statement, which allows the programmer to signal an error condition to the caller of the function or the module. Exceptions are represented by classes that inherit from the `BaseException` class.

- Assertions are statements that check if a certain condition is true or false. They are used as debugging tools to verify the correctness of the program logic and detect any bugs or inconsistencies. Assertions are executed using the `assert` statement, which takes an expression and an optional message as arguments. If the expression evaluates to `False`, an `AssertionError` exception is raised with the message as the argument. If the expression evaluates to `True`, nothing happens. Assertions are usually placed at the start or the end of a function to check the validity of the input or the output.

- The difference between exceptions and assertions is that exceptions address the robustness of the application, while assertions address the correctness. Exceptions are meant to handle unexpected or unavoidable errors that may occur during the program execution, while assertions are meant to verify the assumptions or invariants that must hold true at all times. Exceptions can be caught and handled by the program, while assertions are usually enabled only during the development or testing phase and disabled in the production code.

- An example of using exceptions and assertions in Python is the following:

```python
# Define a function that returns the nth prime number using the Sieve of Eratosthenes algorithm
def nth_prime(n):
    # Check if the input is a positive integer
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    # Initialize a list of numbers from 2 to n^2
    numbers = list(range(2, n**2 + 1))
    # Initialize an empty list of primes
    primes = []
    # Loop until n primes are found
    while len(primes) < n:
        # Take the first number in the list as the next prime
        prime = numbers[0]
        primes.append(prime)
        # Remove all multiples of the prime from the list
        numbers = [x for x in numbers if x % prime != 0]
    # Return the last prime in the list
    return primes[-1]

# Try to call the function with different inputs
try:
    print(nth_prime(10)) # Prints 29
    print(nth_prime(0)) # Raises an AssertionError
    print(nth_prime(1.5)) # Raises an AssertionError
    print(nth_prime(1000)) # Prints 7919
except AssertionError as e:
    print(e) # Prints the assertion message
```