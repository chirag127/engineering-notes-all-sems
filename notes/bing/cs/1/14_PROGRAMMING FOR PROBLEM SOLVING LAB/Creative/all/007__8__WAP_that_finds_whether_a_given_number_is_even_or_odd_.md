## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2 without any remainder. A number is odd if it is not divisible by 2 or has a remainder of 1 when divided by 2.
- To write a program that finds whether a given number is even or odd, we can use the modulo operator (%) which returns the remainder of a division operation. For example, 5 % 2 returns 1, and 6 % 2 returns 0.
- The modulo operator can be used in a conditional statement to check if the remainder is 0 or 1, and print the appropriate message accordingly. For example, in Python, we can write:

```python
# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd using modulo operator
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
```

- The output of the program will depend on the input given by the user. For example, if the user enters 10, the output will be:

```
Enter a number: 10
10 is even.
```

- If the user enters 15, the output will be:

```
Enter a number: 15
15 is odd.
```

- A mnemonic to remember the modulo operator is to think of it as a clock. The clock has 12 hours, and when we go past 12, we start from 0 again. Similarly, when we divide a number by 12, the remainder will be the same as the hour on the clock. For example, 17 % 12 is 5, which is the same as 5 o'clock. The modulo operator can be used to find the remainder of any division, not just by 2 or 12. For example, 23 % 7 is 2, which means 23 divided by 7 has a remainder of 2.