### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an extension of the Euclidean Algorithm for finding the greatest common divisor (GCD) of two numbers. The GCD of two numbers is the largest number that divides both of them. The Euclidean Algorithm is based on the principle that the GCD of two numbers does not change if the smaller number is subtracted from the larger number.

The Extended Euclidean Algorithm not only calculates the GCD of two numbers `a` and `b`, but also finds integers `x` and `y` such that `ax + by = gcd(a, b)`. This is known as Bézout's identity.

The algorithm can be described as follows:
1. If `b = 0`, then `gcd(a, b) = a`, `x = 1`, and `y = 0`.
2. Otherwise, let `g, x1, y1` be the output of the Extended Euclidean Algorithm for `b` and `a mod b`.
3. Then, `gcd(a, b) = g`, `x = y1`, and `y = x1 - floor(a/b) * y1`.

The Extended Euclidean Algorithm can be used to find modular inverses. If `a` and `m` are relatively prime, then the modular inverse of `a` modulo `m` is the integer `x` such that `ax ≡ 1 (mod m)`. This can be found using the Extended Euclidean Algorithm by setting `b = m` and solving for `x` in the equation `ax + my = gcd(a, m) = 1`.

The Extended Euclidean Algorithm can also be used to solve linear Diophantine equations of the form `ax + by = c`, where `a`, `b`, and `c` are given integers and `x` and `y` are unknown integers. If `d = gcd(a, b)` divides `c`, then the equation has a solution. The solution can be found using the Extended Euclidean Algorithm by setting `a' = a/d`, `b' = b/d`, and `c' = c/d`, and solving for `x` and `y` in the equation `a'x + b'y = gcd(a', b') = 1`. The solutions to the original equation are given by `x = x0 * c'` and `y = y0 * c'`, where `x0` and `y0` are the solutions to the equation `a'x + b'y = 1`. Other solutions can be found by adding multiples of `b/d` to `x` and subtracting multiples of `a/d` from `y`.