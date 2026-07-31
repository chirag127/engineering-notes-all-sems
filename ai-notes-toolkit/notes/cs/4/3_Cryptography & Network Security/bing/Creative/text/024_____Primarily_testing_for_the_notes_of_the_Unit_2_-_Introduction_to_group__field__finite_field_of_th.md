Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security.

### Introduction to group, field, finite field of the form GF(p)

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse.
- A field is a group that also satisfies two additional properties: commutativity and distributivity.
- A finite field is a field that has a finite number of elements.
- A finite field of the form GF(p) is a field that has p elements, where p is a prime number.
- Modular arithmetic is a system of arithmetic where numbers are reduced to a remainder after dividing by a fixed modulus.
- Prime numbers are numbers that have exactly two positive divisors: 1 and themselves.
- Relative prime numbers are numbers that have no common positive divisors other than 1.

### Extended Euclidean Algorithm

- The Extended Euclidean Algorithm is a method to find the greatest common divisor (GCD) of two numbers and also the coefficients of a linear combination of the two numbers that equals the GCD.
- The algorithm is based on the following identity: GCD(a, b) = GCD(b, a mod b).
- The algorithm can be used to find the multiplicative inverse of a number modulo another number, which is useful for encryption and decryption.

### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric-key block cipher that encrypts and decrypts data in 128-bit blocks.
- AES uses a secret key of 128, 192, or 256 bits, which is expanded into a series of round keys using a key expansion algorithm.
- AES encryption consists of four stages: AddRoundKey, SubBytes, ShiftRows, and MixColumns, which are repeated for a number of rounds depending on the key size.
- AES decryption consists of the inverse stages: InvMixColumns, InvShiftRows, InvSubBytes, and AddRoundKey, which are repeated in reverse order for the same number of rounds.

### Fermat’s and Euler’s theorem

- Fermat's theorem states that if p is a prime number and a is any integer, then a^p ≡ a (mod p).
- Euler's theorem states that if a and n are relatively prime, then a^φ(n) ≡ 1 (mod n), where φ(n) is the Euler's totient function that counts the number of positive integers less than n that are relatively prime to n.
- Both theorems are useful for encryption and decryption using modular exponentiation.

### Primality testing

- Primality testing is the problem of determining whether a given number is prime or composite.
- There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test, etc.
- Some algorithms are deterministic, meaning they always give the correct answer, while some are probabilistic, meaning they give a high probability of the correct answer.
- Primality testing is important for generating large prime numbers for public-key cryptography.

### Chinese Remainder theorem

- The Chinese Remainder theorem states that if n1, n2, ..., nk are pairwise relatively prime positive integers, and a1, a2, ..., ak are any integers, then there exists a unique integer x such that x ≡ a1 (mod n1), x ≡ a2 (mod n2), ..., x ≡ ak (mod nk), and 0 ≤ x < n1n2...nk.
- The theorem also provides a method to find x using the extended Euclidean algorithm and modular arithmetic.
- The theorem can be used to speed up modular exponentiation and RSA encryption and decryption.

### Discrete Logarithmic Problem

- The discrete logarithmic problem is the problem of finding x given