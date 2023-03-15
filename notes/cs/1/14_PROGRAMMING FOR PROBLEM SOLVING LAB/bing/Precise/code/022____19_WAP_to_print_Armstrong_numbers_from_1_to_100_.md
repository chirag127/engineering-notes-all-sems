## 19. WAP to print Armstrong numbers from 1 to 100

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.

Here is a program in Python that prints all Armstrong numbers from 1 to 100:

```python
for num in range(1, 101):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num)
```

This program uses a for loop to iterate over the numbers from 1 to 100. For each number, it calculates the sum of the cubes of its digits using a while loop. If the sum is equal to the number, it is an Armstrong number and is printed.
