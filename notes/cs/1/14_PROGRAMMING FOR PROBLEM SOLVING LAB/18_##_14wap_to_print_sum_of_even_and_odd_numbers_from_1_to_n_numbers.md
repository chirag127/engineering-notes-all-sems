## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

Here's one way to write the program in Python:

```
def sum_even_odd(n):
    even_sum = 0
    odd_sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum

n = int(input("Enter a number: "))
even_sum, odd_sum = sum_even_odd(n)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
```
