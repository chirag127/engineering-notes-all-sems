### Binary arithmetic

Binary arithmetic is the process of performing mathematical operations on binary numbers, which are represented by only two digits: 0 and 1. Binary arithmetic is essential for digital electronics, such as computers, microprocessors, and logic circuits.

The basic binary arithmetic operations are:

- Binary addition: It is the process of adding two binary numbers and producing a binary sum. The rules of binary addition are:

  - 0 + 0 = 0
  - 0 + 1 = 1
  - 1 + 0 = 1
  - 1 + 1 = 0 with a carry of 1

  To add two binary numbers, we align them from the rightmost bit and add each pair of bits column by column. If there is a carry, we add it to the next column. For example:

  ```
     1101
    +1010
    -----
    10111
  ```

- Binary subtraction: It is the process of subtracting one binary number from another and producing a binary difference. The rules of binary subtraction are:

  - 0 - 0 = 0
  - 0 - 1 = 1 with a borrow of 1
  - 1 - 0 = 1
  - 1 - 1 = 0

  To subtract two binary numbers, we align them from the rightmost bit and subtract each pair of bits column by column. If there is a borrow, we subtract it from the next column. For example:

  ```
     1101
    -1010
    -----
      111
  ```

- Binary multiplication: It is the process of multiplying two binary numbers and producing a binary product. The rules of binary multiplication are:

  - 0 x 0 = 0
  - 0 x 1 = 0
  - 1 x 0 = 0
  - 1 x 1 = 1

  To multiply two binary numbers, we multiply each bit of the multiplicand by each bit of the multiplier and add the partial products. The partial products are shifted left by one bit for each column of the multiplier. For example:

  ```
     1101
    x1010
    -----
     0000
    1101
   0000
  1101
  -----
  1000110
  ```

- Binary division: It is the process of dividing one binary number by another and producing a binary quotient and a binary remainder. The rules of binary division are:

  - 0 / 0 = undefined
  - 0 / 1 = 0
  - 1 / 0 = undefined
  - 1 / 1 = 1

  To divide two binary numbers, we use the long division method. We divide the dividend by the divisor and write the quotient above the dividend. We write the remainder below the dividend. For example:

  ```
    1000
  11)1100
    11
    --
    0100
     11
     --
     0010
  ```

  The quotient is 100 and the remainder is 10.