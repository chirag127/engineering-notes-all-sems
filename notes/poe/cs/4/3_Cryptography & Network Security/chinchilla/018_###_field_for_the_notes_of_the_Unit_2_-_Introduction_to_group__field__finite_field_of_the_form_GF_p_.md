### Unit 2 - Introduction to Group, Field, and Finite Field

#### Group and Field

- A **group** is a set of elements with a binary operation that is associative, has an identity element, and every element has an inverse.
- A **field** is a set of elements with two binary operations (addition and multiplication) that satisfy certain axioms, such as commutativity, associativity, distributivity, and the existence of additive and multiplicative inverses.

#### Finite Field of the form GF(p)

- A **finite field** is a field with a finite number of elements.
- The field of integers modulo p, denoted GF(p), is a finite field with p elements.
- The addition and multiplication operations in GF(p) are defined modulo p, i.e., the result is always reduced to the range 0 to p-1.

#### Modular Arithmetic

- Modular arithmetic is a type of arithmetic where numbers "wrap around" after reaching a certain value, called the modulus.
- The modulus is usually denoted by the symbol "mod" or "%".
- Modular arithmetic is useful in cryptography for generating keys and performing encryption and decryption operations.

#### Prime and Relative Prime Numbers

- A **prime number** is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.
- Two integers a and b are said to be **relatively prime** if their greatest common divisor (GCD) is 1.

#### Extended Euclidean Algorithm

- The **Extended Euclidean Algorithm** is an algorithm used to find the greatest common divisor (GCD) of two integers, as well as the coefficients of Bézout's identity.
- Bézout's identity is a theorem that states that for any two integers a and b, there exist integers x and y such that ax + by = gcd(a,b).

#### Advanced Encryption Standard (AES) Encryption and Decryption

- The **Advanced Encryption Standard (AES)** is a widely used symmetric encryption algorithm.
- AES uses a block size of 128 bits and supports key sizes of 128, 192, or 256 bits.
- AES encryption and decryption involve multiple rounds of substitutions and permutations.

#### Fermat's and Euler's Theorem

- Fermat's theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) is congruent to 1 modulo p.
- Euler's theorem is a generalization of Fermat's theorem, which states that if a and n are coprime integers, then a^φ(n) is congruent to 1 modulo n, where φ is Euler's totient function.

#### Primality Testing

- Primality testing is the process of determining whether a given number is prime or composite.
- There are several primality testing algorithms, including the trial division method, the Miller-Rabin test, and the AKS test.

#### Chinese Remainder Theorem

- The **Chinese Remainder Theorem** is a theorem in number theory that states that if we have a set of simultaneous congruences with pairwise relatively prime moduli, then there exists a unique solution modulo the product of the moduli.
- The Chinese Remainder Theorem is useful in cryptography for constructing public key cryptosystems.

#### Discrete Logarithmic Problem

- The **Discrete Logarithmic Problem (DLP)** is a problem in number theory that involves finding the exponent x in the equation g^x ≡ h (mod p), where g, h, and p are known integers.
- The DLP is difficult to solve for large values of p and is the basis for several public key cryptosystems, including the Diffie-Hellman key exchange and the ElGamal encryption scheme.

#### Principles of Public Key Crypto Systems

- Public key cryptography is a cryptographic scheme that uses two keys, a public key and a private key, to perform encryption and decryption operations.
- The security of public key cryptosystems is based on the difficulty of certain mathematical problems, such as the factorization problem and the discrete logarithmic problem.

#### RSA Algorithm

- The **RSA algorithm** is a widely used public key cryptosystem invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977.
- RSA encryption and decryption involve exponentiation modulo a large composite number.
- The security of the RSA algorithm is based on the difficulty of factoring large composite numbers.

#### Security of RSA

- The security of the RSA algorithm depends on the difficulty of factoring large composite numbers.
- The security of RSA can be improved by using longer key sizes and using appropriate padding schemes.
- There are also attacks on RSA that exploit certain weaknesses in the implementation of the algorithm, such as side-channel attacks and timing attacks.