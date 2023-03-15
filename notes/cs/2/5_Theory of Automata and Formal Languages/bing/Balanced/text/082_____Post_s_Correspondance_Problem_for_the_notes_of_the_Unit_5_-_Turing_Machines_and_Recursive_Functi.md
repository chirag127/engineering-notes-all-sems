### Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows: Given two lists of non-empty strings over Σ, M = (x1, x2, ..., xn) and N = (y1, y2, ..., yn), determine whether there exists a sequence of indices (i1, i2, ..., ik) such that x(i1) x(i2) ... x(ik) = y(i1) y(i2) ... y(ik), where x(i) and y(i) are the ith elements of M and N respectively .
- The strings x(i) and y(i) can be viewed as the top and bottom halves of a domino, and the problem is to find a way to arrange some of the dominoes (possibly with repetitions) such that the top and bottom strings match .
- For example, given the following two lists of strings over the alphabet {a, b}:

  M = (ab, b, aab, abaa)

  N = (b, aa, ba, a)

  A possible solution is the sequence of indices (1, 3, 4, 2, 3), which corresponds to the following arrangement of dominoes:

  ```
  |ab|aab|abaa|b|aab|
  |b |ba |a   |aa|ba |
  ```

  The top and bottom strings are both abaababaaaaba.

- The PCP problem is undecidable, meaning that there is no algorithm that can always correctly answer yes or no for any given instance of the problem  .
- The PCP problem is often used in proofs of undecidability, because it is simpler than the halting problem and the Entscheidungsproblem, and it can be reduced to many other problems in logic or in formal language theory .