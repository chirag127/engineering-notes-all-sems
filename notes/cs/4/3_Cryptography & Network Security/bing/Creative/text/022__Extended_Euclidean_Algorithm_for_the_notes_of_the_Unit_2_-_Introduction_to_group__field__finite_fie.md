### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that if a and b are nonzero integers, then there exist integers x and y such that ax + by = gcd(a,b) and gcd(a,b) is the smallest positive integer that can be written in this form.
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n is positive.
- The extended Euclidean algorithm can be used to compute the multiplicative inverse of a modulo n, which is the integer x such that ax = 1 mod n, if a and n are coprime (i.e., gcd(a,n) = 1). This is useful for many cryptographic applications, such as the RSA algorithm.
- The extended Euclidean algorithm can also be applied to polynomials, to compute the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.

#### Example

- Suppose we want to find x and y such that 102x + 38y = gcd(102,38) and gcd(102,38) itself. We can use the extended Euclidean algorithm as follows:

1. We start by applying the Euclidean algorithm to 102 and 38, which gives us a sequence of equations:

```
102 = 2 * 38 + 26
38 = 1 * 26 + 12
26 = 2 * 12 + 2
12 = 6 * 2 + 0
```

2. The last nonzero remainder is 2, which is the gcd(102,38). We can write it as a linear combination of 102 and 38 by working backwards from the equations:

```
2 = 26 - 2 * 12
2 = 26 - 2 * (38 - 1 * 26)
2 = 3 * 26 - 2 * 38
2 = 3 * (102 - 2 * 38) - 2 * 38
2 = 3 * 102 - 8 * 38
```

3. Therefore, we have x = 3 and y = -8 as the solution. We can check that 102 * 3 + 38 * (-8) = 2, as required.