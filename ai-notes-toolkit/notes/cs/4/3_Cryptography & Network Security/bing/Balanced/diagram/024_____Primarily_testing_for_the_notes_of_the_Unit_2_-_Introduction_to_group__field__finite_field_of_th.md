Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 of Cryptography and Network Security:

### Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm

- A **group** is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse. For example, the set of integers with addition is a group.
- A **field** is a group with an additional binary operation that satisfies four more properties: closure, associativity, identity, and inverse. The additional operation is also commutative and distributive over the first operation. For example, the set of rational numbers with addition and multiplication is a field.
- A **finite field** is a field with a finite number of elements. A finite field of the form GF(p) is a field with p elements, where p is a prime number. For example, GF(2) is a field with two elements: 0 and 1.
- **Modular arithmetic** is a system of arithmetic where numbers are reduced to a fixed range by using the remainder operation. For example, in modulo 7 arithmetic, 8 is equivalent to 1, since 8 mod 7 = 1.
- A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, etc. are prime numbers.
- Two numbers are **relatively prime** or **coprime** if they have no common positive divisors other than 1. For example, 8 and 15 are relatively prime, since their only common divisor is 1.
- The **Extended Euclidean Algorithm** is a method to find the greatest common divisor (GCD) of two numbers and also the coefficients of a linear combination of the two numbers that equals the GCD. For example, the GCD of 30 and 18 is 6, and 6 = 2 * 30 - 3 * 18.

### Advanced Encryption Standard (AES) encryption and decryption

- **AES** is a symmetric-key block cipher that encrypts and decrypts data in 128-bit blocks. It uses a secret key of 128, 192, or 256 bits, and performs 10, 12, or 14 rounds of transformation, depending on the key size.
- The encryption process consists of four steps: key expansion, initial round, main rounds, and final round. The key expansion generates round keys from the secret key using a recursive function. The initial round adds the first round key to the plaintext block using bitwise XOR. The main rounds perform four operations: byte substitution, row shift, column mix, and round key addition. The final round omits the column mix operation.
- The decryption process is the reverse of the encryption process, using the inverse operations and the round keys in reverse order. The inverse operations are: inverse byte substitution, inverse row shift, inverse column mix, and round key addition.

### Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA

- **Fermat's theorem** states that if p is a prime number and a is any integer, then a^p mod p = a mod p. This can be used to test if a number is prime by checking if the equation holds for some values of a.
- **Euler's theorem** states that if a and n are relatively prime, then a^phi(n) mod n = 1, where phi(n) is the Euler's totient function that counts the number of positive integers less than n that are relatively prime to n. This can be used to simplify modular exponentiation by reducing the exponent modulo phi(n).
- **Primality testing** is the problem of determining if a given number is prime or composite. There are various algorithms for primality testing, such as trial division, Fermat's test, Miller-Rabin test, etc. Some of them are deterministic, while others are probabilistic, meaning they can give false positives with a small probability.
- **Chinese Remainder theorem** states that if n1, n2, ..., nk are pairwise coprime positive integers, and a1, a2, ..., ak are any integers, then there exists a unique integer x such that x mod ni = ai for all