### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b. The existence of such integers is guaranteed by Bézout's identity.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, because in that case, x is the multiplicative inverse of a modulo b, and y is the multiplicative inverse of b modulo a.
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which computes ab mod n given a, b and n.
- The extended Euclidean algorithm is the essential tool for computing multiplicative inverses in modular structures, typically the modular integers and the algebraic field extensions. A notable instance of the latter case are the finite fields of non-prime order.
- The extended Euclidean algorithm is based on the Euclidean algorithm, which is an efficient way of computing the greatest common divisor of two numbers. The Euclidean algorithm works by repeatedly applying the division algorithm and taking the remainder until it becomes zero .
- The extended Euclidean algorithm works by keeping track of the quotients and remainders in each step of the Euclidean algorithm, and then using them to express the gcd as a linear combination of the original numbers. This can be done by using a table or a matrix to store the intermediate values.
- The extended Euclidean algorithm can also be applied to polynomials, where it computes the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.
- A possible mnemonic to remember the steps of the extended Euclidean algorithm is: Divide, Remain, Repeat; Backtrack, Express, Complete.
- A possible pseudocode for the extended Euclidean algorithm is:

```
function extended_euclidean(a, b)
  // initialize two matrices
  s = [[1, 0], [0, 1]]
  t = [[0, 1], [1, 0]]
  while b != 0
    // apply division algorithm
    q = a / b
    r = a % b
    // update a and b
    a = b
    b = r
    // update s and t matrices
    s = s - q * t
    swap s and t
  // return gcd and coefficients
  return a, s[0][0], s[0][1]
```
- A possible example of the extended Euclidean algorithm is:

```
Find x and y such that 99x + 78y = gcd(99, 78)

// apply the Euclidean algorithm and store the quotients and remainders
99 = 1 * 78 + 21
78 = 3 * 21 + 15
21 = 1 * 15 + 6
15 = 2 * 6 + 3
6 = 2 * 3 + 0

// gcd(99, 78) = 3, the last non-zero remainder

// backtrack from the bottom and express each remainder as a linear combination of 99 and 78
3 = 15 - 2 * 6
3 = 15 - 2 * (21 - 1 * 15)
3 = 3 * 15 - 2 * 21
3 = 3 * (78 - 3 * 21) - 2 * 21
3 = 3 * 78 - 11 * 21
3 = 3 * 78 - 11 * (99 - 1 * 78)
3 = 14 * 78 - 11 * 99

// x = -11, y = 14
```