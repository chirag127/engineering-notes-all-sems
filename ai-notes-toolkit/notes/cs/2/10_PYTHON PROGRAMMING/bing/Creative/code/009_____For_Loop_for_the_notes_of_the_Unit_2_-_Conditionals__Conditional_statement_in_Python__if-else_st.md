### For Loop

- A for loop is a control structure that allows us to repeat a block of code a fixed number of times.
- The syntax of a for loop in Python is:

```python
for variable in sequence:
    # do something with variable
```

- The sequence can be any iterable object, such as a list, a tuple, a string, or a range object.
- The variable takes on each value in the sequence, one by one, and executes the indented block of code for each iteration.
- The block of code can contain any valid Python statements, including other nested loops or conditional statements.
- The for loop ends when the sequence is exhausted or when a break statement is encountered inside the block.

- Some examples of for loops in Python are:

```python
# print the numbers from 1 to 10
for i in range(1, 11):
    print(i)

# print the elements of a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# print the characters of a string
name = "Sydney"
for char in name:
    print(char)

# print the sum of the even numbers from 1 to 100
sum = 0
for n in range(2, 101, 2):
    sum += n
print(sum)
```

- A for loop can also have an optional else clause, which executes when the loop terminates normally (without a break statement).
- The syntax of a for loop with an else clause is:

```python
for variable in sequence:
    # do something with variable
else:
    # do something else
```

- An example of a for loop with an else clause is:

```python
# check if a number is prime
n = int(input("Enter a positive integer: "))
is_prime = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
```