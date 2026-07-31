## 12. WAP to print the sum of all numbers up to a given number.

- This program can be written in many programming languages such as C, C++, Java, Python, etc.
- The program takes a number as input from the user.
- The program then calculates the sum of all numbers from 1 to the given number.
- The sum can be calculated using a loop or using the formula `n*(n+1)/2`, where `n` is the given number.
- The program then prints the calculated sum.

Here is an example of the program written in Python:

```python
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of all numbers up to", n, "is", sum)
```

This program takes a number as input from the user, calculates the sum of all numbers from 1 to the given number using a loop, and then prints the calculated sum. Another way to calculate the sum is by using the formula `n*(n+1)/2`, as shown below:

```python
n = int(input("Enter a number: "))
sum = n*(n+1)//2
print("The sum of all numbers up to", n, "is", sum)
```

This program takes a number as input from the user, calculates the sum of all numbers from 1 to the given number using the formula `n*(n+1)/2`, and then prints the calculated sum. Both programs produce the same result. The choice of method depends on the programmer's preference and the requirements of the program.