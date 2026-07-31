# While loop

- A while loop is a type of loop that repeats a block of code as long as a given condition is true.
- The syntax of a while loop is:

```python
while condition:
    # block of code
```

- The condition is a boolean expression that evaluates to either True or False.
- The block of code is indented under the while statement and can contain any valid Python statements.
- The while loop checks the condition before each iteration and executes the block of code only if the condition is True.
- The while loop ends when the condition becomes False or when a break statement is encountered inside the loop.
- A while loop can also have an optional else clause that executes after the loop ends normally (without a break statement).

```python
while condition:
    # block of code
else:
    # block of code after the loop
```

- The else clause is useful for performing some final actions after the loop, such as printing a message or closing a file.
- A while loop can be used to implement various algorithms and tasks, such as counting, searching, sorting, etc.

## Example of a while loop

- The following example shows how to use a while loop to print the numbers from 1 to 10.

```python
# initialize a counter variable
counter = 1

# loop until counter is greater than 10
while counter <= 10:
    # print the current value of counter
    print(counter)

    # increment counter by 1
    counter = counter + 1

# print a message after the loop
print("The loop is over.")
```

- The output of the program is:

```text
1
2
3
4
5
6
7
8
9
10
The loop is over.
```