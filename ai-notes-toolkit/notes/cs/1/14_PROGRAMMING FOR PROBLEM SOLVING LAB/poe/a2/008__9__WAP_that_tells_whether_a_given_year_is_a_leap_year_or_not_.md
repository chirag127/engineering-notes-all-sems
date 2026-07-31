 Here is the content in Markdown format without any emojis or external links and in a formal tone:

## 9. WAP that tells whether a given year is a leap year or not.

A year is a leap year if:

1. It is divisible by 4.
2. It is not divisible by 100 unless it is also divisible by 400.

* A program to check if a year is a leap year:

```python
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
```

* Explanation:

The program takes the input year from the user.
It is first checked if the year is divisible by 4. If yes, then it is checked if the year is divisible by 100.
If the year is divisible by 100, then it is checked if it is divisible by 400. If yes, then the year is a leap year.
If the year is not divisible by 4, then it is not a leap year.

This is a formal way of explaining the logic to determine if a year is a leap year or not without using any emojis or external links. The content is written in points and in Markdown format as required.