## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple Interest (SI) is the interest earned on a principal amount for a given period of time at a fixed rate of interest. It is calculated by the formula:

    `SI = (P * R * T) / 100`

    where P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- Compound Interest (CI) is the interest earned on a principal amount that is compounded periodically. It is calculated by the formula:

    `CI = P * (1 + R / 100) ^ T - P`

    where P is the principal amount, R is the rate of interest per annum, and T is the number of compounding periods.

- A program that calculates the SI and CI for a given input of P, R, and T is:

    ```python
    # Python program to calculate SI and CI

    # Input the principal, rate and time
    P = float(input("Enter the principal amount: "))
    R = float(input("Enter the rate of interest: "))
    T = float(input("Enter the time period: "))

    # Calculate the simple interest
    SI = (P * R * T) / 100

    # Calculate the compound interest
    CI = P * (1 + R / 100) ** T - P

    # Print the results
    print("The simple interest is: ", SI)
    print("The compound interest is: ", CI)
    ```