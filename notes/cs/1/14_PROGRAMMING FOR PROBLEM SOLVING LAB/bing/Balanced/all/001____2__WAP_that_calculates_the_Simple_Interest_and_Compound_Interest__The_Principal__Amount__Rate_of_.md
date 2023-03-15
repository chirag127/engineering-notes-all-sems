## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple Interest (SI) is the interest earned on a principal amount for a given period of time at a fixed rate of interest. It is calculated by the formula:

  `SI = (P * R * T) / 100`

  where P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- Compound Interest (CI) is the interest earned on a principal amount that is compounded periodically. It is calculated by the formula:

  `CI = P * (1 + R / 100) ^ T - P`

  where P is the principal amount, R is the rate of interest per annum, T is the number of compounding periods, and ^ is the exponentiation operator.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to perform a certain function or solve a problem.

- To write a WAP that calculates the SI and CI, we need to follow these steps:

  1. Declare the variables to store the input values of P, R, and T, and the output values of SI and CI.
  2. Prompt the user to enter the values of P, R, and T, and read them using the appropriate input function of the programming language.
  3. Calculate the SI and CI using the formulas given above, and store them in the respective variables.
  4. Display the values of SI and CI using the appropriate output function of the programming language.
  5. End the program.

- Here is an example of a WAP that calculates the SI and CI in Python, a popular programming language:

  ```python
  # WAP that calculates the SI and CI
  # Declare the variables
  P = 0 # Principal amount
  R = 0 # Rate of interest per annum
  T = 0 # Time period in years
  SI = 0 # Simple interest
  CI = 0 # Compound interest

  # Prompt the user to enter the values of P, R, and T
  P = float(input("Enter the principal amount: "))
  R = float(input("Enter the rate of interest per annum: "))
  T = float(input("Enter the time period in years: "))

  # Calculate the SI and CI
  SI = (P * R * T) / 100
  CI = P * (1 + R / 100) ** T - P

  # Display the values of SI and CI
  print("The simple interest is: ", SI)
  print("The compound interest is: ", CI)

  # End the program
  ```