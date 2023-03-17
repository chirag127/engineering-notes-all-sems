## 7. WAP to find the greatest of three numbers.

To find the greatest of three numbers, we can use the following steps:

1. Take input of three numbers from the user.
2. Compare the first two numbers and store the greater one in a temporary variable.
3. Compare the third number with the temporary variable and store the greater one in the same variable.
4. The value of the temporary variable now holds the greatest of the three numbers.
5. Print the value of the temporary variable as the output.

Here is the python code to implement the above steps:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2:
    temp = num1
else:
    temp = num2
    
if num3 > temp:
    temp = num3
    
print("The greatest number is ", temp)
```

In the above code, we take input of three numbers from the user using the `input()` function and convert them to integers using the `int()` function. 

We then compare the first two numbers using an `if-else` statement and store the greater one in a temporary variable `temp`. 

Next, we compare the third number with `temp` using another `if` statement and if the third number is greater than `temp`, we update the value of `temp` to hold the greatest of the three numbers. 

Finally, we print the value of `temp` as the output using the `print()` function.

This code can be used to find the greatest of three numbers in Python.