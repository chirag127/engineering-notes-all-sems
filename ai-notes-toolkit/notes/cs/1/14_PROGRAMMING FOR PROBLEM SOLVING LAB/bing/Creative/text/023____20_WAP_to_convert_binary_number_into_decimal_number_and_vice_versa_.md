## 20.WAP to convert binary number into decimal number and vice versa.

- A binary number is a number that consists of only two digits: 0 and 1. It is also called a base-2 number system.
- A decimal number is a number that consists of ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. It is also called a base-10 number system.
- To convert a binary number into a decimal number, we need to multiply each digit of the binary number by its corresponding power of 2, starting from the rightmost digit, and then add up the results. For example, to convert 1011 into decimal, we do:

  - 1011 = (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)
  - 1011 = (8) + (0) + (2) + (1)
  - 1011 = 11

- To convert a decimal number into a binary number, we need to divide the decimal number by 2 repeatedly and write down the remainder of each division, starting from the rightmost digit, until the quotient becomes 0. For example, to convert 13 into binary, we do:

  - 13 / 2 = 6, remainder = 1
  - 6 / 2 = 3, remainder = 0
  - 3 / 2 = 1, remainder = 1
  - 1 / 2 = 0, remainder = 1
  - The binary number is the reverse of the remainders: 1101

- A pseudocode for converting a binary number into a decimal number is:

  - Initialize a variable decimal to 0
  - Initialize a variable power to 0
  - While the binary number is not 0
    - Get the rightmost digit of the binary number and store it in a variable digit
    - Multiply digit by 2^power and add it to decimal
    - Divide the binary number by 10 to remove the rightmost digit
    - Increment power by 1
  - Return decimal

- A pseudocode for converting a decimal number into a binary number is:

  - Initialize a variable binary to 0
  - Initialize a variable power to 0
  - While the decimal number is not 0
    - Get the remainder of dividing the decimal number by 2 and store it in a variable digit
    - Multiply digit by 10^power and add it to binary
    - Divide the decimal number by 2 to get the next quotient
    - Increment power by 1
  - Return binary

- A sample Python code for converting a binary number into a decimal number is:

  ```python
  def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
      digit = binary % 10
      decimal += digit * (2 ** power)
      binary //= 10
      power += 1
    return decimal
  ```

- A sample Python code for converting a decimal number into a binary number is:

  ```python
  def decimal_to_binary(decimal):
    binary = 0
    power = 0
    while decimal != 0:
      digit = decimal % 2
      binary += digit * (10 ** power)
      decimal //= 2
      power += 1
    return binary
  ```