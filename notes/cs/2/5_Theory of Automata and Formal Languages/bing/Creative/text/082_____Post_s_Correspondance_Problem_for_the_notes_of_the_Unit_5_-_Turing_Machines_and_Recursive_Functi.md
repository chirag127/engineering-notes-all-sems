### Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows:
  - Given two lists, M and N, of non-empty strings over Σ, such as:
    - M = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ..., x<sub>n</sub>)
    - N = (y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>, ..., y<sub>n</sub>)
  - Find a sequence of indices (i<sub>1</sub>, i<sub>2</sub>, i<sub>3</sub>, ..., i<sub>k</sub>) such that:
    - x<sub>i<sub>1</sub></sub>x<sub>i<sub>2</sub></sub>x<sub>i<sub>3</sub></sub>...x<sub>i<sub>k</sub></sub> = y<sub>i<sub>1</sub></sub>y<sub>i<sub>2</sub></sub>y<sub>i<sub>3</sub></sub>...y<sub>i<sub>k</sub></sub>
  - Such a sequence is called a solution to the PCP instance.
- The PCP problem is to determine whether a given instance of PCP has a solution or not  .
- The PCP problem is undecidable, meaning that there is no algorithm that can always correctly answer yes or no for any PCP instance   .
- The PCP problem is often used in proofs of undecidability, because it is simpler than the halting problem and the Entscheidungsproblem .
- The PCP problem can be visualized using dominoes, where each domino has a string from M on the top and a string from N on the bottom .
  - A solution to the PCP instance is a way of stacking the dominoes horizontally such that the top and bottom strings match.
  - For example, consider the following PCP instance over the alphabet {a, b}:
    - M = (ab, b, a, ba)
    - N = (a, ba, b, ab)
  - The dominoes for this instance are:

    | ab | b  | a  | ba |
    |----|----|----|----|
    | a  | ba | b  | ab |

  - A solution to this instance is the sequence (1, 4, 2, 3), which corresponds to the following stacking of dominoes:

    | ab | ba | b  | a  |
    |----|----|----|----|
    | a  | ab | ba | b  |

  - The top and bottom strings are both ababab, so they match.