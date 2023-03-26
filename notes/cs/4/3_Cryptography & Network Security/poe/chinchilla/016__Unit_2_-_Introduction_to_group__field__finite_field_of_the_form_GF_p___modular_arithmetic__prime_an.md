## Unit 2 - Introduction to Cryptography

Cryptography is the practice of secure communication in the presence of third parties. Cryptography has been used for centuries to protect communication from unauthorized access. In this unit, we will introduce various concepts related to cryptography, including group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA.

### Group

A group is a set of elements with a binary operation that satisfies certain properties, such as associativity, identity, and inverse. Groups can be used to represent mathematical structures, such as symmetries and transformations.

### Field

A field is a set of elements with two binary operations, addition and multiplication, that satisfy certain properties, such as associativity, commutativity, distributivity, and the existence of inverses. Fields can be used to represent real numbers, complex numbers, and finite fields.

### Finite Field of the Form GF(p)

A finite field of the form GF(p) is a field with a finite number of elements, where p is a prime number. Finite fields are used in cryptography to perform arithmetic operations on integers represented as elements of the field.

### Modular Arithmetic

Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after a certain modulus. Modular arithmetic is used in cryptography to perform arithmetic operations on integers in a finite field.

### Prime and Relative Prime Numbers

A prime number is a positive integer greater than one that has no positive integer divisors other than one and itself. Relative prime numbers are two integers that have no common divisors other than one. Prime and relative prime numbers are used in cryptography for key generation and encryption.

### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an algorithm for finding the greatest common divisor (GCD) of two integers and their respective Bezout coefficients. The Extended Euclidean Algorithm is used in cryptography to find multiplicative inverses in a finite field.

### Advanced Encryption Standard (AES) Encryption and Decryption

The Advanced Encryption Standard (AES) is a symmetric encryption algorithm that uses a block cipher to encrypt and decrypt data. AES is used in cryptography to secure sensitive data, such as financial transactions and military communications.

### Fermat’s and Euler’s Theorem

Fermat’s and Euler’s theorem are two theorems in number theory that relate to modular arithmetic. Fermat’s theorem states that if p is a prime number and a is an integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p. Euler’s theorem states that if a and n are coprime integers, then a^(phi(n)) is congruent to 1 modulo n, where phi(n) is the Euler totient function.

### Primarily Testing

Primarily testing is a method of determining whether a given number is prime. Primarily testing is used in cryptography to generate large prime numbers for key generation.

### Chinese Remainder Theorem

The Chinese Remainder Theorem is a theorem in number theory that relates to modular arithmetic. The Chinese Remainder Theorem states that if n1, n2, ..., nk are pairwise relatively prime integers greater than one, a1, a2, ..., ak are any integers, then there exists an integer x that satisfies the simultaneous congruences x is congruent to a1 modulo n1, x is congruent to a2 modulo n2, ..., x is congruent to ak modulo nk.

### Discrete Logarithmic Problem

The Discrete Logarithmic Problem is a computational problem in number theory that is difficult to solve. The Discrete Logarithmic Problem is used in cryptography to generate large prime numbers for key generation and to perform public-key encryption.

### Principals of Public Key Crypto Systems

Public key cryptography is a cryptographic system that uses pairs of keys, a public key and a private key, to perform encryption and decryption. The security of public key cryptography is based on the difficulty of certain mathematical problems, such as the Discrete Logarithmic Problem and the Integer Factorization Problem.

### RSA Algorithm

The RSA algorithm is a public key encryption algorithm that is widely used in cryptography. The RSA algorithm is based on the difficulty of factoring large integers and is used to secure sensitive data, such as financial transactions and military communications.

### Security of RSA

The security of RSA is based on the difficulty of factoring large integers. However, there are some attacks on RSA that exploit weaknesses in the implementation or the random number generation. To ensure the security of RSA, it is important to use a large key size, a secure implementation, and a good random number generator.