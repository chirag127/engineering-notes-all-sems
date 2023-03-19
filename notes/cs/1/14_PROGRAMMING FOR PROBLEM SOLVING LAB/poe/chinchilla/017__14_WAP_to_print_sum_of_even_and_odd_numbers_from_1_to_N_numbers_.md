## 14. WAP to print sum of even and odd numbers from 1 to N numbers.

In this programming exercise, we will write a Python program to find the sum of even and odd numbers from 1 to N numbers, where N is a user-input positive integer.

To solve this problem, we will use a loop to iterate through the numbers from 1 to N and check if each number is even or odd. We will then add the even numbers and odd numbers separately to find their respective sums.

Here are the steps to write the program:

1. Start by asking the user to enter a positive integer N.
2. Use a loop to iterate through the numbers from 1 to N.
3. For each number, check if it is even or odd. To do this, use the modulo operator (%), which returns the remainder of a division. If the remainder of the number divided by 2 is 0, it is even. Otherwise, it is odd.
4. If the number is even, add it to the sum of even numbers. If it is odd, add it to the sum of odd numbers.
5. After the loop has finished iterating through all the numbers from 1 to N, print the sum of even numbers and the sum of odd numbers.

Here is the Python code to implement the above steps:

``` python
# Ask user to enter a positive integer N
N = int(input("Enter a positive integer: "))

# Initialize variables to store the sum of even and odd numbers
sum_even = 0
sum_odd = 0

# Loop through the numbers from 1 to N
for i in range(1, N+1):
    # Check if the number is even or odd
    if i % 2 == 0:
        # Add the even number to the sum of even numbers
        sum_even += i
    else:
        # Add the odd number to the sum of odd numbers
        sum_odd += i

# Print the sum of even and odd numbers
print("Sum of even numbers from 1 to", N, "is:", sum_even)
print("Sum of odd numbers from 1 to", N, "is:", sum_odd)
```

Note that we have used the `range()` function to generate a sequence of numbers from 1 to N, and the `+=` operator to add the even and odd numbers to their respective sums.

With this program, we can easily find the sum of even and odd numbers from 1 to any positive integer N. This concept can be useful in various applications, such as calculating the average of even or odd numbers in a given range.