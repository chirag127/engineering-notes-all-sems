### Modular Arithmetic

Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value called the modulus. It is an important concept in cryptography and is used in many encryption algorithms.

Here are some key points to remember about modular arithmetic:

- In modular arithmetic, we perform addition, subtraction, and multiplication just like in regular arithmetic, but we also take the result modulo some integer, called the modulus.
- For example, if we are working modulo 7, then 9 + 5 ≡ 0 (mod 7) because 9 + 5 = 14, and 14 divided by 7 leaves a remainder of 0.
- We can also perform division in modular arithmetic, but it is a bit more complicated. We need to find the modular inverse of the divisor, which is a number that, when multiplied by the divisor, gives a remainder of 1 when divided by the modulus.
- For example, if we are working modulo 7 and want to divide 3 by 5, we need to find the modular inverse of 5 modulo 7. This turns out to be 3, because 3 * 5 ≡ 1 (mod 7). So 3/5 ≡ 3 * 3 ≡ 2 (mod 7).
- Prime numbers are important in modular arithmetic because they have certain properties that make calculations easier. For example, if p is a prime number, then every number between 1 and p-1 is relatively prime to p, meaning that they share no factors except 1.
- The Extended Euclidean Algorithm is a method for finding the greatest common divisor of two numbers, as well as their modular inverse if it exists. It is useful for performing division in modular arithmetic.
- The Chinese Remainder Theorem is a method for solving systems of equations in modular arithmetic. It says that if we have two equations x ≡ a (mod m) and x ≡ b (mod n) where m and n are relatively prime, then there is a unique solution modulo mn.
- The Discrete Logarithm Problem is a difficult problem in modular arithmetic that is used in many encryption algorithms. It asks us to find the exponent x in the equation g^x ≡ y (mod p), where g and p are known and y is given.
- Public key cryptography is a type of encryption that uses two keys, one for encryption and one for decryption. The RSA algorithm is a popular public key encryption algorithm that is based on modular arithmetic.
- The security of RSA depends on the difficulty of the Discrete Logarithm Problem and the factoring problem, which asks us to find the prime factors of a large composite number. These problems are believed to be difficult to solve, which is why RSA is considered a secure encryption algorithm.