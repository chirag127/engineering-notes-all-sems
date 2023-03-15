## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

Here is an example of a program that can be used to print the sum of even and odd numbers from 1 to N numbers:

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

- The program starts by taking the value of N as input from the user.
- Two variables, `even_sum` and `odd_sum`, are initialized to 0 to store the sum of even and odd numbers respectively.
- A for loop is used to iterate over the range of numbers from 1 to N.
- Inside the loop, an if-else statement is used to check if the current number is even or odd.
- If the number is even, it is added to the `even_sum` variable. Otherwise, it is added to the `odd_sum` variable.
- After the loop is completed, the final values of `even_sum` and `odd_sum` are printed to display the sum of even and odd numbers respectively.

This program can be modified according to the specific requirements of the user. For example, the range of numbers can be changed, or the program can be modified to only print the sum of even or odd numbers.