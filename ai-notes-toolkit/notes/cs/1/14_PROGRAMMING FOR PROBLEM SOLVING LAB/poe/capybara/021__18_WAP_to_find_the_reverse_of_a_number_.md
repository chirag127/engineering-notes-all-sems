## 18. WAP to find the reverse of a number.

To find the reverse of a number, we need to follow the below steps:

1. Take the input number from the user.
2. Initialize a variable to store the reverse of the number.
3. Using a loop, we can reverse the number.
4. In each iteration, we can get the last digit of the input number using the modulo (%) operator.
5. Append the last digit to the reverse number variable.
6. Divide the input number by 10 to remove the last digit.
7. Repeat steps 4-6 until the input number becomes 0.
8. Print the reverse number.

Below is the Python code to find the reverse of a number:

```python
num = int(input("Enter a number: ")) # input number
reverse = 0 # variable to store reverse of the number

while(num > 0):
    last_digit = num % 10 # get the last digit
    reverse = (reverse * 10) + last_digit # append the last digit to reverse
    num = num // 10 # remove the last digit

print("Reverse of the number:", reverse) # print the reverse number
```

In the above code, we have used a while loop to reverse the number. We have used the modulo operator to get the last digit of the number and the integer division operator (//) to remove the last digit. Then we have appended the last digit to the reverse variable and multiplied it by 10 to shift the digits to the left.

By following the above steps, we can easily find the reverse of any given number.