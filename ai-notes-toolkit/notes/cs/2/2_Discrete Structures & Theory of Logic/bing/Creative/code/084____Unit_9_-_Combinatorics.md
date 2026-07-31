## Unit 9 - Combinatorics

Combinatorics is the branch of mathematics that studies finite or countable discrete structures. It involves counting, arranging, and selecting objects or sets of objects that satisfy certain criteria.

Some of the main topics in combinatorics are:

- **Factorials**: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. Factorials are useful for counting the number of ways to order or permute a set of objects.
- **Permutations**: A permutation of a set of objects is an ordered arrangement of those objects. For example, the permutations of the set {a, b, c} are abc, acb, bac, bca, cab, and cba. The number of permutations of a set of n distinct objects is n!. The number of permutations of n objects taken r at a time, denoted by P(n, r), is n! / (n - r)!. For example, P(5, 3) = 5! / (5 - 3)! = 60.
- **Combinations**: A combination of a set of objects is an unordered selection of those objects. For example, the combinations of the set {a, b, c} taken 2 at a time are ab, ac, and bc. The number of combinations of a set of n distinct objects taken r at a time, denoted by C(n, r) or (n r), is n! / (r! (n - r)!). For example, C(5, 3) = 5! / (3! 2!) = 10.
- **Binomial theorem**: The binomial theorem is a formula that gives the expansion of a binomial expression raised to a positive integer power. For example, (x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3. The general form of the binomial theorem is:

  (x + y)^n = C(n, 0)x^n + C(n, 1)x^(n-1)y + C(n, 2)x^(n-2)y^2 + ... + C(n, n)y^n

  where C(n, r) are the binomial coefficients that count the number of ways to choose r objects from n objects.
- **Pascal's triangle**: Pascal's triangle is a triangular array of numbers that shows the binomial coefficients. The nth row of Pascal's triangle corresponds to the coefficients of the expansion of (x + y)^n. The first few rows of Pascal's triangle are:

  1
  1 1
  1 2 1
  1 3 3 1
  1 4 6 4 1
  1 5 10 10 5 1

  Pascal's triangle has many interesting properties and patterns, such as the sum of the elements in each row is 2^n, the diagonal elements are the natural numbers, and the elements along the edges are all 1.
- **The principle of inclusion-exclusion**: The principle of inclusion-exclusion is a method for counting the number of elements in a union of sets by subtracting the overlaps. For example, if A and B are two sets, then the number of elements in A or B is given by:

  |A or B| = |A| + |B| - |A and B|

  where |X| denotes the number of elements in X. The principle can be extended to more than two sets by using a formula that alternates between adding and subtracting the intersections of different numbers of sets. For example, if A, B, and C are three sets, then the number of elements in A or B or C is given by:

  |A or B or C| = |A| + |B| + |C| - |A and B| - |A and C| - |B and C| + |A and B and C|