## 19.WAP to print Armstrong numbers from 1 to 100.

An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.

To write a program to print Armstrong numbers from 1 to 100, we can follow these steps:

- Initialize a variable n to store the current number, and set it to 1.
- Initialize a variable sum to store the sum of the digits raised to the power of the number of digits, and set it to 0.
- Initialize a variable temp to store a copy of the current number, and set it to n.
- Initialize a variable count to store the number of digits, and set it to 0.
- Repeat the following steps until temp is not equal to 0:
  - Increment count by 1.
  - Divide temp by 10 and store the result in temp.
- Assign n to temp again.
- Repeat the following steps until temp is not equal to 0:
  - Find the remainder of temp divided by 10 and store it in a variable digit.
  - Calculate digit raised to the power of count and add it to sum.
  - Divide temp by 10 and store the result in temp.
- If sum is equal to n, print n as an Armstrong number.
- Increment n by 1.
- If n is less than or equal to 100, go back to step 2.

The code for the program in Python is:

```python
# WAP to print Armstrong numbers from 1 to 100

n = 1 # initialize n to store the current number
while n <= 100: # loop until n is 100 or less
  sum = 0 # initialize sum to store the sum of the digits raised to the power of the number of digits
  temp = n # initialize temp to store a copy of the current number
  count = 0 # initialize count to store the number of digits
  while temp != 0: # loop until temp is 0
    count += 1 # increment count by 1
    temp //= 10 # divide temp by 10 and store the result in temp
  temp = n # assign n to temp again
  while temp != 0: # loop until temp is 0
    digit = temp % 10 # find the remainder of temp divided by 10 and store it in digit
    sum += digit ** count # calculate digit raised to the power of count and add it to sum
    temp //= 10 # divide temp by 10 and store the result in temp
  if sum == n: # if sum is equal to n
    print(n, "is an Armstrong number") # print n as an Armstrong number
  n += 1 # increment n by 1
```