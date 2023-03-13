##### Halestead’s Software Science in software design

- Halestead’s Software Science is a set of software metrics that aim to measure the complexity, quality, and effort of a program based on its source code   .
- The premise of Halestead’s Software Science is that any programming task consists of selecting and arranging a finite number of program tokens, which are basic syntactic units distinguishable by a compiler.
- Halestead’s Software Science defines two types of tokens: operators and operands. Operators are symbols that represent actions or functions, such as +, =, if, while, etc. Operands are symbols that represent data or values, such as variables, constants, literals, etc  .
- Halestead’s Software Science uses four primitive program parameters to derive the expressions for various software metrics  :

  - n1: the number of distinct operators in the program
  - n2: the number of distinct operands in the program
  - N1: the total number of operators in the program
  - N2: the total number of operands in the program

- Some of the software metrics that Halestead’s Software Science provides are  :

  - Program length (N): the total number of tokens in the program, N = N1 + N2
  - Program vocabulary (n): the number of distinct tokens in the program, n = n1 + n2
  - Volume (V): the amount of information contained in the program, V = N * log2(n)
  - Difficulty (D): the difficulty of writing or understanding the program, D = (n1/2) * (N2/n2)
  - Effort (E): the amount of mental effort required to develop the program, E = D * V
  - Time (T): the estimated time required to develop the program, T = E / 18 seconds
  - Bugs (B): the estimated number of errors in the program, B = V / 3000

- Halestead’s Software Science has some advantages and disadvantages as a software metric system :

  - Advantages:

    - It is easy to automate and apply to any programming language
    - It is based on objective and measurable properties of the source code
    - It can provide some insights into the complexity and quality of the program

  - Disadvantages:

    - It does not account for the semantic aspects of the program, such as logic, design, or functionality
    - It does not consider the external factors that affect the development process, such as requirements, testing, or maintenance
    - It is based on some assumptions and empirical constants that may not be valid or generalizable for all programs