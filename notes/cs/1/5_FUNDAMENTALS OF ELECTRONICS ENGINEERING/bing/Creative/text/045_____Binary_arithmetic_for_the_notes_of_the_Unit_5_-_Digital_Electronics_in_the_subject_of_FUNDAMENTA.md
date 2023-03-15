Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of binary arithmetic for the notes of the unit 5 - digital electronics in the subject of fundamentals of electronics engineering.

### Binary arithmetic

- Binary arithmetic is the arithmetic of binary numbers, which are numbers that use only two digits: 0 and 1.
- Binary arithmetic is used to perform calculations in digital circuits and computers, which operate on binary signals.
- Binary arithmetic involves four basic operations: addition, subtraction, multiplication, and division.

#### Binary addition

- Binary addition is the simplest and most common operation in binary arithmetic.
- Binary addition follows the same rules as decimal addition, except that the carry is 2 instead of 10.
- To add two binary numbers, align them from right to left and add each pair of bits column by column, starting from the least significant bit (LSB).
- If the sum of two bits is 0 or 1, write it down as the result bit. If the sum of two bits is 2, write 0 as the result bit and carry 1 to the next column. If the sum of two bits is 3, write 1 as the result bit and carry 1 to the next column.
- Example: Add 1011 and 1101.

```
  1011
+ 1101
------
 11000
```

- The result is 11000, which is 24 in decimal.

#### Binary subtraction

- Binary subtraction is the inverse operation of binary addition.
- Binary subtraction follows the same rules as decimal subtraction, except that the borrow is 2 instead of 10.
- To subtract two binary numbers, align them from right to left and subtract each pair of bits column by column, starting from the LSB.
- If the difference of two bits is 0 or 1, write it down as the result bit. If the difference of two bits is -1, write 1 as the result bit and borrow 1 from the next column. If the difference of two bits is -2, write 0 as the result bit and borrow 1 from the next column.
- Example: Subtract 1011 from 1101.

```
  1101
- 1011
------
   010
```

- The result is 010, which is 2 in decimal.

#### Binary multiplication

- Binary multiplication is the repeated addition of one binary number by another binary number.
- Binary multiplication follows the same rules as decimal multiplication, except that the partial products are shifted by powers of 2 instead of powers of 10.
- To multiply two binary numbers, align them from right to left and multiply each bit of the multiplicand by the LSB of the multiplier, then shift the multiplicand to the left by one bit and repeat the process with the next bit of the multiplier, until all the bits of the multiplier are exhausted. Then add all the partial products to get the final product.
- Example: Multiply 1011 by 1101.

```
    1011
  x 1101
  ------
    1011
   0000
  1011
 1011
------
1111111
```

- The result is 1111111, which is 127 in decimal.

#### Binary division

- Binary division is the inverse operation of binary multiplication.
- Binary division follows the same rules as decimal division, except that the partial quotients are powers of 2 instead of powers of 10.
- To divide two binary numbers, align the divisor and the dividend from left to right and compare the most significant bits (MSBs) of both numbers. If the MSB of the divisor is larger than the MSB of the dividend, write 0 as the first bit of the quotient and shift the divisor to the right by one bit. If the MSB of the divisor is smaller than or equal to the MSB of the dividend, write 1 as the first bit of the quotient and subtract the divisor from the dividend, then shift the divisor to the right by one bit. Repeat the process until the divisor is smaller than the dividend or the dividend becomes zero. The remainder is the final difference of the dividend and the divisor.
- Example: Divide 1101 by 1011.

```
  1011 ) 1101 ( 1
       - 1011
       -----
          0100
```

- The result is 1 with a remainder of 0100, which is 4 in decimal.