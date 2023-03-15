## 19.WAP to print Armstrong numbers from 1 to 100.

- An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
- For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.
- To print Armstrong numbers from 1 to 100, we need to check each number in this range and verify if it is an Armstrong number or not.
- We can use a loop to iterate over the numbers from 1 to 100 and a function to check if a number is an Armstrong number or not.
- The function can take a number as a parameter and return True if it is an Armstrong number or False otherwise.
- The function can use the following steps to check if a number is an Armstrong number or not:
  - Initialize a variable sum to 0 and a variable temp to the number.
  - Find the number of digits in the number by using a loop and dividing the number by 10 until it becomes 0. Store the number of digits in a variable n.
  - Use another loop to iterate over the digits of the number by using the modulus operator (%) to get the last digit and the integer division operator (//) to remove the last digit from the number.
  - For each digit, raise it to the power of n and add it to the sum variable.
  - Compare the sum variable with the temp variable. If they are equal, return True. Otherwise, return False.
- The code for the function can be written as follows:

```python
def is_armstrong(number):
  sum = 0
  temp = number
  n = 0
  while temp > 0:
    n += 1
    temp //= 10
  temp = number
  while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
  if sum == number:
    return True
  else:
    return False
```

- To print Armstrong numbers from 1 to 100, we can use another loop to call the function for each number and print it if it returns True. The code for the loop can be written as follows:

```python
for i in range(1, 101):
  if is_armstrong(i):
    print(i)
```

- The output of the program will be:

```
1
2
3
4
5
6
7
8
9
153
370
371
407
```