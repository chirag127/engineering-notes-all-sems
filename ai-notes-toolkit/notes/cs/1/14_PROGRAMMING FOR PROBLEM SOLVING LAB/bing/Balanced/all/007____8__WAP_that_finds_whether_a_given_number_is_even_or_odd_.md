## 8. WAP that finds whether a given number is even or odd.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- A number is even if it is divisible by 2 without any remainder. A number is odd if it is not divisible by 2 or has a remainder of 1 when divided by 2.
- To find whether a given number is even or odd, we can use the modulo operator (%) which returns the remainder of a division operation. For example, 5 % 2 = 1 and 6 % 2 = 0.
- The algorithm for the WAP is as follows:

  - Step 1: Input a number from the user and store it in a variable, say n.
  - Step 2: Calculate n % 2 and store the result in another variable, say r.
  - Step 3: If r is equal to 0, then print "The number is even." Else, print "The number is odd."
  - Step 4: End the program.

- The pseudocode for the WAP is as follows:

  - START
  - INPUT n
  - r = n % 2
  - IF r == 0 THEN
    - PRINT "The number is even."
  - ELSE
    - PRINT "The number is odd."
  - END IF
  - STOP

- The code for the WAP in Python is as follows:

  ```python
  # WAP that finds whether a given number is even or odd
  # Input a number from the user
  n = int(input("Enter a number: "))
  # Calculate the remainder of n divided by 2
  r = n % 2
  # Check if the remainder is zero
  if r == 0:
    # Print that the number is even
    print("The number is even.")
  else:
    # Print that the number is odd
    print("The number is odd.")
  ```