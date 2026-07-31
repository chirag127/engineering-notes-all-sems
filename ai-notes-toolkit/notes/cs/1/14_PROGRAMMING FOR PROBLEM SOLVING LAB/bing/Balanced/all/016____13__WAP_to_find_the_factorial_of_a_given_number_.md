## 13. WAP to find the factorial of a given number.

- A factorial of a positive integer n is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 5 x 4 x 3 x 2 x 1 = 120.
- To write a program to find the factorial of a given number, we can use a loop to multiply the number by each of its predecessors until we reach 1.
- The pseudocode for the program is as follows:

```
// Input: n, a positive integer
// Output: the factorial of n

// Initialize a variable fact to store the factorial
fact = 1

// Loop from n to 1, decrementing by 1 each iteration
for i = n to 1, step -1
  // Multiply fact by i and update fact
  fact = fact * i
// End of loop

// Print the value of fact as the output
print fact
```

- The program can be written in different programming languages, such as Python, C, Java, etc. Here is an example of the program in Python:

```python
# Input: n, a positive integer
# Output: the factorial of n

# Ask the user to enter a positive integer
n = int(input("Enter a positive integer: "))

# Initialize a variable fact to store the factorial
fact = 1

# Loop from n to 1, decrementing by 1 each iteration
for i in range(n, 0, -1):
  # Multiply fact by i and update fact
  fact = fact * i

# Print the value of fact as the output
print("The factorial of", n, "is", fact)
```

- The program can be tested with different inputs, such as 5, 10, 0, etc. Here are some sample outputs:

```
Enter a positive integer: 5
The factorial of 5 is 120

Enter a positive integer: 10
The factorial of 10 is 3628800

Enter a positive integer: 0
The factorial of 0 is 1
```