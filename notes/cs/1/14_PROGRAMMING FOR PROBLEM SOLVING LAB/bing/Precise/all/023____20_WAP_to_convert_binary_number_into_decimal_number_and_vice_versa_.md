## 20. WAP to convert binary number into decimal number and vice versa.

Converting a binary number into a decimal number involves taking the binary digits (bits) and calculating their respective place values. Here is an example of how to convert the binary number `1011` into a decimal number:

1. Start with the rightmost digit (in this case, `1`). This digit has a place value of 2^0, or 1. So, the value of this digit is 1 * 1 = 1.
2. Move to the next digit to the left (in this case, `1`). This digit has a place value of 2^1, or 2. So, the value of this digit is 1 * 2 = 2.
3. Move to the next digit to the left (in this case, `0`). This digit has a place value of 2^2, or 4. So, the value of this digit is 0 * 4 = 0.
4. Move to the next digit to the left (in this case, `1`). This digit has a place value of 2^3, or 8. So, the value of this digit is 1 * 8 = 8.
5. Add up all the values calculated for each digit: 1 + 2 + 0 + 8 = 11. So, the binary number `1011` is equivalent to the decimal number `11`.

Converting a decimal number into a binary number involves repeatedly dividing the decimal number by 2 and keeping track of the remainders. Here is an example of how to convert the decimal number `11` into a binary number:

1. Divide 11 by 2. The quotient is 5 and the remainder is 1. Write down the remainder (1).
2. Divide 5 by 2. The quotient is 2 and the remainder is 1. Write down the remainder (1).
3. Divide 2 by 2. The quotient is 1 and the remainder is 0. Write down the remainder (0).
4. Divide 1 by 2. The quotient is 0 and the remainder is 1. Write down the remainder (1).
5. Since the quotient is now 0, the process is complete. The remainders, read from bottom to top, form the binary number `1011`. So, the decimal number `11` is equivalent to the binary number `1011`.