Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here is some content on the topic of Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem.

### Advanced Encryption Standard (AES) encryption and decryption

- The Advanced Encryption Standard (AES) is a symmetric block cipher that can encrypt and decrypt information using the same key  .
- AES operates on blocks of 128 bits, and can use keys of 128, 192, or 256 bits. The number of rounds of encryption and decryption depends on the key size: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys .
- Each round consists of four steps: byte substitution, row shift, column mix, and key addition. The last round omits the column mix step .
- Byte substitution replaces each byte in the block with another byte from a predefined table called the S-box. This provides confusion and non-linearity to the cipher .
- Row shift cyclically shifts each row of the block by a different amount. This provides diffusion and permutation to the cipher .
- Column mix multiplies each column of the block by a fixed matrix. This provides diffusion and linear transformation to the cipher .
- Key addition adds the round key to the block using bitwise XOR. The round key is derived from the original key using a key expansion algorithm. This provides confusion and key dependency to the cipher .
- To decrypt a block, the inverse steps are applied in reverse order: key addition, column mix, row shift, and byte substitution. The inverse steps use different tables and matrices from the encryption steps .
- AES is a widely used and secure algorithm that can protect electronic data from unauthorized access. It is approved by the U.S. government and many other standards organizations  .

### Fermat's and Euler's theorem

- Fermat's theorem (or Fermat's little theorem) states that if p is a prime number and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p; that is, a^(p-1) ≡ 1 (mod p)   .
- Euler's theorem (or Euler's totient theorem) is a generalization of Fermat's theorem that applies to any positive integer n and any integer a that is coprime to n (that is, they have no common factors other than 1). It states that a^φ(n) is congruent to 1 modulo n, where φ(n) is Euler's totient function, which counts the number of positive integers less than or equal to n that are coprime to n   .
- For example, φ(12) = 4, because the positive integers less than or equal to 12 that are coprime to 12 are 1, 5, 7, and 11. Therefore, for any integer a that is coprime to 12, a^4 ≡ 1 (mod 12).
- Fermat's theorem is a special case of Euler's theorem when n is a prime number, because φ(p) = p - 1 for any prime p   .
- Both Fermat's and Euler's theorems are useful in number theory and cryptography, especially in the RSA algorithm, which is based on the difficulty of finding the modular inverse of large numbers   .