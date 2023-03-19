## 16.WAP to check whether the entered number is prime or not.

To check whether a given number is prime or not, we can use the following steps:

1. Take an input from the user for the number to be checked.

2. Create a variable 'flag' and initialize it to 0.

3. Use a for loop to iterate over all the numbers from 2 to the square root of the given number.

4. For each number, check if it is a factor of the given number. If it is, set the flag variable to 1 and break out of the loop.

5. After the loop, check the value of the flag variable. If it is still 0, then the given number is a prime number. Otherwise, it is not.

6. Print the result to the user.

Here is the sample code in Python:

```
num = int(input("Enter a number: "))
flag = 0

for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        flag = 1
        break

if flag == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
```

Note: 
- A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.
- It is important to check only up to the square root of the given number because any factor greater than the square root would have a corresponding factor less than the square root.