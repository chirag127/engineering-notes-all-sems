## 9. WAP that tells whether a given year is a leap year or not.

A leap year is a year that has 366 days instead of the usual 365 days. It occurs every 4 years to account for the extra 0.25 day in the Earth's orbit around the sun. To determine whether a given year is a leap year or not, the following conditions must be met:

1. The year must be divisible by 4.
2. The year must not be divisible by 100, except if it is also divisible by 400.

With these conditions in mind, we can write a Python program to determine whether a given year is a leap year or not. Here's how:

```python
year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```

Let's break down the code:

1. We first ask the user to enter a year using the `input()` function. Since the input is a string, we convert it to an integer using the `int()` function and store it in a variable called `year`.
2. We then use an `if` statement to check whether the year satisfies the conditions for a leap year. If the year is divisible by 4 and not divisible by 100, or if it is divisible by 400, then it is a leap year. We use the modulo operator `%` to check for divisibility.
3. If the year satisfies the conditions, we print a message saying that the year is a leap year. Otherwise, we print a message saying that it is not a leap year.

And that's it! With this program, we can easily determine whether a given year is a leap year or not.