## 12. WAP to print the sum of all numbers up to a given number.

Here is a program that can be used to print the sum of all numbers up to a given number:

```python
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of all numbers up to", n, "is", sum)
```

- The program starts by taking an input from the user and storing it in the variable `n`.
- The variable `sum` is initialized to 0.
- A `for` loop is used to iterate over the range of numbers from 1 to `n+1`.
- In each iteration, the value of `i` is added to the `sum` variable.
- After the loop is completed, the final value of `sum` is printed, which is the sum of all numbers up to `n`.

This program can be used to calculate the sum of all numbers up to any given number. It is a simple and efficient way to solve this problem.