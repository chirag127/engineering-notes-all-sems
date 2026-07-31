# Binary arithmetic for the notes of the Unit 5 - Digital Electronics in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

Binary arithmetic is the set of rules for performing arithmetic operations on binary numbers, which are numbers represented in the base-2 system. Binary numbers consist of only two digits: 0 and 1. Binary arithmetic is essential for all the digital computers and many other digital systems.

The basic binary arithmetic operations are:

- Binary addition: It is the process of adding two binary numbers and producing a binary sum. There are four rules of binary addition:

  - 0 + 0 = 0
  - 0 + 1 = 1
  - 1 + 0 = 1
  - 1 + 1 = 10 (carry 1 to the next column)

  For example, to add 1011 and 1101, we align the numbers and add each column from right to left:

  ```
     1011
    +1101
    -----
    11000
  ```

- Binary subtraction: It is the process of subtracting one binary number from another and producing a binary difference. There are four rules of binary subtraction:

  - 0 - 0 = 0
  - 0 - 1 = 1 (borrow 1 from the next column)
  - 1 - 0 = 1
  - 1 - 1 = 0

  For example, to subtract 1001 from 1100, we align the numbers and subtract each column from right to left:

  ```
     1100
    -1001
    -----
      011
  ```

- Binary multiplication: It is the process of multiplying two binary numbers and producing a binary product. There are four rules of binary multiplication:

  - 0 x 0 = 0
  - 0 x 1 = 0
  - 1 x 0 = 0
  - 1 x 1 = 1

  For example, to multiply 101 and 11, we align the numbers and multiply each digit of the multiplier by the multiplicand, and then add the partial products:

  ```
      101
     x 11
     ----
      101
     101
     ----
     1111
  ```

- Binary division: It is the process of dividing one binary number by another and producing a binary quotient and a binary remainder. There are two rules of binary division:

  - 0 / 0 = undefined
  - 0 / 1 = 0
  - 1 / 0 = undefined
  - 1 / 1 = 1

  For example, to divide 1101 by 10, we align the numbers and perform the long division method:

  ```
     110
    ----
  10)1101
     10
     --
     10
     10
     --
      1
  ```

  The quotient is 110 and the remainder is 1.