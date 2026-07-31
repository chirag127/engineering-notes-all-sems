Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 of Cryptography and Network Security:

### Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm

- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with addition is a group.
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as commutativity, distributivity, and non-zero inverses. For example, the set of rational numbers with addition and multiplication is a field.
- A finite field is a field that has a finite number of elements. For example, the set of integers modulo a prime number p, denoted by GF(p), is a finite field with p elements.
- Modular arithmetic is a system of arithmetic where numbers are reduced to a fixed range by using the remainder operation. For example, in modulo 12 arithmetic, 15 is equivalent to 3, since 15 mod 12 = 3.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, etc. are prime numbers.
- Two numbers are relatively prime if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, since their only common divisor is 1.
- The Extended Euclidean Algorithm is a method to find the greatest common divisor (gcd) of two numbers, as well as the coefficients of a linear combination of the two numbers that equals the gcd. For example, the gcd of 30 and 18 is 6, and 6 = 2 * 30 - 3 * 18, so the coefficients are 2 and -3.

### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric-key block cipher that encrypts and decrypts data in 128-bit blocks, using a secret key of 128, 192, or 256 bits.
- AES encryption consists of four stages: AddRoundKey, SubBytes, ShiftRows, and MixColumns, that are repeated for a number of rounds depending on the key size. The final round omits the MixColumns stage.
- AES decryption consists of the inverse stages of encryption: InvMixColumns, InvShiftRows, InvSubBytes, and AddRoundKey, that are repeated for the same number of rounds as encryption. The first round omits the InvMixColumns stage.
- AddRoundKey is a stage where each byte of the state is XORed with a corresponding byte of the round key, which is derived from the secret key using a key expansion algorithm.
- SubBytes is a stage where each byte of the state is replaced by another byte according to a predefined substitution table, called the S-box.
- ShiftRows is a stage where each row of the state is cyclically shifted to the left by a certain number of bytes, depending on the row number.
- MixColumns is a stage where each column of the state is multiplied by a fixed polynomial in a finite field, resulting in a new column.
- InvMixColumns, InvShiftRows, and InvSubBytes are the inverse operations of MixColumns, ShiftRows, and SubBytes, respectively, using different tables or polynomials.

### Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem

- Fermat's theorem states that if p is a prime number and a is any integer, then a^p mod p = a mod p. This can be used to test whether a number is prime or not, by choosing a random base a and checking the equation. However, this test is not reliable, since there are some composite numbers, called Carmichael numbers, that satisfy the equation for any base a.
- Euler's theorem states that if a and n are relatively prime, then a^phi(n) mod n = 1, where phi(n) is the Euler's totient function, which counts the number of positive integers less than n that are relatively prime to n. This is a generalization of Fermat's theorem, since phi(p) = p - 1 for any prime p.
- Primality testing is the problem of determining whether a given number is prime or not. There are various algorithms