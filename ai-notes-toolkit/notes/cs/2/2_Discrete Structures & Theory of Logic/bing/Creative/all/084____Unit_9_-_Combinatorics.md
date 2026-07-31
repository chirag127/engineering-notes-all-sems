## Unit 9 - Combinatorics

Combinatorics is the branch of mathematics that studies the ways of counting, arranging, and selecting objects from a given set or collection. Some of the topics covered in this unit are:

- **Factorial notation**: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. The factorial of 0 is defined to be 1, that is, 0! = 1.
- **Permutations**: A permutation of a set of objects is an ordered arrangement of those objects. For example, the permutations of the set {a, b, c} are abc, acb, bac, bca, cab, and cba. The number of permutations of n distinct objects is n!. The number of permutations of n objects taken r at a time, denoted by P(n, r), is n! / (n - r)!. For example, P(5, 3) = 5! / (5 - 3)! = 60.
- **Combinations**: A combination of a set of objects is an unordered selection of those objects. For example, the combinations of the set {a, b, c} taken 2 at a time are ab, ac, and bc. The number of combinations of n objects taken r at a time, denoted by C(n, r) or (n r), is n! / (r! (n - r)!). For example, C(5, 3) = 5! / (3! 2!) = 10.
- **Binomial theorem**: The binomial theorem is a formula that gives the expansion of a binomial expression raised to a positive integer power. For example, (x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3. The general form of the binomial theorem is:

  (x + y)^n = C(n, 0)x^n + C(n, 1)x^(n-1)y + C(n, 2)x^(n-2)y^2 + ... + C(n, n)y^n

  where C(n, r) are the binomial coefficients that can be arranged in a triangular pattern called Pascal's triangle.
- **Counting principles**: The counting principles are rules that help us to find the number of possible outcomes of a compound event. Some of the counting principles are:

  - **Multiplication principle**: If an event can occur in m ways and another event can occur in n ways, then the number of ways that both events can occur is m x n.
  - **Addition principle**: If an event can occur in m ways and another event can occur in n ways, and the two events are mutually exclusive, then the number of ways that either event can occur is m + n.
  - **Inclusion-exclusion principle**: If an event can occur in m ways and another event can occur in n ways, and the two events are not mutually exclusive, then the number of ways that either event can occur is m + n - k, where k is the number of ways that both events can occur.