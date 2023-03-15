### Floating point arithmetic operation

- A floating point (FP) number is a kind of fraction where the radix point is allowed to move. It is used to represent real numbers with high range and precision.
- A FP number consists of three parts: a sign bit, a significand (or mantissa), and an exponent. The sign bit indicates the sign of the number, the significand represents the significant digits of the number, and the exponent determines the position of the radix point.
- A FP number can be written in the form: (-1)^s x M x 2^E, where s is the sign bit, M is the significand, and E is the exponent.
- The IEEE 754 standard defines a binary floating point format, which is widely used in computer systems. It specifies the number of bits for each part of a FP number, and how to encode the sign, significand, and exponent.
- The IEEE 754 standard defines two types of FP numbers: single-precision and double-precision. Single-precision numbers use 32 bits, with 1 bit for sign, 8 bits for exponent, and 23 bits for significand. Double-precision numbers use 64 bits, with 1 bit for sign, 11 bits for exponent, and 52 bits for significand.
- Arithmetic operations on FP numbers include addition, subtraction, multiplication, and division. These operations are performed with algorithms similar to those used on sign magnitude integers, but with some additional steps to handle the exponent and the radix point.
- Some of the steps involved in FP arithmetic operations are:
  - Aligning the radix points of the operands by adjusting the exponents
  - Performing the operation on the significands and the signs
  - Normalizing the result by shifting the radix point and the exponent
  - Rounding the result to fit the available bits
  - Checking for overflow, underflow, or other special cases
- FP arithmetic operations are more complex and slower than integer operations, and may introduce errors due to rounding or representation limitations. Therefore, FP arithmetic operations should be used with care and understanding of their properties and limitations.