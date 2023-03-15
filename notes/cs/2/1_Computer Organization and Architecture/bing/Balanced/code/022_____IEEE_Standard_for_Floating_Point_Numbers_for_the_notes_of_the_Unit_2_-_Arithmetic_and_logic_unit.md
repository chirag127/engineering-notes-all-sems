### IEEE Standard for Floating Point Numbers

- Floating-point numbers are a way to represent real numbers in hardware, using a fixed number of bits.
- IEEE 754 is the most widely used standard for floating-point arithmetic, which specifies the formats, operations, rounding modes, exceptions, and special values for binary and decimal floating-point numbers.
- IEEE 754 defines two precisions for binary floating-point numbers: single precision (32 bits) and double precision (64 bits).
- A binary floating-point number consists of three components: a sign bit, an exponent, and a significand (also called a fraction or mantissa).
- The sign bit indicates the sign of the number: 0 for positive and 1 for negative.
- The exponent is a biased integer that represents the power of 2 by which the significand is multiplied.
- The significand is a normalized fraction that represents the significant digits of the number, with an implied leading 1 before the binary point.
- The value of a binary floating-point number is given by the formula:

    `(-1)^sign * 2^(exponent - bias) * (1 + significand)`

- The bias is a constant that is added to the exponent to make it an unsigned integer. For single precision, the bias is 127, and for double precision, the bias is 1023.
- The exponent and the significand have different sizes depending on the precision. For single precision, the exponent is 8 bits and the significand is 23 bits. For double precision, the exponent is 11 bits and the significand is 52 bits.
- The exponent can have special values that indicate special cases, such as zero, infinity, or not a number (NaN).
- The significand can have different rounding modes that affect how the number is approximated when it cannot be represented exactly with the given number of bits.
- IEEE 754 also defines arithmetic operations, such as addition, subtraction, multiplication, division, square root, and comparison, that follow certain rules and properties for floating-point numbers.
- IEEE 754 also defines exceptions, such as overflow, underflow, inexact, invalid, and division by zero, that can occur when performing floating-point operations, and how they should be handled or signaled.