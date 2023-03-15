## 20.WAP to convert binary number into decimal number and vice versa.

Binary numbers are composed of only two digits: 0 and 1. Decimal numbers are composed of ten digits: 0 to 9. To convert between binary and decimal numbers, we can use the following algorithms:

- To convert a binary number to a decimal number, we can use the formula:

  - Decimal = Sum of (binary digit * 2^position) for each position from right to left, starting from 0.

  - For example, to convert 1011 to decimal, we can do:

    - Decimal = (1 * 2^0) + (1 * 2^1) + (0 * 2^2) + (1 * 2^3)
    - Decimal = 1 + 2 + 0 + 8
    - Decimal = 11

- To convert a decimal number to a binary number, we can use the following steps:

  - Divide the decimal number by 2 and note the remainder (0 or 1).
  - Repeat the step until the quotient is 0.
  - The binary number is the sequence of remainders in reverse order.

  - For example, to convert 13 to binary, we can do:

    - 13 / 2 = 6, remainder = 1
    - 6 / 2 = 3, remainder = 0
    - 3 / 2 = 1, remainder = 1
    - 1 / 2 = 0, remainder = 1
    - The binary number is 1101

A possible pseudocode for the conversion program is:

```
# Input a binary or decimal number
number = input("Enter a binary or decimal number: ")

# Check if the number is binary or decimal
if number contains only 0 and 1:
  # Convert binary to decimal
  decimal = 0
  position = 0
  for each digit in number from right to left:
    decimal = decimal + (digit * 2^position)
    position = position + 1
  # Output the decimal number
  print("The decimal equivalent is: ", decimal)
else:
  # Convert decimal to binary
  binary = ""
  while number is not 0:
    remainder = number % 2
    binary = remainder + binary
    number = number / 2
  # Output the binary number
  print("The binary equivalent is: ", binary)
```