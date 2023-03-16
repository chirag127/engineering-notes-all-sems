### Unit 2 - Introduction to Group, Field, Finite Field of the form GF(p), Modular Arithmetic, Prime and Relative Prime Numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) Encryption and Decryption, Fermat’s and Euler’s Theorem, Primarily Testing, Chinese Remainder Theorem, Discrete Logarithmic Problem, Principals of Public Key Crypto Systems, RSA Algorithm, Security of RSA

#### Prime and Relative Prime Numbers

- A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. For example, 2, 3, 5, 7, 11, and 13 are prime numbers.
- Two numbers are relatively prime if their greatest common divisor (GCD) is 1. For example, 8 and 9 are relatively prime because their GCD is 1.
- The GCD of two numbers can be calculated using the Euclidean algorithm.
- The Extended Euclidean Algorithm can be used to find the modular inverse of a number.
- The modular inverse of a number a modulo m is a number x such that ax ≡ 1 (mod m).
- The modular inverse of a number a modulo m exists if and only if a and m are relatively prime.
- The modular inverse of a number a modulo m can be used to solve linear congruences of the form ax ≡ b (mod m).
- The Chinese Remainder Theorem can be used to solve systems of linear congruences.
- Fermat's Little Theorem states that if p is a prime number, then for any integer a, a^p ≡ a (mod p).
- Euler's Totient Theorem states that if a and n are relatively prime, then a^φ(n) ≡ 1 (mod n), where φ(n) is the Euler totient function.
- The Euler totient function φ(n) is the number of positive integers less than n that are relatively prime to n.
- Primality testing is the process of determining whether a given number is prime or not.
- There are several primality testing algorithms, including the deterministic Miller-Rabin test and the probabilistic Solovay-Strassen test.
- The Discrete Logarithm Problem is the problem of finding an integer x such that g^x ≡ h (mod p) for given g, h, and p.
- The security of many public key crypto systems, including the RSA algorithm, is based on the difficulty of solving the Discrete Logarithm Problem and the related problem of integer factorization.
- The RSA algorithm is a widely used public key encryption algorithm. It is based on the mathematical properties of large prime numbers.
- The security of the RSA algorithm depends on the difficulty of factoring the product of two large prime numbers.