### SQL operators and their procedure

SQL operators are symbols or keywords that are used to perform operations on values or expressions in SQL statements. They are used to specify conditions, filter results, compare values, perform calculations, concatenate strings, and more. SQL operators can be classified into six types:

- Arithmetic operators: These operators are used for mathematical operations on numerical data, such as adding, subtracting, multiplying, dividing, and finding the remainder. The arithmetic operators in SQL are:

  - `+` (Addition): This operator adds two numbers together. For example, `SELECT 10 + 10;` returns 20.
  - `-` (Subtraction): This operator subtracts one number from another. For example, `SELECT 20 - 10;` returns 10.
  - `*` (Multiplication): This operator multiplies two numbers together. For example, `SELECT 10 * 10;` returns 100.
  - `/` (Division): This operator divides one number by another. For example, `SELECT 20 / 10;` returns 2.
  - `%` (Modulus): This operator returns the remainder of one number divided by another. For example, `SELECT 20 % 10;` returns 0.

- Bitwise operators: These operators are used for manipulating bits in binary data, such as performing logical operations, shifting bits, and inverting bits. The bitwise operators in SQL are:

  - `&` (Bitwise AND): This operator performs a logical AND operation on each pair of bits in two binary values and returns a new binary value. For example, `SELECT 5 & 3;` returns 1, because 5 in binary is 0101 and 3 in binary is 0011, and 0101 & 0011 = 0001.
  - `|` (Bitwise OR): This operator performs a logical OR operation on each pair of bits in two binary values and returns a new binary value. For example, `SELECT 5 | 3;` returns 7, because 5 in binary is 0101 and 3 in binary is 0011, and 0101 | 0011 = 0111.
  - `^` (Bitwise XOR): This operator performs a logical XOR operation on each pair of bits in two binary values and returns a new binary value. For example, `SELECT 5 ^ 3;` returns 6, because 5 in binary is 0101 and 3 in binary is 0011, and 0101 ^ 0011 = 0110.
  - `~` (Bitwise NOT): This operator performs a logical NOT operation on each bit in a binary value and returns a new binary value. For example, `SELECT ~5;` returns -6, because 5 in binary is 0101 and ~0101 = 1010, which is -6 in two's complement notation.
  - `<<` (Left Shift): This operator shifts the bits in a binary value to the left by a specified number of positions and returns a new binary value. For example, `SELECT 5 << 2;` returns 20, because 5 in binary is 0101 and 0101 << 2 = 010100, which is 20 in decimal.
  - `>>` (Right Shift): This operator shifts the bits in a binary value to the right by a specified number of positions and returns a new binary value. For example, `SELECT 20 >> 2;` returns 5, because 20 in binary is 010100 and 010100 >> 2 = 0101, which is 5 in decimal.

- Comparison operators: These operators are used for comparing two values or expressions and returning a boolean value (true or false) based on the result of the comparison. The comparison operators in SQL are:

  - `=` (Equal): This operator returns true if the two values or expressions are equal, and false otherwise. For example, `SELECT 10 = 10;` returns true, and `SELECT 10 = 20;` returns false.
  - `<>` or `!=` (Not Equal): This operator returns true if the two values or expressions are not equal, and false otherwise. For example, `SELECT 10 <> 10;` or `SELECT 10 != 10;` returns false, and `SELECT 10 <> 20;` or `SELECT 10 != 20;` returns true.
  - `>` (Greater Than):