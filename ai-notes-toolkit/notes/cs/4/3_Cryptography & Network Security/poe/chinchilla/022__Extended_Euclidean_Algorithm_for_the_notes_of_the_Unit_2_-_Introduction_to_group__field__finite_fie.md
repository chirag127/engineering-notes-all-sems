### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is a variant of the Euclidean Algorithm that allows us to find the greatest common divisor (GCD) of two integers, as well as the coefficients that satisfy Bezout's identity. It is used extensively in many areas of mathematics and computer science, including number theory, cryptography, and coding theory. In this section, we will discuss the Extended Euclidean Algorithm in detail.

#### Algorithm

Given two integers a and b, the Extended Euclidean Algorithm finds their GCD d and the coefficients x and y such that ax + by = d. The algorithm proceeds as follows:

1. If b = 0, return a, x = 1, and y = 0.
2. Otherwise, recursively apply the algorithm with b and a mod b, and let d, x', and y' be the results.
3. Set x = y' and y = x' - floor(a/b)y'.
4. Return d, x, and y.

#### Example

Suppose we want to find the GCD of 252 and 198, as well as the coefficients that satisfy Bezout's identity. We apply the Extended Euclidean Algorithm as follows:

1. 252 = 1 * 198 + 54
2. 198 = 3 * 54 + 36
3. 54 = 1 * 36 + 18
4. 36 = 2 * 18 + 0

Therefore, the GCD of 252 and 198 is 18. To find the coefficients that satisfy Bezout's identity, we work backwards:

1. 18 = 54 - 1 * 36
2. 18 = 54 - 1 * (198 - 3 * 54) = -1 * 198 + 4 * 54
3. 18 = -1 * 198 + 4 * (252 - 1 * 198) = 4 * 252 - 5 * 198

Therefore, the coefficients that satisfy Bezout's identity are x = 4 and y = -5.

#### Applications

The Extended Euclidean Algorithm has many applications in mathematics and computer science. Some of these applications include:

- Finding modular inverses: If a and n are relatively prime, then the Extended Euclidean Algorithm can be used to find the inverse of a modulo n.
- Solving linear Diophantine equations: The Extended Euclidean Algorithm can be used to find all solutions of a linear Diophantine equation of the form ax + by = c.
- RSA encryption and decryption: The Extended Euclidean Algorithm is used in the RSA cryptosystem to find the modular inverse of the public key, which is used to encrypt messages.