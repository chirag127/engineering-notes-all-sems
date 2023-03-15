##### Halestead’s Software Science in software design

Halestead’s Software Science is a set of software metrics that aim to measure the complexity, quality, and effort of a program based on the number and types of operators and operands in the source code . The basic idea is that any programming task consists of selecting and arranging a finite number of program tokens, which are the basic syntactic units distinguishable by a compiler.

The following base measures can be collected by counting the tokens and determining which are operators and which are operands:

- n1 = Number of distinct operators
- n2 = Number of distinct operands
- N1 = Total number of operators
- N2 = Total number of operands

From these base measures, the following derived measures can be calculated :

- Program vocabulary: n = n1 + n2
- Program length: N = N1 + N2
- Estimated program length: N^ = n1 * log2(n1) + n2 * log2(n2)
- Volume: V = N * log2(n)
- Difficulty: D = (n1 / 2) * (N2 / n2)
- Effort: E = D * V
- Time required to program: T = E / 18 seconds
- Number of delivered bugs: B = V / 3000

These measures are intended to reflect the implementation or expression of algorithms in different languages, but be independent of the programmer’s skill or experience. They can be used to estimate the development time, cost, and quality of a software project.

However, Halestead’s Software Science has also been criticized for its lack of empirical validation, theoretical foundation, and practical applicability . Some of the criticisms include:

- The choice of operators and operands is arbitrary and language-dependent.
- The base measures are not independent of each other and may be correlated.
- The derived measures are not dimensionally consistent and may have no physical meaning.
- The constants used in the formulas are not justified or calibrated .
- The measures do not account for the structure, design, or functionality of the program.
- The measures do not correlate well with other indicators of software complexity, quality, or effort.

Therefore, Halestead’s Software Science should be used with caution and skepticism, and not as the sole basis for software engineering decisions .