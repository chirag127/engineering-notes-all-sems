##### Halestead’s Software Science in software design

- Halestead’s Software Science is a set of software metrics introduced by Maurice Howard Halstead in 1977 as part of his treatise on establishing an empirical science of software development.
- The premise of software science is that any programming task consists of selecting and arranging a finite number of program "tokens," which are basic syntactic units distinguishable by a compiler.
- By counting the tokens and determining which are operators and operands, the following base measures can be collected:
  - n1 = Number of distinct operators
  - n2 = Number of distinct operands
  - N1 = Total number of operators
  - N2 = Total number of operands
- Based on these base measures, Halstead defined the following derived measures:
  - Program length (N) = N1 + N2
  - Vocabulary size (n) = n1 + n2
  - Volume (V) = N * log2(n)
  - Difficulty (D) = (n1/2) * (N2/n2)
  - Effort (E) = D * V
  - Time required to program (T) = E / 18 seconds
  - Number of delivered bugs (B) = V / 3000
- Halstead’s metrics are intended to reflect the implementation or expression of algorithms in different languages, but be independent of the specific language used.
- Halstead’s metrics have been criticized for being based on arbitrary assumptions, lacking empirical validation, and being sensitive to coding style and formatting.
- Halstead’s metrics are included in a number of current commercial tools that count software lines of code.