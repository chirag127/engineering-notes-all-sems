## 13. WAP to find the factorial of a given number.

In this topic, we will discuss how to write a program in Python to find the factorial of a given number. Factorial is a mathematical operation that is used to find the product of all positive integers from 1 to the given number. The factorial of a number n is denoted by n! and is equal to the product of all positive integers from 1 to n.

### Algorithm:

The algorithm to find the factorial of a given number is as follows:

1. Input the value of n.
2. Set the value of factorial to 1.
3. Use a loop to iterate from 1 to n.
4. At each iteration, multiply the value of the factorial by the current value of i.
5. After the loop, the value of factorial will be equal to the factorial of n.
6. Output the value of factorial.

### Code:

```python
# Input the value of n
n = int(input("Enter a number: "))

# Initialize the value of factorial to 1
factorial = 1

# Use a loop to iterate from 1 to n
for i in range(1, n+1):
    # Multiply the value of factorial by the current value of i
    factorial *= i

# Output the value of factorial
print("The factorial of", n, "is", factorial)
```

### Example:

Let's say we want to find the factorial of the number 5. The program will take the input as 5 and will calculate the factorial as follows:

```python
Enter a number: 5
The factorial of 5 is 120
```

Therefore, the factorial of 5 is 120.