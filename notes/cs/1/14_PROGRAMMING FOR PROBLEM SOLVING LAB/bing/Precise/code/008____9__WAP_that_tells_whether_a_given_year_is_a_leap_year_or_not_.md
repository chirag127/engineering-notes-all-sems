## 9. WAP that tells whether a given year is a leap year or not.

A leap year is a year that is divisible by 4, except for end-of-century years which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

Here is an example of a program that checks if a given year is a leap year or not:

```python
year = int(input('Enter a year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, 'is a leap year')
        else:
            print(year, 'is not a leap year')
    else:
        print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
```

This program takes a year as input from the user and checks if it is divisible by 4. If it is, it then checks if it is divisible by 100. If it is, it then checks if it is divisible by 400. If it is, then the year is a leap year. Otherwise, it is not a leap year. If the year is not divisible by 100, then it is a leap year. If the year is not divisible by 4, then it is not a leap year.