Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for Unit 2 of Cryptography and Network Security:

# Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA

## Group
- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity and inverse.
- A group is said to be abelian if it also satisfies the commutative property.
- Examples of groups are the set of integers with addition, the set of nonzero real numbers with multiplication, and the set of permutations with composition.

## Field
- A field is a set of elements with two binary operations, usually called addition and multiplication, that satisfy eight properties: closure, associativity, commutativity, identity, inverse, distributivity, zero and nonzero.
- A field is said to be finite if it has a finite number of elements.
- Examples of fields are the set of rational numbers, the set of real numbers, and the set of complex numbers with the usual addition and multiplication.

## Finite field of the form GF(p)
- A finite field of the form GF(p) is a field with p elements, where p is a prime number.
- The elements of GF(p) are the integers from 0 to p-1, and the addition and multiplication are performed modulo p.
- For example, GF(5) is the field with 5 elements: {0, 1, 2, 3, 4}, and the addition and multiplication are done as follows:

| + | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 1 | 2 | 3 | 4 | 0 |
| 2 | 2 | 3 | 4 | 0 | 1 |
| 3 | 3 | 4 | 0 | 1 | 2 |
| 4 | 4 | 0 | 1 | 2 | 3 |

| x | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 0 | 2 | 4 | 1 | 3 |
| 3 | 0 | 3 | 1 | 4 | 2 |
| 4 | 0 | 4 | 3 | 2 | 1 |

## Modular arithmetic
- Modular arithmetic is a system of arithmetic where numbers are reduced to a fixed range by using the remainder operation.
- The notation a mod n means the remainder of dividing a by n.
- For example, 7 mod 3 = 1, because 7 divided by 3 gives a quotient of 2 and a remainder of 1.
- Modular arithmetic is useful for cryptography because it allows operations to be performed on large numbers without overflow, and it also provides a way to create one-way functions.

## Prime and relative prime numbers
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- For example, 2, 3, 5, 7, 11, 13, 17, 19 are prime numbers.
- A relative prime number is a natural number that has no common positive divisors with another natural number other than 1.
- For example, 8 and 15 are relative prime numbers, because their only common divisor is 1.
- Prime and relative prime numbers are important for cryptography because they are the building blocks of many public key algorithms, such as RSA and Diffie-Hellman.

## Extended Euclidean Algorithm