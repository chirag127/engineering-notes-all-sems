## 19.WAP to print Armstrong numbers from 1 to 100.

- An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
- For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.
- To print Armstrong numbers from 1 to 100, we need to check each number in this range and verify if it is an Armstrong number or not.
- We can use a loop to iterate over the numbers from 1 to 100 and a function to check if a number is an Armstrong number or not.
- The function can take a number as a parameter and return True if it is an Armstrong number or False otherwise.
- The function can use the following steps to check if a number is an Armstrong number or not:
  - Initialize a variable sum to 0 and a variable temp to store the original number.
  - Find the number of digits in the number by using the len() function on the string representation of the number.
  - Use a while loop to iterate over the digits of the number by using the modulo (%) and floor division (//) operators.
  - For each digit, raise it to the power of the number of digits and add it to the sum variable.
  - Compare the sum variable with the original number and return True if they are equal or False otherwise.
- The code for the function can be written as follows:

```python
def is_armstrong(number):
  sum = 0
  temp = number
  digits = len(str(number))
  while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10
  return sum == number
```

- The code for the loop can be written as follows:

```python
for i in range(1, 101):
  if is_armstrong(i):
    print(i)
```

- The output of the code will be:

```text
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
```