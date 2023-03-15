 Here are the notes for ### Chinese Remainder theorem for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security:

### Chinese Remainder theorem:
- The Chinese Remainder theorem states that if n1, n2, ..., nk are pairwise coprime integers, then the system of congruences:
x ≡ a1 (mod n1)
x ≡ a2 (mod n2)
...
x ≡ ak (mod nk)
has a unique solution modulo the product N = n1n2...nk.
- The Chinese Remainder theorem can be used to solve a system of linear congruences and has applications in various areas like cryptography.
- Proof: Given in the wiki article - https://en.wikipedia.org/wiki/Chinese_remainder_theorem

Mnemonics/Learning tricks:
- Pairwise coprime: Numbers whose greatest common divisor is 1. Memorize the phrase 'pairwise coprime' to remember this condition of the Chinese Remainder theorem.
- Product of moduli: The solution is modulo the product of all the moduli. Associate the product of all the moduli n1n2...nk to the solution being modulo this product.

Examples:
- Find the solution to:
x ≡ 3 (mod 5)
x ≡ 7 (mod 11)
Here, n1 = 5, n2 = 11 and N = 5*11 = 55
Using the Chinese Remainder theorem, the solution is x = 3*11 + 7 (mod 55) = 32 (mod 55)

Applications:
- The Chinese Remainder theorem is used in cryptography to construct a public key in the RSA cryptosystem.
- It is used to solve a system of linear congruences and has applications in number theory and computer science.

Advantages:
- The Chinese Remainder theorem provides a way to solve a system of linear congruences in a efficient manner.
- It has useful applications in various fields like cryptography.

Disadvantages:
- The numbers n1, n2, ..., nk must be pairwise coprime for the Chinese Remainder theorem to hold. This coprimality condition may not always be satisfied.
- The solution is modulo the product N = n1n2...nk which can be very large. This can lead to computational issues while implementing the theorem.