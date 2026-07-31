# Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

## Group
- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse.
- A group is abelian if the binary operation is also commutative.
- Examples of groups are the integers with addition, the nonzero rational numbers with multiplication, and the set of permutations of a finite set with composition.

## Field
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy the properties of a group for both operations, as well as the distributive property.
- A field is finite if it has a finite number of elements.
- Examples of fields are the rational numbers, the real numbers, and the complex numbers with the usual addition and multiplication.

## Finite field of the form GF(p)
- A finite field of the form GF(p), where p is a prime number, is simply the ring of integers modulo p, that is, the set {0, 1, ..., p-1} with the arithmetic operations modulo p .
- In GF(p), every nonzero element has a multiplicative inverse, and the addition and multiplication are both commutative and associative .
- Examples of finite fields of the form GF(p) are GF(2), GF(3), and GF(5) .

## Modular arithmetic
- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value, called the modulus.
- Modular arithmetic is useful for cryptography, as it allows for operations that are easy to perform but hard to reverse.
- Examples of modular arithmetic are clock arithmetic, where the modulus is 12 or 24, and the residue classes of integers modulo a prime number, where the modulus is the prime number.

## Prime and relative prime numbers
- A prime number is a positive integer that has exactly two positive divisors, namely 1 and itself.
- A relative prime number, or a coprime number, is a positive integer that shares no common positive divisors with another positive integer, except for 1.
- Examples of prime numbers are 2, 3, 5, 7, 11, and 13.
- Examples of relative prime numbers are 8 and 15, 21 and 22, and 35 and 48.

## Extended Euclidean Algorithm
- The Extended Euclidean Algorithm is an algorithm that computes the greatest common divisor (gcd) of two positive integers, as well as the coefficients of the Bézout's identity, which states that the gcd can be expressed as a linear combination of the two integers.
- The Extended Euclidean Algorithm is useful for cryptography, as it allows for finding the multiplicative inverse of an element modulo a prime number, which is needed for some encryption and decryption schemes.
- An example of the Extended Euclidean Algorithm is the following: to find the gcd of 240 and 46, and the coefficients of the Bézout's identity, we perform the following steps:

```
240 = 5 * 46 + 10
46 = 4 * 10 + 6
10 = 1 * 6 + 4
6 = 1 * 4 + 2
4 = 2 * 2 + 0
```

- The last nonzero remainder is the gcd, which is 2 in this case.
- To find the coefficients of the Bézout's identity, we work backwards from the equations above:

```
2 = 6 - 1 * 4
2 = 6 - 1 * (10 - 1 * 6)
2 = 2 * 6 - 1 * 10
2 = 2 * (46 - 4 * 10) - 1 * 10
2 = 2 * 46 - 9 * 10

```
