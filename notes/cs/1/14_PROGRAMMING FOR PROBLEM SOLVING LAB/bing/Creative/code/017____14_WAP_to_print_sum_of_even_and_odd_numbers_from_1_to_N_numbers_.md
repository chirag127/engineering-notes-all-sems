Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to print the sum of even and odd numbers from 1 to N numbers. Here is the content in markdown format:

```markdown
## 14. WAP to print sum of even and odd numbers from 1 to N numbers.

### Problem statement:

Write a program that takes a positive integer N as input and prints the sum of all even and odd numbers from 1 to N.

### Algorithm:

1. Initialize two variables, `even_sum` and `odd_sum`, to store the sum of even and odd numbers respectively. Set them to zero.
2. Take the input N from the user and store it in a variable `n`.
3. Use a `for` loop to iterate from 1 to N, with a variable `i` as the loop counter.
4. Inside the loop, check if `i` is even or odd using the modulo operator (`%`).
5. If `i` is even, add it to `even_sum`. If `i` is odd, add it to `odd_sum`.
6. After the loop ends, print `even_sum` and `odd_sum` using the `print` function.

### Code:

```python
# Python program to print sum of even and odd numbers from 1 to N

# Initialize even and odd sum to zero
even_sum = 0
odd_sum = 0

# Take input N from the user
n = int(input("Enter a positive integer: "))

# Use a for loop to iterate from 1 to N
for i in range(1, n + 1):
  # Check if i is even or odd
  if i % 2 == 0:
    # Add i to even sum
    even_sum += i
  else:
    # Add i to odd sum
    odd_sum += i

# Print even and odd sum
print("Sum of even numbers from 1 to", n, "is", even_sum)
print("Sum of odd numbers from 1 to", n, "is", odd_sum)
```

### Output:

```
Enter a positive integer: 10
Sum of even numbers from 1 to 10 is 30
Sum of odd numbers from 1 to 10 is 25
```
```