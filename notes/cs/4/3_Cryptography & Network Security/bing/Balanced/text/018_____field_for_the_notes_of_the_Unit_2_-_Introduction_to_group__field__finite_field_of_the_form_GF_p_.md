Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 of Cryptography and Network Security:

### Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with addition is a group.
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as commutativity, distributivity, and the existence of a multiplicative inverse for every nonzero element. For example, the set of rational numbers with addition and multiplication is a field.
- A finite field is a field that has a finite number of elements. For example, the set of integers modulo a prime number p, denoted by GF(p), is a finite field with p elements. In GF(p), the addition and multiplication are performed modulo p, which means the remainder after dividing by p. For example, in GF(5), 2 + 3 = 0 and 2 * 3 = 1.
- Modular arithmetic is a system of arithmetic where numbers are reduced to a fixed range of values by using the modulo operation. For example, in modulo 12 arithmetic, 15 is equivalent to 3, because 15 mod 12 = 3. Modular arithmetic is useful for cryptography because it allows operations to be performed on large numbers without overflow or loss of precision.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, etc. are prime numbers. Prime numbers are important for cryptography because they are the building blocks of finite fields and many cryptographic algorithms rely on their properties.
- Two numbers are relatively prime or coprime if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, because their only common divisor is 1. Two numbers are relatively prime if and only if their greatest common divisor (GCD) is 1. The GCD of two numbers can be computed using the Euclidean algorithm, which repeatedly applies the division algorithm until the remainder is zero. For example, to find the GCD of 24 and 60, we can apply the following steps:

  - 60 = 24 * 2 + 12
  - 24 = 12 * 2 + 0
  - The last nonzero remainder is 12, so GCD(24, 60) = 12.

- The Extended Euclidean Algorithm is an extension of the Euclidean algorithm that also computes the coefficients of a linear combination of the two numbers that equals their GCD. For example, to find the coefficients of 24 and 60 that give their GCD 12, we can apply the following steps:

  - 60 = 24 * 2 + 12, so 12 = 60 - 24 * 2
  - 24 = 12 * 2 + 0, so 24 = 12 * 2
  - Substituting the second equation into the first, we get 12 = 60 - (12 * 2) * 2 = 60 - 24 * 4
  - Therefore, the coefficients are 1 and -4, so 12 = 1 * 60 + (-4) * 24.

### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric-key block cipher that encrypts and decrypts data in blocks of 128 bits using a secret key of 128, 192, or 256 bits. AES is the standard for encryption and decryption of data in many applications and protocols, such as Wi-Fi, VPN, SSL, TLS, etc.
- AES encryption and decryption consist of four main steps: key expansion, initial round, rounds, and final round. Each step involves applying various transformations to the data and the key, such as substitution, permutation, XOR, and arithmetic operations. The number of rounds depends on the key size: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys.
- Key expansion is the process of generating a series of round keys from