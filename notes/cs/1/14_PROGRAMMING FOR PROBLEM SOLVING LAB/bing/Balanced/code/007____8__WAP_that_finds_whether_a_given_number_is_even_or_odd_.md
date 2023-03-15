Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that finds whether a given number is even or odd. Here is the content in markdown format:

## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2, and odd if it is not.
- To check the divisibility by 2, we can use the modulo operator (%) which returns the remainder of the division.
- If the remainder is 0, the number is even, otherwise it is odd.
- Here is an example of a program in Python that finds whether a given number is even or odd:

```python
# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check the remainder of the division by 2
remainder = num % 2

# If the remainder is 0, the number is even
if remainder == 0:
    print(num, "is even.")
# Otherwise, the number is odd
else:
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

- This program can be written in other programming languages as well, using similar logic and syntax.