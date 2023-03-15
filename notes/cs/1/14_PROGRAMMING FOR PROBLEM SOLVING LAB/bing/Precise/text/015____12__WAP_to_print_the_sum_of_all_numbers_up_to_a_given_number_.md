## 12. WAP to print the sum of all numbers up to a given number.

Here is a program that calculates the sum of all numbers up to a given number:

```python
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of all numbers up to", n, "is", sum)
```

- The program prompts the user to enter a number `n`.
- The variable `sum` is initialized to 0.
- A `for` loop is used to iterate over the range of numbers from 1 to `n`.
- In each iteration, the value of `i` is added to the `sum`.
- After the loop is completed, the final value of `sum` is printed, which is the sum of all numbers up to `n`.

This program can be further optimized by using the formula for the sum of the first `n` natural numbers, which is `n*(n+1)/2`. Here is the optimized version of the program:

```python
n = int(input("Enter a number: "))
sum = n*(n+1)//2
print("The sum of all numbers up to", n, "is", sum)
```

- The program prompts the user to enter a number `n`.
- The formula `n*(n+1)//2` is used to calculate the sum of the first `n` natural numbers.
- The result is stored in the variable `sum` and printed.

Both versions of the program produce the same result, but the second version is more efficient as it does not use a loop and performs the calculation in constant time.