## 2. WAP that calculates the Simple Interest and Compound Interest

Simple Interest and Compound Interest are two methods of calculating the interest on a principal amount. The principal, amount, rate of interest, and time are entered through the keyboard.

- Simple Interest is calculated using the formula `SI = (P * R * T) / 100`, where `P` is the principal amount, `R` is the rate of interest, and `T` is the time in years.

- Compound Interest is calculated using the formula `CI = P * (1 + R/100)^T - P`, where `P` is the principal amount, `R` is the rate of interest, and `T` is the time in years.

Here is an example of a program that calculates the Simple Interest and Compound Interest:

```python
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))

SI = (P * R * T) / 100
CI = P * (1 + R/100)**T - P

print("Simple Interest: ", SI)
print("Compound Interest: ", CI)
```

This program takes the principal amount, rate of interest, and time in years as input from the user. It then calculates the Simple Interest and Compound Interest using the respective formulas and prints the results.