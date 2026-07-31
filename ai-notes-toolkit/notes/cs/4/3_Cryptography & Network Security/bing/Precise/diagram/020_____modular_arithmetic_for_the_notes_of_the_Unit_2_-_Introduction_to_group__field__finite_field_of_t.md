### Modular Arithmetic

Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after they reach a certain value called the modulus. It is often used in cryptography and computer science, particularly in the field of public-key cryptography.

1. In modular arithmetic, two integers are said to be congruent modulo n if their difference is divisible by n. This is written as a ≡ b (mod n).
2. The set of integers modulo n, denoted by Zn, is the set of all congruence classes of integers modulo n.
3. Addition, subtraction, and multiplication can be performed in modular arithmetic just as in ordinary arithmetic, with the result being taken modulo n.
4. Division is not always possible in modular arithmetic. However, if a and n are relatively prime, then there exists an integer b such that ab ≡ 1 (mod n). This integer b is called the modular inverse of a modulo n.
5. The extended Euclidean algorithm can be used to find the modular inverse of a modulo n.
6. Fermat's Little Theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) ≡ 1 (mod p).
7. Euler's Totient Theorem states that if a and n are relatively prime, then a^φ(n) ≡ 1 (mod n), where φ(n) is the Euler totient function.
8. The Chinese Remainder Theorem can be used to solve systems of congruences.
9. The Discrete Logarithm Problem is the problem of finding an integer x such that a^x ≡ b (mod n) for given integers a, b, and n.
