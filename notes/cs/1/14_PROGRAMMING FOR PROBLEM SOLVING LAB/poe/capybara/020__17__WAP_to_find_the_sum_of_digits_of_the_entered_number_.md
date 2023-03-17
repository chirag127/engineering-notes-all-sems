## 17. WAP to find the sum of digits of the entered number

To find the sum of digits of a given number, we can use the following algorithm:

1. Start
2. Declare variables 'num', 'sum' and 'digit'
3. Read the value of 'num'
4. Initialize 'sum' to 0
5. Repeat steps 6-7 until 'num' > 0
6. Find the last digit of 'num' and store it in 'digit'
7. Add 'digit' to 'sum' and remove the last digit of 'num'
8. Print the value of 'sum'
9. Stop

Let's see an example code to implement the above algorithm in Python:

```python
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Sum of digits:", sum)
```

Input:
```
Enter a number: 12345
```

Output:
```
Sum of digits: 15
```

Explanation:
The given number is 12345. We are finding the sum of digits using the above algorithm. The last digit of the number is 5, so we add it to the sum. Then, we remove the last digit of the number and it becomes 1234. The last digit of the new number is 4, so we add it to the sum. We repeat this process until the number becomes 0. Finally, we print the sum of digits which is 15.

In conclusion, we can use the above algorithm to find the sum of digits of any given number. The implementation can be done in any programming language of our choice.