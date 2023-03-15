## 17. WAP to find the sum of digits of the entered number.

1. Start by initializing a variable `sum` to 0. This variable will be used to store the sum of the digits of the entered number.
2. Take the input number from the user and store it in a variable `num`.
3. Use a `while` loop to iterate through the digits of the number. The loop should continue until the value of `num` becomes 0.
4. In each iteration of the loop, find the last digit of the number by taking the remainder of the number when divided by 10. This can be done using the modulo operator (`%`).
5. Add the value of the last digit to the `sum` variable.
6. Remove the last digit from the number by dividing it by 10 and taking the integer part of the result. This can be done using the integer division operator (`//`).
7. Repeat steps 4-6 until the value of `num` becomes 0.
8. After the loop ends, the value of the `sum` variable will be the sum of the digits of the entered number.
9. Print the value of the `sum` variable to display the result.

Here is an example implementation of the above algorithm in Python:

```python
sum = 0
num = int(input("Enter a number: "))

while num > 0:
    last_digit = num % 10
    sum += last_digit
    num = num // 10

print("The sum of the digits is:", sum)
```