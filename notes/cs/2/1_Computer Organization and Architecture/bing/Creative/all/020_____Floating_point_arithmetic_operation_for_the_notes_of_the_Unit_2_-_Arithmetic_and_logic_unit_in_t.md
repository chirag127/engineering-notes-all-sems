# Floating point arithmetic operation

- A floating point (FP) number is a kind of fraction where the radix point is allowed to move.
- A floating point number consists of three parts: a sign bit, a significand, and an exponent.
- The sign bit indicates whether the number is positive or negative.
- The significand is the fractional part of the number, normalized to have a leading 1 in binary representation.
- The exponent is the power of two by which the significand is multiplied.
- The floating point representation can implement operations for high range values, such as scientific and engineering calculations.
- The IEEE 754 standard defines a binary floating point format, with different precisions: single (32-bit), double (64-bit), and extended (80-bit or more).
- The architecture details of the floating point format are left to the hardware manufacturers.
- The storage order of individual bytes in binary floating point numbers varies from architecture to architecture.
- The floating point arithmetic operations include addition, subtraction, multiplication, and division.
- The floating point arithmetic operations are done with algorithms similar to those used on sign magnitude integers, but with some additional steps.
- The additional steps include aligning the significands by shifting them according to the exponents, normalizing the result by adjusting the exponent and the significand, and handling special cases such as overflow, underflow, zero, infinity, and NaN (not a number).
- The floating point arithmetic operations are quite often included in the internal hardware, such as a floating point unit (FPU) or a coprocessor.
- If no hardware is available for the floating point arithmetic operations, the compiler can generate software routines to perform them, but this may be slower and less accurate.