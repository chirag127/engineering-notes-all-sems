### Break and Continue

- Break and continue are two keywords that can be used to alter the flow of a loop in Python.
- Break is used to terminate the loop prematurely, while continue is used to skip the current iteration and move to the next one.
- Break and continue can be used with both for and while loops.

#### Break

- The break statement can be used to exit a loop when a certain condition is met, such as finding a target value, reaching a limit, or encountering an error.
- The break statement immediately ends the loop and transfers the control to the statement after the loop body.
- The break statement can be useful to avoid unnecessary iterations or computations that are not needed after a certain point.
- For example, the following code uses a break statement to search for the number 5 in a list and print its index. Once the number is found, the loop is terminated and the index is printed.

```python
# Example of break statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    if numbers[i] == 5:
        print("Found 5 at index", i)
        break # Exit the loop
```

#### Continue

- The continue statement can be used to skip the current iteration of a loop and move to the next one, without terminating the loop.
- The continue statement can be useful to avoid executing some statements in the loop body for certain values or conditions, such as filtering out unwanted values, handling exceptions, or implementing logic.
- For example, the following code uses a continue statement to print only the even numbers in a list. If the number is odd, the continue statement skips the print statement and moves to the next iteration.

```python
# Example of continue statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        continue # Skip the odd numbers
    print(num) # Print the even numbers
```