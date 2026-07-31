## 15. WAP to print the Fibonacci series.

The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. This sequence is widely used in mathematics and computer science, and can be generated using a simple algorithm.

Here is a program in Python to print the Fibonacci series:

```python
# Program to print the Fibonacci series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(a)
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(a)
       c = a + b
       a = b
       b = c
```

Let's break down the code into its individual parts:

1. We first ask the user to input the number of terms they want in the Fibonacci series.
2. We then initialize the first two terms of the series to 0 and 1 respectively.
3. We then check if the number of terms entered by the user is less than or equal to 0. If it is, we print a message asking the user to enter a positive integer. If the number of terms is 1, we simply print the first term of the series and exit the program.
4. If the number of terms is greater than 1, we print the Fibonacci series using a loop. The loop runs 'n' times, where 'n' is the number of terms entered by the user. Inside the loop, we first print the current term 'a', and then calculate the next term 'c' as the sum of the previous two terms 'a' and 'b'. We then update the values of 'a' and 'b' to prepare for the next iteration of the loop.

By running this program, you should be able to generate the Fibonacci series up to the number of terms specified by the user. This program can be easily modified to print the series using different starting terms or to generate the series recursively.