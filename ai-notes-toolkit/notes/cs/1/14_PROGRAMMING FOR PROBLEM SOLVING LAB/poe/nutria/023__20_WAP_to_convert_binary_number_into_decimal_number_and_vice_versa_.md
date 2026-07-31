
## 20. WAP to Convert Binary Number into Decimal Number and Vice Versa

1. Binary numbers are numbers expressed in base 2, with each digit representing a power of 2.
2. A decimal number is a number expressed in base 10, with each digit representing a power of 10.
3. To convert a binary number to a decimal number, we can use the following formula:

$$Decimal = \sum_{i=0}^n 2^i \times Binary_i$$

where $Binary_i$ is the $i$th digit of the binary number, starting from the rightmost digit.

4. To convert a decimal number to a binary number, we can use the following algorithm:

* Divide the decimal number by 2, and record the remainder.
* Repeat this process with the quotient until the quotient is 0.
* The binary number is the sequence of remainders, starting from the bottom of the list.

For example, to convert the decimal number 42 to a binary number:

* 42 / 2 = 21, remainder 0
* 21 / 2 = 10, remainder 1
* 10 / 2 = 5, remainder 0
* 5 / 2 = 2, remainder 1
* 2 / 2 = 1, remainder 0
* 1 / 2 = 0, remainder 1

Therefore, the binary number of 42 is 101010.