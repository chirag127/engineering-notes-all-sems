Hello, I am Sydney, your AI assistant. I can help you with your study material for Python programming. Here is the content for the topic of nested loops:

### Nested Loops

- A nested loop is a loop that is inside another loop.
- A loop is a block of code that repeats a certain number of times or until a condition is met.
- In Python, there are two types of loops: for loops and while loops.
- A for loop iterates over a sequence of items, such as a list, a tuple, a string, or a range object.
- A while loop repeats as long as a boolean expression is True.
- A nested loop can be a for loop inside a for loop, a while loop inside a while loop, a for loop inside a while loop, or a while loop inside a for loop.
- The inner loop executes all its iterations for each iteration of the outer loop.
- Nested loops can be used to create complex patterns, such as grids, tables, matrices, or shapes.
- Nested loops can also be used to iterate over multidimensional data structures, such as lists of lists, tuples of tuples, or dictionaries of dictionaries.
- To exit a nested loop, you can use the break statement, which terminates the current loop and resumes execution at the next statement after the loop.
- You can also use the continue statement, which skips the rest of the current iteration and continues with the next iteration of the loop.
- You can use the else clause after a loop, which executes only if the loop terminates normally, without encountering a break statement.
- Here is an example of a nested for loop that prints a multiplication table:

```python
# Print a multiplication table from 1 to 10
for i in range(1, 11): # Outer loop
    for j in range(1, 11): # Inner loop
        print(i * j, end="\t") # Print the product of i and j, followed by a tab
    print() # Print a new line after each row
```

- Here is an example of a nested while loop that prints a right-angled triangle of asterisks:

```python
# Print a right-angled triangle of asterisks
n = 5 # Number of rows
i = 1 # Outer loop counter
while i <= n: # Outer loop condition
    j = 1 # Inner loop counter
    while j <= i: # Inner loop condition
        print("*", end="") # Print an asterisk, without a new line
        j += 1 # Increment the inner loop counter
    print() # Print a new line after each row
    i += 1 # Increment the outer loop counter
```

- Here is an example of a for loop inside a while loop that prints the Fibonacci sequence up to 100:

```python
# Print the Fibonacci sequence up to 100
a = 0 # First term
b = 1 # Second term
while a < 100: # Outer loop condition
    print(a, end=" ") # Print the current term, followed by a space
    a, b = b, a + b # Update the next two terms using tuple assignment
print() # Print a new line at the end
```

- Here is an example of a while loop inside a for loop that prints the prime numbers from 2 to 20:

```python
# Print the prime numbers from 2 to 20
for n in range(2, 21): # Outer loop
    i = 2 # Inner loop counter
    prime = True # Flag to indicate if n is prime or not
    while i < n: # Inner loop condition
        if n % i == 0: # If n is divisible by i
            prime = False # Set the flag to False
            break # Exit the inner loop
        i += 1 # Increment the inner loop counter
    if prime: # If the flag is True
        print(n, end=" ") # Print the prime number, followed by a space
print() # Print a new line at the end
```