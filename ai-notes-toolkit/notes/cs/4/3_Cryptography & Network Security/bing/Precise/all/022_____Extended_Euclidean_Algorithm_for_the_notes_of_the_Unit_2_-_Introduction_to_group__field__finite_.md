### Extended Euclidean Algorithm

The Extended Euclidean Algorithm is an extension to the Euclidean Algorithm, which computes, besides the greatest common divisor of integers a and b, the coefficients of Bézout's identity, that is integers x and y such that ax + by = gcd(a, b).

The algorithm is based on the observation that the remainders obtained during the application of the Euclidean algorithm to compute the greatest common divisor of two numbers satisfy the same linear equation as the original numbers, but with the coefficients swapped and negated.

The algorithm can be described as follows:

1. Initialize x1 = 1, y1 = 0, x2 = 0, y2 = 1
2. While b ≠ 0:
    1. Compute the quotient and remainder: q = a div b, r = a mod b
    2. Set a = b, b = r
    3. Update the coefficients: x1, y1, x2, y2 = x2, y2, x1 - q * x2, y1 - q * y2
3. The greatest common divisor is a, and the coefficients are x1 and y1.

The Extended Euclidean Algorithm can be used to solve linear Diophantine equations, that is equations of the form ax + by = c, where a, b, and c are given integers and x and y are unknown integers. It can also be used to compute modular inverses, that is to find an integer x such that ax ≡ 1 (mod m), where a and m are given integers and x is an unknown integer.

The algorithm can be implemented efficiently using recursion or iteration. The time complexity of the algorithm is O(log(min(a, b))) in the worst case. The space complexity is O(1) for the iterative version and O(log(min(a, b))) for the recursive version. The algorithm can be extended to compute the greatest common divisor and the coefficients of Bézout's identity for more than two integers. The time complexity of the extended version is O(k * log(max(a1, a2, ..., ak))) in the worst case, where k is the number of integers. The space complexity is O(k) for the iterative version and O(k * log(max(a1, a2, ..., ak))) for the recursive version.