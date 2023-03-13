### Prime and relative prime numbers for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, etc. are prime numbers.
- A relative prime number (or coprime number) is a natural number that has no common positive divisors with another natural number except 1. For example, 8 and 15 are relative prime numbers because their only common divisor is 1.
- Prime and relative prime numbers are important in cryptography because they are difficult to factorize. This means that it is difficult to find the prime factors of a composite number without knowing the factors to begin with. This makes it difficult for someone to intercept a message and read it without the proper key  .
- One of the most widely used public key cryptosystems is the RSA algorithm, which is based on the fact that it is easy to take two (very large) prime numbers and multiply them, while it is extremely hard to do the opposite - meaning: take a very large number, given which it has only two prime factors, and find them.
- The RSA algorithm works as follows:
  - Choose two large prime numbers p and q, and compute their product n = pq. This is called the modulus.
  - Choose a small number e that is relatively prime to (p-1)(q-1). This is called the public exponent.
  - Compute a number d that satisfies the equation ed = 1 mod (p-1)(q-1). This is called the private exponent.
  - The public key is (n, e) and the private key is (n, d).
  - To encrypt a message m, compute c = m^e mod n. This is called the ciphertext.
  - To decrypt a ciphertext c, compute m = c^d mod n. This is called the plaintext.
- The security of the RSA algorithm relies on the assumption that it is hard to factorize large numbers. If someone can find the prime factors of n, they can compute d and break the encryption. However, no efficient algorithm is known for this problem, and the best known methods take exponential time in the size of n.
- Some mnemonics and learning tricks for prime and relative prime numbers are:
  - To check if a number is prime, divide it by all the primes up to its square root. If none of them divides it, then it is prime. For example, to check if 101 is prime, divide it by 2, 3, 5, and 7. None of them divides it, so 101 is prime.
  - To check if two numbers are relative prime, use the Euclidean algorithm to find their greatest common divisor (GCD). If the GCD is 1, then they are relative prime. For example, to check if 8 and 15 are relative prime, use the Euclidean algorithm as follows:

  ```
  15 = 8 * 1 + 7
  8 = 7 * 1 + 1
  7 = 1 * 7 + 0
  ```

  The last nonzero remainder is 1, so the GCD is 1, and 8 and 15 are relative prime.
  - To remember the first 10 prime numbers, use the following rhyme:

  ```
  Two is the only even prime,
  Three is the first odd one in line,
  Five is the last digit of its square,
  Seven is the sum of the first two there,
  Eleven is a palindrome in base ten,
  Thirteen is the product of six plus one,
  Seventeen is a Fermat prime of four,
  Nineteen is the next one to explore,
  Twenty-three is the smallest with eight divisors,
  Twenty-nine is the last one in this verse.
  ```