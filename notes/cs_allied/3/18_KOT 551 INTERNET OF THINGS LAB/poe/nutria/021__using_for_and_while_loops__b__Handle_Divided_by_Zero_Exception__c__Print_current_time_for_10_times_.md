
#### Using For and While Loops
1. For loops are used to iterate through a sequence of values. For example, the following code will print out the numbers from 0 to 9:
```
for i in range(10):
    print(i)
```

2. While loops are used to execute a set of instructions until a certain condition is met. For example, the following code will print out the numbers from 0 to 9:
```
i = 0
while i < 10:
    print(i)
    i += 1
```

#### Handle Divided by Zero Exception
When dividing a number by zero, a ZeroDivisionError is raised. To handle this exception, we can use a try-except block. For example, the following code will print out the result of the division, or an error message if the divisor is zero:

```
try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Error: Cannot divide by zero.')
```

#### Print Current Time for 10 Times
To print the current time for 10 times, we can use a for loop and the datetime module. For example, the following code will print out the current time for 10 times:

```
from datetime import datetime

for i in range(10):
    print(datetime.now())
```