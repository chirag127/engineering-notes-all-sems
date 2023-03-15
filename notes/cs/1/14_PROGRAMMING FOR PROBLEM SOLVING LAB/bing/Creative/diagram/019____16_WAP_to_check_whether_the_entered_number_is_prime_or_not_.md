Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to check whether the entered number is prime or not. Here is the content in markdown format:

## 16.WAP to check whether the entered number is prime or not.

A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11 are prime numbers, but 4, 6, 8, 9, 10 are not.

To check whether a given number is prime or not, we can use the following algorithm:

- Input the number from the user and store it in a variable, say n.
- If n is less than or equal to 1, then it is not a prime number. Print "Not a prime number" and exit the program.
- Otherwise, start a loop from 2 to the square root of n, with a step of 1. For each iteration, store the loop variable in another variable, say i.
- If n is divisible by i, then it is not a prime number. Print "Not a prime number" and exit the loop and the program.
- If the loop ends without finding any divisor of n, then it is a prime number. Print "Prime number" and exit the program.

Here is the code in Python that implements the above algorithm:

```python
# WAP to check whether the entered number is prime or not

# Input the number from the user and store it in n
n = int(input("Enter a number: "))

# If n is less than or equal to 1, then it is not a prime number
if n <= 1:
    print("Not a prime number")
    # Exit the program
    exit()

# Otherwise, start a loop from 2 to the square root of n, with a step of 1
for i in range(2, int(n**0.5) + 1):
    # If n is divisible by i, then it is not a prime number
    if n % i == 0:
        print("Not a prime number")
        # Exit the loop and the program
        break
else:
    # If the loop ends without finding any divisor of n, then it is a prime number
    print("Prime number")
```