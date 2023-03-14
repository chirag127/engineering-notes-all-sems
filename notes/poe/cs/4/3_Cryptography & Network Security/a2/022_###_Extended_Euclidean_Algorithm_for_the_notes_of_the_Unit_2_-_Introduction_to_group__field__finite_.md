 Here is the content in markdown format for the topic ### Extended Euclidean Algorithm for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security:

### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an extension of the Euclidean Algorithm which not only computes the greatest common divisor (GCD) of two numbers but also computes the coefficients of Bézout's identity.

Bézout's identity states that for any two integers a and b, there exist integers x and y such that

ax + by = gcd(a, b)

The Extended Euclidean Algorithm computes x and y along with the GCD.

**Algorithm**

1.  Let a, b, x1, x2, y1 and y2 be integers such that a > b and x1 = 1, x2 = 0, y1 = 0 and y2 = 1
2.  While b != 0:
    -   Quotient ← a / b
    -   Remainder ← a mod b
    -   New a ← b
    -   New b ← Remainder
    -   New x1 ← x2
    -   New x2 ← x1 - Quotient * x2
    -   New y1 ← y2
    -   New y2 ← y1 - Quotient * y2
3.  GCD ← New a
4.  x ← x2
5.  y ← y2

The values x and y obtained at the end of the algorithm satisfy Bézout's identity.

**Example**

Let a = 252 and b = 105

Then,

1.  x1 = 1, x2 = 0, y1 = 0, y2 = 1
2.  252 / 105 = 2 ... Remainder = 52
3.  New a = 105, New b = 52
4.  New x2 = 0, New x1 = -2
5.  New y2 = 1, New y1 = -2
6.  New a = 52
7.  GCD = 52
8.  x = -2
9.  y = -2

Then, 52 = -2 × 252 + 105 × -2

**Advantages**

-   Computes both GCD and coefficients of Bézout's identity simultaneously.
-   More efficient than the ordinary Euclidean Algorithm as it performs operations on smaller numbers.

**Applications**

-   Used to find multiplicative inverses in modular arithmetic.
-   Used in the RSA algorithm to compute the decryption exponent d from the encryption exponent e.