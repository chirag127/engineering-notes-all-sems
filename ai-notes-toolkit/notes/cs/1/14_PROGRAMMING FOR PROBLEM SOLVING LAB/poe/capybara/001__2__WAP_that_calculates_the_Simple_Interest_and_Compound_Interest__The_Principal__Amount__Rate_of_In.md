## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

To calculate Simple Interest and Compound Interest, we need to follow the below steps:

1. Get the input values:
   - Principal
   - Rate of Interest
   - Time
   
2. Calculate Simple Interest:
   - Simple Interest = (Principal * Rate of Interest * Time) / 100
   
3. Calculate Compound Interest:
   - Amount = Principal * (1 + Rate of Interest/100) ^ Time
   - Compound Interest = Amount - Principal

4. Display the results:
   - Display Simple Interest
   - Display Compound Interest

Sample program in Python:

```python
# Get input values
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Calculate Compound Interest
amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

# Display the results
print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
```

Note: Make sure to handle any errors that may occur during the input process or calculations.