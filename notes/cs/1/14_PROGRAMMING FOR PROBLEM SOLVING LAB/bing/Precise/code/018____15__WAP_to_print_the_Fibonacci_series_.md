## 15. WAP to print the Fibonacci series

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers. The simplest Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

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

The program initializes the first two terms of the series, `n1` and `n2`, to 0 and 1, respectively. It also initializes a counter variable `count` to 0.

The program then checks if the number of terms entered by the user is less than or equal to 0. If it is, the program prints an error message asking the user to enter a positive integer.

If the number of terms entered by the user is 1, the program prints the first term of the series, which is 0.

If the number of terms entered by the user is greater than 1, the program enters a while loop that runs until the counter variable `count` is less than the number of terms entered by the user.

Inside the while loop, the program prints the current value of `n1`, which is the current term in the series. It then calculates the next term in the series by adding `n1` and `n2` and assigns the result to the variable `nth`. The program then updates the values of `n1` and `n2` to `n2` and `nth`, respectively, and increments the counter variable `count` by 1.

This process continues until the while loop has run the specified number of times, at which point the program has printed the specified number of terms in the Fibonacci series.