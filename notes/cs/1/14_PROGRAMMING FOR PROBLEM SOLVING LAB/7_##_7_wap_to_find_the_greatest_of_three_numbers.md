## 7. WAP to find the greatest of three numbers.

```
def find_greatest_of_three_numbers(num1, num2, num3):
    greatest = num1
    if num2 > greatest:
        greatest = num2
    if num3 > greatest:
        greatest = num3
    return greatest

print(find_greatest_of_three_numbers(3, 4, 5))
```
