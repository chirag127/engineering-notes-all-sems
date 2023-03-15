### Floating point arithmetic operation

- A floating point (FP) number is a kind of fraction where the radix point is allowed to move.
- A FP number consists of three parts: a sign bit, a significand, and an exponent.
- The sign bit indicates whether the number is positive or negative.
- The significand is the fractional part of the number, normalized to a certain range.
- The exponent is the power of two by which the significand is multiplied.
- The IEEE 754 standard defines a binary floating point format, with different precisions and ranges.
- The most common formats are single precision (32 bits) and double precision (64 bits).
- A FP number is represented as (-1)^s x M x 2^E, where s is the sign bit, M is the significand, and E is the exponent.
- FP arithmetic operations include addition, subtraction, multiplication, and division.
- FP arithmetic operations are done with algorithms similar to those used on sign magnitude integers, but with some additional steps.
- The steps are:
  - Align the operands by shifting the smaller exponent to match the larger one.
  - Perform the operation on the significands, taking care of the sign and overflow.
  - Normalize the result by adjusting the exponent and the significand.
  - Round the result to the nearest representable value, taking care of the precision and the rounding mode.