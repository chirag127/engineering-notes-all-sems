### Halting Problem

- The halting problem is a decision problem about properties of computer programs on a fixed Turing-complete model of computation.
- The problem can be informally stated as follows: Given a description of a program and a finite input, decide whether the program finishes running or will run forever, given that input.
- Alan Turing proved in 1936 that a general algorithm to solve the halting problem for all possible program–input pairs cannot exist.
- The proof is based on a contradiction: Suppose there exists a program H that can decide the halting problem for any program P and input I. Then, we can construct a program R that takes another program Q as input and does the following:
  - Call H with Q and Q as the program and input arguments, respectively.
  - If H returns "halts", then R enters an infinite loop.
  - If H returns "loops", then R halts.
- Now, what happens if we call R with itself as input? There are two possibilities:
  - If R halts when given itself as input, then H must have returned "loops" when called with R and R. But this contradicts the definition of R, which says that it halts only if H returns "halts".
  - If R loops when given itself as input, then H must have returned "halts" when called with R and R. But this contradicts the definition of R, which says that it loops only if H returns "loops".
- Therefore, we have reached a contradiction in both cases, and we must conclude that H cannot exist. This proves that the halting problem is undecidable.
- The halting problem is also uncomputable, meaning that there is no computable function that can map any program–input pair to a Boolean value indicating whether the program halts or not.
- The halting problem is one of the most fundamental problems in computability theory, and has many implications and applications in logic, mathematics, computer science, and philosophy.