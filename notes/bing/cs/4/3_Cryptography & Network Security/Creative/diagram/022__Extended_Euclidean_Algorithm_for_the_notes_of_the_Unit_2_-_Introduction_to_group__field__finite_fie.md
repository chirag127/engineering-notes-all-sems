The Extended Euclidean Algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b. The existence of such integers is guaranteed by Bézout's lemma. The algorithm can be used to find multiplicative inverses in modular arithmetic, which are useful for cryptography and number theory.

The algorithm works as follows:

- If a = 0, then gcd(a,b) = b and x = 0, y = 1. Stop.
- If b = 0, then gcd(a,b) = a and x = 1, y = 0. Stop.
- Write a as a quotient and a remainder of b: a = bq + r.
- Recursively apply the algorithm to b and r: gcd(b,r) = bx' + ry'.
- Substitute r = a - bq into the previous equation: gcd(b,r) = bx' + (a - bq)y'.
- Rearrange the terms: gcd(b,r) = ay' + b(x' - qy').
- Compare with the original equation: gcd(a,b) = ax + by.
- Conclude that x = y' and y = x' - qy'. Stop.

The following diagram illustrates the basic steps of the algorithm using an example of a = 35 and b = 15:

```
  a  |  b  |  q  |  r  |  x  |  y
---------------------------------
 35  | 15  |  2  |  5  |  ?  |  ?
 15  |  5  |  3  |  0  |  0  |  1
  5  |  0  |  -  |  -  |  1  |  0
---------------------------------
gcd(35,15) = 5 = 1*35 + (-2)*15
x = 1, y = -2
```
