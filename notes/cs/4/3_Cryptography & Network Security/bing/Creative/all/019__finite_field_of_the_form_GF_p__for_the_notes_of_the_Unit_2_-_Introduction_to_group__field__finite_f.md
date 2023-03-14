### Finite field of the form GF(p) for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem, Primality testing, Chinese Remainder theorem, Discrete Logarithmic Problem, Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

- A finite field is a set of elements that obeys the axioms of a field, such as commutativity, associativity, distributivity, identity, and inverse for both addition and multiplication operations.
- A finite field has a finite number of elements, which must be a power of a prime number, denoted by p^n, where p is a prime number and n is a positive integer.
- A finite field of the form GF(p) is a special case where n = 1, and the elements are the integers from 0 to p-1, with arithmetic operations modulo p.
- GF stands for Galois field, in honor of the mathematician who first studied finite fields.
- GF(p) is also known as a prime field, because p is a prime number.
- GF(p) has the following properties:
  - The order of GF(p) is p, which means it has p elements.
  - The characteristic of GF(p) is p, which means that adding p copies of any element results in zero, or equivalently, p times any element is zero.
  - Every nonzero element of GF(p) has a multiplicative inverse, which means that for any a in GF(p), there exists a^-1 in GF(p) such that a * a^-1 = 1 (mod p).
  - Every element of GF(p) is a root of the polynomial x^p - x, which means that x^p = x (mod p) for any x in GF(p).
  - GF(p) is a cyclic group under both addition and multiplication, which means that there exists a generator g in GF(p) such that every element of GF(p) can be written as g^k for some integer k, where k ranges from 0 to p-1 for addition and from 0 to p-2 for multiplication.
- GF(p) is important for cryptography because it provides a simple and efficient way of performing arithmetic operations on large numbers, which are often used as keys, messages, or ciphertexts in cryptographic algorithms.
- Some examples of cryptographic algorithms that use GF(p) are:
  - Diffie-Hellman key exchange, which allows two parties to agree on a secret key over a public channel, by using exponentiation and modular arithmetic in GF(p).
  - ElGamal encryption, which is a public-key encryption scheme based on the discrete logarithm problem in GF(p), which is the problem of finding k given g, g^k, and p, where g is a generator of GF(p).
  - Elliptic curve cryptography, which is a type of public-key cryptography that uses points on an elliptic curve as elements of a finite field, where the curve is defined over GF(p) or GF(2^n).
  - Digital signature schemes, such as DSA and ECDSA, which use hash functions and modular arithmetic in GF(p) or GF(2^n) to generate and verify signatures on messages.