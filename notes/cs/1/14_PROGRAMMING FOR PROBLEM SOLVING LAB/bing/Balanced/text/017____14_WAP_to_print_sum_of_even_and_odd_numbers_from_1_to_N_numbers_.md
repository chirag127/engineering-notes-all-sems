## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

- A program to print sum of even and odd numbers from 1 to N numbers is a program that takes a positive integer N as input and calculates the sum of all the even numbers and all the odd numbers from 1 to N, and prints them as output.
- To write such a program, we need to use the following steps:
  - Declare and initialize two variables, `even_sum` and `odd_sum`, to store the sum of even and odd numbers respectively. Assign them the value 0 initially.
  - Declare and initialize another variable, `num`, to store the input value of N. Use the `input()` function to take the input from the user and convert it to an integer using the `int()` function.
  - Use a `for` loop to iterate from 1 to N, using the `range()` function. For each iteration, check if the current value of the loop variable, `i`, is even or odd using the modulo operator (`%`). If `i` is even, add it to `even_sum`. If `i` is odd, add it to `odd_sum`.
  - After the loop ends, print the values of `even_sum` and `odd_sum` using the `print()` function.
- The following is an example of the program in Python:

```python
# Declare and initialize the variables
even_sum = 0
odd_sum = 0

# Take the input from the user
num = int(input("Enter a positive integer: "))

# Use a for loop to iterate from 1 to N
for i in range(1, num + 1):
  # Check if i is even or odd
  if i % 2 == 0:
    # Add i to even_sum
    even_sum += i
  else:
    # Add i to odd_sum
    odd_sum += i

# Print the results
print("The sum of even numbers from 1 to", num, "is", even_sum)
print("The sum of odd numbers from 1 to", num, "is", odd_sum)
```

- The following is an example of the output of the program for the input value of 10:

```
Enter a positive integer: 10
The sum of even numbers from 1 to 10 is 30
The sum of odd numbers from 1 to 10 is 25
```