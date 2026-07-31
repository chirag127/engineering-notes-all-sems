### Halting Problem

- The halting problem is a decision problem about properties of computer programs on a fixed Turing-complete model of computation.
- The problem is to determine, from a description of an arbitrary computer program and an input, whether the program will finish running, or continue to run forever.
- Alan Turing proved in 1936 that a general algorithm to solve the halting problem for all possible program–input pairs cannot exist.
- The proof is based on a contradiction: suppose there exists a program H that can decide the halting problem, then we can construct a program R that uses H to reverse its output, and then feed R to itself as input. This leads to a paradox: if R halts, then it does not halt, and vice versa .
- The halting problem is an example of an undecidable problem, which means that there is no effective method to decide whether a given statement is true or false in a given formal system.
- The halting problem also implies that there are some problems that are computationally harder than others, and that there are limits to what can be computed by a Turing machine .
- The universal halting problem, also known as totality, is the problem of determining whether a given computer program will halt for every input. This problem is not only undecidable, but highly undecidable, meaning that there is no computable function that can approximate its solution.