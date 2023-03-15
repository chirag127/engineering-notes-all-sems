### IEEE Standard for Floating Point Numbers

- Floating-point numbers are a way to represent real numbers in hardware, using a fixed number of bits.
- IEEE 754 is the most widely used standard for floating-point arithmetic, which specifies the formats, methods, and exception handling for binary and decimal floating-point numbers  .
- IEEE 754 defines two precisions for binary floating-point numbers: single precision (32 bits) and double precision (64 bits) .
- A binary floating-point number consists of three components: a sign bit, an exponent, and a significand.
- The sign bit indicates the sign of the number: 0 for positive and 1 for negative.
- The exponent is a biased representation of the power of 2 that scales the significand. The bias is a constant value that is subtracted from the exponent to get the actual value.
- The significand is the fractional part of the number, normalized to have an implied leading 1 bit.
- The format of a single precision binary floating-point number is as follows:

| Sign | Exponent | Significand |
|:----:|:--------:|:-----------:|
| 1 bit| 8 bits   | 23 bits     |

- The format of a double precision binary floating-point number is as follows:

| Sign | Exponent | Significand |
|:----:|:--------:|:-----------:|
| 1 bit| 11 bits  | 52 bits     |

- The value of a binary floating-point number is calculated as follows:

`(-1)^sign * 2^(exponent - bias) * (1 + significand)`

- For example, the single precision binary floating-point number `01000010110010000000000000000000` has the following components:

| Sign | Exponent | Significand |
|:----:|:--------:|:-----------:|
| 0    | 10000101 | 10010000000000000000000 |

- The value of this number is calculated as follows:

`(-1)^0 * 2^(10000101 - 127) * (1 + 10010000000000000000000)`

`= 1 * 2^(133 - 127) * (1 + 0.5625)`

`= 2^6 * 1.5625`

`= 100.0`

- IEEE 754 also defines special values for representing infinity, negative infinity, zero, and not-a-number (NaN) .
- Infinity is represented by an exponent of all 1s and a significand of all 0s .
- Negative infinity is represented by an exponent of all 1s, a sign bit of 1, and a significand of all 0s .
- Zero is represented by an exponent of all 0s and a significand of all 0s . The sign bit can be either 0 or 1 .
- NaN is represented by an exponent of all 1s and a non-zero significand . The sign bit can be either 0 or 1 .
- IEEE 754 also specifies the rules for performing arithmetic operations, such as addition, subtraction, multiplication, division, and square root, on floating-point numbers.
- IEEE 754 also specifies the conditions for raising exceptions, such as overflow, underflow, invalid operation, division by zero, and inexact result, and their default handling.
- IEEE 754 also specifies the rounding modes for converting floating-point numbers to other formats, such as integer or fixed-point. The rounding modes are: round to nearest even, round toward zero, round toward positive infinity, and round toward negative infinity.