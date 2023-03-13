## 7. WAP to find the greatest of three numbers.

- WAP stands for Write a Program.
- To find the greatest of three numbers, we need to compare them using some logical operators, such as `>`, `<`, `==`, etc.
- We can use `if-else` statements to execute different blocks of code based on the result of the comparison.
- We can also use nested `if-else` statements to check multiple conditions in a sequence.
- Here is an example of a program in Python that finds the greatest of three numbers:

```python
# Take three numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Compare the first and second numbers
if num1 > num2:
  # Compare the first and third numbers
  if num1 > num3:
    # The first number is the greatest
    print(num1, "is the greatest of the three numbers.")
  else:
    # The third number is the greatest
    print(num3, "is the greatest of the three numbers.")
else:
  # Compare the second and third numbers
  if num2 > num3:
    # The second number is the greatest
    print(num2, "is the greatest of the three numbers.")
  else:
    # The third number is the greatest
    print(num3, "is the greatest of the three numbers.")
```