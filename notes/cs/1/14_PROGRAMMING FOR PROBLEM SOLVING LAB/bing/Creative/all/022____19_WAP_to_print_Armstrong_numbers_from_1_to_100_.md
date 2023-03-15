## 19.WAP to print Armstrong numbers from 1 to 100.

An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.

To write a program to print Armstrong numbers from 1 to 100, we can follow these steps:

- Initialize a variable `num` to 1.
- Start a loop that runs until `num` is less than or equal to 100.
  - Initialize a variable `sum` to 0.
  - Initialize a variable `temp` to `num`.
  - Start another loop that runs until `temp` is not zero.
    - Find the remainder of `temp` divided by 10 and store it in a variable `digit`.
    - Add `digit` raised to the power of 3 to `sum`.
    - Divide `temp` by 10 and update its value.
  - End the inner loop.
  - Check if `sum` is equal to `num`.
    - If yes, print `num` as an Armstrong number.
  - Increment `num` by 1.
- End the outer loop.

Here is an example of the program in Python:

```python
# WAP to print Armstrong numbers from 1 to 100

num = 1 # initialize num to 1

while num <= 100: # loop until num is less than or equal to 100
  sum = 0 # initialize sum to 0
  temp = num # initialize temp to num
  while temp > 0: # loop until temp is not zero
    digit = temp % 10 # find the remainder of temp divided by 10
    sum += digit ** 3 # add digit raised to the power of 3 to sum
    temp //= 10 # divide temp by 10 and update its value
  if sum == num: # check if sum is equal to num
    print(num, "is an Armstrong number") # print num as an Armstrong number
  num += 1 # increment num by 1
```