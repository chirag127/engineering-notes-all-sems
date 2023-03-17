## 12. WAP to print the sum of all numbers up to a given number.

Below are the steps to write a program in Python to print the sum of all numbers up to a given number:

1. First, we need to take input from the user for a number up to which the sum needs to be calculated.

2. To take input from the user, we can use the input() function in Python.

3. We need to convert the input string to an integer using the int() function.

4. Next, we need to initialize a variable 'sum' to 0. This variable will store the sum of all numbers up to the given number.

5. We will then use a loop to iterate through all the numbers from 1 to the given number.

6. Inside the loop, we will add the current number to the 'sum' variable.

7. Once the loop is complete, we will print the value of the 'sum' variable.

Below is the Python code to print the sum of all numbers up to a given number:

```python
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num+1):
    sum += i

print("The sum of all numbers up to", num, "is", sum)
```

This program will take input from the user for a number up to which the sum needs to be calculated. It will then calculate the sum of all numbers up to the given number and print the result. This program can be used to solve problems that require the calculation of the sum of all numbers up to a certain number, such as finding the sum of all even numbers up to a given number.