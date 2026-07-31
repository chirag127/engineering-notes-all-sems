### Unit 2 - Introduction to Cryptography & Network Security

#### Group, Field, Finite Field of the form GF(p)
- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse.
- A field is a set with two binary operations, addition and multiplication, that satisfy the properties of a group under addition and a group under multiplication, with the additional property of distributivity.
- A finite field is a field with a finite number of elements. A finite field of the form GF(p) is a field with p elements, where p is a prime number.

#### Modular Arithmetic
- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value, called the modulus.
- In modular arithmetic, two numbers are considered equivalent if they have the same remainder when divided by the modulus.

#### Prime and Relative Prime Numbers
- A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
- Two numbers are relatively prime if their greatest common divisor is 1.

#### Extended Euclidean Algorithm
- The extended Euclidean algorithm is an extension of the Euclidean algorithm that computes, in addition to the greatest common divisor of two integers, the coefficients of Bézout's identity.

#### Advanced Encryption Standard (AES) Encryption and Decryption
- The Advanced Encryption Standard (AES) is a symmetric key encryption algorithm that was chosen by the U.S. government to replace the Data Encryption Standard (DES).
- AES uses a block cipher, where the plaintext is divided into blocks of a fixed size and each block is encrypted separately.

#### Fermat’s and Euler’s Theorem
- Fermat's Little Theorem states that if p is a prime number, then for any integer a, the number a^p - a is an integer multiple of p.
- Euler's Theorem states that if a and n are relatively prime, then a^φ(n) ≡ 1 (mod n), where φ(n) is Euler's totient function.

#### Primality Testing
- Primality testing is the process of determining whether a given number is prime or composite.
- There are several algorithms for primality testing, including the deterministic Miller-Rabin test and the probabilistic Solovay-Strassen test.

#### Chinese Remainder Theorem
- The Chinese Remainder Theorem is a theorem that provides a method for solving a system of simultaneous congruences.
- The theorem states that if the moduli of the congruences are pairwise coprime, then there exists a unique solution to the system of congruences modulo the product of the moduli.

#### Discrete Logarithmic Problem
- The discrete logarithm problem is the problem of finding the exponent x in the equation b^x ≡ y (mod p), where p is a prime number and b and y are integers.
- The difficulty of solving the discrete logarithm problem is the basis for the security of several cryptographic algorithms, including the Diffie-Hellman key exchange and the ElGamal encryption.

#### Principals of Public Key Crypto Systems
- Public key cryptography, also known as asymmetric cryptography, is a cryptographic system that uses pairs of keys: public keys, which may be disseminated widely, and private keys, which are known only to the owner.
- The security of public key cryptography is based on the assumption that it is computationally infeasible to compute the private key from the public key.

#### RSA Algorithm
- The RSA algorithm is a public key encryption algorithm that was developed by Ron Rivest, Adi Shamir, and Leonard Adleman.
- The security of the RSA algorithm is based on the difficulty of factoring large composite numbers.

#### Security of RSA
- The security of the RSA algorithm depends on the length of the key used and the strength of the encryption algorithm.
- It is recommended to use a key length of at least 2048 bits for RSA encryption to ensure adequate security.