### Advanced Encryption Standard (AES) encryption and decryption

The Advanced Encryption Standard (AES) is a symmetric block cipher that can encrypt and decrypt information. It is used to protect electronic data by converting it into a form that can only be read by someone with the correct decryption key.

1. AES operates on a fixed block size of 128 bits and uses a key size of 128, 192, or 256 bits.
2. The AES algorithm consists of several rounds of processing, the number of which depends on the key size.
3. Each round consists of four stages: SubBytes, ShiftRows, MixColumns, and AddRoundKey.
4. The SubBytes stage applies a non-linear substitution to each byte of the block.
5. The ShiftRows stage cyclically shifts the rows of the block by a certain number of bytes.
6. The MixColumns stage mixes the columns of the block, providing diffusion across columns.
7. The AddRoundKey stage adds the round key to the block using bitwise XOR.
8. The decryption process is the reverse of the encryption process, using the inverse of each stage.

### Fermat’s and Euler’s theorem

Fermat's Little Theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) is congruent to 1 modulo p. In other words, a^(p-1) % p = 1.

Euler's Totient Theorem is a generalization of Fermat's Little Theorem. It states that if a and n are coprime positive integers, then a^φ(n) is congruent to 1 modulo n, where φ(n) is Euler's totient function, which counts the number of positive integers less than n that are coprime to n.

These theorems are important in number theory and have applications in cryptography, particularly in the RSA algorithm. They can be used to efficiently compute modular exponentiation, which is a key operation in many cryptographic algorithms.