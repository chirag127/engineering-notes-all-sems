 Here is the content in markdown format for ##### Halestead’s Software Science in software design:

##### Halestead’s Software Science in software design

- Halstead's software science is a quantitative method for measuring software complexity. It was proposed by Maurice Halstead in the 1970s.
- It uses two measures - vocabulary (n) and length (N) to calculate software complexity.

Vocabulary (n) - Number of distinct operators and operands in a program.
Length (N) - Total number of operators and operands in a program.

Based on these two measures, the following software metrics can be calculated:

- Program volume (V) = N log2 n
- Difficulty (D) = n (log2 n)/2
- Effort (E) = D × V
- Time required to program (T) = E/18

Advantages:
- Provides quantitative measures for software complexity.
- Gives an estimate of effort and time required to develop software.

Disadvantages:
- Does not consider structured programming concepts like modules, information hiding, etc.
- The empirical constants used in the formulae were determined based on a small sample and may not be accurate.
- The measures are language dependent and hard to calculate for larger programs.

In summary, Halstead's software science provides some basic quantitative measures of software complexity. However, due to the disadvantages mentioned above, it should not be used alone to predict effort and time required for software development. It can be used along with other qualitative techniques to get a better estimate.