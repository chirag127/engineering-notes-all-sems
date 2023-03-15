## 15. WAP to print the Fibonacci series

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers. The simplest Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Here is an example of a program that prints the Fibonacci series:

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

The program initializes two variables, `n1` and `n2`, to 0 and 1, respectively. These variables represent the first two terms of the Fibonacci series. The program also initializes a variable `count` to 0 to keep track of the number of terms printed.

The program then checks if the number of terms entered by the user is less than or equal to 0. If it is, the program prints an error message asking the user to enter a positive integer.

If the number of terms entered by the user is 1, the program prints the first term of the Fibonacci series, which is 0.

If the number of terms entered by the user is greater than 1, the program enters a while loop that continues until the specified number of terms have been printed. In each iteration of the loop, the program prints the value of `n1`, calculates the next term in the series by adding `n1` and `n2`, and updates the values of `n1` and `n2`. The program also increments the `count` variable to keep track of the number of terms printed.

This program can be modified to print the Fibonacci series in different ways, such as using a for loop or using recursion. It can also be modified to perform other operations on the Fibonacci series, such as finding the sum of the first n terms or finding the nth term in the series.