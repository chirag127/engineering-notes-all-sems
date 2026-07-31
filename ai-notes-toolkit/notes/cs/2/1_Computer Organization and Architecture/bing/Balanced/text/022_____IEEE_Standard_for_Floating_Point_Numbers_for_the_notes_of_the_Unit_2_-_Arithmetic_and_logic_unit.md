### IEEE Standard for Floating Point Numbers

- Floating point numbers are a way to represent real numbers in hardware, using a fixed number of bits.
- IEEE 754 is the most widely used standard for floating point arithmetic, which specifies the formats, methods, and exception handling for binary and decimal floating point numbers  .
- IEEE 754 defines two precisions for binary floating point numbers: single precision (32 bits) and double precision (64 bits) .
- A binary floating point number consists of three components: a sign bit, an exponent, and a significand.
- The sign bit indicates the sign of the number: 0 for positive and 1 for negative.
- The exponent is a biased representation of the power of 2 that scales the significand. The bias is a constant value that is subtracted from the exponent to get the actual value.
- The significand is the fractional part of the number, normalized to have an implied leading 1 before the binary point.
- The value of a binary floating point number is given by the formula: (-1)^sign * 2^(exponent - bias) * (1 + significand).
- IEEE 754 also defines special values for representing infinity, negative infinity, zero, and not-a-number (NaN) .
- IEEE 754 also specifies rounding modes, operations, and exceptions for floating point arithmetic. Some of the exceptions are overflow, underflow, division by zero, and invalid operation.