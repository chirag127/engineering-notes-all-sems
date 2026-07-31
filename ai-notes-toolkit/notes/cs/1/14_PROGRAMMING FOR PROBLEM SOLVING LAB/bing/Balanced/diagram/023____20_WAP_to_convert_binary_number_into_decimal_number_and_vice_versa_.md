## 20.WAP to convert binary number into decimal number and vice versa.

Binary numbers are composed of only two digits: 0 and 1. They represent the base-2 system of counting, where each digit has a value of 2^n, where n is the position of the digit from right to left, starting from 0.

Decimal numbers are composed of ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. They represent the base-10 system of counting, where each digit has a value of 10^n, where n is the position of the digit from right to left, starting from 0.

To convert a binary number into a decimal number, we need to multiply each digit of the binary number by its corresponding power of 2, and then add up the results. For example, to convert 1011 into decimal, we do:

1011 = (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)
     = (8) + (0) + (2) + (1)
     = 11

To convert a decimal number into a binary number, we need to divide the decimal number by 2 repeatedly, and record the remainder of each division as a digit of the binary number, starting from the right. For example, to convert 13 into binary, we do:

13 / 2 = 6, remainder 1
6 / 2 = 3, remainder 0
3 / 2 = 1, remainder 1
1 / 2 = 0, remainder 1

The binary number is the sequence of remainders from bottom to top: 1101

A pseudocode for a program that can convert binary numbers into decimal numbers and vice versa is:

```
# Input a number and a choice
num = input("Enter a number: ")
choice = input("Enter 1 for binary to decimal, or 2 for decimal to binary: ")

# If choice is 1, convert binary to decimal
if choice == 1:
  # Initialize a variable to store the decimal value
  decimal = 0
  # Initialize a variable to store the power of 2
  power = 0
  # Loop through each digit of the binary number from right to left
  for i in range(len(num) - 1, -1, -1):
    # Get the digit as an integer
    digit = int(num[i])
    # Multiply the digit by 2^power and add it to the decimal value
    decimal = decimal + (digit * (2^power))
    # Increment the power by 1
    power = power + 1
  # Output the decimal value
  print("The decimal value is: ", decimal)

# If choice is 2, convert decimal to binary
elif choice == 2:
  # Initialize a variable to store the binary value as a string
  binary = ""
  # Loop while the decimal number is greater than 0
  while num > 0:
    # Divide the decimal number by 2 and get the remainder
    remainder = num % 2
    # Convert the remainder to a string and prepend it to the binary value
    binary = str(remainder) + binary
    # Divide the decimal number by 2 and update it
    num = num / 2
  # Output the binary value
  print("The binary value is: ", binary)

# If choice is invalid, output an error message
else:
  print("Invalid choice. Please enter 1 or 2.")
```