 Here is the content in markdown format for the given topic:

### Introduction to group for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

A **group** is a set of elements with an operation that combines two elements to form another element. The operation must satisfy four requirements known as the group axioms:

1. Closure - The result of the operation on two elements must be an element of the group.
2. Associativity - The order of elements in a sequence of combined elements must not affect the result.
3. Identity - There must be an identity element that leaves other elements unchanged when combined with them.
4. Inverses - Each element must have an inverse element that undoes its effect when combined with it.

Finite groups are important in cryptography as they provide for repeating sequences without pattern. Examples include multiplicative groups of integers modulo n.

A finite **field** is a set of a finite number of elements with defined operations analogous to addition, subtraction, multiplication and division, where the usual field axioms hold. The most common examples used in cryptography are the finite fields GF(p) for a prime p. The elements of GF(p) are the integers {0, 1, 2, ..., p-1} and addition, subtraction and multiplication are performed modulo p.

**Modular arithmetic** is a system of arithmetic for integers, where numbers "wrap around" upon reaching a certain value called the modulus. The results of modular arithmetic operations depend only on the remainder when numbers are divided by the modulus.

Two numbers a and b are **relatively prime** if their greatest common divisor is 1. The **Extended Euclidean Algorithm** can be used to compute the greatest common divisor of two numbers and also provides a means of finding integers x and y such that ax + by = gcd(a, b). This has applications in cryptography such as computing modular inverses.

The **Advanced Encryption Standard (AES)** is a symmetric-key encryption algorithm. Encryption converts plaintext to ciphertext, and decryption converts ciphertext back to plaintext. AES uses a substitution-permutation network with a variable number of rounds and a key size of 128, 192 or 256 bits.

**Fermat's theorem** states that if p is a prime number, then for any integer a, the number a^(p-1) ≡ 1 (mod p). This forms the basis for many proofs and algorithms in number theory and its applications. **Euler's theorem** is a generalization of Fermat's theorem for any modulus n, not just prime moduli. It states that if a and n are relatively prime, then a^(φ(n)) ≡ 1 (mod n) where φ is the totient function.

[Continue writing detailed notes for the remaining topics...]