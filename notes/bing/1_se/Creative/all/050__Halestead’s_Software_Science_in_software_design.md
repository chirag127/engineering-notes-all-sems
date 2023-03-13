##### Halestead’s Software Science in software design

- Halestead’s Software Science is a method of measuring the complexity and quality of software based on the analysis of the source code.
- It is based on the premise that any programming task consists of selecting and arranging a finite number of program tokens, which are basic syntactic units distinguishable by a compiler.
- Halestead’s Software Science defines two types of tokens: operators and operands. Operators are symbols that represent actions or functions, such as +, =, if, while, etc. Operands are symbols that represent data or values, such as variables, constants, literals, etc.
- Halestead’s Software Science uses four primitive program parameters to derive various software metrics:

  - n1: the number of distinct operators in the program
  - n2: the number of distinct operands in the program
  - N1: the total number of operators in the program
  - N2: the total number of operands in the program

- The size of the vocabulary of a program (n) is defined as the sum of n1 and n2. The size of the program (N) is defined as the sum of N1 and N2.
- Halestead’s Software Science proposes the following metrics for software complexity and quality:

  - Program length (L): the number of bits required to encode the program. It is calculated as L = n * log2(n).
  - Program volume (V): the amount of information contained in the program. It is calculated as V = N * log2(n).
  - Program level (L): the inverse of program difficulty. It is calculated as L = (2 * n2) / (n1 * N2).
  - Program difficulty (D): the effort required to write or understand the program. It is calculated as D = 1 / L = (n1 * N2) / (2 * n2).
  - Program effort (E): the amount of mental activity required to write or understand the program. It is calculated as E = D * V.
  - Program time (T): the time required to write or understand the program. It is calculated as T = E / S, where S is a constant that represents the speed of the programmer or the reader.
  - Program bugs (B): the estimated number of errors in the program. It is calculated as B = E^(2/3) / 3000.

- Halestead’s Software Science can be used to compare different programs or different versions of the same program in terms of complexity and quality. It can also be used to estimate the development time and cost of a program based on the program volume and effort.
- Halestead’s Software Science has some limitations and criticisms, such as:

  - It assumes that all operators and operands have the same complexity and importance, which may not be true in practice.
  - It does not consider the logical structure, control flow, or data flow of the program, which may affect the complexity and quality of the program.
  - It does not account for the programming language, style, or convention used, which may influence the number and type of tokens in the program.
  - It does not consider the external factors, such as the programmer’s skill, experience, or motivation, which may affect the development time and cost of the program.
  - It does not validate the accuracy or reliability of the metrics, which may vary depending on the source code and the measurement tool used.

- A possible mnemonic to remember the four primitive program parameters is: **n**o **n**onsense, **N**o **N**onsense. The first letter of each word corresponds to the first letter of each parameter. The lowercase letters correspond to the distinct tokens, and the uppercase letters correspond to the total tokens.