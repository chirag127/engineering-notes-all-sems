# Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows: Given two lists of non-empty strings over Σ, M = (x1, x2, ..., xn) and N = (y1, y2, ..., yn), determine whether there exists a sequence of indices (i1, i2, ..., ik) such that x(i1) x(i2) ... x(ik) = y(i1) y(i2) ... y(ik), where x(i) and y(i) denote the ith elements of M and N respectively .
- The strings x(i) and y(i) are called the top and bottom strings of a domino, and the pair (x(i), y(i)) is called a domino. A solution to the PCP problem is a sequence of dominos whose top and bottom strings are equal .
- For example, consider the following instance of the PCP problem over the alphabet {a, b}:

  M = (ab, b, aab, abaa)
  N = (b, aa, a, aba)

  A possible solution is the sequence of indices (1, 3, 4, 2), which corresponds to the following sequence of dominos:

  |ab|aab|abaa|b|
  |b|a|aba|aa|

  The top and bottom strings are both abaababaaa.

- The PCP problem is undecidable, meaning that there is no algorithm that can always correctly answer yes or no for any given instance of the problem. This can be proved by reducing the halting problem to the PCP problem, i.e., by showing that if there were an algorithm for the PCP problem, then we could use it to solve the halting problem, which is known to be undecidable  .
- The PCP problem is often used in proofs of undecidability for other problems in logic or in formal language theory, such as the word problem for context-free grammars, the equivalence problem for regular expressions, or the satisfiability problem for first-order logic .
- The PCP problem is also related to some open problems in combinatorics and number theory, such as the Collatz conjecture, the abc conjecture, and the Erdős–Graham problem.