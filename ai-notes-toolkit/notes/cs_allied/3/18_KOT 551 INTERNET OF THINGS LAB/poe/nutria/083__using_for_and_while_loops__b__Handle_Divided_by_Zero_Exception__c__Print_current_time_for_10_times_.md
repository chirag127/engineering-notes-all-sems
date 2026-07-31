
#### Using For and While Loops

1. For loops are used to iterate through a sequence of values, such as a list or a string. The syntax for a for loop is:

```
for <variable> in <sequence>:
    <statements>
```

2. While loops are used to execute a set of statements until a certain condition is met. The syntax for a while loop is:

```
while <condition>:
    <statements>
```

#### Handling Divided by Zero Exception

When dividing a number by zero, an exception is raised. To handle this exception, the code should include a try-except block. The syntax for a try-except block is:

```
try:
    <statements>
except ZeroDivisionError:
    <statements>
```

#### Printing Current Time for 10 Times

The following code can be used to print the current time for 10 times:

```
import time

for i in range(10):
    current_time = time.strftime("%I:%M:%S %p")
    print(current_time)
```