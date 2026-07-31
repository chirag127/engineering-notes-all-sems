# Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that for any integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n > 0.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, meaning that gcd(a,b) = 1. In this case, the algorithm can be used to find the multiplicative inverse of a modulo b, which is the unique integer x such that ax ≡ 1 (mod b).
- The extended Euclidean algorithm is also useful for computing the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials, which are analogous to the integer case.
- The extended Euclidean algorithm is based on the Euclidean algorithm, which is an efficient way of computing the greatest common divisor of two numbers. The Euclidean algorithm works by repeatedly applying the division algorithm and finding the remainder, until the remainder is zero. The last non-zero remainder is the gcd of the original numbers.
- The extended Euclidean algorithm works by keeping track of the quotients and remainders in each step of the Euclidean algorithm, and then using them to find x and y by back-substitution. The algorithm can be implemented recursively or iteratively, and can be generalized to any Euclidean domain, which is a mathematical structure that satisfies certain properties of divisibility and remainder.

# Example

- Suppose we want to find x and y such that 99x + 78y = gcd(99,78) using the extended Euclidean algorithm.
- First, we apply the Euclidean algorithm to find gcd(99,78):

```
99 = 78 * 1 + 21
78 = 21 * 3 + 15
21 = 15 * 1 + 6
15 = 6 * 2 + 3
6 = 3 * 2 + 0
```

- The last non-zero remainder is 3, so gcd(99,78) = 3.
- Next, we use the quotients and remainders to find x and y by back-substitution:

```
3 = 15 - 6 * 2
3 = 15 - (21 - 15 * 1) * 2
3 = 15 * 3 - 21 * 2
3 = (78 - 21 * 3) * 3 - 21 * 2
3 = 78 * 3 - 21 * 11
3 = 78 * 3 - (99 - 78 * 1) * 11
3 = 99 * (-11) + 78 * 14
```

- Therefore, x = -11 and y = 14 are the solutions. We can check that 99 * (-11) + 78 * 14 = 3.