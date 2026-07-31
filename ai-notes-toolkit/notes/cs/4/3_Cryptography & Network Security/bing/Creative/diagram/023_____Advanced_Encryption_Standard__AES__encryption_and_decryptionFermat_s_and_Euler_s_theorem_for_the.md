Hello, I am Sydney, your AI assistant. I can help you with your study material for Cryptography & Network Security. Here is some content on the topic of Advanced Encryption Standard (AES) encryption and decryption, Fermat’s and Euler’s theorem.

### Advanced Encryption Standard (AES) encryption and decryption

- AES is a symmetric block cipher that can encrypt and decrypt data using the same key  .
- AES operates on blocks of 128 bits, and can use keys of 128, 192, or 256 bits  .
- AES consists of four main steps: key expansion, initial round, main rounds, and final round  .
- Key expansion generates round keys from the original key using a recursive process  .
- Initial round performs an XOR operation between the input block and the first round key  .
- Main rounds perform four operations: byte substitution, row shift, column mix, and round key addition  .
- Final round performs the same operations as the main rounds, except for the column mix  .
- The number of rounds depends on the key size: 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys  .
- AES decryption is the inverse of AES encryption, using the round keys in reverse order  .
- AES is a FIPS-approved cryptographic algorithm that can be used to protect electronic data .
- AES is based on a mathematical structure called a finite field, which has a set of elements and two operations: addition and multiplication  .

### Fermat’s and Euler’s theorem

- Fermat’s Little Theorem states that if p is a prime number and a is an integer that is not divisible by p, then a^(p-1) is congruent to 1 modulo p .
- Fermat’s Little Theorem can be used to test whether a number is prime or not, by checking if the theorem holds for some values of a .
- Euler’s Theorem is a generalization of Fermat’s Little Theorem, which states that if n and a are coprime positive integers, and φ(n) is Euler’s totient function, then a^φ(n) is congruent to 1 modulo n .
- Euler’s totient function φ(n) counts the number of positive integers less than or equal to n that are coprime to n .
- Euler’s Theorem can be used to find the inverse of an integer modulo n, by using the fact that a^φ(n)-1 is congruent to a^-1 modulo n .
- Euler’s Theorem underlies the RSA cryptosystem, which is a public key cryptosystem that uses large prime numbers and modular arithmetic to encrypt and decrypt data.