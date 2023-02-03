## 15. WAP to print the Fibonacci series.

Here is a code snippet in Python to print the Fibonacci series:

```
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci(n)
```

Explanation:
- `n` is the number of terms in the Fibonacci series to be printed.
- The `fibonacci` function takes `n` as an argument and generates the Fibonacci series using a loop.
- The loop starts from `0` and continues till `n-1`.
- In each iteration, `a` is printed and then `a` and `b` are updated to `b` and `a + b` respectively.
- The initial values of `a` and `b` are `0` and `1` respectively.
