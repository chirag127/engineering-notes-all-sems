### Finite field of the form GF(p)

- A finite field is a set of elements that obey certain algebraic rules, such as addition, subtraction, multiplication and division (except by zero).
- A finite field has a finite number of elements, denoted by its order. The order of a finite field must be a power of a prime number, i.e., p^n, where p is a prime number and n is a positive integer.
- A finite field of the form GF(p) is a special case where n = 1, i.e., the order is a prime number p. GF stands for Galois field, named after the mathematician Évariste Galois who pioneered the theory of finite fields.
- GF(p) can be constructed from the set of integers modulo p, denoted by Z_p. Z_p consists of the integers from 0 to p-1, and the arithmetic operations are performed modulo p, i.e., the remainder after dividing by p.
- For example, GF(5) is the finite field of order 5, and it can be represented by Z_5 = {0, 1, 2, 3, 4}. The arithmetic operations modulo 5 are as follows:

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

- Note that every element in GF(p) has an additive inverse, i.e., an element that when added to it gives zero. For example, in GF(5), the additive inverse of 2 is 3, because 2 + 3 = 0 mod 5. Similarly, every element in GF(p) except zero has a multiplicative inverse, i.e., an element that when multiplied by it gives one. For example, in GF(5), the multiplicative inverse of 2 is 3, because 2 x 3 = 1 mod 5.
- A finite field of the form GF(p) has some important properties that are useful for cryptography, such as:

  - The distributive law: a x (b + c) = (a x b) + (a x c) mod p
  - The commutative law: a + b = b + a mod p and a x b = b x a mod p
  - The associative law: (a + b) + c = a + (b + c) mod p and (a x b) x c = a x (b x c) mod p
  - The identity element: a + 0 = a mod p and a x 1 = a mod p
  - The inverse element: a + (-a) = 0 mod p and a x a^-1 = 1 mod p (if a is not zero)

- Some examples of cryptographic algorithms that use finite fields of the form GF(p) are:

  - Diffie-Hellman key exchange: a protocol that allows two parties to agree on a secret key over a public channel, using exponentiation and modular arithmetic in GF(p).
  - ElGamal encryption: a public-key encryption scheme that uses discrete logarithms and modular arithmetic in GF(p).
  - Elliptic curve cryptography: a type of public-key cryptography that uses points on elliptic curves and modular arithmetic in GF(p).
  - Shamir's secret sharing: a scheme that allows a secret to be split into shares and distributed among participants, such that any subset of a certain size can reconstruct the secret,