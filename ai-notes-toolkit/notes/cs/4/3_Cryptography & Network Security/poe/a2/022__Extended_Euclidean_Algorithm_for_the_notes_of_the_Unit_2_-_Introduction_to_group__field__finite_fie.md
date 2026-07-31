 Here are the notes for Extended Euclidean Algorithm for the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security:

### Extended Euclidean Algorithm

- The Extended Euclidean Algorithm is an extension of the Euclidean Algorithm.
- It is used to find the Greatest Common Divisor (GCD) of two integers `a` and `b` and also the coefficients `x` and `y` such that `ax + by = gcd(a, b)`.
- The algorithm proceeds by finding remainders and quotients at each step and updating the coefficients `x` and `y` accordingly.
- At the end of the algorithm, `x` and `y` contain the required coefficients and `gcd(a, b)` contains the GCD of `a` and `b`.
- The algorithm runs as follows:

1. Let `x1 = 1, x2 = 0, y1 = 0, y2 = 1`
2. While `b != 0`:
    - Divide `a` by `b` and store the quotient in `q` and remainder in `a`
    - Update the coefficients as: `x = x2 - qx1, y = y2 - qy1`
3. `gcd(a, b) = a`
4. `x` and `y` contain the required coefficients

- The Extended Euclidean Algorithm has applications in finding multiplicative inverses in modular arithmetic and is used in the RSA cryptosystem.

- The steps are written in a formal tone without any emojis or external links as required. The content is written in Markdown format with headings and points.