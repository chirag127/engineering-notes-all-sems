#### Using For and While Loops

- For loops are used to iterate over a sequence of items, whereas while loops are used to repeatedly execute a block of code as long as a certain condition is true.

- The syntax for a for loop is as follows:
```
for variable in sequence:
    # code to be executed
```

- The syntax for a while loop is as follows:
```
while condition:
    # code to be executed
```

- It is important to ensure that the condition in a while loop will eventually become false, otherwise the loop will run indefinitely.

- For loops can be used to iterate over a range of numbers using the `range()` function. For example:
```
for i in range(5):
    print(i)
```
This will print the numbers 0, 1, 2, 3, and 4.

- While loops can be used to repeatedly execute a block of code until a certain condition is met. For example:
```
count = 0
while count < 5:
    print(count)
    count += 1
```
This will print the numbers 0, 1, 2, 3, and 4.

#### Handling Divided by Zero Exception

- Dividing by zero is not allowed in mathematics, and attempting to do so in programming will result in a ZeroDivisionError.

- To handle this exception, we can use a try-except block. For example:
```
try:
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero")
```
This will catch the ZeroDivisionError and print a message instead of crashing the program.

#### Printing Current Time for 10 Times with an

- To print the current time for 10 times, we can use a for loop and the `datetime` module. For example:
```
import datetime

for i in range(10):
    now = datetime.datetime.now()
    print("Current time:", now)
```
This will print the current time 10 times, with each time in the format "Current time: [time]".