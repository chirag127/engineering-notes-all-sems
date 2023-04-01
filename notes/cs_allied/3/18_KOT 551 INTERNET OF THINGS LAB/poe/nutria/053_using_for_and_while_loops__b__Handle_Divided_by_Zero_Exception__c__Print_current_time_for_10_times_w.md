

# Using For and While Loops

1. For loops are used to execute a set of statements multiple times, until a certain condition is met. They are typically used when the number of iterations is known beforehand.

2. While loops are used to execute a set of statements multiple times, until a certain condition is met. They are typically used when the number of iterations is unknown beforehand.

3. To handle divided by zero exceptions, the programmer should check for any division operations within the loop and ensure that the denominator is not zero.

4. To print the current time for 10 times, the programmer can use the `time.strftime()` function to get the current time, and a `for` loop to print it 10 times. For example:

```
for i in range(10):
    print(time.strftime("%H:%M:%S"))
```