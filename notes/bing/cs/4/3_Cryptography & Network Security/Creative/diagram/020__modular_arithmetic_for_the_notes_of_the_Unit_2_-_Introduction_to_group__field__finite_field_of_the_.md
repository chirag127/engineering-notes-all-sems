Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus. For example, if the modulus is 12, then 15 is equivalent to 3, because 15 mod 12 = 3. Modular arithmetic is useful for cryptography, because it allows operations on large numbers to be performed efficiently and securely.

The following diagram illustrates the basic idea of modular arithmetic using a clock face. The clock has 12 hours, so the modulus is 12. The numbers on the clock are the residues modulo 12, which are the possible remainders when dividing by 12. To add or subtract two numbers modulo 12, we can move the clock hands clockwise or counterclockwise, and find the resulting number on the clock. For example, 9 + 5 = 2 mod 12, because moving the clock hand 5 hours clockwise from 9 gives 2. Similarly, 9 - 5 = 4 mod 12, because moving the clock hand 5 hours counterclockwise from 9 gives 4.

```
    12
  11  1
10      2
  9  3
    8
  7  5
6      4
  5  7
    6
  3  9
2      10
  1  11
    12
```