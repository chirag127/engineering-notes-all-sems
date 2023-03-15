## 9. WAP that tells whether a given year is a leap year or not.

A leap year is a year that has 366 days instead of 365 days. A leap year occurs every four years, except when the year is divisible by 100 but not by 400. For example, 2000 was a leap year, but 1900 was not.

To write a program that tells whether a given year is a leap year or not, we can use the following algorithm:

- Input the year from the user and store it in a variable, say year.
- If year is divisible by 4, then
  - If year is divisible by 100, then
    - If year is divisible by 400, then
      - Print "The year is a leap year."
    - Else
      - Print "The year is not a leap year."
  - Else
    - Print "The year is a leap year."
- Else
    - Print "The year is not a leap year."

Here is an example of how the program can be written in Python:

```python
# Input the year from the user
year = int(input("Enter a year: "))

# Check if the year is divisible by 4
if year % 4 == 0:
  # Check if the year is divisible by 100
  if year % 100 == 0:
    # Check if the year is divisible by 400
    if year % 400 == 0:
      # The year is a leap year
      print("The year is a leap year.")
    else:
      # The year is not a leap year
      print("The year is not a leap year.")
  else:
    # The year is a leap year
    print("The year is a leap year.")
else:
  # The year is not a leap year
  print("The year is not a leap year.")
```