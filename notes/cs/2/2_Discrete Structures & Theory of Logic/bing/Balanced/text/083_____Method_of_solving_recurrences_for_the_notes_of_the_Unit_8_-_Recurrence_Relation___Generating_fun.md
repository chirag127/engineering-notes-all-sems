### Method of solving recurrences

- A recurrence relation is an equation that defines a sequence in terms of its previous terms. For example, T(n) = T(n-1) + n is a recurrence relation that defines the nth term of a sequence as the sum of the previous term and n.
- Recurrence relations often arise in the analysis of algorithms, especially recursive algorithms. For example, the recurrence relation T(n) = 2T(n/2) + n describes the running time of the merge sort algorithm.
- Solving a recurrence relation means finding a closed-form expression or a formula for the general term of the sequence, without referring to the previous terms. For example, the solution of the recurrence relation T(n) = T(n-1) + n is T(n) = n(n+1)/2.
- There are different methods of solving recurrences, depending on the type and complexity of the recurrence relation. Some of the common methods are:

  - **Forward substitution**: This method involves substituting the recurrence relation for n = 0, 1, 2, ... until a pattern is observed. Then, a guess is made for the general form of the solution and verified by induction. This method is simple but may not work for complex recurrences or may require a lot of computation. For example, using this method, we can solve the recurrence relation T(n) = T(n-1) + n as follows:

    - T(0) = 0 (base case)
    - T(1) = T(0) + 1 = 1
    - T(2) = T(1) + 2 = 3
    - T(3) = T(2) + 3 = 6
    - T(4) = T(3) + 4 = 10
    - ...
    - We can see that the sequence is the sum of the first n natural numbers, so we guess that T(n) = n(n+1)/2. To prove this by induction, we assume that T(k) = k(k+1)/2 for some k >= 0 and show that T(k+1) = (k+1)(k+2)/2. This is true because:

      - T(k+1) = T(k) + (k+1) by the recurrence relation
      - T(k+1) = k(k+1)/2 + (k+1) by the induction hypothesis
      - T(k+1) = (k+1)(k+2)/2 by simplifying
      - Therefore, T(n) = n(n+1)/2 for all n >= 0 by induction.

  - **Recursion tree**: This method involves drawing a tree that represents the cost of each level of recursion. The cost of each node is the amount of work done at that level, excluding the recursive calls. The total cost of the recurrence is the sum of the costs of all the nodes in the tree. This method is useful for visualizing the recurrence and estimating its asymptotic behavior. For example, using this method, we can solve the recurrence relation T(n) = 2T(n/2) + n as follows:

    - The recursion tree for this recurrence is:

      ```
      T(n) = n + 2T(n/2)
            /        \
      T(n/2) = n/2 + 2T(n/4)
              /          \
      T(n/4) = n/4 + 2T(n/8)
              /          \
             ...
            /   \
      T(1) = 1 + 2T(1/2)
            /       \
      T(1/2) = 0 + 2T(1/4)
              /         \
             ...
      ```

    - The cost of each level is n, since there are 2^i nodes at level i, each with a cost of n/2^i. The number of levels is log(n), since the recursion stops when n/2^i = 1. Therefore, the total cost of the recurrence is:

      - T(n) = n + n + n + ... + n (log(n) times)
      - T(n) = n log(n)

  - **Master theorem**: This method is a general formula for solving recurrences of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants or functions of n. The master theorem states that the solution of the