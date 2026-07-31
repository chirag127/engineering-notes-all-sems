## 17. WAP to find the sum of digits of the entered number.

To find the sum of digits of the entered number, follow these steps:

1. Initialize a variable `sum` to 0 to store the sum of digits.
2. Take the input number from the user and store it in a variable `num`.
3. Use a while loop to iterate through the digits of the number.
4. In each iteration, find the last digit of the number using the modulus operator (`num % 10`).
5. Add the last digit to the `sum` variable.
6. Remove the last digit from the number by dividing it by 10 (`num = num / 10`).
7. Repeat steps 4-6 until the number becomes 0.
8. Print the value of the `sum` variable.

Here is an example code in Python:

```python
sum = 0
num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("The sum of digits is:", sum)
```

This code takes an input number from the user, and then uses a while loop to iterate through the digits of the number. In each iteration, it finds the last digit using the modulus operator, adds it to the `sum` variable, and then removes the last digit from the number by dividing it by 10. Finally, it prints the value of the `sum` variable.