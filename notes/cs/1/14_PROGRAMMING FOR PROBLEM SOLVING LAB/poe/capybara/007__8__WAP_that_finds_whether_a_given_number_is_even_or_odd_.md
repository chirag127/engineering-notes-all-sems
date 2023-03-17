## 8. WAP that finds whether a given number is even or odd.

Here are some points to help you understand how to write a program that finds whether a given number is even or odd:

- First, you need to understand what makes a number even or odd. An even number is a number that can be divided by 2 without leaving a remainder. A odd number is a number that cannot be divided by 2 without leaving a remainder.

- In order to write a program that can determine whether a given number is even or odd, you need to use a conditional statement. You can use an "if" statement to check whether the number is divisible by 2 or not.

- Here is a sample code to determine whether a number is even or odd in Python:

```
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

- In this code, the user is prompted to enter a number. The program then checks whether the number is divisible by 2 or not using the modulus operator (%). If the remainder is 0, the number is even, and if the remainder is 1, the number is odd.

- You can also use a ternary operator to write the same code in a more concise way:

```
num = int(input("Enter a number: "))

print("The number is even." if num % 2 == 0 else "The number is odd.")
```

- This code does the same thing as the previous code, but it uses a ternary operator instead of an "if" statement.

- Once you have written your program, you can test it with different input values to make sure it works correctly.