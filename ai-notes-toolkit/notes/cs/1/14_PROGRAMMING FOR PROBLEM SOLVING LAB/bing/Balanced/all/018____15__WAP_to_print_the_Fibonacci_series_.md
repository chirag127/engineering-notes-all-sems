## 15. WAP to print the Fibonacci series.

- The Fibonacci series is a sequence of numbers where each term is the sum of the previous two terms.
- The first two terms of the Fibonacci series are 1 and 1.
- The general formula for the nth term of the Fibonacci series is:

  - F(n) = F(n-1) + F(n-2), for n > 2

- To write a program to print the Fibonacci series, we need to:

  - Declare a variable n to store the number of terms to be printed.
  - Declare three variables a, b, and c to store the current, previous, and next term of the series respectively.
  - Initialize a and b to 1, and c to 0.
  - Use a loop to iterate from 1 to n, and print the value of a in each iteration.
  - Update the values of a, b, and c as follows:

    - c = a + b
    - a = b
    - b = c

  - End the loop and the program.

- An example of a program to print the Fibonacci series in Python is:

```python
# WAP to print the Fibonacci series

# Input the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a = 1
b = 1

# Initialize the next term
c = 0

# Print the first term
print(a, end=" ")

# Loop from the second term to the nth term
for i in range(2, n+1):

  # Print the current term
  print(b, end=" ")

  # Update the next term
  c = a + b

  # Update the current and previous terms
  a = b
  b = c

# End the program
```