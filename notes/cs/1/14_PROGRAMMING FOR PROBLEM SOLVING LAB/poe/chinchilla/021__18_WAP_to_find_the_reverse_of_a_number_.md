## 18. WAP to find the reverse of a number

The following points describe how to write a program to find the reverse of a given number:

1. Declare a variable to store the given number and another variable to store the reversed number.
2. Initialize the reversed number variable to zero.
3. Use a loop to extract each digit of the given number from right to left.
4. Append each extracted digit to the reversed number variable by multiplying it with 10 and adding it to the existing reversed number.
5. Continue the loop until all the digits of the given number have been extracted and appended to the reversed number variable.
6. Print the reversed number variable as the output.

Here is the code for the program:

```python
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse of the given number:", rev)
```

This program takes the input number from the user and uses a while loop to extract each digit of the number and append it to the reversed number variable. The loop continues until all the digits have been extracted and appended, and then the reversed number is printed as the output.

Note: The above program assumes that the input number is a positive integer. If the input number can be negative or contain decimal places, additional code may be required to handle these cases.