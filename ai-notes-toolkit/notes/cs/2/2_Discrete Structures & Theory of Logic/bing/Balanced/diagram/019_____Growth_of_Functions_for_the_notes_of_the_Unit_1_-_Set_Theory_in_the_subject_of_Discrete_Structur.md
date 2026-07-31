### Growth of Functions

- A function f(n) is said to grow faster than another function g(n) if f(n) becomes larger than g(n) for sufficiently large values of n.
- The growth of a function is related to its asymptotic behavior, which describes how the function behaves as n approaches infinity.
- The growth of a function can be compared using the following notations:
  - Big-O notation: f(n) = O(g(n)) means that f(n) is bounded above by some constant multiple of g(n) for sufficiently large n. For example, 2n + 3 = O(n) and n^2 = O(n^3).
  - Big-Omega notation: f(n) = Ω(g(n)) means that f(n) is bounded below by some constant multiple of g(n) for sufficiently large n. For example, 2n + 3 = Ω(n) and n^3 = Ω(n^2).
  - Big-Theta notation: f(n) = Θ(g(n)) means that f(n) is bounded above and below by some constant multiples of g(n) for sufficiently large n. For example, 2n + 3 = Θ(n) and n^2 = Θ(n^2).
  - Little-o notation: f(n) = o(g(n)) means that f(n) grows slower than g(n) for sufficiently large n. For example, 2n + 3 = o(n^2) and n = o(n^2).
  - Little-omega notation: f(n) = ω(g(n)) means that f(n) grows faster than g(n) for sufficiently large n. For example, 2n + 3 = ω(n) and n^2 = ω(n).
- The growth of a function can also be classified into the following categories:
  - Constant: f(n) = c, where c is a constant. For example, f(n) = 5.
  - Linear: f(n) = an + b, where a and b are constants. For example, f(n) = 2n + 3.
  - Quadratic: f(n) = an^2 + bn + c, where a, b, and c are constants. For example, f(n) = n^2 + 2n + 1.
  - Polynomial: f(n) = a_k n^k + a_(k-1) n^(k-1) + ... + a_1 n + a_0, where a_k, a_(k-1), ..., a_1, and a_0 are constants. For example, f(n) = 3n^3 + 2n^2 + n + 4.
  - Exponential: f(n) = a^n, where a is a constant. For example, f(n) = 2^n.
  - Logarithmic: f(n) = log_a n, where a is a constant. For example, f(n) = log_2 n.
  - Log-linear: f(n) = n log_a n, where a is a constant. For example, f(n) = n log_2 n.