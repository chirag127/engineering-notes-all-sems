## 2. WAP that calculates the Simple Interest and Compound Interest

Simple Interest and Compound Interest are two methods of calculating the interest on a principal amount. The principal, amount, rate of interest, and time are entered through the keyboard.

### Simple Interest
Simple Interest is calculated using the formula:
```
Simple Interest = (Principal * Rate of Interest * Time) / 100
```
Where:
- Principal is the initial amount of money
- Rate of Interest is the interest rate per year
- Time is the duration of the investment in years

### Compound Interest
Compound Interest is calculated using the formula:
```
Compound Interest = Principal * (1 + Rate of Interest / 100) ^ Time - Principal
```
Where:
- Principal is the initial amount of money
- Rate of Interest is the interest rate per year
- Time is the duration of the investment in years

### Example
Here is an example of a program that calculates the Simple Interest and Compound Interest:

```python
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100
compound_interest = principal * (1 + rate / 100) ** time - principal

print("Simple Interest: ", simple_interest)
print("Compound Interest: ", compound_interest)
```

This program prompts the user to enter the principal amount, rate of interest, and time in years. It then calculates the Simple Interest and Compound Interest using the formulas and displays the results.