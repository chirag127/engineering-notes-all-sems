## 20.WAP to convert binary number into decimal number and vice versa.

Binary numbers are composed of only two digits: 0 and 1. They are used to represent information in computers and digital devices. Decimal numbers are composed of ten digits: 0 to 9. They are used to represent numbers in everyday life.

To convert a binary number into a decimal number, we can use the following algorithm:

- Start from the rightmost digit of the binary number and assign it a power of 2, starting from 0. For example, if the binary number is 1011, then the rightmost digit is 1 and its power of 2 is 0.
- Multiply each digit of the binary number by its corresponding power of 2 and add the results. For example, 1011 = 1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 = 1 + 2 + 0 + 8 = 11.
- The final sum is the decimal equivalent of the binary number. For example, 1011 in binary is 11 in decimal.

To convert a decimal number into a binary number, we can use the following algorithm:

- Divide the decimal number by 2 and note the remainder. For example, if the decimal number is 11, then 11 / 2 = 5 with a remainder of 1.
- Repeat the division process with the quotient until the quotient becomes 0. For example, 5 / 2 = 2 with a remainder of 1, and 2 / 2 = 1 with a remainder of 0.
- Write the remainders in reverse order. For example, the remainders are 1, 1, and 0, so the reverse order is 011.
- The final result is the binary equivalent of the decimal number. For example, 11 in decimal is 1011 in binary.

A mnemonic to remember the conversion from binary to decimal is to use the word BID:

- B stands for Binary, which is the given number.
- I stands for Index, which is the power of 2 assigned to each digit.
- D stands for Decimal, which is the final sum.

A mnemonic to remember the conversion from decimal to binary is to use the word DRB:

- D stands for Decimal, which is the given number.
- R stands for Remainder, which is the result of dividing by 2.
- B stands for Binary, which is the final result.