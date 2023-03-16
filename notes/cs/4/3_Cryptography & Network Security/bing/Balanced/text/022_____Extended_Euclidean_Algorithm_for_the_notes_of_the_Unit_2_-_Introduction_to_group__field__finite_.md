### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that for any two integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n > 0.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, meaning that gcd(a,b) = 1. In this case, the algorithm can be used to find the multiplicative inverse of a modulo b, which is the unique integer x such that ax = 1 mod b.
- The extended Euclidean algorithm can also be applied to polynomials, where it can be used to find the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.
- The algorithm works by repeatedly applying the division algorithm to find the quotients and remainders of dividing a by b and b by the remainder, until the remainder is zero. The quotients and remainders can then be used to find x and y by back-substitution.
- The algorithm can be summarized as follows:

  - Input: Two integers a and b, not both zero.
  - Output: Integers x and y such that ax + by = gcd(a,b).
  - Steps:
    - If a = 0, then return (0, 1) as the solution.
    - If b = 0, then return (1, 0) as the solution.
    - Divide a by b and let q and r be the quotient and remainder, respectively. That is, a = bq + r, where 0 <= r < b.
    - Recursively apply the algorithm to b and r and obtain a solution (x', y') such that bx' + ry' = gcd(b, r).
    - Return (y', x' - qy') as the solution. This is because ax + by = (bq + r)x + by = bx + (rx + by) = bx + (x' - qy')r = bx' + ry' = gcd(b, r) = gcd(a, b).