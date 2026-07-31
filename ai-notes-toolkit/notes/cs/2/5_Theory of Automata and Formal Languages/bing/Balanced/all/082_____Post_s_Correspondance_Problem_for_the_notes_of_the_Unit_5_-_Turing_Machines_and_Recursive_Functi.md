# Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows: Given two lists, M and N, of non-empty strings over Σ, such as:

  M = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ..., x<sub>n</sub>)

  N = (y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>, ..., y<sub>n</sub>)

  Find a sequence of indices (i<sub>1</sub>, i<sub>2</sub>, i<sub>3</sub>, ..., i<sub>k</sub>) such that:

  x<sub>i1</sub>x<sub>i2</sub>x<sub>i3</sub>...x<sub>ik</sub> = y<sub>i1</sub>y<sub>i2</sub>y<sub>i3</sub>...y<sub>ik</sub>

  If such a sequence exists, the PCP problem has a solution. Otherwise, it has no solution.

- The PCP problem can be visualized using dominoes, where each domino has a top string and a bottom string. The goal is to arrange the dominoes horizontally such that the top string and the bottom string are equal .

  For example, given the following dominoes:

  | 1 | 2 | 3 |
  |:-:|:-:|:-:|
  | a | ab | baa |
  | ba | a | aa |

  A possible solution is:

  | 2 | 3 | 1 | 3 |
  |:-:|:-:|:-:|:-:|
  | ab | baa | a | baa |
  | a | aa | ba | aa |

  Because:

  abbabaa = aaaabaa

- The PCP problem is undecidable, meaning that there is no algorithm that can determine whether a given instance of the PCP problem has a solution or not for all possible instances  .
- The PCP problem is often used in proofs of undecidability, because it is simpler than the halting problem and the Entscheidungsproblem .
- The PCP problem can be generalized to the Modified Post Correspondence Problem (MPCP), where the first domino in the sequence must have the same index as the last domino. The MPCP problem is also undecidable, and can be used to prove the undecidability of other problems, such as the emptiness problem for context-free grammars.