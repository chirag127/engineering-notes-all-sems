## 12. WAP to print the sum of all numbers up to a given number.

Here are some key points to keep in mind while solving this problem:

1. The problem statement asks us to find the sum of all numbers up to a given number. For example, if the given number is 5, then we need to find the sum of 1 + 2 + 3 + 4 + 5, which is 15.

2. We can use a loop to iterate over all the numbers up to the given number and keep adding them to a sum variable.

3. We can start the loop from 1 since we need to find the sum of all numbers, including 1. The loop should continue until the given number.

4. We can use a variable to keep track of the sum and initialize it to 0 before starting the loop.

5. After the loop is complete, we can print the sum variable to get the final answer.

Here is the pseudocode for the solution:

```
sum = 0
for i in range(1, given_number+1):
    sum = sum + i
print(sum)
```

Let's break down the above pseudocode:

1. We initialize a variable `sum` to 0 to keep track of the sum of all numbers.

2. We use a for loop to iterate over all numbers from 1 to the given number (inclusive).

3. Inside the loop, we add the current number (`i`) to the `sum` variable.

4. After the loop is complete, we print the final value of `sum`.

Here is the Python code for the solution:

```python
given_number = int(input("Enter a number: "))
sum = 0
for i in range(1, given_number+1):
    sum = sum + i
print("The sum of all numbers up to", given_number, "is", sum)
```

Note that we have used the `input()` function to get the value of the given number from the user. We have also printed a message along with the final answer to make it more informative.

In conclusion, the problem of finding the sum of all numbers up to a given number can be easily solved using a loop and a sum variable. By following the above steps and using the provided pseudocode or code, you can easily solve this problem.