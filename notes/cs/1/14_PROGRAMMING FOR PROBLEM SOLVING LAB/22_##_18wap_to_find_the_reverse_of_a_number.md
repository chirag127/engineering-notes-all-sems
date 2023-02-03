## 18.WAP to find the reverse of a number.

Here's a simple code to find the reverse of a number in Python:
```
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    last_digit = number % 10
    reverse = (reverse * 10) + last_digit
    number = number // 10
print("Reverse of the number is:", reverse)
```
