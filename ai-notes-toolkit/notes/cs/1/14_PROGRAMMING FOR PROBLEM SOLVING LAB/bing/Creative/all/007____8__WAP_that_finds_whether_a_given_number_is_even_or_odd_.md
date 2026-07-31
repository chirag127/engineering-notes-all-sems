## 8. WAP that finds whether a given number is even or odd.

- A WAP (write a program) is a task that requires writing a computer code that performs a specific function or solves a problem.
- To find whether a given number is even or odd, we need to use a mathematical operation called modulo, which returns the remainder of a division.
- The modulo operator is usually denoted by the symbol `%` in most programming languages.
- If a number is divisible by 2, it means it has no remainder when divided by 2, and therefore it is an even number.
- If a number is not divisible by 2, it means it has some remainder when divided by 2, and therefore it is an odd number.
- To check if a number is even or odd, we can use the following logic:

  - Take a number as input from the user and store it in a variable, say `num`.
  - Calculate the remainder of `num` when divided by 2, using the modulo operator, and store it in another variable, say `rem`.
  - If `rem` is equal to 0, then `num` is an even number, and we can print a message saying so.
  - If `rem` is not equal to 0, then `num` is an odd number, and we can print a message saying so.

- Here is an example of a WAP that finds whether a given number is even or odd, written in Python:

```python
# WAP that finds whether a given number is even or odd

# Take a number as input from the user and store it in a variable, say num
num = int(input("Enter a number: "))

# Calculate the remainder of num when divided by 2, using the modulo operator, and store it in another variable, say rem
rem = num % 2

# If rem is equal to 0, then num is an even number, and we can print a message saying so
if rem == 0:
  print(num, "is an even number.")

# If rem is not equal to 0, then num is an odd number, and we can print a message saying so
else:
  print(num, "is an odd number.")
```

- Here is an example of the output of the WAP, when the user enters 5 as the input:

```
Enter a number: 5
5 is an odd number.
```