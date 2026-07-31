### Computability for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages

- Computability theory, also known as recursion theory, is the branch of mathematics and computer science that studies the limits and possibilities of computation.
- Computability theory deals with the concept of an effective procedure, which is a procedure that can be carried out by following specific rules.
- Computability theory also investigates the properties of different models of computation, such as Turing machines, recursive functions, lambda calculus, and cellular automata.
- Some of the main questions that computability theory tries to answer are:
  - What are the computable functions, i.e., the functions that can be computed by some model of computation?
  - What are the incomputable functions, i.e., the functions that cannot be computed by any model of computation?
  - What are the degrees of unsolvability, i.e., the levels of difficulty of incomputable problems?
  - What are the relations between different models of computation, i.e., which models are equivalent, more powerful, or less powerful than others?
- Some of the main results of computability theory are:
  - The Church-Turing thesis, which states that any function that can be computed by an effective procedure can be computed by a Turing machine.
  - The halting problem, which is the problem of deciding whether a given Turing machine will halt on a given input. This problem is undecidable, i.e., there is no Turing machine that can solve it for all inputs.
  - The Rice theorem, which states that any non-trivial property of the functions computed by Turing machines is undecidable, i.e., there is no Turing machine that can decide whether a given Turing machine has that property or not.
  - The recursion theorem, which states that any Turing machine can effectively construct a copy of itself.
  - The reducibility relation, which is a way of comparing the difficulty of undecidable problems. If a problem A can be reduced to a problem B, i.e., if a solution to B can be used to solve A, then A is no harder than B. The hardest problems are called recursively enumerable, i.e., they can be enumerated by a Turing machine, but not decided.
  - The arithmetical hierarchy, which is a classification of the sets of natural numbers that can be defined by using arithmetic operations and quantifiers. The higher the level of the hierarchy, the more complex the set is. The lowest level, called $\Sigma_0^0$ or $\Pi_0^0$, contains the computable sets. The next level, called $\Sigma_1^0$ or $\Pi_1^0$, contains the recursively enumerable sets and their complements. The higher levels, called $\Sigma_n^0$ or $\Pi_n^0$ for $n > 1$, contain the sets that can be defined by using $n$ alternations of quantifiers.
  - The Turing degree, which is a measure of the degree of unsolvability of a set of natural numbers. Two sets have the same Turing degree if they are Turing equivalent, i.e., if they can compute each other. The lowest Turing degree, called $0$, contains the computable sets. The next Turing degree, called $0'$, contains the halting problem and its Turing equivalent sets. The higher Turing degrees, called $0''$, $0'''$, etc., contain the sets that can compute the halting problem and its Turing equivalent sets, and so on.