### Unit 2 - Introduction to Cryptography & Network Security

#### Group, Field, Finite Field of the form GF(p)
- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse.
- A field is a set with two binary operations, addition and multiplication, that satisfy the properties of a group and additional properties such as distributivity.
- A finite field is a field with a finite number of elements. A finite field of the form GF(p) has p elements, where p is a prime number.

#### Modular Arithmetic
- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value, called the modulus.
- The modulus is a positive integer, and the result of a modular operation is always in the range [0, modulus-1].

#### Prime and Relative Prime Numbers
- A prime number is a positive integer greater than 1 that is divisible by only 1 and itself.
- Two numbers are relatively prime if their greatest common divisor is 1.

#### Extended Euclidean Algorithm
- The extended Euclidean algorithm is an algorithm to compute the greatest common divisor of two numbers and the coefficients of Bézout's identity.

#### Advanced Encryption Standard (AES) Encryption and Decryption
- AES is a symmetric key encryption algorithm that uses a fixed-length key to encrypt and decrypt data blocks of a fixed size.
- The key length can be 128, 192, or 256 bits, and the block size is 128 bits.

#### Fermat’s and Euler’s Theorem
- Fermat's Little Theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) is congruent to 1 modulo p.
- Euler's Theorem states that if a and n are relatively prime, then a^φ(n) is congruent to 1 modulo n, where φ(n) is Euler's totient function.

#### Primality Testing
- Primality testing is the process of determining whether a given number is prime or composite.
- There are several algorithms for primality testing, including deterministic and probabilistic methods.

#### Chinese Remainder Theorem
- The Chinese Remainder Theorem is a theorem that provides a method for solving a system of simultaneous congruences with different moduli.

#### Discrete Logarithmic Problem
- The discrete logarithm problem is the problem of finding the exponent x in the equation b^x ≡ y (mod p), where p is a prime number and b and y are integers.

#### Principles of Public Key Crypto Systems
- Public key cryptography is a cryptographic system that uses a pair of keys, a public key and a private key, to encrypt and decrypt messages.
- The public key is used to encrypt messages, and the private key is used to decrypt them.

#### RSA Algorithm
- The RSA algorithm is a public key encryption algorithm that is widely used for secure data transmission.
- The security of the RSA algorithm is based on the difficulty of factoring large composite numbers.

#### Security of RSA
- The security of the RSA algorithm depends on the length of the key and the difficulty of factoring large composite numbers.
- As computational power increases, the key length must also increase to maintain security.
