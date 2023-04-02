
# Using For and While Loops
For and while loops are programming structures used to execute a set of instructions repeatedly. 

## For Loops
A for loop is used to iterate over a sequence of items. The syntax of a for loop is as follows:

```
for item in sequence:
  # Execute instructions
```

The instructions within the loop are executed once for each item in the sequence.

## While Loops
A while loop is used to execute instructions as long as a certain condition is true. The syntax of a while loop is as follows:

```
while condition:
  # Execute instructions
```

The instructions within the loop are executed repeatedly until the condition is no longer true.

## Handling Divided by Zero Exceptions
When a program attempts to divide by zero, a divided by zero exception is raised. This exception must be handled in order to ensure the program does not crash.

The following code snippet shows how to handle a divided by zero exception using a try-except block:

```
try:
  # Execute instructions that may result in a divided by zero
except ZeroDivisionError:
  # Execute instructions to handle the exception
```

The instructions within the try block are attempted to be executed. If a divided by zero exception is raised, the instructions within the except block are executed instead.

## Printing Current Time
The following code snippet shows how to print the current time for 10 times using a for loop:

```
import time

for i in range(10):
  print(time.asctime())
```

The code prints the current time (in a human-readable format) 10 times.