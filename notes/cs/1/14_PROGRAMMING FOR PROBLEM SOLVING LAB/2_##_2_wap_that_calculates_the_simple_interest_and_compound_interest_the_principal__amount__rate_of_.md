## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

Here's the code in Python for calculating Simple Interest and Compound Interest:

```
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * (1 + (rate / 100)) ** time

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest_amount = simple_interest(principal, rate, time)
compound_interest_amount = compound_interest(principal, rate, time)

print("Simple Interest:", simple_interest_amount)
print("Compound Interest:", compound_interest_amount)
```
