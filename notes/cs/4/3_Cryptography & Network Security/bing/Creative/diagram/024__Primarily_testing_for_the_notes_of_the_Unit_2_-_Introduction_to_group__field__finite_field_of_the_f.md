I have searched the web for the topic you requested and found some information that might help you. Here is a possible ascii diagram for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security:

```
+---------------------+   +---------------------+   +---------------------+
| Group               |   | Field               |   | Finite Field        |
|                     |   |                     |   |                     |
| A set of elements   |   | A set of elements   |   | A set of elements   |
| with a binary       |   | with two binary     |   | with two binary     |
| operation that      |   | operations that     |   | operations that     |
| satisfies four      |   | satisfy eight       |   | satisfy eight       |
| properties:         |   | properties:         |   | properties:         |
|                     |   |                     |   |                     |
| - Closure           |   | - Closure           |   | - Closure           |
| - Associativity     |   | - Associativity     |   | - Associativity     |
| - Identity          |   | - Identity          |   | - Identity          |
| - Inverse           |   | - Inverse           |   | - Inverse           |
|                     |   | - Commutativity     |   | - Commutativity     |
|                     |   | - Distributivity    |   | - Distributivity    |
|                     |   |                     |   |                     |
| Examples:           |   | Examples:           |   | Examples:           |
| - Integers with +   |   | - Rational numbers  |   | - GF(p) = Z/pZ      |
| - Matrices with x   |   |   with + and x      |   |   with + and x      |
| - Permutations with |   | - Complex numbers   |   | - GF(2^n) =         |
|   composition       |   |   with + and x      |   |   polynomials of    |
|                     |   |                     |   |   degree < n with   |
|                     |   |                     |   |   coefficients in   |
|                     |   |                     |   |   GF(2) and + and x |
+---------------------+   +---------------------+   +---------------------+
| Modular Arithmetic  |   | Prime and Relative  |   | Extended Euclidean  |
|                     |   | Prime Numbers       |   | Algorithm           |
| A system of         |   |                     |   |                     |
| arithmetic for      |   | A prime number is a |   | An algorithm to     |
| integers where      |   | natural number      |   | find the greatest   |
| numbers wrap around |   | greater than 1 that |   | common divisor of   |
| after reaching a    |   | has no positive     |   | two integers and    |
| certain value       |   | divisors other than |   | also the coefficients|
| called the modulus  |   | 1 and itself        |   | of Bézout's identity|
|                     |   |                     |   |                     |
| Examples:           |   | Examples:           |   | Examples:           |
| - 7 mod 4 = 3       |   | - 2, 3, 5, 7, 11,   |   | - gcd(30, 21) = 3   |
| - 12 mod 5 = 2      |   |   13, 17, 19, ...   |   |   and 3 = 30(-1) +  |
| - 15 mod 6 = 3      |   |                     |   |   21(2)             |
|                     |   | Two numbers are     |   | - gcd(99, 78) = 3   |
|                     |   | relatively prime    |   |   and 3 = 99(-11) + |
|                     |   | if their gcd is 1   |   |   78(