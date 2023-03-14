### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b .
- The existence of such integers is guaranteed by Bézout's lemma .
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation.
- By reversing the steps in the Euclidean algorithm, it is possible to find these integers x and y .
- The whole idea is to start with the gcd and recursively work our way backwards.
- This can be done by treating the numbers as variables until we end up with an expression that is a linear combination of our initial numbers.
- The extended Euclidean algorithm also refers to a very similar algorithm for computing the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.
- The extended Euclidean algorithm is particularly useful when a and b are coprime.
- With that provision, x is the modular multiplicative inverse of a modulo b, and y is the modular multiplicative inverse of b modulo a.
- Similarly, the polynomial extended Euclidean algorithm allows one to compute the multiplicative inverse in algebraic field extensions and, in particular in finite fields of non prime order.
- It follows that both extended Euclidean algorithms are widely used in cryptography.
- In particular, the computation of the modular multiplicative inverse is an essential step in the derivation of key-pairs in the RSA public-key encryption method.

#### Example

- Suppose we want to find x and y such that 102x + 38y = gcd(102,38) = 2.
- We start with the Euclidean algorithm to find the gcd:

```
102 = 2 * 38 + 26
38 = 1 * 26 + 12
26 = 2 * 12 + 2
12 = 6 * 2 + 0
```

- The gcd is the last non-zero remainder, which is 2.
- We then reverse the steps and write the gcd in terms of the previous two terms:

```
2 = 26 - 2 * 12
```

- We replace 12 by taking the previous line (38 = 1 * 26 + 12) and writing it in terms of 12:

```
2 = 26 - 2 * (38 - 1 * 26)
```

- We collect the like terms and simplify:

```
2 = 3 * 26 - 2 * 38
```

- We repeat the process until we reach the original numbers:

```
2 = 3 * 26 - 2 * 38
2 = 3 * (102 - 2 * 38) - 2 * 38
2 = 3 * 102 - 8 * 38
```

- We have found x and y such that 102x + 38y = 2, where x = 3 and y = -8.

#### Pseudo-code of the Algorithm

- The following is a pseudo-code of the extended Euclidean algorithm:

```
function extended_gcd(a, b)
    if b == 0
        return (a, 1, 0)
    else
        (d, x, y) = extended_gcd(b, a mod b)
        return (d, y, x - (a div b) * y)
```

- The function returns the gcd and the coefficients x and y in a tuple.
- The function uses recursion to work backwards from the Euclidean algorithm.
- The function assumes that a and b are non-negative integers.

#### Python Solution

- The following is a Python implementation of the extended Euclidean algorithm:

```
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)
```

- The function returns the gcd and the coefficients x and y in a tuple.
- The function uses recursion to work backwards from the Euclidean algorithm.
- The function assumes that a and b