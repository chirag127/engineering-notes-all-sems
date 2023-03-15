## 20.WAP to convert binary number into decimal number and vice versa.

- A binary number is a number that consists of only two digits: 0 and 1. It is also called a base-2 number system.
- A decimal number is a number that consists of ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. It is also called a base-10 number system.
- To convert a binary number into a decimal number, we can use the following algorithm:
  - Start from the rightmost digit of the binary number and assign it a power of 2, starting from 0.
  - Multiply each digit by its corresponding power of 2 and add the results together.
  - The final sum is the decimal equivalent of the binary number.
- For example, to convert 1011 into decimal, we can do the following:
  - Assign powers of 2 to each digit: 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0
  - Multiply and add: 8 + 0 + 2 + 1 = 11
  - The decimal equivalent of 1011 is 11.
- To convert a decimal number into a binary number, we can use the following algorithm:
  - Divide the decimal number by 2 and note the remainder.
  - Repeat the division process until the quotient is 0.
  - The binary equivalent of the decimal number is the sequence of remainders in reverse order.
- For example, to convert 13 into binary, we can do the following:
  - Divide 13 by 2 and note the remainder: 13 / 2 = 6, remainder = 1
  - Divide 6 by 2 and note the remainder: 6 / 2 = 3, remainder = 0
  - Divide 3 by 2 and note the remainder: 3 / 2 = 1, remainder = 1
  - Divide 1 by 2 and note the remainder: 1 / 2 = 0, remainder = 1
  - The binary equivalent of 13 is the sequence of remainders in reverse order: 1101
- A pseudocode for converting binary to decimal is:

```
function binary_to_decimal(binary):
  decimal = 0
  power = 0
  for each digit in binary from right to left:
    decimal = decimal + digit * 2^power
    power = power + 1
  return decimal
```

- A pseudocode for converting decimal to binary is:

```
function decimal_to_binary(decimal):
  binary = ""
  while decimal > 0:
    remainder = decimal % 2
    binary = remainder + binary
    decimal = decimal / 2
  return binary
```