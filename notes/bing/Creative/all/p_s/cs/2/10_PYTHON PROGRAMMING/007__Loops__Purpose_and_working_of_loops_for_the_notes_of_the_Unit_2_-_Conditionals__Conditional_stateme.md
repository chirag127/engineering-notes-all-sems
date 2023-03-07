### Loops: Purpose and working of loops

- Loops are a way of repeating a block of code multiple times until a certain condition is met.
- Loops are useful for performing tasks that require iteration, such as processing a list of items, generating a sequence of numbers, or printing a pattern of characters.
- Python supports two types of loops: while loops and for loops.

#### While Loop

- A while loop executes a block of code as long as a given condition is true.
- The syntax of a while loop is:

```python
while condition:
    # code block
```

- The condition is a boolean expression that evaluates to True or False.
- The code block is indented under the while statement and can contain any valid Python statements.
- The code block is executed repeatedly until the condition becomes False or a break statement is encountered.
- A break statement can be used to exit the loop prematurely.
- A continue statement can be used to skip the current iteration and move to the next one.
- Example of a while loop:

```python
# print the numbers from 1 to 10
n = 1
while n <= 10:
    print(n)
    n = n + 1
```

#### For Loop

- A for loop is used for iterating over a sequence, such as a list, a tuple, a dictionary, a set, or a string.
- The syntax of a for loop is:

```python
for item in sequence:
    # code block
```

- The item variable takes the value of each element in the sequence in each iteration.
- The code block is indented under the for statement and can contain any valid Python statements.
- The code block is executed once for each element in the sequence, or until a break statement is encountered.
- A break statement can be used to exit the loop prematurely.
- A continue statement can be used to skip the current iteration and move to the next one.
- Example of a for loop:

```python
# print the elements of a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

#### While versus For Loops in Python

- While loops are more general and can be used for any kind of iteration, but they require more care to avoid infinite loops or off-by-one errors.
- For loops are more concise and convenient for iterating over sequences, but they cannot be used for indefinite or infinite loops.
- For loops can also use the range() function to generate a sequence of numbers on the fly, such as:

```python
# print the numbers from 1 to 10 using a for loop and range()
for n in range(1, 11):
    print(n)
```

#### Nested Loops

- Nested loops are loops that contain another loop inside them.
- The inner loop is executed completely for each iteration of the outer loop.
- Nested loops can be used to create complex patterns or traverse multidimensional data structures, such as:

```python
# print a multiplication table using nested loops
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
```

- Nested loops can also be a combination of while and for loops, such as:

```python
# print the Fibonacci sequence using a while loop and a for loop
a = 0
b = 1
while a < 100:
    print(a, end=" ")
    a, b = b, a + b
print()
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()
```

Some possible mnemonics and learning tricks for the topic are:

- To remember the syntax of a while loop, think of the word WHILE as an acronym: **W**hile **H**ere **I** **L**oop **E**ndlessly.
- To remember the syntax of a for loop, think of the word FOR as an acronym: **F**or **O**ne **R**ound.
- To remember the difference between a while loop and a for loop, think of a while loop as a clock that keeps ticking until it is stopped, and a for loop as a stopwatch that counts a fixed number of laps.
- To remember the order of execution of nested loops, think of the outer loop as the rows and the inner loop as the columns of a table. The inner loop completes one column before moving to the next one, and the outer loop completes one row before moving to the next one.