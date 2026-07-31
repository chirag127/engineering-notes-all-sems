### Halestead’s Software Science

- Halestead’s Software Science is a set of software metrics introduced by Maurice Howard Halestead in 1977 to measure the complexity, quality, and effort of a program.
- The premise of software science is that any programming task consists of selecting and arranging a finite number of program "tokens," which are basic syntactic units distinguishable by a compiler.
- Halestead’s Software Science uses four basic measures to derive other metrics:
  - n1 = Number of distinct operators
  - n2 = Number of distinct operands
  - N1 = Total number of operators
  - N2 = Total number of operands
- The derived metrics are :
  - Program length (N) = N1 + N2
  - Vocabulary size (n) = n1 + n2
  - Volume (V) = N * log2(n)
  - Difficulty (D) = (n1/2) * (N2/n2)
  - Effort (E) = D * V
  - Time required to program (T) = E / 18 seconds
  - Number of delivered bugs (B) = V / 3000
- Halestead’s Software Science can be used to compare different implementations of the same algorithm, estimate the development time and cost, and assess the maintainability and reliability of a program .