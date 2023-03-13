## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- A WAP (Write a Program) is a common term used in computer science and programming to describe a task or a problem that requires writing a code or a program to solve it.
- Simple Interest and Compound Interest are two types of interest that are calculated on a principal amount that is borrowed or invested for a certain period of time at a certain rate of interest.
- Simple Interest is calculated by multiplying the principal amount, the rate of interest and the time period. The formula is:

    `Simple Interest = (Principal * Rate * Time) / 100`

- Compound Interest is calculated by adding the interest earned to the principal amount and then calculating the interest on the new amount for the next period. The formula is:

    `Compound Interest = Principal * (1 + Rate / 100) ^ Time - Principal`

- To write a WAP that calculates the Simple Interest and Compound Interest, the following steps are required:

    1. Declare the variables to store the principal amount, the rate of interest, the time period, the simple interest and the compound interest.
    2. Prompt the user to enter the values for the principal amount, the rate of interest and the time period and store them in the respective variables.
    3. Calculate the simple interest using the formula and store the result in the simple interest variable.
    4. Calculate the compound interest using the formula and store the result in the compound interest variable.
    5. Display the values of the principal amount, the rate of interest, the time period, the simple interest and the compound interest to the user.

- A possible WAP that calculates the Simple Interest and Compound Interest in Python is:

    ```python
    # Declare the variables
    principal = 0.0
    rate = 0.0
    time = 0.0
    simple_interest = 0.0
    compound_interest = 0.0

    # Prompt the user to enter the values
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))

    # Calculate the simple interest
    simple_interest = (principal * rate * time) / 100

    # Calculate the compound interest
    compound_interest = principal * (1 + rate / 100) ** time - principal

    # Display the values
    print("The principal amount is: ", principal)
    print("The rate of interest is: ", rate)
    print("The time period is: ", time)
    print("The simple interest is: ", simple_interest)
    print("The compound interest is: ", compound_interest)
    ```

- A possible mnemonic to remember the formulas for simple interest and compound interest is:

    `SIR TIP` for Simple Interest = (Principal * Rate * Time) / 100

    `CIR PIP` for Compound Interest = Principal * (1 + Rate / 100) ^ Time - Principal

    where SIR stands for Simple Interest Rate, CIR stands for Compound Interest Rate, TIP stands for Time In Periods, and PIP stands for Principal In Periods.