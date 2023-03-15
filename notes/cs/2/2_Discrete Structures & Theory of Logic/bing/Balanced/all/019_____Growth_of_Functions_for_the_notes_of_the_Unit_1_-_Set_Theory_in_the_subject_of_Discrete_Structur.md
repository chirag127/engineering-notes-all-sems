# Growth of Functions

- The growth of a function is a measure of how fast its value increases as the input value increases.
- The growth of a function is important for analyzing the efficiency and complexity of algorithms, as well as the asymptotic behavior of sequences and series.
- The growth of a function is determined by the highest order term: if you add a bunch of terms, the function grows about as fast as the largest term (for large enough input values).
- For example, f(x) = x^2 + 1 grows as fast as g(x) = x^2 + 2 and h(x) = x^2 + x + 1, because for large x, x^2 is much bigger than 1, 2, or x + 1.
- The growth of functions is often described using a special notation – the Big-O Notation, Big-Omega Notation, and Big-Theta Notation. These special notations estimate the growth of the function by comparing it to another simpler function.
- Big-O Notation: f(x) is O(g(x)) if there are constants C and k such that |f(x)| <= C|g(x)| whenever x > k. In other words, Big-O is the upper bound for the growth of the function.
- Big-Omega Notation: f(x) is Omega(g(x)) if there are constants C and k such that |f(x)| >= C|g(x)| whenever x > k. In other words, Big-Omega is the lower bound for the growth of the function.
- Big-Theta Notation: f(x) is Theta(g(x)) if there are constants C1, C2 and k such that C1|g(x)| <= |f(x)| <= C2|g(x)| whenever x > k. In other words, Big-Theta is the tight bound for the growth of the function.
- For example, f(x) = 3x^2 + 5 is O(x^2), Omega(x^2), and Theta(x^2), because we can choose C = 8, k = 1 for Big-O, C = 2, k = 1 for Big-Omega, and C1 = 2, C2 = 8, k = 1 for Big-Theta.
- Some common classes of functions and their growth rates are:

| Class | Example | Growth Rate |
| --- | --- | --- |
| Constant | f(x) = 5 | O(1) |
| Logarithmic | f(x) = log x | O(log x) |
| Linear | f(x) = 3x + 2 | O(x) |
| Polynomial | f(x) = x^3 + 2x + 1 | O(x^n) |
| Exponential | f(x) = 2^x | O(a^x) |
| Factorial | f(x) = x! | O(x!) |

- The growth rate of a function can be used to compare the efficiency of different algorithms for solving the same problem. For example, an algorithm that runs in O(n) time is more efficient than an algorithm that runs in O(n^2) time, because the former grows slower than the latter as the input size n increases.