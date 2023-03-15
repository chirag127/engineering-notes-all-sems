## Unit 9 - Combinatorics

Combinatorics is the branch of mathematics that studies finite or countable discrete structures. It involves counting, arranging, and selecting objects or sets of objects according to certain rules or criteria.

Some of the main topics in combinatorics are:

- **Factorials**: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. Factorials are useful for counting the number of ways to order or permute a set of objects.
- **Permutations**: A permutation of a set of objects is an ordered arrangement of those objects. For example, the permutations of the set {a, b, c} are abc, acb, bac, bca, cab, and cba. The number of permutations of a set of n distinct objects is n!. The number of permutations of n objects taken r at a time, denoted by P(n, r), is n! / (n - r)!. For example, P(5, 3) = 5! / (5 - 3)! = 60.
- **Combinations**: A combination of a set of objects is an unordered selection of those objects. For example, the combinations of the set {a, b, c} taken two at a time are ab, ac, and bc. The number of combinations of a set of n distinct objects taken r at a time, denoted by C(n, r) or (n r), is n! / (r! (n - r)!). For example, C(5, 3) = 5! / (3! 2!) = 10.
- **Binomial theorem**: The binomial theorem is a formula that gives the expansion of a binomial expression raised to a positive integer power. For example, (x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3. The general form of the binomial theorem is:

(x + y)^n = C(n, 0)x^n + C(n, 1)x^(n-1)y + C(n, 2)x^(n-2)y^2 + ... + C(n, n)y^n

The coefficients C(n, r) are called binomial coefficients and can be arranged in a triangular pattern known as Pascal's triangle.
- **Multinomial theorem**: The multinomial theorem is a generalization of the binomial theorem that gives the expansion of a sum of more than two terms raised to a positive integer power. For example, (x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2xz + 2yz. The general form of the multinomial theorem is:

(x_1 + x_2 + ... + x_k)^n = C(n, n_1, n_2, ..., n_k)x_1^n_1 x_2^n_2 ... x_k^n_k

where C(n, n_1, n_2, ..., n_k) is the multinomial coefficient, which is equal to n! / (n_1! n_2! ... n_k!) and n_1 + n_2 + ... + n_k = n.
- **Inclusion-exclusion principle**: The inclusion-exclusion principle is a method for counting the number of elements in a union of sets by subtracting the number of elements in the intersections of the sets. For example, if A, B, and C are sets, then the number of elements in A ∪ B ∪ C is given by:

|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|

where |S| denotes the cardinality or size of the set S.
- **Pigeonhole principle**: The pigeonhole principle is a simple but powerful idea that states that if n items are put into m containers, where n > m, then at least one container must contain more than one item. For example, if 13 people are in a room, then at least two of them must have the same birthday (assuming there are 12 months in a year). The pigeonhole principle can be used to prove the existence of certain patterns or properties in discrete structures.