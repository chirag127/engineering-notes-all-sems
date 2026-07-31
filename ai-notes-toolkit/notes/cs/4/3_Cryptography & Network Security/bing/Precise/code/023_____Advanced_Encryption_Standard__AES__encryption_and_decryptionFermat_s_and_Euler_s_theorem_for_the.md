### Advanced Encryption Standard (AES) encryption and decryption

Advanced Encryption Standard (AES) is a symmetric block cipher that is used to encrypt and decrypt data. It is a widely used encryption standard that is considered to be very secure. AES is based on the Rijndael cipher, which was developed by two Belgian cryptographers, Joan Daemen and Vincent Rijmen.

AES operates on blocks of data that are 128 bits in size. The key size used for encryption can be 128, 192, or 256 bits. The number of rounds used in the encryption process depends on the key size, with 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys.

The AES encryption process involves several steps, including:

1. Key expansion: The key is expanded into an array of key schedule words.
2. Initial round: The input block is XORed with the initial round key.
3. Main rounds: The main rounds involve several operations, including substitution, shift rows, mix columns, and add round key.
4. Final round: The final round involves substitution, shift rows, and add round key.

The AES decryption process is the reverse of the encryption process and involves the same steps in reverse order.

Fermat’s and Euler’s theorem are important concepts in number theory that are used in cryptography. Fermat’s Little Theorem states that if p is a prime number and a is an integer not divisible by p, then a^(p-1) is congruent to 1 modulo p. Euler’s Theorem is a generalization of Fermat’s Little Theorem and states that if a and n are coprime, then a^φ(n) is congruent to 1 modulo n, where φ(n) is Euler’s totient function.

These theorems are used in several cryptographic algorithms, including the RSA algorithm, which is a widely used public key encryption algorithm. The security of RSA is based on the difficulty of factoring large prime numbers.