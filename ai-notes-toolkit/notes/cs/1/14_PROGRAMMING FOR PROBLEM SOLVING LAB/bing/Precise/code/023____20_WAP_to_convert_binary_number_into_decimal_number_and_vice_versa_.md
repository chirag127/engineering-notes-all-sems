## 20. WAP to convert binary number into decimal number and vice versa

Converting a binary number to a decimal number involves multiplying the value of each digit by its place value and then adding the results. The place value of each digit in a binary number is a power of 2, with the rightmost digit having a place value of 2^0, the next digit to the left having a place value of 2^1, and so on.

Here is an example of converting the binary number 1011 to decimal:

1. Start with the rightmost digit, which has a value of 1 and a place value of 2^0. Multiply the value by the place value: 1 * 2^0 = 1
2. Move to the next digit to the left, which has a value of 1 and a place value of 2^1. Multiply the value by the place value: 1 * 2^1 = 2
3. Move to the next digit to the left, which has a value of 0 and a place value of 2^2. Multiply the value by the place value: 0 * 2^2 = 0
4. Move to the next digit to the left, which has a value of 1 and a place value of 2^3. Multiply the value by the place value: 1 * 2^3 = 8
5. Add the results of each multiplication: 1 + 2 + 0 + 8 = 11

Therefore, the binary number 1011 is equivalent to the decimal number 11.

Converting a decimal number to a binary number involves repeatedly dividing the decimal number by 2 and recording the remainder until the decimal number becomes 0. The binary number is then formed by arranging the remainders in reverse order.

Here is an example of converting the decimal number 11 to binary:

1. Divide 11 by 2 to get a quotient of 5 and a remainder of 1. Record the remainder.
2. Divide 5 by 2 to get a quotient of 2 and a remainder of 1. Record the remainder.
3. Divide 2 by 2 to get a quotient of 1 and a remainder of 0. Record the remainder.
4. Divide 1 by 2 to get a quotient of 0 and a remainder of 1. Record the remainder.
5. Since the quotient is now 0, stop the division process.
6. Arrange the remainders in reverse order to form the binary number: 1011

Therefore, the decimal number 11 is equivalent to the binary number 1011.