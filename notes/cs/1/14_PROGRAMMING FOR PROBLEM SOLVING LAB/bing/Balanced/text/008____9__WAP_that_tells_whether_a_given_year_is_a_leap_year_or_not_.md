## 9. WAP that tells whether a given year is a leap year or not.

- A leap year is a year that has 366 days instead of 365 days.
- A leap year occurs every four years, except when the year is divisible by 100 and not divisible by 400.
- For example, 2000 and 2020 are leap years, but 1900 and 2100 are not.
- To write a program that tells whether a given year is a leap year or not, we can use the following algorithm:
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
- To implement the algorithm in Python, we can use the following code:

```python
# Input the year from the user and store it in a variable, say year.
year = int(input("Enter a year: "))

# If year is divisible by 4, then
if year % 4 == 0:
  # If year is divisible by 100, then
  if year % 100 == 0:
    # If year is divisible by 400, then
    if year % 400 == 0:
      # Print "The year is a leap year."
      print("The year is a leap year.")
    # Else
    else:
      # Print "The year is not a leap year."
      print("The year is not a leap year.")
  # Else
  else:
    # Print "The year is a leap year."
    print("The year is a leap year.")
# Else
else:
  # Print "The year is not a leap year."
  print("The year is not a leap year.")
```