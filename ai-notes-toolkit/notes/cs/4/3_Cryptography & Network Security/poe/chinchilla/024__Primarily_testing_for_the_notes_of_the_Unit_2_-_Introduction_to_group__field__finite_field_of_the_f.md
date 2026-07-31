### Primarily testing for the notes of the Unit 2

In this unit, you will learn about various concepts related to cryptography and network security. Here are the key points that you should focus on:

1. Introduction to group, field, and finite field of the form GF(p):
   - A group is a set of elements with an operation that satisfies certain properties.
   - A field is a set of elements with two operations (addition and multiplication) that satisfy certain properties.
   - A finite field of the form GF(p) is a field with a finite number of elements, where p is a prime number.

2. Modular arithmetic:
   - Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value.
   - Modular arithmetic is useful in cryptography for generating pseudorandom numbers and performing encryption and decryption operations.

3. Prime and relative prime numbers:
   - A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.
   - Two integers are said to be relatively prime if they have no common factors other than 1.

4. Extended Euclidean Algorithm:
   - The Extended Euclidean Algorithm is a method for finding the greatest common divisor of two integers and their Bezout coefficients.
   - The Bezout coefficients can be used to solve linear Diophantine equations, which are important in cryptography.

5. Advanced Encryption Standard (AES) encryption and decryption:
   - AES is a symmetric key encryption algorithm that is widely used for securing data.
   - AES operates on blocks of plaintext and ciphertext, using a key to perform encryption and decryption operations.

6. Fermat’s and Euler’s theorem:
   - Fermat’s theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) ≡ 1 (mod p).
   - Euler’s theorem extends Fermat’s theorem to all positive integers a and integers n that are relatively prime, stating that a^φ(n) ≡ 1 (mod n), where φ(n) is the Euler totient function.

7. Chinese Remainder theorem:
   - The Chinese Remainder Theorem is a method for solving a system of linear congruences.
   - The theorem states that if n1, n2,..., nk are pairwise relatively prime integers, and a1, a2,..., ak are any integers, then there exists a unique integer x modulo N = n1n2...nk that satisfies the congruences x ≡ a1 (mod n1), x ≡ a2 (mod n2),..., x ≡ ak (mod nk).

8. Discrete Logarithmic Problem:
   - The Discrete Logarithmic Problem is a computational problem related to the discrete logarithm function.
   - The problem is difficult to solve in general, and its difficulty is the foundation for many cryptographic protocols.

9. Principals of public key crypto systems:
   - Public key cryptography is a cryptographic method that uses two keys: a public key and a private key.
   - The public key can be freely distributed, while the private key is kept secret.
   - Public key cryptography provides a way to securely exchange information without needing a shared secret key.

10. RSA algorithm:
   - The RSA algorithm is a widely used public key encryption algorithm.
   - The algorithm is based on the difficulty of factoring large integers, which is used to generate the public and private keys.

11. Security of RSA:
   - The security of RSA depends on the difficulty of factoring large integers.
   - RSA can be vulnerable to attacks if the keys are not generated properly or if the implementation is flawed.
   - Various techniques can be used to enhance the security of RSA, such as using longer key lengths, using padding schemes, and using randomization techniques.