### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric-key block cipher algorithm that can encrypt and decrypt data using the same secret key.
- AES operates on 128-bit blocks of data, and can use a key size of 128, 192, or 256 bits.
- AES consists of four main steps: key expansion, initial round, rounds, and final round.
- Key expansion generates a set of round keys from the secret key using a recursive process called the Rijndael key schedule.
- Initial round performs an XOR operation between the input block and the first round key.
- Rounds consist of four sub-steps: sub-bytes, shift-rows, mix-columns, and add-round-key. Each round applies a different round key to the data.
- Sub-bytes is a non-linear substitution of each byte in the block using a predefined lookup table called the S-box.
- Shift-rows is a cyclic permutation of the bytes in each row of the block, with different offsets for each row.
- Mix-columns is a linear transformation that mixes the bytes in each column of the block using a matrix multiplication.
- Add-round-key is an XOR operation between the block and the round key.
- Final round is similar to the rounds, except that it does not perform the mix-columns step.
- Decryption is the inverse of encryption, using the round keys in reverse order and applying the inverse of each sub-step.

### Fermat's and Euler's theorem

- Fermat's theorem states that if p is a prime number and a is any integer, then a^p ≡ a (mod p).
- Euler's theorem generalizes Fermat's theorem to the case where p is not necessarily prime, but a and p are relatively prime, i.e., gcd(a, p) = 1. It states that a^φ(p) ≡ 1 (mod p), where φ(p) is the Euler's totient function, which counts the number of positive integers less than p that are relatively prime to p.
- Both Fermat's and Euler's theorem are useful for simplifying modular arithmetic and for designing cryptographic algorithms.