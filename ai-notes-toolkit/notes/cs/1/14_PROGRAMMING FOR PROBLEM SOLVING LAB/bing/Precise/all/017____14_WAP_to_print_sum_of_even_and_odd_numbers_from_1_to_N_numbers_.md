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

- The program prompts the user to enter the value of N.
- Two variables, `even_sum` and `odd_sum`, are initialized to 0 to store the sum of even and odd numbers, respectively.
- A for loop is used to iterate over the range of numbers from 1 to N.
- Inside the loop, an if-else statement is used to check if the current number is even or odd.
- If the number is even, it is added to the `even_sum` variable. Otherwise, it is added to the `odd_sum` variable.
- After the loop, the sum of even and odd numbers is printed.

This program can be used to calculate the sum of even and odd numbers from 1 to any given value of N. It can be modified to perform other calculations as well.