### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that for any two integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n > 0.
- The extended Euclidean algorithm is particularly useful for computing multiplicative inverses in modular structures, such as the modular integers and the finite fields. A multiplicative inverse of a modulo n is an integer x such that ax = 1 mod n, where a and n are coprime, i.e., gcd(a,n) = 1.
- The extended Euclidean algorithm can also be used to compute the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.

#### Algorithm

- The extended Euclidean algorithm is based on the Euclidean algorithm, which is an efficient way of computing the greatest common divisor of two numbers. The Euclidean algorithm works as follows:

  - If a = 0, then gcd(a,b) = b and we can stop.
  - If b = 0, then gcd(a,b) = a and we can stop.
  - Write a in quotient remainder form: a = bq + r, where q and r are integers and 0 <= r < b.
  - Find gcd(b,r) using the Euclidean algorithm, since gcd(a,b) = gcd(b,r).

- The extended Euclidean algorithm keeps track of the quotients and the remainders in each step of the Euclidean algorithm, and uses them to compute x and y in Bézout's identity. The algorithm works as follows:

  - Initialize x0 = 1, y0 = 0, x1 = 0, y1 = 1, r0 = a, r1 = b.
  - Repeat until r1 = 0:
    - Write r0 in quotient remainder form: r0 = r1q + r2, where q and r2 are integers and 0 <= r2 < r1.
    - Update x2 = x0 - qx1, y2 = y0 - qy1, r2 = r0 - qr1.
    - Set x0 = x1, y0 = y1, x1 = x2, y1 = y2, r0 = r1, r1 = r2.
  - Return x0, y0, r0 as the solution.

#### Example

- Suppose we want to find x and y such that 99x + 78y = gcd(99,78) using the extended Euclidean algorithm. We have:

  - x0 = 1, y0 = 0, x1 = 0, y1 = 1, r0 = 99, r1 = 78.
  - r0 = r1q + r2, where q = 1 and r2 = 21. So, x2 = x0 - qx1 = 1 - 0 = 1, y2 = y0 - qy1 = 0 - 1 = -1, r2 = r0 - qr1 = 99 - 78 = 21.
  - x0 = x1 = 0, y0 = y1 = 1, x1 = x2 = 1, y1 = y2 = -1, r0 = r1 = 78, r1 = r2 = 21.
  - r0 = r1q + r2, where q = 3 and r2 = 15. So, x2 = x0 - qx1 = 0 - 3(1) = -3, y2 = y0 - qy1 = 1 - 3(-1) = 4, r2 = r0 - qr1 = 78 - 3(21) = 15.
  - x0 = x1 = 1, y0 = y1 = -1, x1 = x2 = -3, y1 = y2 = 4, r0 = r1 = 21, r1 = r2 = 15