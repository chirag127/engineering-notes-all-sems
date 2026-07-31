Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program that tells whether a given year is a leap year or not. Here is the content in markdown format:

## 9. WAP that tells whether a given year is a leap year or not.

A leap year is a year that has 366 days instead of 365 days. A leap year occurs every four years, except when the year is divisible by 100 but not by 400. For example, 2000 was a leap year, but 1900 was not.

To write a program that tells whether a given year is a leap year or not, we can use the following algorithm:

- Input the year from the user and store it in a variable called `year`.
- Check if the year is divisible by 4. If not, then it is not a leap year and print "Not a leap year".
- If the year is divisible by 4, then check if it is divisible by 100. If not, then it is a leap year and print "Leap year".
- If the year is divisible by 100, then check if it is divisible by 400. If yes, then it is a leap year and print "Leap year". If not, then it is not a leap year and print "Not a leap year".

Here is an example of the program in Python:

```python
# Input the year from the user
year = int(input("Enter a year: "))

# Check if the year is divisible by 4
if year % 4 == 0:
  # Check if the year is divisible by 100
  if year % 100 == 0:
    # Check if the year is divisible by 400
    if year % 400 == 0:
      # The year is divisible by 4, 100 and 400, so it is a leap year
      print("Leap year")
    else:
      # The year is divisible by 4 and 100, but not by 400, so it is not a leap year
      print("Not a leap year")
  else:
    # The year is divisible by 4, but not by 100, so it is a leap year
    print("Leap year")
else:
  # The year is not divisible by 4, so it is not a leap year
  print("Not a leap year")
```

Here is an example of the output of the program:

```text
Enter a year: 2020
Leap year
```