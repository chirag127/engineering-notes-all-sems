#### Using For and While Loops

When it comes to programming, loops are an important concept that you will come across time and again. They allow you to repeat a set of instructions multiple times without having to write the same code over and over again. In this topic, we will discuss how to use for and while loops in your program.

##### For Loops

For loops are used to iterate over a sequence of elements such as a list, tuple, or string. The basic syntax of a for loop is as follows:

```
for variable in sequence:
    # code to be executed
```

Here, the `variable` represents the current element in the sequence, while the `sequence` is the list, tuple or string that you want to iterate over.

##### While Loops

While loops, on the other hand, are used to execute a block of code repeatedly as long as the specified condition is true. The basic syntax of a while loop is as follows:

```
while condition:
    # code to be executed
```

Here, the `condition` is a boolean expression that is evaluated before each iteration. If the condition is true, the code inside the loop is executed. This process continues until the condition becomes false.

##### Handling Divided by Zero Exception

Dividing by zero is an error in programming that can cause your program to crash. To handle this error, you can use a try-except block. The code inside the try block is executed, and if an exception occurs, the code inside the except block is executed.

```
try:
    # code that may raise an exception
except ZeroDivisionError:
    # code to handle the exception
```

In this case, if the code inside the try block raises a ZeroDivisionError, the code inside the except block is executed.

##### Printing Current Time for 10 Times

To print the current time for 10 times, you can use a for loop along with the `datetime` module in Python. The `datetime.now()` function returns the current date and time.

```
import datetime

for i in range(10):
    current_time = datetime.datetime.now()
    print("Current Time:", current_time)
```

Here, the `range(10)` function creates a sequence of numbers from 0 to 9, and the for loop iterates over this sequence 10 times. Inside the loop, the current time is printed using the `datetime.now()` function.

In conclusion, understanding how to use for and while loops is an essential skill for any programmer. Additionally, being able to handle exceptions and print the current time can enhance the functionality and usability of your programs.