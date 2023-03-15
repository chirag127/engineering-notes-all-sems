Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to check whether the entered number is prime or not. Here is the content in markdown format:

## 16.WAP to check whether the entered number is prime or not.

A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11 are prime numbers, but 4, 6, 8, 9, 10 are not.

To check whether a given number is prime or not, we can use the following algorithm:

- Step 1: Input the number n from the user.
- Step 2: Initialize a variable flag to 1. This variable will store the result of the check.
- Step 3: If n is less than or equal to 1, then set flag to 0 and go to step 6. This is because 1 and negative numbers are not prime.
- Step 4: Loop from 2 to the square root of n. For each iteration, check if n is divisible by the current loop variable. If yes, then set flag to 0 and break the loop. This is because if n has a divisor other than 1 and itself, then it is not prime.
- Step 5: End the loop.
- Step 6: If flag is 1, then print n is prime. Otherwise, print n is not prime.
- Step 7: Stop.

Here is an example of the program in Python:

```python
# WAP to check whether the entered number is prime or not

# Input the number from the user
n = int(input("Enter a number: "))

# Initialize the flag to 1
flag = 1

# Check if n is less than or equal to 1
if n <= 1:
  # Set flag to 0
  flag = 0
else:
  # Loop from 2 to the square root of n
  for i in range(2, int(n**0.5) + 1):
    # Check if n is divisible by i
    if n % i == 0:
      # Set flag to 0 and break the loop
      flag = 0
      break

# Print the result based on the flag
if flag == 1:
  print(n, "is prime")
else:
  print(n, "is not prime")
```

Here is an example of the output:

```
Enter a number: 17
17 is prime
```

```
Enter a number: 12
12 is not prime
```
