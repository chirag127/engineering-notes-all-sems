 Here is the formal content written using Markdown format without any emojis or external links:

# Using Loops

## For Loop

1. For loop is used to iterate over a sequence (list, string, tuple) or other iterable objects.
2. The syntax is:
for element in sequence:
    # do something

3. The loop will run the block of code for each element in the sequence sequentially.

Example:
for i in range(10):
    print(i)

Output:
0
1
2
3
4
5
6
7
8
9

## While Loop

1. While loop executes a block of code repeatedly until a specified condition is met.
2. The syntax is:
while condition:
    # do something

3. The loop will keep executing the code block as long as the condition evaluates to True.

Example:
count = 0
while count < 5:
    print(count)
    count += 1  # increment count

Output:
0
1
2
3
4

## Handling Zero Division Error

1. When a program encounters a zero divisor, it throws a ZeroDivisionError.
2. To handle this exception and avoid the program from crashing, we use a try-except block.
3. The code that can cause a zero division error is placed inside the try block and the exception handling code is placed in the except block.

Example:
try:
    x = 10 / 0  # can cause zero division error
except ZeroDivisionError:
    print("Cannot divide by zero!")

Output:
Cannot divide by zero!

## Printing Current Time

1. We can use the time module to print the current time.
2. The syntax is:
import time

for i in range(10):
    print(time.ctime())

3. This will print the current time 10 times.