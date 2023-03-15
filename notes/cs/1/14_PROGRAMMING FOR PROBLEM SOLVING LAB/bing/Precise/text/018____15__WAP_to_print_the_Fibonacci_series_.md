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

- The program starts by initializing the variables `n1` and `n2` to 0 and 1, respectively. These variables represent the first two terms of the Fibonacci series.
- The variable `count` is initialized to 0 and is used to keep track of the number of terms printed.
- The program then checks if the number of terms entered by the user is less than or equal to 0. If it is, the program prints an error message and exits.
- If the number of terms entered by the user is 1, the program prints the first term of the Fibonacci series, which is 0.
- If the number of terms entered by the user is greater than 1, the program enters a while loop that continues until the specified number of terms have been printed.
- Inside the while loop, the program prints the current value of `n1`, which represents the next term in the Fibonacci series.
- The program then calculates the next term in the series by adding `n1` and `n2` and storing the result in the variable `nth`.
- The values of `n1` and `n2` are then updated to `n2` and `nth`, respectively, to prepare for the next iteration of the loop.
- The `count` variable is incremented by 1 to keep track of the number of terms printed.
- The while loop continues until the specified number of terms have been printed.

This is one way to write a program to print the Fibonacci series. There are many other ways to accomplish the same task, and the specific implementation may vary depending on the programming language and the requirements of the specific program.