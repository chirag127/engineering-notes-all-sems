# Advanced Encryption Standard (AES) encryption and decryption

The Advanced Encryption Standard (AES) is a symmetric block cipher used to encrypt and decrypt data. It is based on the Rijndael cipher and was selected by the U.S. National Institute of Standards and Technology (NIST) as the standard for encryption in 2001.

AES operates on blocks of data, typically 128 bits in size, and uses a key of 128, 192, or 256 bits. The key size determines the number of rounds the algorithm will perform, with 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys.

The AES algorithm consists of four main operations: SubBytes, ShiftRows, MixColumns, and AddRoundKey. These operations are performed in a series of rounds, with the number of rounds determined by the key size.

SubBytes is a non-linear substitution operation that replaces each byte in the block with a corresponding byte from a fixed substitution table (S-box).

ShiftRows is a transposition operation that cyclically shifts the rows of the block by a certain number of bytes.

MixColumns is a mixing operation that combines the columns of the block using a matrix multiplication.

AddRoundKey is an operation that adds the round key to the block using bitwise XOR.

The AES algorithm also includes an initial round of AddRoundKey and a final round that consists of SubBytes, ShiftRows, and AddRoundKey, but not MixColumns.

Decryption using AES is performed using the inverse of each operation in reverse order.

# Fermat’s and Euler’s theorem

Fermat's Little Theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) is congruent to 1 modulo p. In other words, a^(p-1) % p = 1.

Euler's Totient Theorem is a generalization of Fermat's Little Theorem. It states that if a and n are coprime, then a^φ(n) is congruent to 1 modulo n, where φ(n) is Euler's totient function, which gives the number of positive integers less than n that are coprime to n.

These theorems are useful in number theory and cryptography, particularly in the RSA algorithm, where they are used to compute modular inverses and to perform encryption and decryption.