## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple Interest (SI) is the amount of interest earned on a given principal amount for a certain period of time at a fixed rate of interest. It is calculated by the formula:

  `SI = (P * R * T) / 100`

  where P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- Compound Interest (CI) is the amount of interest earned on a given principal amount for a certain period of time at a variable rate of interest. It is calculated by the formula:

  `CI = P * (1 + R/100)^T - P`

  where P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- To write a program that calculates the SI and CI for a given input of P, R, and T, we can use the following steps:

  1. Declare and initialize the variables P, R, and T to store the input values.
  2. Declare and initialize the variables SI and CI to store the output values.
  3. Calculate the SI using the formula `SI = (P * R * T) / 100` and assign it to the variable SI.
  4. Calculate the CI using the formula `CI = P * (1 + R/100)^T - P` and assign it to the variable CI.
  5. Display the values of SI and CI using print statements.

- An example of a program in Python that implements the above steps is:

  ```python
  # WAP that calculates the Simple Interest and Compound Interest
  # The Principal, Amount, Rate of Interest and Time are entered through the keyboard

  # Input the values of P, R, and T
  P = float(input("Enter the principal amount: "))
  R = float(input("Enter the rate of interest per annum: "))
  T = float(input("Enter the time period in years: "))

  # Initialize the variables SI and CI
  SI = 0.0
  CI = 0.0

  # Calculate the SI using the formula SI = (P * R * T) / 100
  SI = (P * R * T) / 100

  # Calculate the CI using the formula CI = P * (1 + R/100)^T - P
  CI = P * (1 + R/100)**T - P

  # Display the values of SI and CI
  print("The simple interest is: ", SI)
  print("The compound interest is: ", CI)
  ```