 Here is the content in markdown format for the topic ### Extended Euclidean Algorithm for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security:

### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an extension of the Euclidean Algorithm which not only finds the greatest common divisor (GCD) of two integers but also finds the coefficients of Bézout's identity.

Bézout's identity states that for any two integers a and b, there exist integers x and y such that

ax + by = GCD(a, b)

The Extended Euclidean Algorithm finds such integers x and y.

The algorithm is as follows:

1. Let r0 = a, r1 = b, s0 = 1, s1 = 0, t0 = 0, t1 = 1
2. While r1 != 0
   - Let q = ⌊r0/r1⌋      // Integer division
   - Let r2 = r0 % r1    // Modulo
   - Let s2 = s0 - q*s1  // Coefficient computation
   - Let t2 = t0 - q*t1
   - Let r0 = r1
   - Let r1 = r2
   - Let s0 = s1
   - Let s1 = s2
   - Let t0 = t1
   - Let t1 = t2
3. GCD(a, b) = r0
4. The required Bézout coefficients are s0 and t0

The above algorithm can be generalized to find the GCD and Bézout coefficients of more than two integers.

Advantages:
- Finds the GCD and Bézout coefficients in one algorithm
- More efficient than calculating GCD and then finding Bézout coefficients separately

Applications:
- Used in RSA encryption scheme to compute multiplicative inverses modulo n
- Used in elliptic curve cryptography
- Used to solve Diophantine equations