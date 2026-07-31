# Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b.
- The existence of such integers is guaranteed by Bézout's lemma.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, as x is then the multiplicative inverse of a modulo b, and y is the multiplicative inverse of b modulo a.
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation.
- The extended Euclidean algorithm is based on the Euclidean algorithm, which is an efficient way of computing the greatest common divisor of two numbers.
- The Euclidean algorithm works by repeatedly applying the division algorithm and finding the remainder until it becomes zero.
- The extended Euclidean algorithm works by keeping track of the quotients and remainders in each step, and then using back substitution to find x and y.

## Example

- Suppose we want to find x and y such that 99x + 78y = gcd(99,78) = 3.
- We apply the Euclidean algorithm as follows:

```
99 = 78 * 1 + 21
78 = 21 * 3 + 15
21 = 15 * 1 + 6
15 = 6 * 2 + 3
6 = 3 * 2 + 0
```

- The last non-zero remainder is 3, which is the gcd of 99 and 78.
- We then use back substitution to find x and y:

```
3 = 15 - 6 * 2
3 = 15 - (21 - 15) * 2
3 = 15 * 3 - 21 * 2
3 = (78 - 21 * 3) * 3 - 21 * 2
3 = 78 * 3 - 21 * 11
3 = 78 * 3 - (99 - 78) * 11
3 = 78 * 14 - 99 * 11
```

- Therefore, x = -11 and y = 14 are the solutions.