### Advanced Encryption Standard (AES) encryption and decryption

- The Advanced Encryption Standard (AES) is a symmetric block cipher that can encrypt and decrypt data using the same key. 
- AES can use keys of 128, 192, or 256 bits to encrypt and decrypt data in blocks of 128 bits. 
- AES consists of four main operations: byte substitution, row shift, column mix, and key addition. These operations are repeated for a number of rounds depending on the key size. 
- AES is a widely used encryption standard that provides strong security and high performance. AES is used in various applications such as secure communication, data storage, digital signatures, and cryptography. 

### Fermat's and Euler's theorem

- Fermat's theorem (or Fermat's little theorem) states that if p is a prime number and a is an integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p. That is, a^(p-1) - 1 is divisible by p. 
- Euler's theorem is a generalization of Fermat's theorem that applies to any positive integer n and any integer a that is coprime to n. That is, a and n have no common factors other than 1. Euler's theorem states that a^(φ(n)) is congruent to 1 modulo n, where φ(n) is the Euler's totient function that counts the number of positive integers less than or equal to n that are coprime to n.  
- Both Fermat's and Euler's theorem are useful for simplifying calculations involving large powers modulo n. For example, to find the last digit of 7^100, we can use Fermat's theorem with p = 10 and a = 7. Since 7 and 10 are coprime, we have 7^(10-1) ≡ 1 (mod 10). Therefore, 7^100 ≡ (7^9)^11 ≡ 1^11 ≡ 1 (mod 10). So the last digit of 7^100 is 1. 
- Both Fermat's and Euler's theorem are also important for the theory and practice of public-key cryptography, which is based on the idea of using different keys for encryption and decryption. One of the most popular public-key cryptosystems is RSA, which relies on the difficulty of factoring large numbers.  

### Mnemonics and learning tricks

- A possible mnemonic to remember the four operations of AES is: "Bake Some Rice Cake, Keep Adding". This corresponds to Byte substitution, Shift rows, Mix columns, and Add round key. 
- A possible mnemonic to remember the formula for Euler's totient function is: "Phi is the product of primes". This means that φ(n) is equal to n times the product of (1 - 1/p) for each distinct prime factor p of n. For example, φ(12) = 12 * (1 - 1/2) * (1 - 1/3) = 4. 
- A possible learning trick to apply Fermat's or Euler's theorem is to use modular exponentiation, which is a method of computing large powers modulo n by repeatedly squaring and reducing the base. For example, to compute 7^100 (mod 10), we can use the following steps:

  - 7^2 ≡ 49 ≡ 9 (mod 10)
  - 7^4 ≡ (7^2)^2 ≡ 9^2 ≡ 81 ≡ 1 (mod 10)
  - 7^8 ≡ (7^4)^2 ≡ 1^2 ≡ 1 (mod 10)
  - 7^16 ≡ (7^8)^2 ≡ 1^2 ≡ 1 (mod 10)
  - 7^32 ≡ (7^16)^2 ≡ 1^2 ≡ 1 (mod 10)
  - 7^64 ≡ (7^32)^2 ≡ 1^2 ≡ 1 (mod 10)
  - 7^100 ≡ 7^64 * 7^32 * 7^4 ≡ 1 * 1 *