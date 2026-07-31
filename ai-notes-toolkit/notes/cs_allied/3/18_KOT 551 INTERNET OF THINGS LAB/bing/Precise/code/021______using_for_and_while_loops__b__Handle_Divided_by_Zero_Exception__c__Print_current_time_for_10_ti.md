#### Using For and While Loops
- For loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable object.
- The syntax for a for loop is: `for variable in sequence: statements`
- While loops are used to repeatedly execute a block of code as long as a condition is true.
- The syntax for a while loop is: `while condition: statements`

#### Handle Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and will result in an error in most programming languages.
- In Python, attempting to divide by zero will raise a `ZeroDivisionError`.
- This error can be handled using a try-except block.
- The syntax for handling a ZeroDivisionError is:
```
try:
    # code that may raise a ZeroDivisionError
except ZeroDivisionError:
    # code to handle the error
```

#### Print Current Time for 10 Times with an Interval
- The `time` module in Python provides various time-related functions, including the `time()` function which returns the current time in seconds since the epoch.
- The `ctime()` function in the `time` module can be used to convert the time in seconds to a human-readable string.
- The `sleep()` function in the `time` module can be used to pause the execution of the program for a specified number of seconds.
- To print the current time for 10 times with an interval, the following code can be used:
```
import time

for i in range(10):
    print(time.ctime())
    time.sleep(1) # pause for 1 second
```