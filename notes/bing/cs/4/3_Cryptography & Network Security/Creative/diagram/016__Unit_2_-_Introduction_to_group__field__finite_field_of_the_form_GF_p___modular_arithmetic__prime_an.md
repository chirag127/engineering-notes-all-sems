The following is an attempt to draw a detailed ascii diagram for Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA.

Please note that this is not a complete or accurate representation of the concepts, but only a rough sketch based on some online sources. For a better understanding, please refer to the original sources or textbooks.

```
+-----------------------------------------------------------------------------+
| Unit 2 - Introduction to Cryptography                                       |
+-----------------------------------------------------------------------------+
|                                                                             |
| +----------------+ +----------------+ +----------------+ +----------------+ |
| | Group         | | Field         | | Finite Field  | | Modular       | |
| | - A set of    | | - A set of    | | - A field with| | Arithmetic    | |
| |   elements    | |   elements    | |   a finite    | | - A system of | |
| |   with a      | |   with two    | |   number of    | |   arithmetic  | |
| |   binary      | |   binary      | |   elements     | |   where       | |
| |   operation   | |   operations  | | - Examples:    | |   numbers     | |
| |   that        | |   that        | |   GF(2), GF(5),| |   wrap around | |
| |   satisfies   | |   satisfies   | |   GF(2^8), etc.| |   after       | |
| |   some        | |   some        | | - Used in      | |   reaching a  | |
| |   properties  | |   properties  | |   cryptography | |   fixed value | |
| | - Examples:   | | - Examples:   | |   such as AES  | | - Example:    | |
| |   (Z, +),     | |   (Q, +, x),  | |                | |   mod 12      | |
| |   (R, +), etc.| |   (R, +, x),  | +----------------+ +----------------+ |
| | - Used in     | |   etc.        | | Prime and      | | Extended      | |
| |   cryptography| | - Used in     | | Relative Prime | | Euclidean     | |
| |   such as     | |   cryptography| | Numbers        | | Algorithm     | |
| |   Diffie-     | |   such as     | | - A prime      | | - An algorithm| |
| |   Hellman     | |   elliptic    | |   number is a  | |   to find the | |
| |   key         | |   curve       | |   number that  | |   greatest    | |
| |   exchange    | |   cryptography| |   has only two | |   common      | |
| +----------------+ +----------------+ |   factors: 1   | |   divisor     | |
| | AES           | | Fermat's and  | |   and itself   | |   and the     | |
| | - A symmetric | | Euler's       | | - Two numbers  | |   coefficients| |
| |   block cipher| | Theorem       | |   are relative | |   of Bézout's | |
| |   that uses   | | - Two         | |   prime if     | |   identity    | |
| |   128, 192, or| |   theorems    | |   their        | | - Used in     | |
| |   256-bit keys| |   that relate | |   greatest     | |   cryptography| |
| |   to encrypt  | |   the         | |   common       | |   such as     | |
| |   and decrypt | |   modular     | |   divisor is 1 | |   RSA         | |
| |   128-bit     | |   exponent of | | - Examples:     | +----------------+ |
| |   blocks of   | |   a number    | |   2 and 3 are  | | Chinese       | |
| |   data        | |   to its      | |   relative     |