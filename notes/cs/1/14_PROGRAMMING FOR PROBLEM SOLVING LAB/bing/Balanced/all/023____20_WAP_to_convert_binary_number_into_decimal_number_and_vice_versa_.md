## 20.WAP to convert binary number into decimal number and vice versa.

A binary number is a number that consists of only two digits: 0 and 1. A decimal number is a number that consists of ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. To convert a binary number into a decimal number, we need to multiply each digit of the binary number by a power of 2, starting from the rightmost digit and moving to the left. The power of 2 starts from 0 and increases by 1 for each digit. Then, we need to add up all the products to get the decimal number. For example, to convert the binary number 1011 into a decimal number, we do the following:

1011 = (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)
     = (8) + (0) + (2) + (1)
     = 11

To convert a decimal number into a binary number, we need to divide the decimal number by 2 repeatedly and write down the remainder of each division, starting from the bottom and moving to the top. The remainders will form the binary number. For example, to convert the decimal number 13 into a binary number, we do the following:

13 / 2 = 6, remainder = 1
6 / 2 = 3, remainder = 0
3 / 2 = 1, remainder = 1
1 / 2 = 0, remainder = 1

The binary number is 1101.

A pseudocode for a program that can convert binary number into decimal number and vice versa is:

```
# Input a number and a choice
num = input("Enter a number: ")
choice = input("Enter 1 for binary to decimal or 2 for decimal to binary: ")

# If choice is 1, convert binary to decimal
if choice == 1:
  # Initialize decimal as 0 and power as 0
  decimal = 0
  power = 0
  # Loop through each digit of the binary number from right to left
  for i in range(len(num) - 1, -1, -1):
    # Convert the digit to an integer
    digit = int(num[i])
    # Multiply the digit by 2 raised to the power and add it to decimal
    decimal = decimal + (digit * (2 ** power))
    # Increment the power by 1
    power = power + 1
  # Print the decimal number
  print("The decimal number is: ", decimal)

# If choice is 2, convert decimal to binary
elif choice == 2:
  # Initialize binary as an empty string
  binary = ""
  # Loop while the decimal number is greater than 0
  while num > 0:
    # Divide the decimal number by 2 and get the remainder
    remainder = num % 2
    # Convert the remainder to a string and prepend it to binary
    binary = str(remainder) + binary
    # Divide the decimal number by 2 and update it
    num = num // 2
  # Print the binary number
  print("The binary number is: ", binary)

# If choice is invalid, print an error message
else:
  print("Invalid choice")
```