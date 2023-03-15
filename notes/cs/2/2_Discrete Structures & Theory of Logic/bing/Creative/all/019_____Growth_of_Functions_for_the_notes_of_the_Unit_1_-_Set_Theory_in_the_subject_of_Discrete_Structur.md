# Growth of Functions

- The growth of a function is a measure of how fast its values increase as the input values increase.
- The growth of a function is important for analyzing the efficiency and complexity of algorithms and data structures.
- The growth of a function is often described using a special notation – the Big-O Notation, Big-Omega Notation, and Big-Theta Notation. These special notations estimate the growth of the function by comparing it to another simpler function.
- The Big-O Notation, denoted by O(g(x)), represents the upper bound of the growth of a function f(x). It means that f(x) grows at most as fast as g(x) for sufficiently large values of x. For example, f(x) = x^2 + 1 is O(x^2) because x^2 + 1 is always less than or equal to 2x^2 for x > 1.
- The Big-Omega Notation, denoted by Ω(g(x)), represents the lower bound of the growth of a function f(x). It means that f(x) grows at least as fast as g(x) for sufficiently large values of x. For example, f(x) = x^2 + 1 is Ω(x^2) because x^2 + 1 is always greater than or equal to x^2 for x > 0.
- The Big-Theta Notation, denoted by Θ(g(x)), represents the exact bound of the growth of a function f(x). It means that f(x) grows at the same rate as g(x) for sufficiently large values of x. For example, f(x) = x^2 + 1 is Θ(x^2) because x^2 + 1 is always between x^2 and 2x^2 for x > 1.
- The growth of a function is determined by the highest order term: if you add a bunch of terms, the function grows about as fast as the largest term (for large enough input values). For example, f(x) = x^2 + 1 grows as fast as g(x) = x^2 + 2 and h(x) = x^2 + x + 1, because for large x, x^2 is much bigger than 1, 2, or x + 1.
- The growth of a function is also affected by the base of the exponent: if you have a function of the form f(x) = a^x, where a is a constant, then the larger the value of a, the faster the function grows. For example, f(x) = 2^x grows faster than g(x) = 1.5^x, which grows faster than h(x) = 1.1^x.
- The growth of a function can be compared using the following rules:
  - If f(x) and g(x) are polynomials, then f(x) is O(g(x)) if and only if the degree of f(x) is less than or equal to the degree of g(x).
  - If f(x) and g(x) are exponential functions, then f(x) is O(g(x)) if and only if the base of f(x) is less than or equal to the base of g(x).
  - If f(x) is a polynomial and g(x) is an exponential function, then f(x) is O(g(x)).
  - If f(x) is a logarithmic function and g(x) is a polynomial or an exponential function, then f(x) is O(g(x)).