## 9. WAP that tells whether a given year is a leap year or not.

To determine whether a given year is a leap year or not, we can use the following algorithm:

1. Take the year as input from the user.
2. Check if the year is divisible by 4. If it is not divisible by 4, it is not a leap year. If it is divisible by 4, go to step 3.
3. Check if the year is divisible by 100. If it is divisible by 100, go to step 4. If it is not divisible by 100, it is a leap year.
4. Check if the year is divisible by 400. If it is divisible by 400, it is a leap year. If it is not divisible by 400, it is not a leap year.

Here is a sample Python code that implements the above algorithm:

```python
year = int(input("Enter the year: "))

if year % 4 != 0:
    print(year, "is not a leap year.")
elif year % 100 != 0:
    print(year, "is a leap year.")
elif year % 400 != 0:
    print(year, "is not a leap year.")
else:
    print(year, "is a leap year.")
```

In this code, we first take the year as input from the user using the `input()` function. We then check if the year is divisible by 4 using the modulo operator `%`. If it is not divisible by 4, we print a message saying that it is not a leap year. If it is divisible by 4, we check if it is divisible by 100 and 400 using similar modulo checks. If it is not divisible by 100, it is a leap year. If it is divisible by 100, we check if it is divisible by 400. If it is divisible by 400, it is a leap year. If it is not divisible by 400, it is not a leap year.

This algorithm correctly determines whether a given year is a leap year or not, as per the rules of the Gregorian calendar.