## 20.WAP to convert binary number into decimal number and vice versa.

- A binary number is a number that consists of only two digits: 0 and 1. For example, 1010 is a binary number.
- A decimal number is a number that consists of ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. For example, 42 is a decimal number.
- To convert a binary number into a decimal number, we can use the following algorithm:
  - Start from the rightmost digit of the binary number and assign it a power of 2, starting from 0. For example, for 1010, the rightmost digit is 0 and its power of 2 is 2^0 = 1.
  - Multiply each digit by its corresponding power of 2 and add the results. For example, for 1010, we have 0 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 = 0 + 2 + 0 + 8 = 10.
  - The final sum is the decimal equivalent of the binary number. For example, 1010 in binary is 10 in decimal.
- To convert a decimal number into a binary number, we can use the following algorithm:
  - Divide the decimal number by 2 and note the remainder. For example, for 42, we have 42 / 2 = 21 with a remainder of 0.
  - Repeat the division process with the quotient until the quotient becomes 0. For example, for 42, we have 21 / 2 = 10 with a remainder of 1, then 10 / 2 = 5 with a remainder of 0, then 5 / 2 = 2 with a remainder of 1, then 2 / 2 = 1 with a remainder of 0, then 1 / 2 = 0 with a remainder of 1.
  - Write the remainders in reverse order. For example, for 42, we have 0, 1, 0, 1, 0, 1 as the remainders, so we write them as 101010.
  - The final result is the binary equivalent of the decimal number. For example, 42 in decimal is 101010 in binary.