### Unit 2 - Introduction to Cryptography & Network Security

In this unit, you will learn about the following topics:
- Group and field
- Finite field of the form GF(p)
- Modular arithmetic
- Prime and relative prime numbers
- Extended Euclidean Algorithm
- Advanced Encryption Standard (AES) encryption and decryption
- Fermat’s and Euler’s theorem
- Primarily testing
- Chinese Remainder theorem
- Discrete Logarithmic Problem
- Principals of public key crypto systems
- RSA algorithm
- Security of RSA

#### Group and Field
- A group is a set of elements with a binary operation that satisfies certain properties like associativity, identity, and inverse.
- A field is a set of elements with two operations, addition and multiplication, that satisfies certain properties like commutativity, distributivity, and existence of additive and multiplicative inverses.

#### Finite field of the form GF(p)
- A finite field of the form GF(p) is a field with a finite number of elements, where p is a prime number.
- The elements of GF(p) are the integers between 0 and p-1.
- Addition and multiplication in GF(p) are done modulo p.

#### Modular arithmetic
- Modular arithmetic is a way of doing arithmetic with remainders.
- In modular arithmetic, we work with a modulus, which is a positive integer.
- The result of an operation is the remainder when the operation is divided by the modulus.

#### Prime and relative prime numbers
- A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.
- Two positive integers are said to be relatively prime if they have no common positive integer divisors other than 1.

#### Extended Euclidean Algorithm
- The Extended Euclidean Algorithm is an algorithm to compute the greatest common divisor (GCD) of two integers a and b, as well as the coefficients x and y that satisfy ax + by = gcd(a,b).

#### Advanced Encryption Standard (AES) encryption and decryption
- AES is a symmetric encryption algorithm that uses a block cipher with a block size of 128 bits.
- AES has three key sizes: 128 bits, 192 bits, and 256 bits.
- AES encryption and decryption involve several rounds of operations like substitution, permutation, and XOR.

#### Fermat’s and Euler’s theorem
- Fermat’s theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) ≡ 1 (mod p).
- Euler’s theorem states that if a and n are relatively prime positive integers, then a^φ(n) ≡ 1 (mod n), where φ(n) is the Euler totient function.

#### Primarily testing
- Primarily testing is an algorithm to determine whether a given positive integer is a prime number.
- There are several algorithms for primarily testing, like Trial Division, Miller-Rabin, and AKS.

#### Chinese Remainder theorem
- The Chinese Remainder theorem is a theorem in number theory and modular arithmetic.
- The theorem states that if n1, n2, ..., nk are pairwise relatively prime positive integers, and a1, a2, ..., ak are any integers, then the system of congruences:
x ≡ a1 (mod n1)
x ≡ a2 (mod n2)
...
x ≡ ak (mod nk)
has a unique solution modulo N = n1n2...nk.

#### Discrete Logarithmic Problem
- The Discrete Logarithmic Problem is a problem in number theory and cryptography.
- The problem is to find an integer x such that a^x ≡ b (mod p), where p is a prime number and a and b are positive integers.

#### Principals of public key crypto systems
- Public key cryptography is a cryptographic system that uses two keys, a public key and a private key.
- The public key is used for encryption, and the private key is used for decryption.
- Public key cryptography has several applications, like secure communication and digital signatures.

#### RSA algorithm
- RSA is a public key encryption algorithm.
- RSA involves several steps, like key generation, encryption, and decryption.
- RSA is based on the difficulty of factoring large composite numbers.

#### Security of RSA
- The security of RSA depends on the difficulty of factoring large composite numbers.
- There are several attacks on RSA, like Brute Force, Frequency Analysis, and Side-Channel.
- To enhance the security of RSA, techniques like key size increase, padding, and randomization are used.