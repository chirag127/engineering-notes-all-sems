# Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's identity, which states that for any integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and mod is the modulo operation.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, meaning that gcd(a,b) = 1. In this case, the algorithm can be used to find the multiplicative inverse of a modulo b, which is the unique integer x such that ax = 1 mod b.
- The extended Euclidean algorithm is also useful for computing the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.

## Algorithm

- The extended Euclidean algorithm is based on the Euclidean algorithm, which is an efficient way of computing the greatest common divisor of two numbers. The Euclidean algorithm works as follows:

  - If A = 0 then GCD(A,B) = B, since the GCD(0,B) = B, and we can stop.
  - If B = 0 then GCD(A,B) = A, since the GCD(A,0) = A, and we can stop.
  - Write A in quotient remainder form (A = B⋅Q + R)
  - Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)

- The extended Euclidean algorithm keeps track of the quotients Q and the remainders R in each step, and uses them to compute the coefficients x and y of Bézout's identity. The algorithm works as follows:

  - Initialize x1 = 1, y1 = 0, x2 = 0, y2 = 1
  - If A = 0 then x = x2, y = y2, and we can stop.
  - If B = 0 then x = x1, y = y1, and we can stop.
  - Write A in quotient remainder form (A = B⋅Q + R)
  - Update x1 = x2, y1 = y2, x2 = x1 - Q⋅x2, y2 = y1 - Q⋅y2
  - Find x and y using the extended Euclidean Algorithm with inputs B and R

- The algorithm terminates when either A or B becomes zero, and returns the values of x and y such that ax + by = gcd(a,b).

## Example

- Suppose we want to find the integers x and y such that 99x + 78y = gcd(99,78) using the extended Euclidean algorithm. We start by applying the Euclidean algorithm to find the gcd:

  - 99 = 78⋅1 + 21
  - 78 = 21⋅3 + 15
  - 21 = 15⋅1 + 6
  - 15 = 6⋅2 + 3
  - 6 = 3⋅2 + 0

- The gcd is the last nonzero remainder, which is 3. Now we use the extended Euclidean algorithm to find the coefficients x and y:

  - Initialize x1 = 1, y1 = 0, x2 = 0, y2 = 1
  - 99 = 78⋅1 + 21, update x1 = 0, y1 = 1, x2 = 1 - 1⋅0 = 1, y2 = 0 - 1⋅1 = -1
  - 78 = 21⋅3 + 15, update x1 = 1, y1 = -1, x2 = 0 - 3⋅1 = -3, y2 = 1 - 3⋅(-1) = 4
  - 21 = 15⋅1 + 6, update x1 = -3, y1 = 4, x2 = 1 -