## 6. WAP that checks whether the two numbers entered by the user are equal or not.

- A WAP (write a program) is a task that requires writing a computer code that performs a specific function or solves a problem.
- To check whether the two numbers entered by the user are equal or not, the WAP needs to do the following steps:
  - Take input from the user for two numbers, say `a` and `b`.
  - Compare the values of `a` and `b` using the `==` operator, which returns `True` if they are equal and `False` otherwise.
  - Print the result of the comparison on the screen.
- An example of a WAP that checks whether the two numbers entered by the user are equal or not in Python is:

```python
# Take input from the user for two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Compare the values of a and b using the == operator
result = (a == b)

# Print the result of the comparison on the screen
print("The two numbers are equal:", result)
```

- An example of the output of the WAP for different inputs is:

```
Enter the first number: 10
Enter the second number: 10
The two numbers are equal: True
```

```
Enter the first number: 5
Enter the second number: 7
The two numbers are equal: False
```