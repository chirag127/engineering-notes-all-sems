### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that for any integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n > 0.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, meaning that gcd(a,b) = 1. In this case, the algorithm can be used to find the multiplicative inverse of a modulo b, which is the unique integer x such that ax ≡ 1 (mod b).
- The extended Euclidean algorithm can also be generalized to compute the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.
- The algorithm works by applying the Euclidean algorithm repeatedly until the remainder is zero, and then backtracking to find the coefficients x and y. The Euclidean algorithm is an efficient way of computing the greatest common divisor of two numbers by using the division algorithm and the property that gcd(a,b) = gcd(b,r), where r is the remainder of dividing a by b.
- The pseudocode of the extended Euclidean algorithm is as follows:

```
function extended_gcd(a, b)
    if b == 0
        return (a, 1, 0) // base case: gcd(a,0) = a, x = 1, y = 0
    else
        (d, x, y) = extended_gcd(b, a mod b) // recursive call: gcd(a,b) = gcd(b, a mod b)
        return (d, y, x - (a div b) * y) // backtrack: x = y, y = x - (a div b) * y
```

- The function returns a tuple (d, x, y) such that d = gcd(a,b) and ax + by = d.
- For example, to find the multiplicative inverse of 7 modulo 26, we can call the function with a = 7 and b = 26. The function returns (1, 15, -4), which means that gcd(7,26) = 1 and 7 * 15 + 26 * (-4) = 1. Therefore, the multiplicative inverse of 7 modulo 26 is 15, since 7 * 15 ≡ 1 (mod 26).