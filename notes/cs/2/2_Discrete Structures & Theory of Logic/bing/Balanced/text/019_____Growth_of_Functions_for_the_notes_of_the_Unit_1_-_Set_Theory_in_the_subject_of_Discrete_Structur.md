### Growth of Functions

- A function f(n) is said to grow faster than a function g(n) if there exists a positive constant c and a positive integer N such that f(n) > c g(n) for all n > N.
- The growth of a function is a measure of how quickly its values increase as the input variable increases.
- The growth of a function can be compared using asymptotic notation, such as big O, big Omega, and big Theta, which describe the upper, lower, and tight bounds of a function respectively.
- Asymptotic notation is useful for analyzing the efficiency and complexity of algorithms, as well as the behavior of sequences and series.
- Some examples of common functions and their growth rates are:

| Function | Growth Rate |
| -------- | ----------- |
| Constant | O(1)        |
| Logarithmic | O(log n)   |
| Linear | O(n)         |
| Linearithmic | O(n log n) |
| Quadratic | O(n^2)      |
| Cubic | O(n^3)        |
| Exponential | O(2^n)     |
| Factorial | O(n!)       |

- The growth rate of a function can be determined by applying some rules, such as:

  - If f(n) and g(n) are positive functions, then O(f(n) + g(n)) = O(max(f(n), g(n))).
  - If f(n) and g(n) are positive functions, then O(f(n) g(n)) = O(f(n)) O(g(n)).
  - If f(n) and g(n) are positive functions, then O(f(g(n))) = O(g(n)) if f(n) is O(1), and O(f(n)) if g(n) is O(1).
  - If f(n) and g(n) are positive functions, then O(f(n)^g(n)) = O(2^g(n) log f(n)).
  - If f(n) and g(n) are positive functions, then O(log f(n)) = O(log g(n)) if f(n) and g(n) have the same asymptotic growth rate.