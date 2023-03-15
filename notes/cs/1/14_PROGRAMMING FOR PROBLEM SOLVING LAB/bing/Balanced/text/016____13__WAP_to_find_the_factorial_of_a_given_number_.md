## 13. WAP to find the factorial of a given number.

- A factorial of a positive integer n is the product of all positive integers from 1 to n, denoted by n!.
- For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.
- The factorial of 0 is defined as 1, i.e., 0! = 1.
- To write a program to find the factorial of a given number, we can use a loop to multiply the numbers from 1 to n.
- We can use either a for loop or a while loop, depending on the programming language and the preference of the programmer.
- Here is an example of a program to find the factorial of a given number in Python:

```python
# Python program to find the factorial of a given number

# Input the number from the user
n = int(input("Enter a positive integer: "))

# Initialize the factorial as 1
factorial = 1

# Check if the number is valid
if n < 0:
    print("Invalid input. Factorial is not defined for negative numbers.")
else:
    # Use a for loop to multiply the numbers from 1 to n
    for i in range(1, n + 1):
        factorial = factorial * i

    # Print the result
    print("The factorial of", n, "is", factorial)
```