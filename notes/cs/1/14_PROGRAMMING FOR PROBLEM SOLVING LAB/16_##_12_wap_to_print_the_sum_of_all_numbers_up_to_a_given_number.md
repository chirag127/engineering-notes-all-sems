## 12. WAP to print the sum of all numbers up to a given number.

Here's a sample code in Python to print the sum of all numbers up to a given number:
```
def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

num = int(input("Enter a number: "))
print("Sum of numbers up to", num, "is", sum_of_numbers(num))
```
