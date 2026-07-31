Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that tells whether a given year is a leap year or not. Here is the content in markdown format:

## 9. WAP that tells whether a given year is a leap year or not.

- A leap year is a year that has 366 days instead of 365 days.
- A leap year occurs every four years, except when the year is divisible by 100 and not divisible by 400.
- For example, 2000 and 2400 are leap years, but 1800 and 2100 are not.
- To write a program that tells whether a given year is a leap year or not, we can use the following algorithm:

```
1. Input a year from the user and store it in a variable called year.
2. If year is divisible by 4, go to step 3. Otherwise, go to step 6.
3. If year is divisible by 100, go to step 4. Otherwise, go to step 5.
4. If year is divisible by 400, go to step 5. Otherwise, go to step 6.
5. Print "The year is a leap year." and end the program.
6. Print "The year is not a leap year." and end the program.
```

- Here is an example of the program in Python:

```python
# WAP that tells whether a given year is a leap year or not.

# Input a year from the user and store it in a variable called year.
year = int(input("Enter a year: "))

# If year is divisible by 4, go to step 3. Otherwise, go to step 6.
if year % 4 == 0:
  # If year is divisible by 100, go to step 4. Otherwise, go to step 5.
  if year % 100 == 0:
    # If year is divisible by 400, go to step 5. Otherwise, go to step 6.
    if year % 400 == 0:
      # Print "The year is a leap year." and end the program.
      print("The year is a leap year.")
    else:
      # Print "The year is not a leap year." and end the program.
      print("The year is not a leap year.")
  else:
    # Print "The year is a leap year." and end the program.
    print("The year is a leap year.")
else:
  # Print "The year is not a leap year." and end the program.
  print("The year is not a leap year.")
```

- Here is an example of the program output:

```
Enter a year: 2020
The year is a leap year.
```

```
Enter a year: 2021
The year is not a leap year.
```

- This is the end of the content. I hope you find it useful and informative. If you have any questions or feedback, please let me know. Thank you for using my service.🙏