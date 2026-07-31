### Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows:
  - Given two lists, M and N, of non-empty strings over Σ, such as:
    - M = (x1, x2, x3, ..., xn)
    - N = (y1, y2, y3, ..., yn)
  - Find a sequence of indices (i1, i2, i3, ..., ik) such that:
    - x(i1) x(i2) x(i3) ... x(ik) = y(i1) y(i2) y(i3) ... y(ik)
  - If such a sequence exists, the PCP problem has a solution. Otherwise, it has no solution.
- The PCP problem can be represented using dominoes (tiles) with two strings written on them, one on the top and one on the bottom .
  - Each domino corresponds to a pair of strings (xi, yi) from the lists M and N.
  - The sequence of indices is equivalent to a sequence of dominoes that can be stacked horizontally such that the top and bottom strings match.
  - For example, consider the following instance of the PCP problem over the alphabet {a, b}:
    - M = (ab, b, a, aba)
    - N = (a, ba, b, aa)
  - This can be represented by the following dominoes:

    ```
    |  ab  |  b  |  a  |  aba  |
    |  a   |  ba |  b  |  aa   |
    ```

  - A possible solution is the sequence of indices (1, 4, 3, 2, 3) or the sequence of dominoes:

    ```
    |  ab  |  aba  |  a  |  b  |  a  |
    |  a   |  aa   |  b  |  ba |  b  |
    ```

  - The top and bottom strings are both abababab.

- The PCP problem is undecidable, meaning that there is no algorithm that can determine whether a given instance of the PCP problem has a solution or not  .
  - This can be proved by reducing the halting problem, which is a well-known undecidable problem, to the PCP problem.
  - The halting problem asks whether a given Turing machine will halt on a given input or not.
  - The idea of the reduction is to construct an instance of the PCP problem that encodes the computation of the Turing machine on the input, such that the PCP problem has a solution if and only if the Turing machine halts on the input.
  - The details of the reduction are beyond the scope of this note, but can be found in  or other sources.