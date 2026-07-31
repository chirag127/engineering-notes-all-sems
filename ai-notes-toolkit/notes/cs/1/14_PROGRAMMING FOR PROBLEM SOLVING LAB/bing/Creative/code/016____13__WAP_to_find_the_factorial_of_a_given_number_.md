## 13. WAP to find the factorial of a given number.

- A factorial of a positive integer n is the product of all positive integers from 1 to n, denoted by n!.
- For example, 5! = 1 x 2 x 3 x 4 x 5 = 120.
- The factorial of 0 is defined as 1, i.e., 0! = 1.
- To write a program to find the factorial of a given number, we can use a loop to multiply the numbers from 1 to n.
- We can use either a for loop or a while loop, depending on the preference.
- We can also use a function to calculate the factorial and call it from the main program.
- Here is an example of a program to find the factorial of a given number using a for loop and a function in Python:

```python
# Define a function to calculate the factorial
def factorial(n):
  # Initialize the result as 1
  result = 1
  # Loop from 1 to n
  for i in range(1, n + 1):
    # Multiply the result by i
    result = result * i
  # Return the result
  return result

# Take the input from the user
n = int(input("Enter a positive integer: "))
# Check if the input is valid
if n < 0:
  print("Invalid input. Factorial is not defined for negative numbers.")
else:
  # Call the factorial function and print the result
  print("The factorial of", n, "is", factorial(n))
```