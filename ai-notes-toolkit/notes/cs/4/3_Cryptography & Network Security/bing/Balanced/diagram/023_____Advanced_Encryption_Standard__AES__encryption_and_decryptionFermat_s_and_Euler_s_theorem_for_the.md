Hello, I am Sydney, your AI assistant. I can help you with your topic of interest. Here is some content in markdown format that you can use for your notes.

### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric-key block cipher that can encrypt and decrypt data using a secret key.
- AES operates on a fixed block size of 128 bits and supports three key sizes: 128, 192, and 256 bits.
- AES consists of four main steps: key expansion, initial round, rounds, and final round.
- Key expansion generates a set of round keys from the secret key using a key schedule algorithm.
- Initial round performs an XOR operation between the input block and the first round key.
- Rounds consist of four sub-steps: sub-bytes, shift-rows, mix-columns, and add-round-key. Each round applies a different round key to the block.
- Sub-bytes is a non-linear substitution of each byte in the block using a lookup table called S-box.
- Shift-rows is a cyclic permutation of each row in the block by a different offset.
- Mix-columns is a linear transformation of each column in the block using a matrix multiplication.
- Add-round-key is an XOR operation between the block and the round key.
- Final round is similar to the rounds, except that it does not perform the mix-columns step.
- AES decryption is the inverse of AES encryption, using the same round keys in reverse order.
- AES decryption consists of four main steps: key expansion, initial round, rounds, and final round.
- Key expansion is the same as in encryption.
- Initial round performs an XOR operation between the input block and the last round key.
- Rounds consist of four sub-steps: inv-sub-bytes, inv-shift-rows, inv-mix-columns, and add-round-key. Each round applies a different round key to the block.
- Inv-sub-bytes is the inverse of sub-bytes, using a lookup table called inverse S-box.
- Inv-shift-rows is the inverse of shift-rows, using a negative offset for each row.
- Inv-mix-columns is the inverse of mix-columns, using a different matrix for the multiplication.
- Add-round-key is the same as in encryption.
- Final round is similar to the rounds, except that it does not perform the inv-mix-columns step.

### Fermat's and Euler's theorem

- Fermat's theorem states that if p is a prime number and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p. That is, a^(p-1) mod p = 1.
- Euler's theorem generalizes Fermat's theorem to the case where p is not necessarily prime, but a and p are relatively prime. That is, they have no common factors other than 1. Euler's theorem states that a^phi(p) is congruent to 1 modulo p, where phi(p) is the Euler's totient function, which counts the number of positive integers less than p that are relatively prime to p.
- Both Fermat's and Euler's theorem are useful for modular arithmetic and cryptography, as they can be used to simplify calculations and reduce the size of exponents.