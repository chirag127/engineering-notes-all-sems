## 2. WAP that calculates the Simple Interest and Compound Interest

Simple Interest and Compound Interest are two methods of calculating the interest on a principal amount over a period of time. The main difference between the two is the frequency of interest calculation.

Simple Interest is calculated only on the initial principal amount, whereas Compound Interest is calculated on the initial principal and also on the accumulated interest of previous periods.

Here is an example of a program that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest, and Time are entered through the keyboard.

```python
# Python program to calculate Simple Interest and Compound Interest

# Taking input from the user
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of Interest: "))
T = float(input("Enter the Time in years: "))

# Calculating Simple Interest
SI = (P * R * T) / 100
print("Simple Interest: ", SI)

# Calculating Compound Interest
CI = P * (pow((1 + R / 100), T))
print("Compound Interest: ", CI)
```

In the above program, the user is prompted to enter the Principal amount, Rate of Interest, and Time in years. The program then calculates the Simple Interest and Compound Interest using the respective formulas and displays the result.

Simple Interest is calculated using the formula `SI = (P * R * T) / 100`, where `P` is the Principal amount, `R` is the Rate of Interest, and `T` is the Time in years.

Compound Interest is calculated using the formula `CI = P * (pow((1 + R / 100), T))`, where `P` is the Principal amount, `R` is the Rate of Interest, and `T` is the Time in years.

This program can be modified to include additional features such as the ability to choose the frequency of compounding (e.g. annually, semi-annually, quarterly, etc.) and the ability to calculate the final amount after the interest has been applied.