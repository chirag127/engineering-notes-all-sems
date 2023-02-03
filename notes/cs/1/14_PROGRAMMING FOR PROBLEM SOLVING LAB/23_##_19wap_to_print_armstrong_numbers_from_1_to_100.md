## 19.WAP to print Armstrong numbers from 1 to 100.

Here's an example of a Python function to print Armstrong numbers from 1 to 100:

```
def is_armstrong(num):
    # Calculate the sum of cubes of individual digits
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == num

for i in range(1, 101):
    if is_armstrong(i):
        print(i)
```
