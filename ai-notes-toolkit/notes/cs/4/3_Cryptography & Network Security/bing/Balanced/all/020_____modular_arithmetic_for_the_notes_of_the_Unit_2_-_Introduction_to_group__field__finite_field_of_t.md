# Modular Arithmetic

- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the modulus  .
- For example, if the modulus is 12, then 13 is equivalent to 1, 14 is equivalent to 2, and so on. We write this as 13 ≡ 1 (mod 12), 14 ≡ 2 (mod 12), etc.
- Modular arithmetic can be used to model situations where numbers cycle or repeat, such as clocks, calendars, cryptography, etc.
- The basic operations of modular arithmetic are addition, subtraction, multiplication, and division. They follow the same rules as normal arithmetic, except that the result is always reduced to the smallest positive remainder by dividing by the modulus and taking the remainder.
- For example, 7 + 8 = 15, but 15 ≡ 3 (mod 12), so 7 + 8 ≡ 3 (mod 12). Similarly, 9 - 5 = 4, but 4 ≡ 4 (mod 12), so 9 - 5 ≡ 4 (mod 12). Likewise, 6 × 4 = 24, but 24 ≡ 0 (mod 12), so 6 × 4 ≡ 0 (mod 12). Finally, 8 ÷ 4 = 2, but 2 ≡ 2 (mod 12), so 8 ÷ 4 ≡ 2 (mod 12).
- However, not every integer has a multiplicative inverse in modular arithmetic. A multiplicative inverse of a number a is a number b such that a × b ≡ 1 (mod n). For example, 3 has a multiplicative inverse of 4 in modulo 11, because 3 × 4 ≡ 1 (mod 11). But 2 has no multiplicative inverse in modulo 12, because there is no number b such that 2 × b ≡ 1 (mod 12).
- A number a has a multiplicative inverse in modulo n if and only if a and n are coprime, meaning that they have no common factors other than 1. For example, 3 and 11 are coprime, but 2 and 12 are not.
- To find the multiplicative inverse of a number a in modulo n, we can use the extended Euclidean algorithm, which finds the greatest common divisor (gcd) of a and n, and also the coefficients x and y such that ax + ny = gcd(a, n). If gcd(a, n) = 1, then a and n are coprime, and x is the multiplicative inverse of a in modulo n. For example, to find the multiplicative inverse of 3 in modulo 11, we have:

3x + 11y = 1

- Using the extended Euclidean algorithm, we get:

11 = 3 × 3 + 2

3 = 2 × 1 + 1

2 = 1 × 2 + 0

- Working backwards, we get:

1 = 3 - 2 × 1

1 = 3 - (11 - 3 × 3) × 1

1 = 3 × 4 - 11 × 1

- Therefore, x = 4 and y = -1, and 4 is the multiplicative inverse of 3 in modulo 11. We can check that 3 × 4 ≡ 1 (mod 11).
- Modular arithmetic is useful for many applications in cryptography, such as the RSA algorithm, which is based on the difficulty of factoring large numbers. It is also related to other concepts in number theory, such as Fermat's theorem, Euler's theorem, primality testing, Chinese remainder theorem, and discrete logarithm problem.