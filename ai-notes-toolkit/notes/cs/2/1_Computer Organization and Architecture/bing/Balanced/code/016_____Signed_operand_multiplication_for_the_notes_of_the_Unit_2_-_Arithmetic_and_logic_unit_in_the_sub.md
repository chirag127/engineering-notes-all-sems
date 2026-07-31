### Signed operand multiplication

- Signed operand multiplication is the process of multiplying two binary numbers that have a sign bit, either in 2's complement or signed-magnitude representation.
- The sign bit is usually the most significant bit of the number, and it indicates whether the number is positive (0) or negative (1).
- There are different algorithms for performing signed operand multiplication, depending on the representation and the hardware design of the arithmetic and logic unit (ALU).
- Some of the common algorithms are:

  - **Shift-and-add multiplication**: This algorithm is similar to the unsigned multiplication, but it requires some modifications to handle the sign bit and the negative numbers. The basic steps are:

    - Convert the multiplier and the multiplicand to positive numbers and remember their original signs.
    - Initialize the product to 0 and align the multiplier with the least significant bit of the product.
    - Repeat for n times, where n is the number of bits in the multiplier:
      - If the least significant bit of the multiplier is 1, add the multiplicand to the product and discard the overflow bit.
      - Shift the product and the multiplier one bit to the right, filling the vacated bit with the sign bit of the product.
    - If the original signs of the multiplier and the multiplicand are different, complement the product to get the final result.

  - **Booth's algorithm**: This algorithm is more efficient than the shift-and-add multiplication, as it reduces the number of additions and subtractions required. It operates on the fact that strings of 0's in the multiplier require no addition but just shifting and a string of 1's in the multiplier from bit weight 2^k to 2^m can be treated as 2^(m+1) - 2^k. The basic steps are:

    - Append a 0 to the right of the multiplier and call it the least significant bit (LSB).
    - Initialize the product to 0 and align the multiplicand with the LSB of the multiplier.
    - Repeat for n times, where n is the number of bits in the multiplier:
      - Examine the LSB and the bit to its right of the multiplier and perform one of the following actions based on their values:
        - 00: Do nothing.
        - 01: Subtract the multiplicand from the product and discard the overflow bit.
        - 10: Add the multiplicand to the product and discard the overflow bit.
        - 11: Do nothing.
      - Shift the product and the multiplier one bit to the right, filling the vacated bit with the sign bit of the product.
    - The final product is obtained by discarding the LSB of the multiplier.