### Floating point arithmetic operation

- A floating point (FP) number is a kind of fraction where the radix point is allowed to move.
- A FP number is represented by two parts: a sign bit, a significand and an exponent.
- The sign bit indicates whether the number is positive or negative.
- The significand is the fractional part of the number, normalized to have a leading 1 in binary.
- The exponent is the power of two by which the significand is multiplied.
- The IEEE 754 standard defines a binary floating point format with different precisions: single (32-bit), double (64-bit) and extended (80-bit or more).
- The format consists of three fields: sign (1 bit), exponent (8, 11 or 15 bits) and fraction (23, 52 or 64 bits or more).
- The exponent field is biased by a constant value to represent both positive and negative exponents.
- The fraction field is the significand without the leading 1, which is implied for normalized numbers.
- There are some special values in the IEEE 754 format, such as zero, infinity and NaN (not a number).
- Floating point arithmetic operations include addition, subtraction, multiplication and division.
- The operations are done with algorithms similar to those used on sign magnitude integers, but with some additional steps.
- The steps are: align the operands by shifting the smaller exponent, add or subtract the significands, normalize the result, round the result and check for overflow or underflow.
- The operations are quite often included in the internal hardware of the computer, or implemented by software routines if no hardware is available.
- The operations are subject to errors due to finite precision, rounding and representation.