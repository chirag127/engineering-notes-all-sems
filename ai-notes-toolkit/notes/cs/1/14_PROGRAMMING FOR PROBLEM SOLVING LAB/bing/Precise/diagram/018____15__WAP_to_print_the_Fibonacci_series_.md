## 15. WAP to print the Fibonacci series

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers. The simplest Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Here is an example of a program that prints the Fibonacci series in Python:

```python
n = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
```

This program prompts the user to enter the number of terms in the Fibonacci series to be printed. It then uses a while loop to calculate and print the Fibonacci series up to the specified number of terms.