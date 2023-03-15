Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that finds whether a given number is even or odd. Here is the content in markdown format:

## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2, and odd if it is not.
- To check the divisibility by 2, we can use the modulo operator (%) which returns the remainder of a division.
- If the remainder is 0, the number is even, otherwise it is odd.
- Here is an example of a program in Python that finds whether a given number is even or odd:

```python
# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if num % 2 == 0:
  # If yes, print that the number is even
  print(num, "is even.")
else:
  # If no, print that the number is odd
  print(num, "is odd.")
```

- Here is the output of the program for some sample inputs:

```text
Enter a number: 10
10 is even.

Enter a number: 15
15 is odd.

Enter a number: 0
0 is even.
```

- Some points to remember:

  - The modulo operator (%) returns the remainder of a division. For example, 7 % 2 returns 1, and 8 % 2 returns 0.
  - The input() function in Python takes a string as an argument and returns the user input as a string. To convert the input to an integer, we use the int() function.
  - The if-else statement in Python is used to execute a block of code based on a condition. The syntax is:

  ```python
  if condition:
    # code to execute if condition is True
  else:
    # code to execute if condition is False
  ```

  - The indentation (spaces or tabs) in Python is important to define the scope of the code blocks. The code inside the if or else block should be indented by the same amount of spaces or tabs.