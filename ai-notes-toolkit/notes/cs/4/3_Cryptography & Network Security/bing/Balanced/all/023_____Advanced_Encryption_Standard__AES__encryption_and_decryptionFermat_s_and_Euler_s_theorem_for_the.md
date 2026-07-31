# Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric block cipher that can encrypt and decrypt data using the same key  .
- AES operates on blocks of 128 bits and can use keys of 128, 192, or 256 bits .
- AES consists of four main operations: byte substitution, row shift, column mix, and key addition  .
- AES performs these operations in several rounds, depending on the key size. For 128-bit keys, there are 10 rounds; for 192-bit keys, there are 12 rounds; and for 256-bit keys, there are 14 rounds .
- AES encryption transforms plaintext into ciphertext by applying the operations in each round, using a different round key derived from the original key .
- AES decryption reverses the process by applying the inverse operations in the reverse order, using the same round keys .
- AES is a widely used and secure algorithm that can protect electronic data from unauthorized access or modification  .

# Fermat's and Euler's theorem

- Fermat's theorem (or Fermat's little theorem) states that if p is a prime number and a is any integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p   .
- Euler's theorem (or Euler's totient theorem) is a generalization of Fermat's theorem that states that if n and a are coprime positive integers, and φ(n) is Euler's totient function, then a^φ(n) is congruent to 1 modulo n   .
- Euler's totient function φ(n) counts the number of positive integers less than or equal to n that are coprime to n   .
- Fermat's theorem is a special case of Euler's theorem when n is a prime number, since φ(p) = p - 1 for any prime p   .
- Both Fermat's and Euler's theorems are useful in number theory and cryptography, especially in the RSA algorithm, which is based on the difficulty of finding the modular inverse of large numbers   .