### Advanced Encryption Standard (AES) Encryption and Decryption

1. AES is a symmetric key encryption algorithm used to protect electronic data. 

2. It employs a block cipher that encrypts and decrypts data in blocks of 128 bits. 

3. The AES algorithm has three key sizes: 128, 192, and 256 bits. 

4. The encryption and decryption process in AES involves four basic operations: 

   a. SubBytes: A non-linear substitution of each byte in the block.
   
   b. ShiftRows: A transposition operation that shifts the rows of the block.
   
   c. MixColumns: A matrix multiplication operation on each column of the block.
   
   d. AddRoundKey: A bitwise XOR operation with a round key derived from the encryption key.

5. The AES decryption process is the inverse of the encryption process and involves the same four operations in reverse order.

6. AES encryption and decryption can be performed using software or hardware implementations. 

7. AES is widely used in various applications such as secure communication, data storage, and electronic commerce.


### Fermat’s and Euler’s Theorem

1. Fermat’s theorem states that if p is a prime number and a is any positive integer not divisible by p, then a^(p-1) ≡ 1 (mod p).

2. Euler’s theorem is an extension of Fermat’s theorem and states that if a and m are coprime positive integers, then a^(φ(m)) ≡ 1 (mod m), where φ(m) is Euler’s totient function that counts the number of positive integers less than or equal to m that are coprime with m.

3. Fermat’s and Euler’s theorems are widely used in number theory and cryptography.

4. These theorems provide a fast way to compute large modular exponentiations.

5. The RSA algorithm, which is a widely used public-key encryption algorithm, is based on the difficulty of factoring large integers, which in turn relies on the difficulty of computing modular exponentiations.


### Unit 2 - Introduction to Group, Field, Finite Field of the Form GF(p), Modular Arithmetic, Prime and Relative Prime Numbers, Extended Euclidean Algorithm, Primarily Testing, Chinese Remainder Theorem, Discrete Logarithmic Problem, Principles of Public Key Crypto Systems, RSA Algorithm, Security of RSA

1. Group theory is a branch of mathematics that studies the properties of groups, which are sets of elements with a binary operation that satisfies certain axioms.

2. Fields are mathematical structures that extend the concept of numbers to include operations such as addition, subtraction, multiplication, and division.

3. Finite fields of the form GF(p) are fields with a finite number of elements, where p is a prime number.

4. Modular arithmetic is a system of arithmetic for integers that involves taking remainders with respect to a fixed integer modulus.

5. Prime numbers are positive integers greater than 1 that are divisible only by 1 and themselves.

6. Relative prime numbers, also known as coprime numbers, are positive integers that share no common factors other than 1.

7. The Extended Euclidean Algorithm is an algorithm for computing the greatest common divisor of two integers and their corresponding Bezout coefficients.

8. Primarily testing is a method for determining whether a given number is prime or composite.

9. The Chinese Remainder Theorem is a theorem that provides a method for solving a system of linear congruences.

10. The Discrete Logarithmic Problem is a problem in number theory and cryptography that involves computing the discrete logarithm of a given number with respect to a given base.

11. Public key cryptography is a cryptographic system that uses a pair of keys, one for encryption and one for decryption.

12. The RSA algorithm is a widely used public-key encryption algorithm based on the difficulty of factoring large integers.

13. The security of RSA depends on the difficulty of factoring large integers and the randomness of the keys generated.