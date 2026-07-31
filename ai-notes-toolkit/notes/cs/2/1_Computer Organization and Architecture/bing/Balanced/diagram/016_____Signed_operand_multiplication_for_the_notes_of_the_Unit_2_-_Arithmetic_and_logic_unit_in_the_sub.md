### Signed operand multiplication

- Signed operand multiplication is the process of multiplying two binary numbers that have a sign bit (usually the most significant bit) indicating whether they are positive or negative.
- There are different methods to perform signed operand multiplication, such as signed-magnitude representation, two's complement representation, and Booth's algorithm.
- In this section, we will focus on the signed-magnitude representation and Booth's algorithm.

#### Signed-magnitude representation

- In signed-magnitude representation, the sign bit is 0 for positive numbers and 1 for negative numbers, and the remaining bits represent the magnitude of the number in binary.
- For example, +5 is represented as 0101 and -5 is represented as 1101 in 4-bit signed-magnitude representation.
- To multiply two numbers in signed-magnitude representation, we follow these steps:
  - Convert the multiplier and multiplicand to positive numbers and remember the original signs.
  - Perform the multiplication using the successive shift and add algorithm, which consists of the following steps:
    - Initialize the product register to 0 and align the multiplier with the least significant bit of the product.
    - If the least significant bit of the multiplier is 1, add the multiplicand to the product and store the result in the product register.
    - Shift the product and the multiplier one bit to the right, discarding the least significant bit of the product and inserting the sign bit of the multiplier in the most significant bit of the product.
    - Repeat the previous two steps until the multiplier becomes 0.
  - If the original signs of the multiplier and multiplicand are different, complement the sign bit of the product to make it negative.
- For example, to multiply -3 and +4 in 4-bit signed-magnitude representation, we do the following:
  - Convert -3 to 0011 and +4 to 0100 and remember that the signs are different.
  - Perform the successive shift and add algorithm as follows:

| Step | Product | Multiplier | Operation |
| --- | --- | --- | --- |
| 0 | 0000 | 0011 | Initial values |
| 1 | 0100 | 0001 | Add multiplicand to product |
| 2 | 0010 | 0000 | Shift right |
| 3 | 0001 | 0000 | Shift right |
| 4 | 0000 | 0000 | Shift right |
| 5 | 0000 | 0000 | Shift right |

  - The final product is 0000 0000, which is 0 in decimal.
  - Since the signs are different, we complement the sign bit of the product to make it negative, resulting in 1000 0000, which is -128 in decimal.
  - However, this is an incorrect answer, because the correct answer is -12, which cannot be represented in 4-bit signed-magnitude representation.
  - This shows that signed-magnitude representation can cause overflow and underflow errors when multiplying large or small numbers.

#### Booth's algorithm

- Booth's algorithm is a more efficient method to multiply two signed binary numbers in two's complement representation, which uses the complement of the negative numbers instead of the sign bit.
- For example, +5 is represented as 0101 and -5 is represented as 1011 in 4-bit two's complement representation.
- To multiply two numbers in two's complement representation using Booth's algorithm, we follow these steps:
  - Initialize the product register to 0 and append an extra bit (called Qn+1) to the right of the multiplier, which is initially 0.
  - Examine the least significant bit of the multiplier and Qn+1 and perform one of the following operations based on their values:

| Multiplier | Qn+1 | Operation |
| --- | --- | --- |
| 0 | 0 | Do nothing |
| 0 | 1 | Add multiplicand to product |
| 1 | 0 | Subtract multiplicand from product |
| 1 | 1 | Do nothing |

  - Shift the product and the multiplier (including Qn+1) one bit to the right, preserving the sign bit of the product. This is called an arithmetic shift right operation.
  - Repeat the previous two steps n times, where n is the number of bits in the multiplier.
  - The final product is obtained by discarding Qn+1 from the product register.
- For example, to multiply -3 and +4 in 4-bit two's complement representation using Booth's algorithm, we do the