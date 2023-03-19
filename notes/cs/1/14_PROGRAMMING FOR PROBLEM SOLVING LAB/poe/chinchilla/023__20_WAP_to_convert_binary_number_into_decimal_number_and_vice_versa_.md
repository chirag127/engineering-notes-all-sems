## 20. WAP to convert binary number into decimal number and vice versa.

To convert a binary number into a decimal number or vice versa, we need to understand the basic concepts of binary and decimal number systems. In this study material, we will learn about these concepts and the steps involved in converting a binary number into a decimal number and vice versa.

### Binary number system:

A binary number system is a number system that uses only two digits, 0 and 1. The value of each digit in a binary number is determined by its position in the number, with the rightmost digit being the least significant digit and the leftmost digit being the most significant digit. The value of a binary number is calculated by multiplying each digit by its corresponding power of 2 and adding the results.

### Decimal number system:

The decimal number system is a number system that uses ten digits, 0 through 9. The value of each digit in a decimal number is determined by its position in the number, with the rightmost digit being the least significant digit and the leftmost digit being the most significant digit. The value of a decimal number is calculated by multiplying each digit by its corresponding power of 10 and adding the results.

### Converting binary to decimal:

To convert a binary number into a decimal number, follow these steps:

1. Write down the binary number.
2. Starting from the rightmost digit, assign each digit a power of 2, starting with 2^0 for the rightmost digit and increasing by a power of 2 for each subsequent digit.
3. Multiply each digit by its corresponding power of 2.
4. Add the results of the multiplications to get the decimal equivalent of the binary number.

### Example:

Convert the binary number 101011 into a decimal number.

1. Write down the binary number: 101011.
2. Starting from the rightmost digit, assign each digit a power of 2: 2^0, 2^1, 2^2, 2^3, 2^4, 2^5.
3. Multiply each digit by its corresponding power of 2: 1 x 2^0, 1 x 2^1, 0 x 2^2, 1 x 2^3, 0 x 2^4, 1 x 2^5.
4. Add the results of the multiplications: 1 + 2 + 0 + 8 + 0 + 32 = 43.

Therefore, the decimal equivalent of the binary number 101011 is 43.

### Converting decimal to binary:

To convert a decimal number into a binary number, follow these steps:

1. Write down the decimal number.
2. Divide the decimal number by 2 and write down the quotient and remainder.
3. Divide the quotient by 2 and write down the quotient and remainder.
4. Continue dividing the quotient by 2 and writing down the quotient and remainder until the quotient becomes 0.
5. Write down the remainders in reverse order to get the binary equivalent of the decimal number.

### Example:

Convert the decimal number 43 into a binary number.

1. Write down the decimal number: 43.
2. Divide 43 by 2: quotient = 21, remainder = 1.
3. Divide 21 by 2: quotient = 10, remainder = 1.
4. Divide 10 by 2: quotient = 5, remainder = 0.
5. Divide 5 by 2: quotient = 2, remainder = 1.
6. Divide 2 by 2: quotient = 1, remainder = 0.
7. Divide 1 by 2: quotient = 0, remainder = 1.
8. Write down the remainders in reverse order: 101011.

Therefore, the binary equivalent of the decimal number 43 is 101011.

In conclusion, understanding the concepts of binary and decimal number systems and the steps involved in converting a binary number into a decimal number and vice versa is crucial in computer science and programming. By following the steps outlined in this study material, one can easily convert a binary number into a decimal number or vice versa.