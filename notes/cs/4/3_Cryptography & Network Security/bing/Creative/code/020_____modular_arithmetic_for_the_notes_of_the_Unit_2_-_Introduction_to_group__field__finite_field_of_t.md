Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here are some notes on the topic of modular arithmetic for the Unit 2.

### Modular arithmetic

- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus.
- The modulus is denoted by a positive integer m, and the set of all integers that are congruent modulo m is denoted by Z_m.
- Two integers a and b are said to be congruent modulo m, written as a ≡ b (mod m), if they have the same remainder when divided by m. For example, 17 ≡ 5 (mod 12) because both 17 and 5 have the same remainder of 5 when divided by 12.
- Congruence modulo m is an equivalence relation, meaning that it satisfies the following properties:
  - Reflexive: a ≡ a (mod m) for any integer a.
  - Symmetric: if a ≡ b (mod m), then b ≡ a (mod m).
  - Transitive: if a ≡ b (mod m) and b ≡ c (mod m), then a ≡ c (mod m).
- Congruence modulo m also preserves the operations of addition, subtraction, and multiplication, meaning that the following properties hold:
  - If a ≡ b (mod m) and c ≡ d (mod m), then a + c ≡ b + d (mod m).
  - If a ≡ b (mod m) and c ≡ d (mod m), then a - c ≡ b - d (mod m).
  - If a ≡ b (mod m) and c ≡ d (mod m), then a * c ≡ b * d (mod m).
- However, congruence modulo m does not preserve the operation of division, meaning that the following property does not hold in general:
  - If a ≡ b (mod m) and c ≡ d (mod m), then a / c ≡ b / d (mod m).
- This is because division by zero is undefined, and some integers may not have a multiplicative inverse modulo m. For example, 2 / 4 ≡ 1 / 2 (mod 6), but 2 and 4 do not have multiplicative inverses modulo 6, so the equation does not make sense.
- A multiplicative inverse of an integer a modulo m is an integer b such that a * b ≡ 1 (mod m). For example, 3 is a multiplicative inverse of 5 modulo 8, because 3 * 5 ≡ 1 (mod 8).
- An integer a has a multiplicative inverse modulo m if and only if a and m are coprime, meaning that they have no common factors other than 1. For example, 6 and 9 are not coprime, because they have a common factor of 3, so 6 does not have a multiplicative inverse modulo 9.
- The set of all integers that have a multiplicative inverse modulo m is denoted by Z_m^*. For example, Z_8^* = {1, 3, 5, 7}.
- The size of Z_m^* is given by Euler's totient function, denoted by φ(m), which counts the number of positive integers less than or equal to m that are coprime to m. For example, φ(8) = 4, because there are 4 positive integers less than or equal to 8 that are coprime to 8, namely 1, 3, 5, and 7.
- Euler's totient function has some useful properties, such as:
  - If p is a prime number, then φ(p) = p - 1, because every positive integer less than p is coprime to p.
  - If p and q are distinct prime numbers, then φ(p * q) = (p - 1) * (q - 1), because every positive integer less than p * q is either coprime to both p and q, or divisible by either p or q, but not both.
  - If m and n are coprime, then φ(m * n) = φ(m) * φ(n), because every positive integer less than m * n is either coprime to both m and n, or divisible by a common factor of m and n, which is 1.
- Modular arithmetic is useful for many applications in cryptography, such as encryption, decryption, digital signatures, and