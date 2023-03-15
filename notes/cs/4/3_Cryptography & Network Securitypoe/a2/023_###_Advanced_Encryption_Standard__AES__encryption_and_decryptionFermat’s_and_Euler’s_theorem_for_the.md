 Here are the notes for the topic ### Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security:

### Advanced Encryption Standard (AES)

- AES is a symmetric-key encryption algorithm. It encrypts and decrypts data with the same key.
- It has a fixed block size of 128 bits and a key size of 128, 192, or 256 bits.
- The algorithm is iterative rather than feistel structure based. It consists of repeated application of rounds of processing. Each round involves a nonlinear substitution step, a linear mixing step, and the addition of a round key.
- The rounds transform the input plaintext block into an unrecognizable ciphertext block. The number of rounds used depends on the key size (128/192/256 rounds for 128/192/256-bit keys respectively).
- The strengths of AES are its strong security, efficiency, and simplicity. It is resistant to all known attacks if implemented properly with a sufficiently large key size.
- The potential weaknesses could be related to side-channel attacks or implementation weaknesses. It does not provide authentication hence additional measures are required to provide integrity and authenticity.

 Mnemonics/Tricks:
- AES is fast and secure (easy to remember properties)
- Number of rounds = key size in bits (easy to remember relationship)

Fermat's Theorem:
- For any integer a and prime number p, if a^p ≡ a (mod p), then a is a multiple of p.
- Proven using the definition of congruence and the fact that p is a prime.
- Used in primality testing to check if a number is prime or composite. If it passes the Fermat test, it is likely prime. If it fails, it is definitely composite.

Euler's Theorem:
- For any integer a and prime number p, a^φ(p) ≡ 1 (mod p) where φ is the totient function.
- Proven using the definition of congruence and Euler's product formula for totient.
- Used to find solutions to discrete logarithm problems. Important in cryptography for the security of some public key algorithms like Diffie-Hellman key exchange.

[Detailed explanations, examples, diagrams, etc can be added here for the topics]