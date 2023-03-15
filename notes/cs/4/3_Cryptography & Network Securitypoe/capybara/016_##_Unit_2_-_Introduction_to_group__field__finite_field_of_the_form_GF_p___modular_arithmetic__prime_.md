## Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

### Introduction

This unit focuses on various topics related to cryptography, including group theory, modular arithmetic, and public key cryptography. Understanding these concepts is essential for any cryptography practitioner. In this section, we will discuss each concept in detail.

### Group Theory

A group is a mathematical object that consists of a set of elements and a binary operation that combines any two elements to form a third element. To be considered a group, the operation must satisfy four axioms:

- Closure: The operation must combine any two elements in the group to form another element in the group.
- Associativity: The order in which the elements are combined does not matter.
- Identity: There exists an element called the identity element, such that when combined with any other element, it returns the same element.
- Inverse: For every element, there exists an inverse element such that when combined, they result in the identity element.

### Field and Finite Field of the form GF(p)

A field is a set of elements that support addition, subtraction, multiplication, and division. A finite field is a field with a finite number of elements. The notation GF(p) refers to a finite field of p elements, where p is a prime number. 

### Modular Arithmetic

Modular arithmetic is a type of arithmetic that involves performing operations on remainders. It is used extensively in cryptography, particularly in public key cryptography. In modular arithmetic, numbers "wrap around" after reaching a certain value, called the modulus. 

### Prime and Relative Prime Numbers

A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself. A relative prime number is a positive integer whose greatest common divisor with another positive integer is 1. 

### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an algorithm that calculates the greatest common divisor of two integers and also finds their corresponding Bezout coefficients. The algorithm is useful in solving problems related to modular arithmetic and public key cryptography.

### Advanced Encryption Standard (AES) encryption and decryption

AES is a symmetric encryption algorithm that is widely used in cryptography. It is a block cipher that encrypts data in blocks of fixed size. The algorithm uses a key, which must be known to both the sender and the receiver, to encrypt and decrypt data.

### Fermat’s and Euler’s theorem

Fermat's theorem states that if p is a prime number and a is any positive integer not divisible by p, then a^(p-1) ≡ 1 (mod p). Euler's theorem is a generalization of Fermat's theorem that applies to any positive integer n, not just prime numbers.

### Primarily testing

Primarily testing is the process of determining whether a given number is prime or composite. There are several algorithms for primarily testing, including the Miller-Rabin test and the AKS test.

### Chinese Remainder theorem

The Chinese Remainder Theorem is a theorem that states that if we have a system of linear congruences with pairwise relatively prime moduli, then there exists a unique solution modulo the product of the moduli.

### Discrete Logarithmic Problem

The Discrete Logarithmic Problem is a mathematical problem that arises in cryptography. Given a number g and a number y, the problem is to find an integer x such that g^x ≡ y (mod p), where p is a prime number.

### Principals of public key crypto systems

Public key cryptography allows two parties to communicate securely over an insecure channel without having to share a secret key. It relies on the use of public and private keys, where the public key is used for encryption and the private key is used for decryption.

### RSA algorithm

The RSA algorithm is a public key encryption algorithm that is widely used in cryptography. It relies on the difficulty of factoring large integers to ensure the security of the algorithm.

### Security of RSA

The security of RSA depends on the difficulty of factoring large integers. If an attacker is able to factor the modulus used in RSA, they can recover the private key and decrypt any messages encrypted using the corresponding public key. Therefore, it is essential to use large primes when generating RSA keys to ensure the security of the algorithm.