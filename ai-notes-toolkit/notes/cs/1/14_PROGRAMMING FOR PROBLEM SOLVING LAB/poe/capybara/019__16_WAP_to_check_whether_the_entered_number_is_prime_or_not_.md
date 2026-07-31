## WAP to check whether the entered number is prime or not.

To determine whether a given number is prime or not is an important concept in mathematics. Prime numbers are those numbers that are only divisible by 1 and themselves. In this article, we will discuss how to write a program in Python to check whether the entered number is prime or not.

Here are the steps to check whether a number is prime or not:

1. First, we need to take the input from the user. We can use the input() function in Python to take input from the user.

2. Next, we need to convert the input into an integer. We can use the int() function in Python to convert the input into an integer.

3. Now, we need to check whether the entered number is greater than 1 or not. If the number is less than or equal to 1, it is not a prime number.

4. If the number is greater than 1, we need to check whether it is divisible by any number other than 1 and itself. We can use a for loop to check this.

5. Inside the for loop, we need to check whether the number is divisible by the current number in the loop. If it is divisible, we can break out of the loop and print that the number is not prime.

6. If the loop completes without finding a divisor, we can print that the number is prime.

Here is the Python code to check whether a number is prime or not:

```
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
```

In conclusion, checking whether a given number is prime or not is an important concept in mathematics. By following the above steps and using the Python code provided, you can easily determine whether a number is prime or not.