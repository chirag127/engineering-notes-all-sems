### Advanced Encryption Standard (AES) encryption and decryption

- The Advanced Encryption Standard (AES) is a symmetric block cipher that can encrypt and decrypt data using the same key  .
- AES was adopted by the U.S. government in 2001 as a standard for protecting electronic data, and is widely used in various applications such as banking, e-commerce, and wireless communications  .
- AES operates on fixed blocks of 128 bits, and can use keys of 128, 192, or 256 bits  .
- AES encryption and decryption consist of four main steps: byte substitution, row shift, column mix, and key addition  .
- Byte substitution replaces each byte in the block with another byte from a predefined table called the S-box  .
- Row shift cyclically shifts each row of the block by a certain number of positions to the left  .
- Column mix transforms each column of the block by multiplying it with a fixed matrix  .
- Key addition adds the round key to the block using bitwise XOR  .
- AES encryption repeats these steps for a number of rounds, depending on the key size. For 128-bit keys, there are 10 rounds; for 192-bit keys, there are 12 rounds; and for 256-bit keys, there are 14 rounds  .
- AES decryption reverses these steps using the inverse S-box, inverse row shift, inverse column mix, and key subtraction  .
- AES is considered to be very secure and efficient, as it has no known practical attacks and can be implemented in hardware and software  .

### Fermat's and Euler's theorem

- Fermat's little theorem states that, if p is a prime number and a is any integer, then a^p ≡ a (mod p)   .
- This means that a raised to the power of p is congruent to a itself modulo p, or in other words, the remainder of dividing a^p by p is equal to a   .
- For example, if p = 7 and a = 3, then 3^7 = 2187, and 2187 mod 7 = 3   .
- Fermat's little theorem can be used to test whether a number is prime or not, by checking if it satisfies the theorem for some values of a   .
- However, there are some composite numbers that also satisfy the theorem for all values of a, and these are called Carmichael numbers   .
- For example, 561 is a Carmichael number, because 2^561 ≡ 2 (mod 561), 3^561 ≡ 3 (mod 561), and so on   .
- Euler's theorem is a generalization of Fermat's little theorem, that applies to any positive integer n and any integer a that is coprime to n   .
- Euler's theorem states that a^φ(n) ≡ 1 (mod n), where φ(n) is Euler's totient function, which counts the number of positive integers less than or equal to n that are coprime to n   .
- For example, if n = 12 and a = 5, then φ(12) = 4, and 5^4 = 625, and 625 mod 12 = 1 [^7^