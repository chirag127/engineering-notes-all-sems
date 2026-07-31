# For Loop

- A for loop is a type of loop that iterates over a sequence of items, such as a list, a tuple, a string, or a range object.
- The syntax of a for loop is:

```python
for item in sequence:
    # do something with item
```

- The item variable can be any valid identifier, and it takes the value of each element in the sequence in each iteration.
- The sequence can be any iterable object that supports the `__iter__` and `__next__` methods, such as a list, a tuple, a string, or a range object.
- The body of the loop is indented under the for statement, and it can contain any valid Python statements, including other loops, conditionals, or function calls.
- The loop terminates when the sequence is exhausted, or when a `break` or `return` statement is encountered inside the loop body.
- A for loop can also have an optional `else` clause, which is executed when the loop ends normally, i.e., without a `break` or `return` statement. The syntax of a for loop with an else clause is:

```python
for item in sequence:
    # do something with item
else:
    # do something else
```

- The else clause is useful when we want to perform some action after the loop, but only if the loop was not interrupted by a `break` or `return` statement.
- Some examples of for loops are:

```python
# print the elements of a list
my_list = [1, 2, 3, 4, 5]
for x in my_list:
    print(x)

# print the characters of a string
my_string = "Hello"
for ch in my_string:
    print(ch)

# print the numbers from 0 to 9 using a range object
for i in range(10):
    print(i)

# print the even numbers from 0 to 10 using a range object with a step argument
for i in range(0, 11, 2):
    print(i)

# print the sum of the elements of a list using a loop variable
my_list = [1, 2, 3, 4, 5]
sum = 0
for x in my_list:
    sum = sum + x
print(sum)

# print the factorial of a number using a loop variable and a break statement
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
    if i == n:
        break
print(factorial)

# print the first 10 Fibonacci numbers using a loop variable and a return statement
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a + b
        if i == n - 1:
            return
fibonacci(10)

# print the prime numbers from 2 to 20 using a nested loop and a flag variable
for i in range(2, 21):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

# print the multiplication table of a number using a nested loop and an f-string
n = 5
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
```