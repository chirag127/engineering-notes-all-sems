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
- The variables `even_sum` and `odd_sum` are initialized to 0.
- A for loop is used to iterate from 1 to N+1.
- Inside the for loop, an if-else statement is used to check if the current number is even or odd.
- If the current number is even, it is added to the `even_sum` variable.
- If the current number is odd, it is added to the `odd_sum` variable.
- After the for loop, the sum of even and odd numbers is printed.

This program can be used to calculate the sum of even and odd numbers from 1 to any given value of N. It is a simple and efficient way to solve this problem.