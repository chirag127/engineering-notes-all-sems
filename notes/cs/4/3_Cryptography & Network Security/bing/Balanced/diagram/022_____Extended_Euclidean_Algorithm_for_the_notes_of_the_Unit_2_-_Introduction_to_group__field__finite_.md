### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b. The existence of such integers is guaranteed by Bézout's lemma.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, because in that case, x is the multiplicative inverse of a modulo b, and y is the multiplicative inverse of b modulo a.
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which computes ab mod n by repeated multiplication, while the extended Euclidean algorithm computes x and y by repeated subtraction.
- The extended Euclidean algorithm can be implemented as follows:

```
function extended_gcd(a, b)
    if a == 0
        return (b, 0, 1)
    else
        (g, x, y) = extended_gcd(b mod a, a)
        return (g, y - (b div a) * x, x)
```

- The function returns the greatest common divisor g of a and b, and the coefficients x and y of Bézout's identity. The function can be modified to return only x or y if needed.
- The extended Euclidean algorithm can be used to compute multiplicative inverses in modular structures, such as the modular integers and the finite fields of non-prime order.
- The extended Euclidean algorithm can also be used to solve linear Diophantine equations, such as finding all integer solutions to ax + by = c, where a, b and c are given integers.
- The extended Euclidean algorithm can also be used to compute the lowest common multiple of two numbers, by using the formula lcm(a,b) = (a * b) / gcd(a,b).