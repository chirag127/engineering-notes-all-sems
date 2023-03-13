## 13. WAP to find the factorial of a given number.

- The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.
- The factorial of 0 is defined as 1, i.e., 0! = 1.
- The factorial function can be used to calculate the number of permutations of n distinct objects taken r at a time, i.e., nPr = n! / (n - r)!.
- The factorial function can also be used to calculate the number of combinations of n distinct objects taken r at a time, i.e., nCr = n! / (r! x (n - r)!).
- The factorial function grows very fast as n increases. For example, 10! = 3628800, 20! = 2432902008176640000, and 100! has 158 digits.
- One way to write a program to find the factorial of a given number is to use a loop that iterates from 1 to n and multiplies the result by each iteration. For example, in Python:

```python
# Python program to find the factorial of a given number

# Input the number
n = int(input("Enter a positive integer: "))

# Initialize the result
result = 1

# Loop from 1 to n
for i in range(1, n + 1):
  # Multiply the result by i
  result = result * i

# Print the result
print("The factorial of", n, "is", result)
```

- Another way to write a program to find the factorial of a given number is to use recursion, which is a technique of calling a function within itself. For example, in Python:

```python
# Python program to find the factorial of a given number using recursion

# Define a recursive function to calculate the factorial
def factorial(n):
  # Base case: 0! = 1
  if n == 0:
    return 1
  # Recursive case: n! = n x (n - 1)!
  else:
    return n * factorial(n - 1)

# Input the number
n = int(input("Enter a positive integer: "))

# Call the recursive function and print the result
print("The factorial of", n, "is", factorial(n))
```

- A mnemonic to remember the definition of factorial is: **F**or **A**ll **C**ounting **T**asks, **O**rder **R**eally **I**mportant **A**lgebra **L**essons. The first letter of each word spells FACTORIAL.