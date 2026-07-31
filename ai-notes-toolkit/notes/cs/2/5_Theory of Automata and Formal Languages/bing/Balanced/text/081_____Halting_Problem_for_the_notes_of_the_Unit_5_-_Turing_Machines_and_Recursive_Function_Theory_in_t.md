### Halting Problem

- The halting problem is a decision problem about properties of computer programs on a fixed Turing-complete model of computation, i.e., all programs that can be written in some given programming language that is general enough to be equivalent to a Turing machine.
- The problem is to determine, from a description of an arbitrary computer program and an input, whether the program will finish running, or continue to run forever.
- Alan Turing proved in 1936 that a general algorithm to solve the halting problem for all possible program–input pairs cannot exist.
- The proof is based on a contradiction: suppose there exists a program H that can decide the halting problem, then we can construct a program P that uses H as a subroutine and does the opposite of what H predicts, leading to a paradox.
- The halting problem is an early example of a decision problem, and also a good example of the limits of determinism in computer science.
- The halting problem is also related to other undecidable problems, such as the universal halting problem, which is the problem of determining whether a given computer program will halt for every input. This problem is not only undecidable, but highly undecidable, meaning that there is no algorithm that can even partially solve it.
- Generally, all the undecidable problems revolve around the difficulty of determining properties about the input and output of programs.