# Halting Problem

- The halting problem is a decision problem about properties of computer programs on a fixed Turing-complete model of computation, i.e., all programs that can be written in some given programming language that is general enough to be equivalent to a Turing machine.
- The halting problem asks whether, given a description of an arbitrary computer program and an input, it is possible to determine whether the program will finish running or continue to run forever.
- Alan Turing proved in 1936 that a general algorithm to solve the halting problem for all possible program–input pairs cannot exist. This means that there is no single program that can correctly answer "yes" or "no" for every possible program and input.
- The proof of the undecidability of the halting problem is based on a contradiction. Suppose there exists a program H that can solve the halting problem, i.e., H takes as input a program P and an input I and returns "yes" if P halts on I and "no" otherwise. Then, we can construct another program R that takes as input a program Q and does the following:
  - Call H with Q and Q as inputs, i.e., ask H whether Q halts when given itself as input.
  - If H returns "yes", then R enters an infinite loop and never halts.
  - If H returns "no", then R halts immediately and returns "done".
- Now, we have a paradox. What happens if we run R with itself as input, i.e., R(R)? There are two possibilities:
  - If R(R) halts, then H must have returned "no" when called with R and R as inputs, i.e., H must have said that R does not halt when given itself as input. But this contradicts the fact that R(R) halts.
  - If R(R) does not halt, then H must have returned "yes" when called with R and R as inputs, i.e., H must have said that R halts when given itself as input. But this contradicts the fact that R(R) does not halt.
- Therefore, we have reached a contradiction, and we must conclude that our assumption that H exists was wrong. Hence, there is no program that can solve the halting problem for all possible program–input pairs.
- The halting problem is not only undecidable, but also highly undecidable, meaning that there is no computable function that can approximate the answer to the halting problem with any degree of accuracy. For example, there is no program that can correctly answer "yes", "no", or "don't know" for every possible program and input, even if it is allowed to say "don't know" for some cases.
- The halting problem is an example of the limits of computability and determinism in computer science. It shows that there are some problems that are inherently unsolvable by any algorithm, and that there are some aspects of computation that are fundamentally unpredictable.