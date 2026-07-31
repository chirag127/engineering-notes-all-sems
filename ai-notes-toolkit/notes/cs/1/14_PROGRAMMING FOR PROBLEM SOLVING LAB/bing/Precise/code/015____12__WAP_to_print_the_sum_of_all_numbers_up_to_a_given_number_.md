## 12. WAP to print the sum of all numbers up to a given number.

- This problem can be solved using a loop to iterate through all the numbers from 1 to the given number and adding them to a variable that keeps track of the sum.
- The loop can be a for loop or a while loop.
- The loop should start from 1 and end at the given number (inclusive).
- The sum variable should be initialized to 0 before the loop starts.
- Inside the loop, the current number should be added to the sum variable.
- After the loop ends, the sum variable will contain the sum of all the numbers from 1 to the given number.
- The sum can then be printed using a print statement.

Here is an example code in Python that implements the above algorithm:

```python
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of all numbers up to", n, "is", sum)
```

This code prompts the user to enter a number, then calculates the sum of all numbers from 1 to the entered number using a for loop, and finally prints the result. The same algorithm can be implemented using a while loop as well.