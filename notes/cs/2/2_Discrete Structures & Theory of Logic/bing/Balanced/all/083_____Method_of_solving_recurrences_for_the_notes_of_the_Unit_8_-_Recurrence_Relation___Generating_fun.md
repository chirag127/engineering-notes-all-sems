# Method of solving recurrences

- A recurrence relation is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- Recurrence relations are often used to model the time complexity of algorithms that use recursion or divide and conquer techniques.
- There are several methods of solving recurrence relations, such as:

  - Forward substitution: This method involves solving the recurrence relation for small values of n until a pattern is observed, then making a guess and proving it by induction.
  - Recursion tree: This method involves drawing a tree that represents the cost of each recursive call, then summing up the costs at each level of the tree and finding a closed-form expression for the total cost.
  - Master method: This method is applicable for recurrence relations of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants or functions of n. The method provides a formula for the asymptotic behavior of T(n) based on the comparison of f(n) and n^(log_b a).
  - Akra-Bazzi method: This method is a generalization of the master method that can handle recurrence relations of the form T(n) = g(n) + \sum_{i=1}^k a_i T(b_i n + h_i(n)), where g(n), a_i, b_i, and h_i(n) are constants or functions of n. The method involves finding a constant p that satisfies a certain equation, then using it to derive the asymptotic behavior of T(n).