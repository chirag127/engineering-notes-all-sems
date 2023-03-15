## 14. WAP to print sum of even and odd numbers from 1 to N numbers.

Here is a program that calculates the sum of even and odd numbers from 1 to N numbers:

```python
N = int(input("Enter the value of N: "))

even_sum = 0
odd_sum = 0

for i in range(1, N+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
```

This program takes the value of N as input from the user. It then initializes two variables, `even_sum` and `odd_sum`, to store the sum of even and odd numbers respectively.

The program then uses a for loop to iterate over the range of numbers from 1 to N. For each number, it checks if the number is even by checking if the remainder when the number is divided by 2 is equal to 0. If the number is even, it is added to the `even_sum` variable. Otherwise, it is added to the `odd_sum` variable.

After the loop is completed, the program prints the sum of even and odd numbers.