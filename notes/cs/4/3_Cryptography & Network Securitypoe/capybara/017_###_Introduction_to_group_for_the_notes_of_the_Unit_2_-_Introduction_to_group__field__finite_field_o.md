### Introduction to Group

A group is a set of elements with a binary operation that follows certain properties. In order for a set to be a group, it must satisfy the following four axioms: closure, associativity, identity, and inverse. 

- Closure: For any two elements a and b in the group, their product (a * b) must also be in the group.
- Associativity: The order in which we perform the binary operation does not matter. That is, (a * b) * c = a * (b * c).
- Identity: There exists an element e in the group such that a * e = e * a = a, where e is called the identity element.
- Inverse: For every element a in the group, there exists an element a^-1 such that a * a^-1 = a^-1 * a = e, where a^-1 is called the inverse of a.

Groups are important in cryptography because they provide a framework for constructing and analyzing cryptographic algorithms. 

### Field and Finite Field of the Form GF(p)

A field is a set of elements with two binary operations: addition and multiplication. In order for a set to be a field, it must satisfy the following properties: 

- The set must be closed under addition and multiplication
- Addition and multiplication must be associative and commutative
- There exist identity elements for addition and multiplication
- Every non-zero element has a multiplicative inverse
- Addition and multiplication must distribute over each other

A finite field of the form GF(p) is a field with p elements, where p is a prime number. GF(p) is also called a prime field or a Galois field. Finite fields are useful in cryptography because they provide a way to do arithmetic with integers modulo a prime number.

### Modular Arithmetic, Prime and Relative Prime Numbers

Modular arithmetic is a system of arithmetic for integers that involves only their remainders when divided by a fixed divisor. In modular arithmetic, we work with numbers that are congruent modulo a fixed number, called the modulus. 

- If two numbers a and b have the same remainder when divided by the modulus, we say that they are congruent modulo the modulus, written as a ≡ b (mod m).
- Addition and multiplication in modular arithmetic are performed in the same way as regular addition and multiplication, except that we take the remainder when dividing by the modulus.

Prime numbers are an important concept in number theory and cryptography. A prime number is a number that is only divisible by 1 and itself. 

Two numbers are relatively prime if they have no common factors other than 1. Relatively prime numbers are important in number theory and cryptography because they provide a way to construct modular inverses.

### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an algorithm for finding the greatest common divisor (GCD) of two integers, as well as the coefficients of a linear combination of those integers that equals their GCD. The algorithm can also be used to find modular inverses.

The algorithm works by repeatedly applying the division algorithm and the fact that the GCD of two numbers is the same as the GCD of one of the numbers and the remainder of the division of the other number by the first number.

### Advanced Encryption Standard (AES) Encryption and Decryption

The Advanced Encryption Standard (AES) is a symmetric key encryption algorithm that is widely used in modern cryptography. AES operates on fixed-length blocks of data and uses a key to encrypt and decrypt the data.

The algorithm uses a series of substitution and permutation operations to transform the data, and the key is used to determine the specific transformations that are applied.

### Fermat’s and Euler’s Theorem

Fermat’s and Euler’s Theorem are two important results in number theory and cryptography. 

Fermat’s Theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) ≡ 1 (mod p).

Euler’s Theorem states that if a and n are relatively prime integers, then a^φ(n) ≡ 1 (mod n), where φ(n) is the Euler totient function.

### Primarily Testing

Primarily testing is the process of determining whether a given number is prime or composite. There are many different algorithms for primarily testing, including the Sieve of Eratosthenes, the Miller-Rabin test, and the AKS algorithm.

### Chinese Remainder Theorem

The Chinese Remainder Theorem is a theorem in number theory that provides a way to solve a system of linear congruences. The theorem states that if we have a system of linear congruences of the form 

x ≡ a1 (mod m1)
x ≡ a2 (mod m2)
...
x ≡ ak (mod mk)

where the moduli m1, m2, ..., mk are pairwise relatively prime, then there exists a unique solution for x modulo M = m1 * m2 * ... * mk