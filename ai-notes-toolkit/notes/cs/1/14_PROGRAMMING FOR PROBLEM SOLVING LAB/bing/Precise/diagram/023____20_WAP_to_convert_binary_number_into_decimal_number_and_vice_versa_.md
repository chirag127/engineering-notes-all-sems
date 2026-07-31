## 20. WAP to convert binary number into decimal number and vice versa

Converting a binary number into a decimal number involves taking the binary digits (bits) and calculating their respective decimal values based on their position in the binary number. The formula for converting a binary number to a decimal number is as follows:

```
Decimal = b0 * 2^0 + b1 * 2^1 + b2 * 2^2 + ... + bn * 2^n
```

Where `b0` is the least significant bit (LSB) and `bn` is the most significant bit (MSB).

Here is an example of converting the binary number `1011` to its decimal equivalent:

```
Decimal = 1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3
        = 1 + 2 + 0 + 8
        = 11
```

Converting a decimal number into a binary number involves repeatedly dividing the decimal number by 2 and keeping track of the remainders. The remainders, when read in reverse order, form the binary equivalent of the decimal number.

Here is an example of converting the decimal number `11` to its binary equivalent:

```
11 / 2 = 5 remainder 1
 5 / 2 = 2 remainder 1
 2 / 2 = 1 remainder 0
 1 / 2 = 0 remainder 1
```

Reading the remainders in reverse order, we get `1011`, which is the binary equivalent of the decimal number `11`.