Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that calculates the simple interest and compound interest. Here is the content in markdown format:

## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple interest is the interest calculated on the principal amount only. It is given by the formula:

```
SI = (P * R * T) / 100
```

where SI is the simple interest, P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- Compound interest is the interest calculated on the principal amount as well as the accumulated interest. It is given by the formula:

```
CI = P * (1 + R / 100) ^ T - P
```

where CI is the compound interest, P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- To write a program that calculates the simple interest and compound interest, we need to:

  - Declare four variables to store the principal amount, rate of interest, time period, and interest.
  - Prompt the user to enter the values of these variables using the keyboard.
  - Calculate the simple interest using the formula and store it in a variable.
  - Calculate the compound interest using the formula and store it in another variable.
  - Display the results to the user.

- Here is an example of the program in Python:

```python
# WAP that calculates the Simple Interest and Compound Interest
# The Principal, Amount, Rate of Interest and Time are entered through the keyboard

# Declare the variables
P = 0 # Principal amount
R = 0 # Rate of interest
T = 0 # Time period
SI = 0 # Simple interest
CI = 0 # Compound interest

# Prompt the user to enter the values
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time period: "))

# Calculate the simple interest
SI = (P * R * T) / 100

# Calculate the compound interest
CI = P * (1 + R / 100) ** T - P

# Display the results
print("The simple interest is: ", SI)
print("The compound interest is: ", CI)
```

- Here is an example of the output of the program:

```
Enter the principal amount: 10000
Enter the rate of interest: 10
Enter the time period: 5
The simple interest is:  5000.0
The compound interest is:  6105.100000000006
```

- This is the end of the content. I hope you find it useful and informative. If you have any questions or feedback, please let me know. Thank you for using my service.🙏