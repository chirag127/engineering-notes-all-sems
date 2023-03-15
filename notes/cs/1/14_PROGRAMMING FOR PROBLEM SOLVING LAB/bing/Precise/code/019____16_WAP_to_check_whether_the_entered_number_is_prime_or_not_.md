## 16. WAP to check whether the entered number is prime or not.

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. In other words, it is a number that is only divisible by 1 and itself. To check whether a number is prime or not, we can follow these steps:

1. Take input from the user and store it in a variable.
2. Initialize a flag variable to 0.
3. Run a loop from 2 to the square root of the entered number.
4. Check if the entered number is divisible by the current value of the loop variable.
5. If it is divisible, set the flag variable to 1 and break the loop.
6. After the loop, check the value of the flag variable.
7. If the flag variable is 0, the entered number is prime. Otherwise, it is not prime.

Here is an example code in Python that implements the above algorithm:

```python
num = int(input("Enter a number: "))
flag = 0

for i in range(2, int(num**(0.5))+1):
    if num % i == 0:
        flag = 1
        break

if flag == 0:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
```

This code takes a number as input from the user and checks whether it is prime or not using the above algorithm. If the entered number is prime, it prints that the number is prime. Otherwise, it prints that the number is not prime.