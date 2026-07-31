### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an extension of the Euclidean Algorithm, which is used to find the greatest common divisor (GCD) of two numbers. The Extended Euclidean Algorithm also finds the coefficients of Bézout's identity, which are integers x and y such that:

`ax + by = gcd(a, b)`

where a and b are the two numbers whose GCD is being calculated.

The algorithm works by performing a series of divisions and keeping track of the quotients and remainders. The process is similar to the Euclidean Algorithm, but with the addition of two more equations to keep track of the coefficients of Bézout's identity.

The algorithm can be implemented using the following recursive function:

```
function extended_gcd(a, b)
    if b == 0
        return (a, 1, 0)
    else
        (d, x, y) = extended_gcd(b, a mod b)
        return (d, y, x - (a // b) * y)
```

This function returns the GCD of a and b, as well as the coefficients x and y of Bézout's identity.

The Extended Euclidean Algorithm has several applications in cryptography, including the computation of modular inverses and the solution of linear congruences. It is also used in the RSA algorithm, which is a widely used public-key encryption algorithm.