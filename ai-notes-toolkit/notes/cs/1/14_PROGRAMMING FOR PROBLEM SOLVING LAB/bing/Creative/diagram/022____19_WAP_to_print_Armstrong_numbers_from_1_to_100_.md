Hello, I am Sydney, your AI assistant. I can help you with any topic.

Here is the content for the topic ## 19.WAP to print Armstrong numbers from 1 to 100.

An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.

To print Armstrong numbers from 1 to 100, we can use the following algorithm:

- Initialize a variable `num` to 1.
- Repeat the following steps until `num` is greater than 100:
  - Initialize a variable `sum` to 0.
  - Initialize a variable `temp` to `num`.
  - Repeat the following steps until `temp` is 0:
    - Find the remainder of `temp` divided by 10 and store it in a variable `digit`.
    - Add `digit` cubed to `sum`.
    - Divide `temp` by 10 and update its value.
  - If `sum` is equal to `num`, print `num` as an Armstrong number.
  - Increment `num` by 1.

Here is the code for the algorithm in Python:

```python
# WAP to print Armstrong numbers from 1 to 100
num = 1 # initialize num to 1
while num <= 100: # repeat until num is greater than 100
  sum = 0 # initialize sum to 0
  temp = num # initialize temp to num
  while temp > 0: # repeat until temp is 0
    digit = temp % 10 # find the remainder of temp divided by 10
    sum += digit ** 3 # add digit cubed to sum
    temp //= 10 # divide temp by 10 and update its value
  if sum == num: # if sum is equal to num
    print(num, "is an Armstrong number") # print num as an Armstrong number
  num += 1 # increment num by 1
```