
## 19.WAP to print Armstrong numbers from 1 to 100.

1. An Armstrong number is a number such that the sum of its digits raised to the third power is equal to the number itself.

2. For example, 153 is an Armstrong number, because 1^3 + 5^3 + 3^3 = 153.

3. To print Armstrong numbers from 1 to 100, we can use a loop to iterate through all numbers from 1 to 100.

4. Within the loop, we can check if each number is an Armstrong number using the following algorithm:

- Initialize a variable `sum` to 0.
- Extract each digit of the number and raise it to the third power.
- Add the result to the `sum` variable.
- If the `sum` is equal to the number, then it is an Armstrong number.

5. The following is an example of code that prints Armstrong numbers from 1 to 100:

```
for i in range(1, 101):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if i == sum:
        print(i)
```