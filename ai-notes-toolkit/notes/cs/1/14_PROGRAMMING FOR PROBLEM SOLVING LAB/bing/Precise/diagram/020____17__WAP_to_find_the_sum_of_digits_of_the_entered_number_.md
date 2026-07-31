## 17. WAP to find the sum of digits of the entered number.

1. To find the sum of digits of a number, we can use a while loop to iterate through each digit of the number.
2. We can use the modulo operator (%) to obtain the last digit of the number and add it to a variable that keeps track of the sum of the digits.
3. We can then use integer division (//) to remove the last digit from the number and continue the loop until the number becomes 0.
4. The final value of the variable that keeps track of the sum of the digits will be the sum of all the digits of the entered number.

Here is an example of a Python program that implements this algorithm:

```python
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10
print("The sum of digits of the entered number is:", sum_of_digits)
```

This program prompts the user to enter a number, then uses a while loop to iterate through each digit of the number and add it to the `sum_of_digits` variable. Finally, it prints the sum of the digits of the entered number.