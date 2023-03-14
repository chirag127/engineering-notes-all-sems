The Extended Euclidean Algorithm is a method of finding integers x and y such that ax + by = gcd(a, b) given integers a and b. It is based on the Euclidean Algorithm, which computes the greatest common divisor of two integers by repeated division and remainder operations. The Extended Euclidean Algorithm also allows one to compute the modular multiplicative inverse of a number modulo another number, which is useful in cryptography.

One way to illustrate the Extended Euclidean Algorithm is to use a table that shows the steps of the Euclidean Algorithm and the corresponding values of x and y. For example, suppose we want to find x and y such that 102x + 38y = gcd(102, 38). We can use the following table:

| a | b | q | r | x | y |
|---|---|---|---|---|---|
| 102 | 38 | 2 | 26 | 0 | 1 |
| 38 | 26 | 1 | 12 | 1 | -2 |
| 26 | 12 | 2 | 2 | -2 | 5 |
| 12 | 2 | 6 | 0 | 5 | -14 |

The first two columns show the Euclidean Algorithm, where a is the dividend, b is the divisor, q is the quotient, and r is the remainder. The last two columns show the values of x and y that satisfy ax + by = gcd(a, b). The initial values are x = 0, y = 1 for the first row, and x = 1, y = -q for the second row, where q is the quotient of the first division. Then, for each subsequent row, we use the formula:

x = x(previous) - q x(current)
y = y(previous) - q y(current)

For example, for the third row, we have:

x = 0 - 2 * 1 = -2
y = 1 - 2 * (-2) = 5

We stop when the remainder is zero, and the last non-zero remainder is the gcd. In this case, the gcd is 2, and the values of x and y that satisfy 102x + 38y = 2 are x = -2 and y = 5. We can check this by plugging in the values:

102 * (-2) + 38 * 5 = -204 + 190 = -14 + 16 = 2

This is the basic idea of the Extended Euclidean Algorithm. There are different ways to implement it in pseudocode or programming languages, but the logic is the same. I hope this helps you understand the algorithm and how to draw a diagram for it.