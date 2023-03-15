### Growth of Functions

- The growth of a function is a measure of how fast its output value increases as its input value becomes larger.
- The growth of a function is determined by the highest order term: if you add a bunch of terms, the function grows about as fast as the largest term (for large enough input values).
- For example, f(x) = x^2 + 1 grows as fast as g(x) = x^2 + 2 and h(x) = x^2 + x + 1, because for large x, x^2 is much bigger than 1, 2, or x + 1.
- The growth of functions is often described using a special notation – the Big-O Notation, Big-Omega Notation, and Big-Theta Notation. Theses special notations estimate the growth of the function by comparing it to another simpler function.
- Big-O Notation: We say f(x) is O(g(x)) if there are constants C and k such that |f(x)| <= C|g(x)| whenever x > k. In other words, Big-O is the upper bound for the growth of the function.
- Big-Omega Notation: We say f(x) is Omega(g(x)) if there are constants C and k such that |f(x)| >= C|g(x)| whenever x > k. In other words, Big-Omega is the lower bound for the growth of the function.
- Big-Theta Notation: We say f(x) is Theta(g(x)) if there are constants C1, C2 and k such that C1|g(x)| <= |f(x)| <= C2|g(x)| whenever x > k. In other words, Big-Theta is the tight bound for the growth of the function.
- For example, f(x) = 3x^2 + 5x + 2 is O(x^2), Omega(x^2), and Theta(x^2), because we can choose appropriate constants C, C1, C2 and k to satisfy the inequalities.
- The growth of functions is important for analyzing the efficiency and complexity of algorithms, as it gives an estimate of how fast the running time or the memory usage of an algorithm increases as the input size increases .