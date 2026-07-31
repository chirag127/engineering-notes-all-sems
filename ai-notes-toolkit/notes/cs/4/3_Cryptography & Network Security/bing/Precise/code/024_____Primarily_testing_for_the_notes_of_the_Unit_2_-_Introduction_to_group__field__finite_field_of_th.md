### Unit 2 - Introduction to Cryptography & Network Security

#### Group, Field, Finite Field of the form GF(p)
- A group is a set of elements with a binary operation that satisfies four properties: closure, associativity, identity, and inverse.
- A field is a set with two binary operations, addition and multiplication, that satisfy the properties of a group under addition and a group under multiplication, with the additional property of distributivity.
- A finite field is a field with a finite number of elements. A finite field of the form GF(p) is a field with p elements, where p is a prime number.

#### Modular Arithmetic
- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value, called the modulus.
- In modular arithmetic, two numbers are considered equivalent if they have the same remainder when divided by the modulus.

#### Prime and Relative Prime Numbers
- A prime number is a positive integer greater than 1 that is divisible by only 1 and itself.
- Two numbers are relatively prime if their greatest common divisor is 1.

#### Extended Euclidean Algorithm
- The extended Euclidean algorithm is an algorithm to compute the greatest common divisor of two numbers and the coefficients of Bézout's identity, which states that for any two integers a and b, there exist integers x and y such that ax + by = gcd(a, b).

#### Advanced Encryption Standard (AES) Encryption and Decryption
- The Advanced Encryption Standard (AES) is a symmetric key encryption algorithm that uses a fixed-length key to encrypt and decrypt data blocks of a fixed size.
- AES is a block cipher, meaning it operates on fixed-size blocks of data, typically 128 bits.

#### Fermat’s and Euler’s Theorem
- Fermat's Little Theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) is congruent to 1 modulo p.
- Euler's Theorem is a generalization of Fermat's Little Theorem that states that if a and n are relatively prime, then a^φ(n) is congruent to 1 modulo n, where φ(n) is Euler's totient function.

#### Primality Testing
- Primality testing is the process of determining whether a given number is prime or composite.
- There are several algorithms for primality testing, including the deterministic Miller-Rabin test and the probabilistic Solovay-Strassen test.

#### Chinese Remainder Theorem
- The Chinese Remainder Theorem is a theorem that provides a method for solving a system of simultaneous congruences with different moduli.
- The theorem states that if the moduli are pairwise relatively prime, then the system of congruences has a unique solution modulo the product of the moduli.

#### Discrete Logarithmic Problem
- The discrete logarithm problem is the problem of finding the exponent x in the equation b^x ≡ y (mod p), where p is a prime number and b and y are integers.
- The discrete logarithm problem is considered hard, meaning that no efficient algorithm is known for solving it.

#### Principles of Public Key Crypto Systems
- Public key cryptography, also known as asymmetric cryptography, is a cryptographic system that uses a pair of keys, one public and one private, to encrypt and decrypt messages.
- The public key is used to encrypt messages, while the private key is used to decrypt them. The security of public key cryptography relies on the difficulty of certain mathematical problems, such as the discrete logarithm problem and the integer factorization problem.

#### RSA Algorithm
- The RSA algorithm is a public key encryption algorithm that is widely used for secure data transmission.
- The security of the RSA algorithm relies on the difficulty of factoring large composite numbers.

#### Security of RSA
- The security of the RSA algorithm depends on the size of the key used. Larger keys provide more security, but also require more computational resources to use.
- There are several known attacks against the RSA algorithm, including the factoring attack and the chosen ciphertext attack. However, these attacks are not practical for large key sizes. 
