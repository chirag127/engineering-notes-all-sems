## 17. WAP to find the sum of digits of the entered number.

1. To find the sum of digits of a number, we can use a while loop to iterate through each digit of the number.
2. First, initialize a variable to store the sum of the digits, for example `sum = 0`.
3. Then, use a while loop to iterate through each digit of the number. In each iteration, use the modulo operator `%` to obtain the last digit of the number, add it to the sum, and then remove the last digit from the number by dividing it by 10.
4. Continue this process until the number becomes 0.
5. The final value of the `sum` variable will be the sum of the digits of the entered number.

Here is an example of the code in Python:

```python
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("The sum of the digits is:", sum)
```

This code prompts the user to enter a number, and then uses a while loop to calculate the sum of its digits. The result is then printed to the screen.