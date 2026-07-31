### Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows:
  - Given two lists, M and N, of non-empty strings over Σ, such as:
    - M = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ..., x<sub>n</sub>)
    - N = (y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>, ..., y<sub>n</sub>)
  - Find a sequence of indices (i<sub>1</sub>, i<sub>2</sub>, i<sub>3</sub>, ..., i<sub>k</sub>) such that:
    - x<sub>i1</sub>x<sub>i2</sub>x<sub>i3</sub>...x<sub>ik</sub> = y<sub>i1</sub>y<sub>i2</sub>y<sub>i3</sub>...y<sub>ik</sub>
  - Such a sequence is called a solution to the PCP instance.
- The PCP problem is undecidable, meaning that there is no algorithm that can determine whether a given PCP instance has a solution or not   .
- The PCP problem is often used in proofs of undecidability, because it is simpler than the halting problem and the Entscheidungsproblem .
- The PCP problem can be illustrated using dominoes, where each domino has a top string and a bottom string, and the goal is to arrange the dominoes horizontally such that the top string and the bottom string are equal .
- For example, consider the following PCP instance over the alphabet {a, b}:
  - M = (ab, b, a, abab)
  - N = (b, aa, aba, a)
  - The dominoes corresponding to this instance are:

    | ab | b | a | abab |
    | -- | - | - | ---- |
    | b  | aa| aba| a    |

  - A possible solution to this instance is the sequence (1, 4, 2, 3), which gives:

    | ab | abab | b | a |
    | -- | ---- | - | - |
    | b  | a    | aa| aba|

  - Note that the top string and the bottom string are both ababaabaa.