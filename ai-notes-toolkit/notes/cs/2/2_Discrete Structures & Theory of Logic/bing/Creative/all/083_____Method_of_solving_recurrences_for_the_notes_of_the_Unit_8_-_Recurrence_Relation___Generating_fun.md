# Method of solving recurrences

A recurrence relation is an equation that defines a sequence recursively, that is, each term of the sequence is expressed in terms of previous terms. Recurrence relations are often used to model the time complexity of recursive algorithms, such as divide and conquer algorithms.

There are several methods of solving recurrence relations, such as:

- **Forward substitution**: This method involves solving the recurrence relation for n = 0, 1, 2, ... until a pattern is observed. Then, a guess is made for the general form of the solution and verified by induction.
- **Recursion tree**: This method involves converting the recurrence relation into a tree, where each node represents the cost incurred at each level of recursion. The total cost is then obtained by summing up the costs of all the nodes .
- **Master theorem**: This method is applicable for a special class of divide and conquer recurrences of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants or functions. The master theorem provides a formula for the asymptotic behavior of T(n) based on the comparison of f(n) and n^(log_b a).
- **Akra-Bazzi method**: This method is a generalization of the master theorem that can handle more general forms of divide and conquer recurrences, such as T(n) = g(n) + a_1T(n/b_1) + ... + a_kT(n/b_k), where g(n) and a_i are constants or functions and b_i are constants.
- **Generating functions**: This method involves finding a function that generates the terms of the sequence as its coefficients, and then manipulating the function algebraically or analytically to obtain a closed-form expression for the sequence .