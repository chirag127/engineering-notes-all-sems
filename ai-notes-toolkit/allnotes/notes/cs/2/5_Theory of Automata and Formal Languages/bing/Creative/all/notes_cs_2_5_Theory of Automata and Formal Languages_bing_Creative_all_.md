

## Unit 1 - Basic Concepts and Automata Theory

- This unit introduces the basic concepts and terminology of formal languages, grammars, and automata theory, which are the foundations of theoretical computer science and compiler design.
- A **formal language** is a set of strings over a finite alphabet. An alphabet is a non-empty set of symbols, such as {0, 1} or {a, b, c, ..., z}. A string is a finite sequence of symbols from an alphabet, such as 0101 or hello. The empty string, denoted by ε, is the string with no symbols. The length of a string is the number of symbols in it, such as |0101| = 4 and |ε| = 0. The set of all strings over an alphabet Σ is denoted by Σ*.
- A **grammar** is a set of rules that describe how to generate strings in a formal language. A grammar consists of four components: a set of non-terminal symbols (also called variables), a set of terminal symbols (also called alphabet), a start symbol (a special non-terminal symbol), and a set of production rules. A production rule has the form A → α, where A is a non-terminal symbol and α is a string of non-terminal and terminal symbols. A grammar can be used to derive strings in a formal language by starting from the start symbol and applying production rules until only terminal symbols are left. For example, the grammar G = ({S, A, B}, {0, 1}, S, {S → 0A, S → 1B, A → 0, A → 0S, A → 1AA, B → 1, B → 1S, B → 0BB}) can generate the string 010011 by the derivation S → 0A → 00S → 001B → 0011.
- A **finite automaton** is a mathematical model of computation that can recognize formal languages. A finite automaton consists of five components: a set of states, a set of input symbols (also called alphabet), a transition function that maps a state and an input symbol to a new state, an initial state, and a set of final states. A finite automaton can process an input string by starting from the initial state and following the transition function for each input symbol until the end of the string. If the final state is in the set of final states, the input string is accepted; otherwise, it is rejected. For example, the finite automaton M = ({q0, q1, q2}, {0, 1}, δ, q0, {q0}) with the transition function δ defined as follows can accept the string 010011:

| state | input | new state |
| ----- | ----- | --------- |
| q0    | 0     | q1        |
| q0    | 1     | q2        |
| q1    | 0     | q0        |
| q1    | 1     | q1        |
| q2    | 0     | q2        |
| q2    | 1     | q0        |

The processing of the input string is shown below:

q0 --0--> q1 --1--> q1 --0--> q0 --0--> q1 --1--> q1 --1--> q0 (accept)

- There are different types of finite automata, such as deterministic finite automata (DFA), nondeterministic finite automata (NFA), and ε-NFA. A DFA is a finite automaton that has exactly one transition for each state and input symbol. An NFA is a finite automaton that can have zero, one, or more transitions for each state and input symbol. An ε-NFA is an NFA that can also have transitions for the empty string ε. An NFA or an ε-NFA can be converted to an equivalent DFA using the subset construction algorithm.
- A **regular expression** is a notation that can describe formal languages using symbols and operators. A regular expression can be defined recursively as follows:

  - ε is a regular expression that denotes the language {ε}.
  - a is a regular expression that denotes the language {a}, where a is any symbol in the alphabet.
  - If r and s are regular expressions, then
    - (r) is a regular expression that denotes the same language as r.
    - (r + s) is a regular expression that denotes the union of the languages denoted by r and s.
    - (rs) is a regular expression that denotes the concatenation of the languages denoted by r and s.
    - (r*)



# Introduction to Theory of Computation

- Theory of computation (TOC) is a branch of computer science that is concerned with how problems can be solved using algorithms and how efficiently they can be solved.
- TOC includes the fundamental mathematical properties of computer hardware, software and their applications.
- TOC deals with what problems can be solved on a model of computation, using an algorithm, how efficiently they can be solved or to what degree (e.g., approximate solutions versus precise ones).
- A model of computation is an abstract representation of a computing device, such as a Turing machine, a finite automaton, a pushdown automaton, etc.
- An algorithm is a finite sequence of well-defined instructions that can be executed by a model of computation to solve a problem.
- TOC can be divided into three main branches: computability theory, complexity theory and automata theory.
- Computability theory studies what kinds of problems can be solved by algorithms, and what kinds of problems are inherently unsolvable (undecidable).
- Complexity theory studies how efficiently problems can be solved by algorithms, and what kinds of problems are inherently hard (intractable) or easy (tractable).
- Automata theory studies the properties and behaviors of abstract machines that can recognize and generate various classes of languages, such as regular languages, context-free languages, etc.
- TOC has applications in various fields of computer science, such as compiler design, cryptography, artificial intelligence, verification, etc.



# Automata for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages

- Automata Theory is a branch of computer science and mathematics that deals with designing abstract self-propelled computing devices that follow a predetermined sequence of operations automatically.
- An automaton is an abstract computing device that can be in one of a finite number of states and can change its state according to some input or output.
- Automata theory studies the properties and limitations of different types of automata, such as finite automata, pushdown automata, and Turing machines.
- Automata theory also explores the relationship between automata and formal languages, which are sets of strings that can be generated or recognized by automata.
- Automata theory is closely related to the theory of computation, which investigates the fundamental questions of what can and cannot be computed by various models of computation.
- Automata theory has applications in many areas of computer science, such as compiler design, parsing, verification, cryptography, artificial intelligence, and more.

: https://www.tutorialspoint.com/automata_theory/index.htm
: https://eecs.wsu.edu/~ananth/CptS317/Lectures/IntroToAutomataTheory.pdf
: https://www.javatpoint.com/theory-of-automata
: https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/lecture-notes/
: https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/pages/lecture-notes/
: https://www.ics.uci.edu/~goodrich/teach/cs162/notes/



# Computability

Computability is the study of what can and cannot be computed by following specific rules or procedures. It is also known as recursion theory.

Some of the main topics in computability theory are:

- Computable functions: functions that can be calculated by a finite set of instructions, such as arithmetic operations, logical operations, or string manipulations.
- Turing machines: abstract models of computation that can simulate any computable function. A Turing machine consists of a tape, a head, and a finite set of states and rules.
- Church-Turing thesis: the conjecture that any function that can be computed by an effective procedure can also be computed by a Turing machine. This thesis implies that there is no single best model of computation, and that all models are equivalent in power.
- Decidability: the property of a problem or a language that can be solved or recognized by a Turing machine in a finite amount of time. For example, the problem of determining whether a given number is prime is decidable, but the problem of determining whether a given mathematical statement is true is undecidable.
- Reducibility: the relation between two problems or languages that indicates that one problem can be transformed into another problem by a computable function. For example, the problem of determining whether a given number is even can be reduced to the problem of determining whether the last digit of the number is 0 or 2 or 4 or 6 or 8.
- Recursive function theory: the study of functions that can be defined by recursion, i.e., by using their own values as arguments. For example, the factorial function n! can be defined by n! = n * (n-1)! for n > 0 and 0! = 1. Recursive functions are a subset of computable functions, and can be classified into different classes based on their complexity and properties.
- Time and space measures: the study of how much time and space are required to compute a function or solve a problem by a Turing machine. For example, the time complexity of a problem is the number of steps or tape cells used by the Turing machine as a function of the input size, and the space complexity is the number of tape cells used by the Turing machine as a function of the input size.
- Completeness: the property of a problem or a language that is the hardest in its class of problems or languages, i.e., any other problem or language in the same class can be reduced to it. For example, the halting problem, which is the problem of determining whether a given Turing machine will halt on a given input, is undecidable and complete for the class of undecidable problems.
- Hierarchy theorems: the results that show that there are different levels of complexity and decidability for problems and languages, and that there are problems and languages that are strictly harder or easier than others. For example, the time hierarchy theorem states that there are problems that can be solved in polynomial time but not in linear time, and the space hierarchy theorem states that there are problems that can be solved in polynomial space but not in logarithmic space.
- Inherently complex problems: the problems that are provably hard to solve or approximate by any Turing machine, regardless of the model of computation or the resources available. For example, the satisfiability problem, which is the problem of determining whether a given propositional logic formula can be satisfied by some assignment of truth values to its variables, is NP-complete, which means that it is as hard as any problem in the class NP, and that there is no known polynomial-time algorithm to solve it or to find a near-optimal solution.
- Oracles: the hypothetical devices that can answer any question or solve any problem in a single step, regardless of its complexity or decidability. For example, an oracle for the halting problem can tell whether any Turing machine will halt on any input in one step. Oracles can be used to study the limits of computation and the effects of adding extra power to Turing machines.



# Complexity

Complexity is a measure of the resources required to perform a computation by an abstract machine, such as an automaton. Complexity theory is a branch of theoretical computer science that studies the limits and trade-offs of various computational models and problems.

Some of the topics covered in complexity theory are:

- Classes of abstract machines, such as finite automata, pushdown automata, Turing machines, and circuits, and their expressive power and limitations.
- Classes of computational problems, such as decision problems, function problems, optimization problems, and counting problems, and their hardness and tractability.
- Complexity measures, such as time, space, communication, randomness, and non-determinism, and their relations and trade-offs.
- Complexity classes, such as P, NP, L, NL, PSPACE, NPSPACE, BPP, RP, ZPP, NC, AC, and many others, and their inclusions, separations, and collapses.
- Complexity reductions, such as polynomial-time reductions, logarithmic-space reductions, and many-one reductions, and their applications to show hardness and completeness of problems.
- Complexity hierarchies, such as the time hierarchy, the space hierarchy, the polynomial hierarchy, and the arithmetic hierarchy, and their properties and consequences.
- Complexity lower bounds, such as diagonalization, circuit lower bounds, communication complexity lower bounds, and interactive proof lower bounds, and their techniques and challenges.
- Complexity upper bounds, such as dynamic programming, greedy algorithms, divide and conquer, approximation algorithms, randomized algorithms, and parallel algorithms, and their analysis and limitations.

Complexity theory is closely related to other branches of theoretical computer science, such as automata theory, computability theory, logic, algebra, and cryptography. It also has connections to other disciplines, such as mathematics, physics, biology, and philosophy.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of alphabet for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages.

# Alphabet
- An alphabet is a finite, non-empty set of symbols, usually denoted by Σ.
- A symbol is an abstract entity that has no inherent meaning, but can be used to represent something.
- Examples of alphabets are:
  - Σ = {0, 1} (the binary alphabet)
  - Σ = {a, b, c, ..., z} (the lowercase English alphabet)
  - Σ = {+, -, *, /, (, ), 0, 1, ..., 9} (the arithmetic alphabet)
- The size or cardinality of an alphabet Σ is the number of symbols in it, denoted by |Σ|.
- Examples of sizes of alphabets are:
  - |{0, 1}| = 2
  - |{a, b, c, ..., z}| = 26
  - |{+, -, *, /, (, ), 0, 1, ..., 9}| = 14
- An alphabet can be used to form strings or words, which are finite sequences of symbols from the alphabet.
- Examples of strings or words are:
  - 1010 (a string over {0, 1})
  - hello (a string over {a, b, c, ..., z})
  - (3+4)*5 (a string over {+, -, *, /, (, ), 0, 1, ..., 9})
- The length of a string w is the number of symbols in it, denoted by |w|.
- Examples of lengths of strings are:
  - |1010| = 4
  - |hello| = 5
  - |(3+4)*5| = 7
- The empty string is the string of length zero, denoted by ε or λ.
- The empty string is a valid string over any alphabet.
- Examples of empty strings are:
  - ε (over {0, 1})
  - ε (over {a, b, c, ..., z})
  - ε (over {+, -, *, /, (, ), 0, 1, ..., 9})
- The set of all strings over an alphabet Σ is denoted by Σ*.
- Examples of sets of all strings are:
  - {0, 1}* = {ε, 0, 1, 00, 01, 10, 11, 000, 001, ..., }
  - {a, b, c, ..., z}* = {ε, a, b, c, ..., z, aa, ab, ac, ..., az, ba, bb, bc, ..., zz, aaa, aab, ..., }
  - {+, -, *, /, (, ), 0, 1, ..., 9}* = {ε, +, -, *, /, (, ), 0, 1, ..., 9, ++, +-, +*, +/, +(, +), +0, +1, ..., +9, -, +, --, -, *, -, /, -, (, -, ), -0, -1, ..., -9, *, +, *, -, **, *, /, *, (, *, ), *0, *1, ..., *9, ..., }
- The set of all strings of length n over an alphabet Σ is denoted by Σ^n.
- Examples of sets of all strings of length n are:
  - {0, 1}^3 = {000, 001, 010, 011, 100, 101, 110, 111}
  - {a, b, c, ..., z}^2 = {aa, ab, ac, ..., az, ba, bb, bc, ..., bz, ca, cb, cc, ..., cz, ..., za, zb, zc, ..., zz}
  - {+, -, *, /, (, ), 0, 1, ..., 9}^1 = {+, -, *, /, (, ), 0, 1, ..., 9}
- The set of all strings of length at most n over an alphabet Σ is denoted by Σ≤n.
- Examples of sets of all strings of length at most n are:
  - {0, 1}≤2 = {ε, 0, 1, 00, 01, 10,



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some symbols for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages:

# Unit 1 - Basic Concepts and Automata Theory

- **Σ**: The alphabet, a finite set of symbols.
- **ε**: The empty string, a string of length zero.
- **w**: A string, a finite sequence of symbols from the alphabet.
- **|w|**: The length of a string, the number of symbols in the string.
- **w<sup>R</sup>**: The reverse of a string, the string obtained by reversing the order of symbols in the string.
- **L**: A language, a set of strings over the alphabet.
- **L<sup>C</sup>**: The complement of a language, the set of strings over the alphabet that are not in the language.
- **L<sup>R</sup>**: The reverse of a language, the set of strings obtained by reversing the strings in the language.
- **L<sub>1</sub> ∪ L<sub>2</sub>**: The union of two languages, the set of strings that are in either language or both.
- **L<sub>1</sub> ∩ L<sub>2</sub>**: The intersection of two languages, the set of strings that are in both languages.
- **L<sub>1</sub> - L<sub>2</sub>**: The difference of two languages, the set of strings that are in the first language but not in the second.
- **L<sub>1</sub> ⊆ L<sub>2</sub>**: The subset relation, the first language is a subset of the second if every string in the first language is also in the second.
- **L<sub>1</sub> ⊂ L<sub>2</sub>**: The proper subset relation, the first language is a proper subset of the second if it is a subset and not equal to the second.
- **L<sub>1</sub> = L<sub>2</sub>**: The equality relation, the two languages are equal if they contain the same strings.
- **L<sup>*</sup>**: The Kleene star of a language, the set of strings obtained by concatenating zero or more strings from the language.
- **L<sup>+</sup>**: The Kleene plus of a language, the set of strings obtained by concatenating one or more strings from the language.
- **L<sup>n</sup>**: The nth power of a language, the set of strings obtained by concatenating n strings from the language.
- **M**: A machine, an abstract model of computation.
- **Q**: The set of states, a finite set of possible configurations of the machine.
- **q<sub>0</sub>**: The initial state, the state in which the machine starts its computation.
- **F**: The set of final or accepting states, a subset of states that indicate successful computation.
- **δ**: The transition function, a function that defines how the machine changes its state and/or output based on its current state and input.
- **(q, w) ⇒ (p, x)**: The transition relation, a relation that indicates that the machine can go from state q to state p and consume input w and produce output x in one step.
- **(q, w) ⇒* (p, x)**: The extended transition relation, a relation that indicates that the machine can go from state q to state p and consume input w and produce output x in zero or more steps.
- **M(w)**: The output of the machine on input w, the output produced by the machine after consuming the entire input w.
- **L(M)**: The language recognized or accepted by the machine, the set of inputs for which the machine produces a successful output.
- **M<sub>1</sub> ≡ M<sub>2</sub>**: The equivalence relation, the two machines are equivalent if they recognize the same language.



# String

- A string is a sequence of symbols of finite length .
- A string is denoted by w in automata.
- A string can be empty or null, which means it has no symbols.
- A string can be a single letter or a combination of letters from an alphabet.
- An alphabet is a finite, non-empty set of symbols .
- A symbol is an abstract entity that has no meaning by itself.
- Examples of alphabets are {0, 1}, {a, b, c}, {x, y} .
- Examples of strings are 000111, abc, xyxy, ε (empty string) .
- The length of a string is the number of symbols in it.
- The length of the empty string is zero.
- The set of all strings over an alphabet Σ is denoted by Σ*.
- Examples of Σ* are {0, 1}*, {a, b, c}*, {x, y}*.
- Strings are important in automata theory because they represent the input and output of abstract machines and automata.
- Automata are mathematical models of computation that can accept or reject strings based on some rules.
- Examples of automata are finite automata, pushdown automata, Turing machines.
- Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them.



# Formal Languages

- A formal language is a language designed for use in situations in which natural language is unsuitable, as for example in mathematics, logic, or computer programming .
- A formal language consists of a set of symbols (also called alphabet or vocabulary) and a set of rules (also called syntax or grammar) that define how the symbols can be combined to form valid strings (also called words or sentences) of the language.
- A formal language can be finite or infinite, depending on whether it has a finite or infinite number of valid strings.
- A formal language can be described by various methods, such as regular expressions, context-free grammars, or Turing machines.
- A formal language can be classified into different classes or families, based on the properties and limitations of the methods that can describe or recognize it, such as regular languages, context-free languages, context-sensitive languages, or recursively enumerable languages.
- A formal language can be used to model various phenomena or systems, such as natural languages, programming languages, protocols, automata, logic, or computation.



# Deterministic Finite Automaton (DFA)

- A deterministic finite automaton (DFA) is a type of finite state machine that accepts or rejects a given string of symbols by running through a unique sequence of states determined by the string.
- A DFA is defined by a 5-tuple M = (Q, Σ, δ, q0, F) where  :
  - Q is a finite set of states
  - Σ is a finite set of input symbols (alphabet)
  - δ is a transition function that maps Q x Σ to Q (δ: Q x Σ -> Q)
  - q0 is the initial state (q0 ∈ Q)
  - F is a set of final or accepting states (F ⊆ Q)
- A DFA can be represented by a state transition diagram, which is a directed graph with nodes as states and edges as transitions labeled by symbols from Σ.
- A DFA can also be represented by a state transition table, which is a tabular representation of the transition function δ.
- A DFA accepts a string w = a1a2...an if there exists a sequence of states r0, r1, ... rn such that:
  - r0 = q0
  - ri+1 = δ(ri, ai+1) for i = 0, 1, ... n-1
  - rn ∈ F
- A DFA rejects a string w if it does not accept it.
- A DFA recognizes a regular language, which is a language that can be expressed by a regular expression or a regular grammar.
- A DFA is deterministic because for each state and input symbol, there is exactly one transition to a next state.
- A DFA is finite because it has a finite number of states and a finite alphabet.



# Definition for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages

- Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them.
- An automaton is a self-propelled computing device that follows a predetermined sequence of operations automatically.
- A finite automaton is an automaton with a finite number of states.
- A regular language is a set of strings that can be recognized by a finite automaton.
- A pushdown automaton is an automaton that has a stack as an auxiliary memory and can recognize context-free languages.
- A Turing machine is an abstract model of computation that can simulate any algorithm and can recognize recursively enumerable languages.
- Decidability is the property of a problem that can be solved by a Turing machine in a finite amount of time.



# Representation for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages

- Automata theory is a branch of computer science and mathematics that studies the logic and behavior of abstract machines, called automata, that can perform computations and solve problems  .
- Automata theory is also related to the theory of computation, which explores the limits and capabilities of different models of machines, such as Turing machines, finite automata, pushdown automata, etc .
- Automata theory has applications in various fields, such as robotics, compiler design, natural language processing, cryptography, etc .
- Some basic concepts and definitions in automata theory are:
  - Alphabet: A finite, non-empty set of symbols, usually denoted by Σ.
  - String: A finite sequence of symbols from an alphabet, also called a word.
  - Language: A set of strings over an alphabet, usually denoted by L.
  - Automaton: An abstract machine that can change its state in response to some input symbols and produce some output symbols.
  - Deterministic: An automaton is deterministic if it has exactly one transition for each state and input symbol.
  - Non-deterministic: An automaton is non-deterministic if it can have more than one transition for some state and input symbol.
  - Acceptance: An automaton accepts an input string if it reaches a final state after reading the string.
  - Recognition: An automaton recognizes a language if it accepts all and only the strings in the language.
- Some types of automata and their properties are:
  - Finite automaton (FA): An automaton that has a finite number of states and can only read the input symbols one by one.
  - Regular language: A language that can be recognized by a finite automaton.
  - Regular expression: A notation for describing regular languages using symbols, concatenation, union, and closure.
  - Regular grammar: A grammar that generates regular languages using rules of the form A -> a or A -> aB, where A and B are variables and a is a terminal symbol.
  - Non-regular language: A language that cannot be recognized by any finite automaton.
  - Pumping lemma: A technique for proving that a language is non-regular by showing that any sufficiently long string in the language can be pumped, i.e., repeated in some part, to produce another string in the language.
  - Pushdown automaton (PDA): An automaton that has a finite number of states and a stack that can store an unbounded amount of symbols.
  - Context-free language (CFL): A language that can be recognized by a pushdown automaton.
  - Context-free grammar (CFG): A grammar that generates context-free languages using rules of the form A -> α, where A is a variable and α is a string of variables and terminals.
  - Non-context-free language: A language that cannot be recognized by any pushdown automaton.
  - Pumping lemma for CFLs: A technique for proving that a language is non-context-free by showing that any sufficiently long string in the language can be pumped in two parts, to produce another string in the language.
  - Turing machine (TM): An automaton that has a finite number of states and an infinite tape that can store and manipulate symbols.
  - Recursively enumerable language (REL): A language that can be recognized by a Turing machine.
  - Decidable language: A language that can be recognized by a Turing machine that always halts.
  - Undecidable language: A language that cannot be recognized by any Turing machine that always halts.
  - Halting problem: The problem of determining whether a given Turing machine will halt on a given input, which is undecidable.
  - Church-Turing thesis: The hypothesis that any function that can be computed by an algorithm can be computed by a Turing machine.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of acceptability of a string and language.

# Acceptability of a String and Language

- A string is a finite sequence of symbols from a given alphabet.
- A language is a set of strings over a given alphabet.
- An alphabet is a finite, non-empty set of symbols, usually denoted by Σ.
- A string is accepted by a language if it belongs to that language, i.e., if it is an element of the language set.
- A string is rejected by a language if it does not belong to that language, i.e., if it is not an element of the language set.
- For example, if Σ = {a, b} and L = {a, aa, aaa, ...}, then the string a is accepted by L, but the string b is rejected by L.
- An automaton is a mathematical model of computation that can accept or reject strings over a given alphabet.
- An automaton consists of a finite set of states, a finite set of input symbols, a transition function that maps states and input symbols to states, an initial state, and a set of final or accepting states.
- An automaton processes a string by starting from the initial state and following the transition function for each symbol of the string, until it reaches the end of the string or a state that has no transition for the next symbol.
- An automaton accepts a string if it ends in a final state after processing the string.
- An automaton rejects a string if it does not end in a final state or if it cannot process the whole string.
- For example, the following automaton accepts the language L = {a, aa, aaa, ...} over the alphabet Σ = {a, b}:

automaton

- The automaton has two states, q0 and q1, where q0 is the initial state and q1 is the final state.
- The automaton has two input symbols, a and b, and the transition function is defined by the following table:

| State | Input | Next State |
| ----- | ----- | ---------- |
| q0    | a     | q1         |
| q0    | b     | -          |
| q1    | a     | q1         |
| q1    | b     | -          |

- The automaton accepts the string a by starting from q0, reading a, and moving to q1, which is a final state.
- The automaton rejects the string b by starting from q0, reading b, and having no transition for b, which means it cannot process the whole string.
- The automaton also rejects the string ab by starting from q0, reading a, moving to q1, reading b, and having no transition for b, which means it cannot process the whole string.



# Non Deterministic Finite Automaton (NFA)

- A Non Deterministic Finite Automaton (NFA) is a type of finite automaton that can have more than one possible transition from a given state for a given input symbol.
- An NFA can be formally defined as a 5-tuple (Q, Σ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols (alphabet)
  - δ is a transition function that maps Q × Σε to 2^Q, where Σε = Σ ∪ {ε} and ε is the empty string
  - q0 is the initial state
  - F is a set of final or accepting states
- An NFA accepts an input string if there exists at least one sequence of transitions from the initial state to a final state that consumes the entire input string.
- An NFA can have ε-transitions, which are transitions that do not consume any input symbol and can be taken spontaneously.
- An NFA can also have multiple initial or final states, unlike a DFA.
- An NFA can be converted to an equivalent DFA using the subset construction algorithm.
- Every DFA is also an NFA, but not every NFA is a DFA.
- An NFA is more expressive and easier to construct than a DFA for a given regular language, but less efficient to simulate.

## Example of NFA

- Consider the following NFA that accepts the language L = {xa | x ∈ {a,b}*}, which is the set of strings that end with 'a':

NFA example

- The NFA has four states: q0, q1, q2, and q3, where q0 is the initial state and q3 is the only final state.
- The NFA has five transitions: (q0, ε, q1), (q0, ε, q2), (q1, a, q1), (q1, b, q1), and (q2, a, q3).
- The NFA can accept the input string 'baa' by following the sequence of transitions: q0, ε, q2, a, q3.
- The NFA can also accept the input string 'aba' by following the sequence of transitions: q0, ε, q1, a, q1, b, q1, a, q3.
- The NFA cannot accept the input string 'abb' because there is no sequence of transitions that leads to a final state.



# Equivalence of DFA and NFA

- A **DFA** (Deterministic Finite Automaton) is a finite state machine that accepts or rejects a given string of symbols, where each state has exactly one transition for each symbol in the alphabet.
- An **NFA** (Nondeterministic Finite Automaton) is a finite state machine that accepts or rejects a given string of symbols, where each state can have zero, one or more transitions for each symbol in the alphabet, or even transitions without any symbols (called epsilon-transitions).
- A DFA and an NFA are called **equivalent** if they recognize the same language, that is, if they accept exactly the same set of strings.
- The **equivalence theorem** states that for any NFA, there exists a DFA that recognizes the same language, and vice versa .
- The proof of the equivalence theorem consists of two parts:
  - **From NFA to DFA**: Given an NFA N, we can construct a DFA D that simulates the behavior of N on any input string, by keeping track of all the possible states that N can be in after reading each symbol. This is done by using the **subset construction** algorithm, which creates a new state in D for each subset of states in N, and defines the transitions and the final states accordingly.
  - **From DFA to NFA**: Given a DFA D, we can construct an NFA N that mimics the behavior of D on any input string, by simply copying the states, transitions and final states of D. This is trivial, since every DFA is also an NFA.



# NFA with ε-Transition

- An NFA with ε-transition is a type of nondeterministic finite automaton (NFA) that allows the machine to change its state without consuming any input symbol. Such transitions are labeled with ε in the state diagram.
- Formally, an NFA with ε-transition is a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) to 2^Q, the power set of Q
  - q0 is the initial state
  - F is a set of final or accepting states
- The transition function δ can be extended to δ*: 2^Q × Σ* → 2^Q, where Σ* is the set of all strings over Σ, as follows:
  - δ*(R, ε) = ε-closure(R), where ε-closure(R) is the set of all states reachable from R by following only ε-transitions
  - δ*(R, aw) = δ*(δ*(R, a), w), where a ∈ Σ and w ∈ Σ*
- The language accepted by an NFA with ε-transition is L(N) = {w ∈ Σ* | δ*(q0, w) ∩ F ≠ ∅}, i.e., the set of all strings that lead to at least one accepting state from the initial state.
- An NFA with ε-transition can be converted to an equivalent NFA without ε-transition by applying the following steps:
  - For each state q ∈ Q, compute ε-closure(q) and store it in a table
  - For each state q ∈ Q and each symbol a ∈ Σ, compute δ'(q, a) = ε-closure(δ(ε-closure(q), a)) and store it in a table
  - Construct a new NFA (Q, Σ, δ', q0, F'), where F' = {q ∈ Q | ε-closure(q) ∩ F ≠ ∅}
- An NFA with ε-transition can also be converted to an equivalent deterministic finite automaton (DFA) by applying the subset construction algorithm, which uses the extended transition function δ* to construct a new DFA (Q', Σ, δ'', q0', F''), where:
  - Q' = 2^Q, i.e., the set of all subsets of Q
  - q0' = ε-closure(q0), i.e., the initial state of the new DFA is the ε-closure of the initial state of the NFA
  - F'' = {R ∈ Q' | R ∩ F ≠ ∅}, i.e., the set of all subsets of Q that contain at least one accepting state of the NFA
  - δ''(R, a) = δ*(R, a), i.e., the transition function of the new DFA is the same as the extended transition function of the NFA
- An example of an NFA with ε-transition that accepts the language L = {a^n b^n | n ≥ 0} is shown below:

NFA with ε-transition example

- The equivalent NFA without ε-transition is shown below:

NFA without ε-transition example

- The equivalent DFA is shown below:

DFA example



# Equivalence of NFA's with and without ε-Transition

- An NFA (Non-deterministic Finite Automaton) is a finite state machine that can have multiple transitions for the same input symbol and state.
- An ε-transition is a special kind of transition that does not consume any input symbol and can be taken spontaneously.
- An ε-NFA is an NFA that has one or more ε-transitions.
- An NFA without ε-transitions is also called a DFA (Deterministic Finite Automaton), because it has a unique transition for each input symbol and state.
- The equivalence of NFA's with and without ε-transitions means that for any given ε-NFA, there exists an equivalent NFA without ε-transitions that accepts the same language, and vice versa.
- The equivalence can be proved by showing how to convert an ε-NFA to an NFA without ε-transitions, and how to convert an NFA without ε-transitions to an ε-NFA.

## Converting an ε-NFA to an NFA without ε-transitions

- The main idea is to find the set of states that can be reached from any state by taking zero or more ε-transitions. This set is called the ε-closure of a state.
- For each state q and input symbol a, we find the set of states that can be reached from q by taking a transition on a, followed by zero or more ε-transitions. This set is called the ε-transition function of q on a, denoted by δε(q,a).
- We construct a new NFA without ε-transitions, where the states are the same as the original ε-NFA, and the transition function is defined by δ'(q,a) = δε(q,a) for all q and a.
- The initial state of the new NFA is the ε-closure of the initial state of the original ε-NFA, and the final states are those that contain at least one final state of the original ε-NFA.

## Converting an NFA without ε-transitions to an ε-NFA

- The main idea is to introduce ε-transitions between states that have the same transition on a given input symbol, and to eliminate the original transitions.
- For each input symbol a, we find the set of pairs of states (p,q) such that δ(p,a) = q. We add an ε-transition from p to q for each such pair, and remove the transition on a from p.
- We construct a new ε-NFA, where the states are the same as the original NFA without ε-transitions, and the transition function is defined by the new ε-transitions and the remaining transitions on other symbols.
- The initial state and the final states of the new ε-NFA are the same as the original NFA without ε-transitions.



# Finite Automata with Output

- A finite automata with output is a mathematical model of computation that can be in one of a finite number of states and can produce output symbols based on the input symbols and the current state .
- A finite automata with output is also known as a finite state machine (FSM) or a transducer .
- There are two types of finite automata with output: Moore machines and Mealy machines.
- A Moore machine is a finite automata with output where the output depends only on the current state. The output is associated with each state and is produced whenever the machine enters that state.
- A Mealy machine is a finite automata with output where the output depends on both the current state and the input symbol. The output is associated with each transition and is produced whenever the machine takes that transition.
- A finite automata with output can be represented by a 6-tuple (Q, Σ, Γ, δ, λ, q0) where :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite output alphabet
  - δ is a transition function that maps Q × Σ to Q
  - λ is an output function that maps Q to Γ (for Moore machines) or Q × Σ to Γ (for Mealy machines)
  - q0 is the initial state in Q
- A finite automata with output can be used to model various systems that have discrete inputs, outputs, and states, such as digital circuits, communication protocols, parsers, etc.  .
- A finite automata with output can be converted from one type to another by adding or removing states and transitions.
- A finite automata with output can be simulated by a program that keeps track of the current state, reads the input symbols, updates the state according to the transition function, and produces the output symbols according to the output function.



# Moore Machine

- A Moore machine is a type of finite state machine (FSM) that has an output value associated with each state    .
- The output value of a Moore machine depends only on the current state, not on the input symbols    .
- A Moore machine can be formally defined as a 6-tuple (Q, Σ, Γ, δ, ω, q0), where    :
  - Q is a finite set of states.
  - Σ is a finite set of input symbols.
  - Γ is a finite set of output symbols.
  - δ : Q × Σ → Q is the transition function that maps a state and an input symbol to a next state.
  - ω : Q → Γ is the output function that maps a state to an output symbol.
  - q0 ∈ Q is the initial state.
- A Moore machine can be represented by a state diagram, where each state is labeled with its output symbol and each transition is labeled with an input symbol    .
- A Moore machine can be used to model systems that produce outputs based on their current states, such as traffic lights, vending machines, counters, etc    .
- A Moore machine is different from a Mealy machine, which is another type of FSM that has an output value associated with each transition . The output value of a Mealy machine depends on both the current state and the input symbol .
- A Moore machine typically has more states than a Mealy machine for a given problem, but a Mealy machine may have more transitions and output symbols.

## Example

- Suppose we have the following Moore machine:

Moore machine example

- The Moore machine has 6 states: q0, q1, q2, q3, q4, and q5.
- The Moore machine has 2 input symbols: 0 and 1.
- The Moore machine has 2 output symbols: A and B.
- The Moore machine has the following transition function:

| Current state | Input symbol | Next state |
|---------------|--------------|------------|
| q0            | 0            | q1         |
| q0            | 1            | q2         |
| q1            | 0            | q3         |
| q1            | 1            | q4         |
| q2            | 0            | q5         |
| q2            | 1            | q0         |
| q3            | 0            | q1         |
| q3            | 1            | q2         |
| q4            | 0            | q5         |
| q4            | 1            | q0         |
| q5            | 0            | q3         |
| q5            | 1            | q4         |

- The Moore machine has the following output function:

| State | Output symbol |
|-------|---------------|
| q0    | A             |
| q1    | A             |
| q2    | A             |
| q3    | B             |
| q4    | B             |
| q5    | B             |

- The Moore machine has q0 as the initial state.
- The Moore machine produces an output symbol for each state it enters, regardless of the input symbol that causes the transition.
- For example, if the Moore machine receives the input string 0101, it will go through the following sequence of states and outputs:

| Input symbol | Current state | Output symbol | Next state |
|--------------|---------------|---------------|------------|
| -            | q0            | A             | -          |
| 0            | q0            | A             | q1         |
| 1            | q1            | A             | q4         |
| 0            | q4            | B             |



# Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input. It is also known as a **deterministic finite-state transducer**  because it can transform an input sequence into an output sequence.

Some characteristics of a Mealy machine are:

- It has a finite set of states, denoted by **Q**.
- It has a finite set of input symbols, denoted by **∑**.
- It has a finite set of output symbols, denoted by **O**.
- It has a start state, denoted by **q0**, which belongs to **Q**.
- It has a state transition function, denoted by **δ**, which maps a state and an input symbol to a next state: **δ: Q × ∑ → Q**.
- It has an output function, denoted by **λ**, which maps a state and an input symbol to an output symbol: **λ: Q × ∑ → O**.

A Mealy machine can be represented by a **state diagram**, where each state is labeled with its name and each transition is labeled with the input symbol and the output symbol separated by a slash (/). For example, the following state diagram shows a Mealy machine that detects the sequence 101 in the input and outputs 1 when the sequence is complete:

Mealy machine example

A Mealy machine can also be represented by a **transition table**, where each row corresponds to a state and each column corresponds to an input symbol. The entries in the table show the next state and the output symbol for each state and input symbol. For example, the following transition table shows the same Mealy machine as the state diagram above:

| State | 0 | 1 |
|-------|---|---|
| A     | A/0 | B/0 |
| B     | A/0 | C/0 |
| C     | D/1 | B/0 |
| D     | A/0 | B/0 |

Some advantages of a Mealy machine are:

- It can have fewer states than a Moore machine (another type of finite-state machine) for the same functionality .
- It can respond faster to the input changes because the output depends on the input as well as the state .

Some disadvantages of a Mealy machine are:

- It can have more complex logic than a Moore machine because the output depends on the input as well as the state .
- It can have glitches (unwanted changes) in the output because the output can change asynchronously with the state .



# Equivalence of Moore and Mealy Machine

- A Moore machine is a finite state machine where the output depends only on the current state.
- A Mealy machine is a finite state machine where the output depends on the current state and the input.
- The equivalence of the Moore and Mealy machine means that both the machines produce the same output for the same input.
- A Mealy machine can always be converted to a Moore machine, with the possible addition of extra states .
- A Moore machine can be converted to a Mealy machine by attaching the output of each state to the corresponding input transitions.

## Conversion from Moore to Mealy Machine

- To convert a Moore machine to a Mealy machine, follow these steps:
  - For each state in the Moore machine, identify the output associated with it.
  - For each input transition from that state, label the transition with the output of the source state.
  - Remove the output labels from the states and keep only the state names.
  - The resulting machine is a Mealy machine equivalent to the original Moore machine.

## Conversion from Mealy to Moore Machine

- To convert a Mealy machine to a Moore machine, follow these steps:
  - For each state in the Mealy machine, identify the set of outputs that can be produced from that state for different inputs.
  - If the set contains only one output, keep the state as it is and label it with that output.
  - If the set contains more than one output, create a new state for each output and label it with that output.
  - For each input transition from the original state, redirect it to the new state corresponding to the output of that transition.
  - Remove the output labels from the transitions and keep only the input symbols.
  - The resulting machine is a Moore machine equivalent to the original Mealy machine.



# Minimization of Finite Automata

- Finite automata (FA) are abstract models of computation that can recognize regular languages.
- A FA consists of a finite set of states, a finite set of input symbols, a transition function that maps states and symbols to states, an initial state, and a set of final states.
- A FA is said to be **minimal** if it has the least number of states among all the FA that recognize the same language.
- Minimization of FA is the process of finding a minimal FA that is equivalent to a given FA.
- Minimization of FA has several benefits, such as reducing the compile time, memory usage, and complexity of the FA .
- There are different methods to minimize FA, depending on whether the FA is deterministic (DFA) or nondeterministic (NFA), and whether the FA has output (Moore or Mealy machine) or not.
- The general steps to minimize FA are as follows  :
  - Step 1: Remove the unreachable states, i.e., the states that cannot be reached from the initial state by any input sequence.
  - Step 2: Partition the states into equivalence classes, i.e., the sets of states that have the same behavior for any input sequence.
  - Step 3: Replace each equivalence class by a single representative state, and adjust the transitions and final states accordingly.
  - Step 4: Check if the resulting FA is minimal, i.e., there are no two distinct states that have the same transitions for all input symbols.
- The partitioning algorithm for DFA is based on the notion of **distinguishability**, i.e., two states are distinguishable if there exists an input sequence that leads to different final states from them.
- The partitioning algorithm for NFA is based on the notion of **bisimulation**, i.e., two states are bisimilar if they can simulate each other's behavior for any input sequence.
- The partitioning algorithm for Moore and Mealy machines is similar to the DFA case, but with the additional condition that the output of the states must also be the same for each input symbol.



# Myhill-Nerode Theorem

- The Myhill-Nerode theorem is a fundamental result in the theory of regular languages. It provides a necessary and sufficient condition for a language to be regular  .
- The theorem is based on the notion of **equivalence classes** of strings with respect to a language. Two strings are said to be **equivalent** with respect to a language if they can be extended by the same set of strings to form words in the language  .
- Formally, for a language L, we define an equivalence relation ~L on the set of all strings as follows: for any two strings x and y, x ~L y if and only if for all strings z, xz is in L if and only if yz is in L  .
- The equivalence relation ~L partitions the set of all strings into disjoint subsets called **equivalence classes**. Each equivalence class contains all the strings that are equivalent with respect to L. We denote the equivalence class of a string x by [x]L  .
- The Myhill-Nerode theorem states that a language L is regular if and only if it has a **finite** number of equivalence classes, and moreover, that this number is equal to the number of states in the **minimal deterministic finite automaton (DFA)** accepting L  .
- The Myhill-Nerode theorem can be used to prove that a language is regular by showing that it has a finite number of equivalence classes. This can be done by an exhaustive case analysis in which, beginning from the empty string, distinguishing extensions are used to find additional equivalence classes until no more can be found  .
- The Myhill-Nerode theorem can also be used to prove that a language is not regular by showing that it has an **infinite** number of equivalence classes. This can be done by finding an infinite set of strings that are pairwise **distinguishable** with respect to L, meaning that for any two distinct strings x and y in the set, there exists a string z such that xz is in L but yz is not, or vice versa  .
- The Myhill-Nerode theorem can also be used to construct the minimal DFA for a regular language L by taking the equivalence classes of L as the states, the initial state as the equivalence class of the empty string, the final states as the equivalence classes that contain strings in L, and the transition function as the mapping from an equivalence class [x]L and a symbol a to the equivalence class [xa]L  .

: Myhill–Nerode theorem - Wikipedia
: THE MYHILL-NERODE THEOREM - Columbia University
: Basic Theorems in TOC (Myhill nerode theorem) - GeeksforGeeks



# Simulation of DFA and NFA

- A **deterministic finite automaton (DFA)** is a finite state machine that accepts or rejects a given string of symbols, by running through a state sequence uniquely determined by the string.
- A **nondeterministic finite automaton (NFA)** is a finite state machine where, from each state, there can be more than one possible next state for a given input symbol.
- Both DFA and NFA can be used to recognize the same set of regular languages, but they may differ in the number of states and transitions.
- To simulate a DFA, we need to keep track of the current state and the input symbol, and follow the unique transition to the next state until the end of the input. If the final state is an accepting state, we accept the input; otherwise, we reject it.
- To simulate an NFA, we need to keep track of all the possible current states and the input symbol, and follow all the possible transitions to the next states until the end of the input. If any of the final states is an accepting state, we accept the input; otherwise, we reject it .
- To convert an NFA to an equivalent DFA, we can use the **subset construction** algorithm, which creates a new state in the DFA for each subset of states in the NFA, and defines the transitions based on the union of the transitions of the NFA states in the subset .
- To illustrate the simulation and conversion of DFA and NFA, we can use tools such as **JFLAP** or **Automaton Simulator**, which allow us to create, edit, test, and visualize finite automata.



# Unit 2 - Regular Expressions and Languages

## Objectives
- To understand the concept of regular expressions and how they can be used to describe regular languages.
- To learn the syntax and semantics of regular expressions and how to construct them from simpler components.
- To learn how to convert regular expressions to finite automata and vice versa.
- To learn how to apply regular expressions to pattern matching and text processing problems.

## Contents
- Regular expressions are a concise and powerful notation for specifying sets of strings, also known as regular languages.
- Regular expressions can be defined recursively as follows:
  - The empty set ∅, the empty string ε, and any single symbol a are regular expressions.
  - If r and s are regular expressions, then so are (r + s), (r · s), and (r*), where + denotes union, · denotes concatenation, and * denotes Kleene closure.
  - Nothing else is a regular expression.
- The meaning of a regular expression is the set of strings that it describes, also known as the language of the regular expression.
- The language of a regular expression can be defined recursively as follows:
  - L(∅) = ∅, L(ε) = {ε}, and L(a) = {a} for any symbol a.
  - L(r + s) = L(r) ∪ L(s), L(r · s) = L(r) · L(s), and L(r*) = L(r)*, where ∪ denotes set union, · denotes set concatenation, and * denotes set closure.
  - Nothing else is a language of a regular expression.
- Regular expressions can be simplified and manipulated using various laws and properties, such as:
  - Idempotence: r + r = r
  - Commutativity: r + s = s + r
  - Associativity: (r + s) + t = r + (s + t) and (r · s) · t = r · (s · t)
  - Distributivity: r · (s + t) = (r · s) + (r · t) and (r + s) · t = (r · t) + (s · t)
  - Identity: r · ε = ε · r = r
  - Annihilation: r · ∅ = ∅ · r = ∅
  - Zero or more: r* = ε + r · r*
  - One or more: r+ = r · r*
  - Optional: r? = ε + r
- Regular expressions can be converted to finite automata using various algorithms, such as:
  - Thompson's construction: This algorithm constructs a nondeterministic finite automaton (NFA) with ε-transitions from a regular expression by applying a set of rules for each operator in the regular expression.
  - Glushkov's construction: This algorithm constructs a deterministic finite automaton (DFA) from a regular expression by computing the sets of first, last, and follow positions for each symbol in the regular expression.
  - McNaughton-Yamada-Thompson algorithm: This algorithm constructs a DFA from a regular expression by first applying Thompson's construction to obtain an NFA with ε-transitions, then eliminating the ε-transitions, and then minimizing the resulting NFA.
- Finite automata can be converted to regular expressions using various algorithms, such as:
  - State elimination: This algorithm eliminates states from a finite automaton one by one and replaces the transitions involving the eliminated state with regular expressions until only the initial and final states remain.
  - Kleene's theorem: This theorem states that for any finite automaton, there exists a regular expression that describes the same language as the finite automaton. The proof of this theorem provides a method to construct such a regular expression by using a system of equations involving regular expressions.
- Regular expressions can be used to solve various problems involving pattern matching and text processing, such as:
  - Finding all occurrences of a pattern in a text.
  - Validating the format of an input string.
  - Extracting information from a text.
  - Replacing or modifying parts of a text.



# Regular Expressions for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A **regular expression** is a symbolic notation that can be used to describe a **regular language**  .
- A **regular language** is a set of strings that can be recognized by a **finite automaton**  .
- A **finite automaton** is a mathematical model of computation that consists of a finite set of states, a finite set of input symbols, a transition function that maps states and symbols to new states, and a set of final or accepting states.
- Regular expressions can be defined recursively over an alphabet ∑ as follows:
  - The empty set ɸ is a regular expression that denotes the language ɸ.
  - The empty string ɛ is a regular expression that denotes the language {ɛ}.
  - For any symbol a ∈ ∑, a is a regular expression that denotes the language {a}.
  - If R and S are regular expressions, then so are:
    - R + S (union), which denotes the language L(R) ∪ L(S).
    - RS (concatenation), which denotes the language L(R)L(S).
    - R* (Kleene star), which denotes the language L(R)*.
  - Nothing else is a regular expression.
- Regular expressions can be used to specify patterns that can be matched in input text. For example, the regular expression a*b* denotes the language of all strings that consist of zero or more a's followed by zero or more b's, such as ɛ, a, b, ab, aa, bb, aab, abb, etc.
- Regular expressions can be represented by **regular grammars**, which are a type of formal grammar that have rules of the form A -> a or A -> aB or A -> ɛ, where A and B are variables and a is a terminal symbol. For example, the regular grammar with rules S -> aS | bS | ɛ generates the same language as the regular expression a*b*.
- Regular expressions, regular languages, and finite automata are equivalent in expressive power, meaning that for any regular expression, there exists a regular language and a finite automaton that accept the same set of strings, and vice versa  . There are algorithms to convert between these different representations.



# Transition Graph

A transition graph is a graphical representation of a finite automaton. It consists of the following components :

- A finite set of states, at least one of which is designated as the start state and some (maybe none) of which are designated as the final states.
- A finite set of input symbols, called the alphabet, from which the input strings are formed.
- A set of directed edges, labeled with input symbols, that connect the states. Each edge represents a possible transition from one state to another on reading an input symbol.

A transition graph can be interpreted as a flowchart for an algorithm that recognizes a language. The algorithm starts from the start state and reads the input string from left to right, following the edges that match the input symbols. If the algorithm reaches a final state after reading the entire input string, then the input string is accepted by the transition graph. Otherwise, the input string is rejected.

For example, the following transition graph recognizes the language of all strings over {0,1} that end with 1:

Transition graph example

Some properties of transition graphs are:

- If there is no way to factor a word w that is the concatenation of edge labels of a successful path in a transition graph, then w does not belong to the language recognized by the transition graph.
- Every finite automaton can be viewed as a transition graph, but not every transition graph can be viewed as a finite automaton. Transition graphs generalize finite automata by allowing edges to be labeled with more than one symbol or with the empty string.
- A transition graph can be converted into an equivalent finite automaton by introducing new states and edges to eliminate the edges that are labeled with more than one symbol or with the empty string. This process is called the state-splitting method.



# Kleene's Theorem

- Kleene's theorem is a fundamental result in the theory of automata and formal languages that shows the equivalence between regular languages, regular expressions, and finite automata.
- Kleene's theorem consists of two parts: the forward part and the backward part.
- The forward part states that for any regular expression of a language, there exists a finite automaton (either deterministic or nondeterministic) that recognizes the same language.
- The backward part states that for any finite automaton (either deterministic or nondeterministic) that recognizes a language, there exists a regular expression that describes the same language.
- The proof of the forward part relies on the construction of a finite automaton from a regular expression using the following rules:
  - For any symbol a in the alphabet, there is a finite automaton that recognizes the language {a}.
  - For any two finite automata that recognize the languages L1 and L2, there is a finite automaton that recognizes the union of L1 and L2, using the union operation on regular expressions.
  - For any two finite automata that recognize the languages L1 and L2, there is a finite automaton that recognizes the concatenation of L1 and L2, using the concatenation operation on regular expressions.
  - For any finite automaton that recognizes a language L, there is a finite automaton that recognizes the Kleene closure of L, using the star operation on regular expressions.
- The proof of the backward part relies on the construction of a regular expression from a finite automaton using the following steps:
  - Convert the finite automaton into a generalized nondeterministic finite automaton (GNFA) that has a single start state and a single accept state, and that allows transitions labeled with regular expressions.
  - Eliminate all the states of the GNFA except the start state and the accept state, by applying the following rule: for any state q that is neither the start state nor the accept state, remove q and add transitions between the states that had incoming and outgoing transitions to q, labeled with the regular expression that corresponds to the paths through q.
  - The regular expression that labels the transition from the start state to the accept state of the resulting GNFA is the regular expression that describes the language recognized by the original finite automaton.



# Finite Automata and Regular Expression

- Finite automata are abstract machines that can recognize patterns in strings and accept or reject them based on some rules .
- Regular expressions are algebraic notations that can describe the set of strings accepted by finite automata .
- Regular expressions and finite automata are equivalent in expressive power, meaning that for every regular expression, there exists a finite automaton that accepts the same language, and vice versa   .
- There are two types of finite automata: deterministic finite automata (DFA) and nondeterministic finite automata (NFA). DFA have only one transition for each input symbol and state, while NFA can have multiple transitions or no transition for the same input symbol and state .
- NFA can also have epsilon transitions, which are transitions that do not consume any input symbol and can be taken spontaneously .
- DFA and NFA are also equivalent in expressive power, meaning that for every NFA, there exists a DFA that accepts the same language, and vice versa  .
- The process of converting a regular expression to a finite automaton is called regular expression to finite automaton construction. There are different methods for this process, such as state decomposition method, Thompson's construction method, and Glushkov's construction method .
- The process of converting a finite automaton to a regular expression is called finite automaton to regular expression conversion. There are different methods for this process, such as state elimination method, Kleene's theorem, and Brzozowski's algebraic method .
- Regular expressions and finite automata are useful tools for modeling and analyzing various aspects of computation, such as lexical analysis, pattern matching, text processing, and formal languages .



# Arden's Theorem for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Arden's Theorem is a mathematical statement that is used to find out a regular expression that represents the language accepted by a finite automaton  .
- Arden's Theorem states that, if P and Q are two regular expressions over an alphabet , and if P does not contain the empty string , then the following equation in R given by R = Q + RP has a unique solution; R = QP*  .
- The proof of Arden's Theorem is based on the following steps:
  - Show that R = QP* is a solution of R = Q + RP by substituting R = QP* in the equation and simplifying it.
  - Show that R = QP* is the only solution of R = Q + RP by assuming that there is another solution S and deriving a contradiction.
- Arden's Theorem can be applied to convert a finite automaton into a regular expression by following these steps  :
  - Construct a system of equations for each state of the finite automaton, where the equation for a state q is of the form q = Q + RP, where Q is the set of symbols that lead to a final state from q, and R is the set of symbols that lead to another state from q.
  - Solve the system of equations using Arden's Theorem, starting from the final states and moving backwards to the initial state.
  - The solution for the initial state is the regular expression that represents the language accepted by the finite automaton.
- An example of applying Arden's Theorem to convert a finite automaton into a regular expression is given below:

Finite automaton

- The system of equations for this finite automaton is:

q1 = q1.0 + q2.1 + q2.0

q2 = q1.1 + q2.0 + q3.0 + q3.1

q3 = q2.1 + q3.0 + q3.1

- Solving the system of equations using Arden's Theorem, we get:

q3 = (q2.1 + q3.0 + q3.1)*

q2 = (q1.1 + q2.0 + q3.0 + q3.1)*

q1 = (q1.0 + q2.1 + q2.0)*

q1 = (q1.0 + (q1.1 + q2.0 + q3.0 + q3.1)*.1 + (q1.1 + q2.0 + q3.0 + q3.1)*.0)*

q1 = (q1.0 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.1 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.0)*

q1 = (q1.0 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.1 + (q1.1 + q2.0 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.0)*

q1 = (q1.0 + (q1.1 + q2.0 + (q2.1 + (q2.1 + q3.0 + q3.1)*.0 + (q2.1 + q3.0 + q3.1)*.1)*.0 + (q2.



# Algebraic Method Using Arden’s Theorem

- Arden’s theorem is a mathematical statement that can be used to find a regular expression equivalent to a given finite automaton.
- Arden’s theorem states that if P and Q are two regular expressions over an alphabet Σ, and if P does not contain the empty string ε, then the following equation in R has a unique solution:

  R = Q + RP

  The solution is given by:

  R = QP*

- Arden’s theorem can be applied to solve a system of linear equations involving regular expressions, which can be obtained from the transition function of a finite automaton.
- To use Arden’s theorem, we need to follow these steps:

  - Convert the given finite automaton into an equivalent one with a single final state, by adding a new state and connecting it to all the original final states with ε-transitions.
  - Label each state of the automaton with a variable, such as R1, R2, R3, etc.
  - For each state, write an equation of the form Ri = Qi + ∑Rjaj, where Qi is the set of symbols that can be read from the state without changing it, and Rjaj is the product of the variable corresponding to the next state and the symbol that causes the transition.
  - If the state is the final state, add ε to the right-hand side of the equation.
  - Simplify the equations by eliminating the variables that contain ε, using the fact that P + εP* = P*.
  - Solve the remaining equations using Arden’s theorem, starting from the final state and substituting the values of the variables in the other equations.
  - The regular expression corresponding to the finite automaton is the value of the variable associated with the initial state.



# Regular and Non-Regular Languages

- A **regular language** is a language that can be expressed with a **regular expression** or a **deterministic or non-deterministic finite automaton** or state machine.
- A **language** is a set of strings which are made up of characters from a specified alphabet, or set of symbols.
- Regular languages are a subset of the set of all strings.
- Regular languages correspond to problems that can be solved with **finite memory**. Only need to remember one of finitely many things.
- Examples of regular languages are:
  - All strings of length = 2 over {a, b}* i.e. L = {aa, ab, ba, bb}.
  - All strings that start and end with the same symbol over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaa, bbb, ...}.
  - All strings that contain an even number of a's over {a, b}* i.e. L = {b, ab, ba, bb, aab, aba, baa, bba, bbb, ...}.
- A **non-regular language** is a language that **cannot** be expressed with a regular expression or a finite automaton.
- Non-regular languages correspond to problems that cannot be solved with finite memory. May need to remember one of infinitely many different things.
- Examples of non-regular languages are:
  - All strings that are palindromes over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaa, bbb, abba, baab, ...}.
  - All strings that have the same number of a's and b's over {a, b}* i.e. L = {ab, ba, aabb, abab, baba, bbaa, ...}.
  - All strings of the form a^n b^n over {a, b}* i.e. L = {ab, aabb, aaabbb, aaaabbbb, ...}.
- There are different methods to prove that a language is regular or non-regular, such as:
  - Using **closure properties** of regular languages, i.e. showing that the language can be obtained by applying some operations (such as union, intersection, complement, concatenation, star, etc.) on some known regular languages.
  - Using **regular expressions** or **finite automata** to describe the language, i.e. showing that there exists a way to construct a pattern or a machine that can generate or recognize the language.
  - Using the **pumping lemma** for regular languages, i.e. showing that there exists a contradiction between the assumption that the language is regular and the property that any sufficiently long string in the language can be pumped, i.e. repeated some parts without changing the membership in the language.



# Closure properties of Regular Languages

- Closure properties on regular languages are defined as certain operations on a language which are guaranteed to produce a regular language  .
- Closure refers to some operation on a language, resulting in a new language that is of same “type” as originally operated on i.e., regular.
- Regular languages are closed under following operations  :
  - Union: If L1 and L2 are regular languages, then L1 ∪ L2 is also a regular language.
  - Intersection: If L1 and L2 are regular languages, then L1 ∩ L2 is also a regular language.
  - Complement: If L is a regular language, then L is also a regular language.
  - Difference: If L1 and L2 are regular languages, then L1 - L2 is also a regular language.
  - Concatenation: If L1 and L2 are regular languages, then L1L2 is also a regular language.
  - Kleene star: If L is a regular language, then L* is also a regular language.
  - Kleene plus: If L is a regular language, then L+ is also a regular language.
  - Reversal: If L is a regular language, then LR is also a regular language, where LR is the language obtained by reversing the strings of L.
  - Homomorphism: If L is a regular language and h is a homomorphism, then h(L) is also a regular language.
  - Inverse homomorphism: If L is a regular language and h is a homomorphism, then h-1(L) is also a regular language.
  - Substitution: If L is a regular language and σ is a substitution, then σ(L) is also a regular language.
  - Prefix: If L is a regular language, then Pref(L) is also a regular language, where Pref(L) is the language of all prefixes of the strings of L.
  - Suffix: If L is a regular language, then Suff(L) is also a regular language, where Suff(L) is the language of all suffixes of the strings of L.
  - Substring: If L is a regular language, then Sub(L) is also a regular language, where Sub(L) is the language of all substrings of the strings of L.



# Pigeonhole Principle

The pigeonhole principle is a simple but powerful idea that can be used to prove the existence of certain mathematical facts. It can be stated as follows:

- If n items are put into m containers, with n > m, then at least one container must contain more than one item.

- Alternatively, if n items are distributed among m containers, then there is at least one container that contains at least ⌈n/m⌉ items, where ⌈x⌉ denotes the smallest integer greater than or equal to x.

The principle is also known as the Dirichlet principle, after the German mathematician Peter Gustav Lejeune Dirichlet, who used it in his work on number theory.

The principle can be illustrated by a simple example: Suppose you have 10 pigeons and 9 pigeonholes. If you put the pigeons into the pigeonholes, then by the pigeonhole principle, there must be at least one pigeonhole that contains more than one pigeon. This is obvious, since there are more pigeons than pigeonholes.

The principle can also be applied to more abstract situations, such as points, colors, numbers, or functions. Here are some examples of the applications of the pigeonhole principle:

- If you have 5 pairs of socks in a drawer, and you randomly pick 3 socks from the drawer, then by the pigeonhole principle, you must have at least one pair of matching socks. This is because there are only 2 possible colors for the socks, and you have 3 items.

- If you have 13 people in a room, then by the pigeonhole principle, there must be at least two people who share the same birthday. This is because there are only 12 possible months for the birthdays, and you have 13 items.

- If you have 10 points inside a unit square, then by the pigeonhole principle, there must be two points that are at most √2/10 units apart. This is because you can divide the square into 10 smaller squares of side length √2/10, and each point must lie in one of these squares.

- If you have a function f: N → N that maps the natural numbers to the natural numbers, then by the pigeonhole principle, there must be two distinct natural numbers x and y such that f(x) = f(y). This is because there are infinitely many natural numbers, and only finitely many possible values for f(n).

The pigeonhole principle is a useful tool for proving the existence of certain mathematical objects or properties, but it does not tell us how to find them or construct them. For example, the pigeonhole principle tells us that there must be two people in a room who share the same birthday, but it does not tell us who they are or how to find them. To do that, we need more information or a different method.



# Pumping Lemma for Regular Languages

- The pumping lemma for regular languages is a theorem that describes a property of all regular languages.
- A regular language is a language that can be recognized by a finite automaton or generated by a regular expression.
- The pumping lemma states that for any regular language L, there exists a constant p (called the pumping length) such that any string w in L with length at least p can be divided into three substrings, w = xyz, where:

  - |y| > 0 (y is not empty)
  - |xy| <= p (y is within the first p symbols of w)
  - xy^i z is in L for all i >= 0 (repeating y any number of times preserves membership in L)

- The pumping lemma can be used to prove that a language is not regular by showing a contradiction. For example, to prove that the language L = {a^n b^n | n >= 0} is not regular, we can assume that it is regular and has a pumping length p, and then choose a string w = a^p b^p in L. By the pumping lemma, we can write w = xyz, where y = a^k for some k > 0. Then, by the pumping lemma, xy^2 z = a^(p+k) b^p should also be in L, but this is not the case, since the number of a's and b's are not equal. Therefore, we have reached a contradiction, and L is not regular.



# Application of Pumping Lemma

- Pumping lemma is a tool to prove that certain languages are not regular. It should never be used to show that a language is regular .
- Pumping lemma states that if L is a regular language, then there exists a constant n (called the pumping length) such that for any string w in L with length at least n, w can be written as w = xyz, where
  - x, y, and z are substrings of w
  - y is not empty
  - xy has length at most n
  - for any non-negative integer k, xy^kz is also in L
- The intuition behind pumping lemma is that any regular language can be recognized by a finite automaton, and if a string is long enough, the automaton must enter some state more than once while reading the string. This means that there is a loop in the automaton that can be repeated any number of times without changing the final state .
- To use pumping lemma to prove that a language is not regular, we follow these steps:
  - Assume that the language is regular and let n be the pumping length
  - Choose a string w in the language with length at least n
  - Show that for any possible way of writing w as w = xyz, where x, y, and z satisfy the conditions of pumping lemma, there exists a value of k such that xy^kz is not in the language
  - Conclude that the language does not satisfy pumping lemma and hence is not regular
- For example, let L = {a^nb^n | n >= 0} be the language of strings with equal number of a's and b's. We can prove that L is not regular by using pumping lemma as follows:
  - Assume that L is regular and let n be the pumping length
  - Choose w = a^nb^n, which is in L and has length 2n >= n
  - Write w as w = xyz, where x, y, and z satisfy the conditions of pumping lemma
  - Since xy has length at most n, it must consist of only a's, so we can write x = a^p, y = a^q, and z = a^r b^n, where p + q + r = n and q > 0
  - Now, for any k, xy^kz = a^p a^kq a^r b^n = a^(p + kq + r) b^n
  - If we choose k = 2, then xy^kz = a^(p + 2q + r) b^n, which is not in L, because p + 2q + r != n
  - Therefore, L does not satisfy pumping lemma and hence is not regular .



# Decidability

- Decidability is a property of a problem or a language that indicates whether it can be solved by an algorithm in a finite number of steps.
- A problem is decidable if there exists a Turing machine that halts on every input and gives a correct answer (yes or no) for the problem.
- A language is decidable if there exists a Turing machine that accepts and halts on every string in the language, and rejects and halts on every string not in the language.
- Decidable languages are also called recursive languages, and they correspond to algorithmically solvable decision problems.
- Some examples of decidable problems are:
  - Given a deterministic finite automaton (DFA), does it accept a given string?
  - Given a DFA, is its language empty?
  - Given a DFA, is its language finite?
  - Given two DFAs, are their languages equal?
- Decidability is an important concept in the theory of computation, as it helps to classify problems and languages according to their computational complexity and tractability.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on the decision properties of regular expressions and languages.

# Decision properties of regular expressions and languages

- Decision properties are questions that can be answered yes or no for a given language or expression.
- For example, is a language empty? Is a language finite? Is a word in a language? Are two languages equal?
- Decision properties are important for analyzing and comparing languages and expressions, and for designing algorithms and machines that operate on them.
- Regular expressions and languages have many decision properties that are decidable, meaning that there exists an algorithm that can answer them in finite time.
- Some of the common decision properties of regular expressions and languages are:

  - Emptiness: Given a regular expression or a language, is it empty? That is, does it generate or accept any words at all?
  - Non-emptiness: Given a regular expression or a language, is it non-empty? That is, does it generate or accept at least one word?
  - Finiteness: Given a regular expression or a language, is it finite? That is, does it generate or accept only a finite number of words?
  - Infiniteness: Given a regular expression or a language, is it infinite? That is, does it generate or accept an infinite number of words?
  - Membership: Given a regular expression or a language and a word, is the word in the language? That is, does the expression generate or the language accept the word?
  - Equality: Given two regular expressions or languages, are they equal? That is, do they generate or accept the same set of words?
  - Subset: Given two regular expressions or languages, is one a subset of the other? That is, does every word generated or accepted by one expression or language also generated or accepted by the other?
  - Superset: Given two regular expressions or languages, is one a superset of the other? That is, does every word generated or accepted by the other expression or language also generated or accepted by the one?
  - Intersection: Given two regular expressions or languages, do they have a non-empty intersection? That is, is there at least one word that is generated or accepted by both expressions or languages?
  - Complement: Given a regular expression or a language, is its complement regular? That is, is the set of words that are not generated or accepted by the expression or language also a regular language?

- These decision properties can be solved using different methods, such as converting regular expressions to finite automata, applying closure properties of regular languages, or using algebraic properties of regular expressions.
- For example, to check the emptiness of a regular expression, we can convert it to a finite automaton and see if there is a path from the initial state to any final state. If there is no such path, then the expression is empty. If there is such a path, then the expression is non-empty.
- Another example is to check the equality of two regular expressions. We can convert them to finite automata and then minimize them using a standard algorithm. If the minimized automata are isomorphic, then the expressions are equal. If they are not isomorphic, then the expressions are not equal.



# Finite Automata and Regular Languages

- A **finite automaton** is a mathematical model of a machine that can accept or reject a string of symbols based on its states and transitions .
- A **regular language** is a set of strings that can be described by a **regular expression** or recognized by a finite automaton .
- A **regular expression** is a notation that uses symbols and operators to define a regular language .
- A **regular grammar** is a type of grammar that generates a regular language by applying rules that replace a single non-terminal symbol with a string of terminal and non-terminal symbols .

## Properties of Regular Languages

- Regular languages are closed under the following operations: union, concatenation, star, complement, intersection, and difference .
- Regular languages can be decided by algorithms that test membership, emptiness, equivalence, and containment.
- Regular languages can be minimized by finding the smallest equivalent finite automaton.
- Regular languages can be pumped by applying the pumping lemma, which states that any sufficiently long string in a regular language can be divided into three parts that can be repeated to form new strings in the same language.

## Examples of Regular Languages

- The language of all strings over {a,b} that end with a .
- The language of all binary numbers that are divisible by 3 .
- The language of all strings over {0,1} that do not contain the substring 11 .
- The language of all strings over {a,b,c} that have an equal number of a's and b's.
- The language of all strings over {a,b} that have an odd length.



# Regular Languages and Computers

- Regular languages are a class of formal languages that can be defined by regular expressions or recognized by finite automata.
- Regular languages are used in parsing and designing programming languages, as well as in modeling simple computational problems that require a very small amount of memory.
- Regular languages have several equivalent characterizations, such as:
  - A language is regular if and only if it can be defined by a regular expression.
  - A language is regular if and only if it can be recognized by a deterministic finite automaton (DFA).
  - A language is regular if and only if it can be recognized by a nondeterministic finite automaton (NFA).
  - A language is regular if and only if it can be recognized by a right-linear grammar.
  - A language is regular if and only if it can be recognized by a left-linear grammar.
  - A language is regular if and only if it can be recognized by a regular grammar.
- Regular languages have several closure properties, such as:
  - The union of two regular languages is regular.
  - The intersection of two regular languages is regular.
  - The complement of a regular language is regular.
  - The concatenation of two regular languages is regular.
  - The Kleene star of a regular language is regular.
  - The reversal of a regular language is regular.
  - The homomorphism of a regular language is regular.
  - The inverse homomorphism of a regular language is regular.
- Regular languages have several decidability properties, such as:
  - The emptiness problem: Given a regular language L, decide whether L is empty or not.
  - The finiteness problem: Given a regular language L, decide whether L is finite or not.
  - The membership problem: Given a regular language L and a word w, decide whether w belongs to L or not.
  - The equivalence problem: Given two regular languages L1 and L2, decide whether L1 and L2 are equal or not.
  - The inclusion problem: Given two regular languages L1 and L2, decide whether L1 is a subset of L2 or not.
  - The minimization problem: Given a regular language L, find a DFA that recognizes L and has the minimum number of states.
- Regular languages have several limitations, such as:
  - They cannot recognize languages that require an unbounded amount of memory, such as the language of balanced parentheses or the language of palindromes.
  - They cannot recognize languages that are not closed under intersection, such as the language of prime numbers or the language of squares.
  - They cannot recognize languages that are not closed under complement, such as the language of odd-length words or the language of words that contain an even number of a's and an odd number of b's.
  - They cannot recognize languages that are not closed under concatenation, such as the language of words that start and end with the same symbol or the language of words that contain exactly two a's.
  - They cannot recognize languages that are not closed under Kleene star, such as the language of words that contain at least one a or the language of words that contain exactly one b.



# Simulation of Transition Graph and Regular Language

- A transition graph is a graphical representation of a deterministic finite automaton (DFA) that recognizes a regular language.
- A transition graph consists of a finite set of states, an alphabet of input symbols, a start state, a set of final states, and a set of transitions labeled with input symbols that show how to move from one state to another.
- A transition graph can be used to simulate the process of accepting or rejecting an input string by a DFA. The simulation starts from the start state and follows the transitions that match the input symbols until the end of the input string is reached. If the simulation ends in a final state, the input string is accepted; otherwise, it is rejected.
- A transition graph can also be used to generate a regular expression that denotes the same language as the DFA. The regular expression can be obtained by concatenating the labels of the transitions along any successful path from the start state to a final state. The regular expression for the whole language is the union of the regular expressions for all the successful paths.
- A regular expression is a compact and concise way of describing a regular language using symbols and operators. A regular expression can be converted into a transition graph using the following rules:
  - For each symbol a in the alphabet, create a transition graph with two states and a transition labeled with a from the first state to the second state. The first state is the start state and the second state is the final state.
  - For any two transition graphs A and B, create a transition graph for the union of their languages by adding a new start state and a new final state, and adding epsilon-transitions from the new start state to the start states of A and B, and from the final states of A and B to the new final state. An epsilon-transition is a transition that does not consume any input symbol.
  - For any two transition graphs A and B, create a transition graph for the concatenation of their languages by adding an epsilon-transition from the final state of A to the start state of B, and making the start state of A the start state and the final state of B the final state of the new transition graph.
  - For any transition graph A, create a transition graph for the Kleene closure of its language by adding a new start state and a new final state, and adding epsilon-transitions from the new start state to the start state of A, from the final state of A to the new final state, and from the final state of A to the start state of A. The new start state and the new final state are the start state and the final state of the new transition graph, respectively.



## Unit 3 - Regular and Non-Regular Grammars

- A grammar is a set of rules that defines how a language is generated from a finite alphabet of symbols.
- A grammar consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- A production rule is of the form A -> B, where A is a non-terminal symbol and B is a string of terminal and/or non-terminal symbols.
- A grammar can be used to derive strings of the language by starting from the start symbol and applying production rules until only terminal symbols are left.
- A grammar is said to be regular if all its production rules are of one of the following forms: A -> a, A -> aB, or A -> ε, where A and B are non-terminal symbols, a is a terminal symbol, and ε is the empty string.
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton.
- A grammar is said to be non-regular if it has at least one production rule that is not of the forms mentioned above.
- A non-regular grammar can generate a non-regular language, which is a language that cannot be recognized by a finite automaton.
- Examples of regular languages are: {a^n b^n | n >= 0}, {w | w contains an even number of a's}, {w | w is a palindrome}.
- Examples of non-regular languages are: {a^n b^n c^n | n >= 0}, {w | w is the reverse of some other string in the language}, {w | w contains an equal number of a's and b's}.



# Context Free Grammar (CFG) for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A context free grammar (CFG) is a formal grammar that can be used to generate all possible strings in a given formal language .
- A formal grammar consists of a set of production rules that can be applied to a symbol or a string of symbols to produce another string of symbols.
- A context free grammar is called so because each production rule can be applied to a nonterminal symbol regardless of its context, i.e., the symbols that surround it.
- A context free grammar can be defined by four tuples as: G = (V, T, P, S) where :
  - V is a finite set of nonterminal symbols, also called variables or syntactic categories.
  - T is a finite set of terminal symbols, also called tokens or lexical categories.
  - P is a finite set of production rules, each of the form A -> α, where A is a nonterminal symbol and α is a string of terminals and/or nonterminals (α can be empty).
  - S is a special nonterminal symbol, called the start symbol, that is used to derive the strings of the language.
- A context free grammar can generate a context free language, which is a set of all strings that can be derived from the start symbol using the production rules.
- A context free grammar can be used to specify the syntax of a language, such as a programming language or a natural language .
- A context free grammar can be used to design parsers, which are programs that analyze the structure and meaning of a string of symbols according to a given grammar.
- A context free grammar can be represented by a parse tree, which is a graphical representation of the derivation of a string from the start symbol using the production rules .
- A context free grammar can be classified into different types, such as regular, deterministic, ambiguous, unambiguous, etc., based on certain properties of the grammar or the language it generates .



# Definition for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A **regular grammar** is a formal grammar that can generate a **regular language** .
- A regular language is a language that can be recognized by a **finite automaton**.
- A regular grammar can be either **right-regular** or **left-regular**.
- In a **right-regular grammar**, every production rule has at most one non-terminal on the **right-hand side**, and that non-terminal is the **last symbol** in the right-hand side.
- In a **left-regular grammar**, every production rule has at most one non-terminal on the **left-hand side**, and that non-terminal is the **first symbol** in the left-hand side.
- The general form of a right-regular grammar is:

  - A → a
  - A → aB
  - A → ε

  where A, B are non-terminals, a is a terminal, and ε is the empty string.

- The general form of a left-regular grammar is:

  - A → a
  - A → Ba
  - A → ε

  where A, B are non-terminals, a is a terminal, and ε is the empty string.

- A **non-regular grammar** is a formal grammar that can generate a **non-regular language**.
- A non-regular language is a language that cannot be recognized by a finite automaton.
- A non-regular grammar can have production rules that are not in the form of a regular grammar.
- For example, a non-regular grammar can have production rules like:

  - A → aAa
  - A → B
  - B → bBb
  - B → ε

  where A, B are non-terminals, a, b are terminals, and ε is the empty string.

- A non-regular grammar can also be a **context-free grammar** or a **context-sensitive grammar**.
- A context-free grammar is a grammar that has only one non-terminal on the left-hand side of each production rule.
- A context-sensitive grammar is a grammar that has no restrictions on the form of the production rules.



# Derivations for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A **derivation** is a process of generating a string from a grammar by applying production rules.
- A **regular grammar** is a grammar that can generate a regular language, which is a language that can be recognized by a finite automaton.
- A **non-regular grammar** is a grammar that can generate a language that is not regular, which means that it cannot be recognized by a finite automaton.
- There are two types of regular grammars: **left-regular** and **right-regular**. A left-regular grammar has production rules of the form A -> aB or A -> a, where A and B are non-terminals and a is a terminal. A right-regular grammar has production rules of the form A -> Ba or A -> a, where A and B are non-terminals and a is a terminal.
- A regular grammar can be converted to a finite automaton by the following steps:
  - The number of states in the automaton will be equal to the number of non-terminals plus one.
  - Each state in the automaton represents each non-terminal in the regular grammar.
  - The additional state will be the final state of the automaton.
  - For each production rule A -> aB, add a transition from the state corresponding to A to the state corresponding to B with the label a.
  - For each production rule A -> a, add a transition from the state corresponding to A to the final state with the label a.
  - The initial state of the automaton is the state corresponding to the start symbol of the grammar.
- A finite automaton can be converted to a regular grammar by the following steps:
  - The set of non-terminals of the grammar is the set of states of the automaton.
  - The start symbol of the grammar is the initial state of the automaton.
  - For each transition from state A to state B with the label a, add a production rule A -> aB to the grammar.
  - For each final state F, add a production rule F -> epsilon to the grammar, where epsilon is the empty string.
- A **derivation tree** is a graphical representation of a derivation, where the root node is the start symbol, the internal nodes are non-terminals, and the leaf nodes are terminals. The string generated by the derivation is obtained by concatenating the labels of the leaf nodes from left to right.
- A **regular expression** is a compact notation for describing a regular language using symbols, operators, and parentheses. The basic symbols are the terminals of the language, and the operators are union (+), concatenation (.), and Kleene star (*). The parentheses are used to group expressions and change the order of precedence of the operators. For example, the regular expression (a+b)*.a.b describes the language of all strings that end with ab and contain only a and b.
- A regular expression can be converted to a finite automaton by the following steps:
  - Construct a finite automaton for each basic symbol, which has two states and one transition labeled by the symbol.
  - For each union operator, construct a finite automaton that has a new initial state with epsilon-transitions to the initial states of the two operands, and a new final state with epsilon-transitions from the final states of the two operands.
  - For each concatenation operator, construct a finite automaton that has the initial state of the first operand, the final state of the second operand, and an epsilon-transition from the final state of the first operand to the initial state of the second operand.
  - For each Kleene star operator, construct a finite automaton that has a new initial state with an epsilon-transition to the initial state of the operand, a new final state with an epsilon-transition from the final state of the operand, and an epsilon-transition from the new initial state to the new final state.
  - Eliminate the epsilon-transitions by applying the following rules:
    - If there is an epsilon-transition from state A to state B, and a transition from state B to state C with the label a, then add a transition from state A to state C with the label a.
    - If there is an epsilon-transition from state A to state B, and state B is a final state, then make state A a final state.
    - Remove all the epsilon-transitions.
- A finite automaton can be converted



# Languages

- In automata theory, a formal language is a set of strings of symbols drawn from a finite alphabet .
- A formal language can be specified either by a set of rules (such as regular expressions or a context-free grammar) that generates the language, or by a formal machine that accepts (recognizes) the language .
- A word is a finite string of symbols from the alphabet.
- A language is a set of words, which may be finite or infinite.
- A formal language is a mathematical object that can be studied and analyzed using various tools and techniques.
- Formal languages are classified into different types based on their expressive power and the complexity of the machines or rules that define them.
- Some of the most common types of formal languages are:
  - Regular languages: These are the languages that can be defined by regular expressions or recognized by finite automata .
  - Context-free languages: These are the languages that can be defined by context-free grammars or recognized by pushdown automata.
  - Context-sensitive languages: These are the languages that can be defined by context-sensitive grammars or recognized by linear bounded automata.
  - Recursively enumerable languages: These are the languages that can be defined by Turing machines or generated by recursively enumerable grammars.
- Each type of formal language has its own properties and limitations, and some types are subsets of others.
- For example, regular languages are a subset of context-free languages, which are a subset of context-sensitive languages, which are a subset of recursively enumerable languages.
- Formal languages have many applications in computer science, such as compiler design, natural language processing, cryptography, logic, and verification  .



# Derivation Trees and Ambiguity

- A derivation tree or a parse tree is a graphical representation of the derivation of a string by a context-free grammar (CFG).
- A derivation tree shows how the start symbol of the grammar is transformed into the string by applying the production rules in each step.
- A derivation tree has the following properties:
  - The root node of the tree corresponds to the start symbol of the grammar.
  - The internal nodes of the tree correspond to the variables of the grammar.
  - The leaf nodes of the tree correspond to the terminals of the grammar or the empty string.
  - The order of the children of a node corresponds to the order of the symbols in the right-hand side of the production rule used to replace the node.
- A derivation tree can be either leftmost or rightmost, depending on whether the leftmost or the rightmost non-terminal is replaced at each step.
- A derivation tree can be used to show the syntactic structure and the precedence of the operators in a string generated by a CFG.
- A CFG is said to be ambiguous if there exists more than one derivation tree for the same string  .
- Ambiguity is a property of grammars, not languages. There can be multiple grammars for the same language, where some are ambiguous and some are not.
- Some languages are inherently ambiguous, meaning that there are no unambiguous grammars for them.
- Ambiguity can cause problems in parsing and interpreting the strings of a language, as different derivation trees may imply different meanings or actions.
- Ambiguity can be resolved by using additional rules or conventions to select a unique derivation tree for each string, or by modifying the grammar to eliminate the ambiguity.



# Regular Grammars

- A regular grammar is a type of formal grammar that can generate regular languages, which are the languages that can be accepted by finite automata.
- A regular grammar consists of four components: a finite set of non-terminal symbols, a finite set of terminal symbols, a start symbol, and a finite set of production rules.
- A production rule is a pair of a non-terminal symbol and a string of symbols (either terminal or non-terminal) that can be derived from the non-terminal symbol.
- There are two types of regular grammars: right-regular and left-regular. A right-regular grammar has production rules of the form A -> aB or A -> a, where A and B are non-terminal symbols and a is a terminal symbol. A left-regular grammar has production rules of the form A -> Ba or A -> a, where A and B are non-terminal symbols and a is a terminal symbol.
- A regular grammar is equivalent to a nondeterministic finite automaton (NFA), meaning that for any regular grammar, there exists an NFA that accepts the same language, and vice versa .
- The equivalence between regular grammars and NFAs can be established by a systematic procedure that converts one to the other. For example, given a right-regular grammar, an NFA can be constructed as follows:
  - The states of the NFA are the non-terminal symbols of the grammar, plus one additional state for the empty string.
  - The initial state of the NFA is the start symbol of the grammar.
  - The final state of the NFA is the additional state for the empty string.
  - The transitions of the NFA are based on the production rules of the grammar. For each rule of the form A -> aB, there is a transition from state A to state B with label a. For each rule of the form A -> a, there is a transition from state A to the final state with label a.
- Regular grammars are useful for describing the syntax of simple languages, such as arithmetic expressions, identifiers, keywords, etc. They are also useful for designing lexical analyzers, which are programs that scan the input and divide it into tokens.
- Regular grammars have some limitations, such as not being able to generate languages that require counting, nesting, or recursion. For example, the language of balanced parentheses, which consists of strings of the form (n)^(n), where n is any natural number, is not regular and cannot be generated by a regular grammar.
- Regular grammars are the simplest type of grammars in the Chomsky hierarchy, which is a classification of formal languages based on their generative power. The hierarchy consists of four classes: regular, context-free, context-sensitive, and recursively enumerable. Each class is a proper subset of the next one, meaning that every language that can be generated by a grammar of a lower class can also be generated by a grammar of a higher class, but not the other way around.



# Right Linear and Left Linear Grammars

- A **linear grammar** is a type of context-free grammar in which the right-hand side of each production rule consists of at most one non-terminal symbol and any number of terminal symbols.
- A **right linear grammar** is a linear grammar in which the non-terminal symbol, if any, is at the right end of the right-hand side of each production rule. For example, A -> aB | a | epsilon is a right linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A **left linear grammar** is a linear grammar in which the non-terminal symbol, if any, is at the left end of the right-hand side of each production rule. For example, A -> Ba | a | epsilon is a left linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- Right linear and left linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are precisely the **regular languages** .
- To convert a right linear grammar to a left linear grammar, we can use the following steps :
  - Reverse the right-hand side of each production rule. For example, A -> aB becomes A -> Ba.
  - Replace each non-terminal symbol with a new one. For example, A -> Ba becomes A' -> B'a.
  - Swap the start symbol with the non-terminal that corresponds to the original start symbol. For example, if S is the original start symbol and S' is the new one, then S' -> B'a becomes S -> aB'.
  - Reverse the right-hand side of each production rule again. For example, S -> aB' becomes S -> B'a.
- To convert a left linear grammar to a right linear grammar, we can use the same steps but in reverse order :
  - Reverse the right-hand side of each production rule. For example, A -> Ba becomes A -> aB.
  - Swap the start symbol with the non-terminal that corresponds to the original start symbol. For example, if S is the original start symbol and S' is the new one, then S -> aB becomes S' -> Ba.
  - Replace each non-terminal symbol with a new one. For example, S' -> Ba becomes S' -> B'a.
  - Reverse the right-hand side of each production rule again. For example, S' -> B'a becomes S' -> aB'.



# Conversion of FA into CFG and Regular grammar into FA

## FA to CFG conversion

- A finite automaton (FA) is a model of computation that accepts or rejects strings of symbols.
- A context-free grammar (CFG) is a set of rules that generates strings of symbols.
- A FA can be converted into a CFG that generates the same language as the FA.
- The general idea of the algorithm is as follows :
  - For each state q of the FA, introduce a new variable Q.
  - The variable corresponding to the starting state will be the starting variable of the new CFG.
  - For each transition of the FA q a -> q', add a rule Q -> aQ' to the CFG.
  - For each final state q of the FA, add a rule Q -> epsilon to the CFG, where epsilon is the empty string.

- For example, consider the following FA that accepts strings of a's and b's that end with ab:

FA example

- The corresponding CFG is:

S -> aS | bA | epsilon

A -> aB | bA

B -> bS | epsilon

## Regular grammar to FA conversion

- A regular grammar is a special type of CFG that has rules of the form A -> aB or A -> a, where A and B are variables and a is a terminal symbol.
- A regular grammar can be converted into a FA that recognizes the same language as the grammar.
- The general idea of the algorithm is as follows:
  - For each variable A of the grammar, create a state qA in the FA.
  - The state corresponding to the starting variable will be the initial state of the FA.
  - For each rule A -> aB in the grammar, add a transition qA a -> qB to the FA.
  - For each rule A -> a in the grammar, add a transition qA a -> qF to the FA, where qF is a new final state.
  - If the grammar has a rule S -> epsilon, where S is the starting variable, then make the initial state also a final state.

- For example, consider the following regular grammar that generates strings of a's and b's that end with ab:

S -> aS | bA | epsilon

A -> aB | bA

B -> bS

- The corresponding FA is:

FA example



# Simplification of CFG

- A context-free grammar (CFG) is a set of production rules that generate strings belonging to a language.
- A CFG may contain some redundant or unnecessary productions and symbols that do not affect the language generated by the grammar.
- Simplification of CFGs is the process of removing these productions and symbols to obtain an equivalent grammar that is simpler and more concise.
- Simplification of CFGs consists of the following steps:

  - **Removal of useless productions**: These are the productions that can never take part in the derivation of any string, either because the left-hand side symbol is unreachable from the start symbol, or because the right-hand side symbol can never terminate in a string of terminals. To remove these productions, we first find the set of reachable symbols and the set of terminating symbols, and then eliminate the productions that involve symbols that are not in both sets.
  - **Removal of null productions**: These are the productions of the form A -> ε, where A is a non-terminal and ε is the empty string. To remove these productions, we first find the set of nullable symbols, and then replace each occurrence of a nullable symbol in the right-hand side of a production with ε, and remove the resulting null productions. We also add new productions to preserve the language generated by the grammar.
  - **Removal of unit productions**: These are the productions of the form A -> B, where A and B are non-terminals. To remove these productions, we first find the set of unit pairs, and then replace each unit production with the productions that have the same left-hand side symbol and a non-unit right-hand side symbol. We also remove any duplicate productions that may arise.
  - **Removal of equivalent symbols**: These are the symbols that have the same set of productions, and thus generate the same language. To remove these symbols, we first find the set of equivalent pairs, and then replace each occurrence of an equivalent symbol in the right-hand side of a production with the other symbol in the pair. We also remove any duplicate productions that may arise.



# Normal Forms for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A normal form is a standard way of writing the production rules of a grammar that satisfies certain properties or constraints.
- Normal forms are useful for simplifying the analysis and manipulation of grammars, such as parsing, generating, and proving properties of languages.
- There are different types of normal forms for different types of grammars, such as regular, context-free, context-sensitive, and unrestricted grammars.
- Some of the most common normal forms for context-free grammars are Chomsky normal form and Greibach normal form.

## Chomsky normal form

- A context-free grammar is in Chomsky normal form if all of its production rules are of the form:

  - A → BC, where A, B, and C are nonterminal symbols
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string

- Any context-free grammar can be converted to an equivalent grammar in Chomsky normal form by applying a series of transformations, such as eliminating ε-productions, unit productions, and useless symbols, and introducing new nonterminal symbols.
- Chomsky normal form is useful for designing efficient parsing algorithms, such as the CYK algorithm, which can determine whether a given string belongs to the language of a grammar in Chomsky normal form in polynomial time.

## Greibach normal form

- A context-free grammar is in Greibach normal form if all of its production rules are of the form:

  - A → aα, where A is a nonterminal symbol, a is a terminal symbol, and α is a (possibly empty) string of nonterminal symbols

- Any context-free grammar can be converted to an equivalent grammar in Greibach normal form by applying a series of transformations, such as eliminating left recursion, left factoring, and introducing new nonterminal symbols.
- Greibach normal form is useful for designing recursive-descent parsing algorithms, which can construct a parse tree for a given string by recursively applying the production rules of the grammar.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on Chomsky Normal Form (CNF) for the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages.

# Chomsky Normal Form (CNF)

- Chomsky Normal Form (CNF) is a special form of context-free grammar (CFG) that has only two types of production rules: A -> BC or A -> a, where A, B, and C are non-terminal symbols and a is a terminal symbol.
- Any context-free grammar can be converted into an equivalent CNF grammar that generates the same language.
- CNF is useful for simplifying the parsing algorithms for context-free languages, such as the CYK algorithm, which runs in polynomial time for CNF grammars.
- The conversion of a CFG to a CNF grammar involves the following steps:

  1. Eliminate the start symbol from the right-hand side of any production rule, by introducing a new start symbol S0 and adding the rule S0 -> S, where S is the original start symbol.
  2. Eliminate the epsilon rules, i.e., the rules of the form A -> epsilon, where epsilon is the empty string, by replacing each occurrence of A in the right-hand side of any rule with an optional A, i.e., A | epsilon.
  3. Eliminate the unit rules, i.e., the rules of the form A -> B, where A and B are non-terminal symbols, by replacing each occurrence of A in the right-hand side of any rule with the right-hand side of B, and repeating this process until no unit rules are left.
  4. Eliminate the terminal symbols from the right-hand side of any rule that has more than one symbol, by introducing new non-terminal symbols for each terminal symbol and adding the corresponding rules. For example, if there is a rule A -> aB, then introduce a new non-terminal symbol Xa and add the rules A -> XaB and Xa -> a.
  5. Eliminate the non-terminal symbols from the right-hand side of any rule that has more than two symbols, by introducing new non-terminal symbols for each pair of consecutive symbols and adding the corresponding rules. For example, if there is a rule A -> BCD, then introduce a new non-terminal symbol Y and add the rules A -> BY and Y -> CD.

- Here is an example of converting a CFG to a CNF grammar:

  - The original CFG is:

    ```
    S -> ASA | aB
    A -> B | S
    B -> b | epsilon
    ```

  - The CNF grammar is:

    ```
    S0 -> S
    S -> AS1 | XB
    S1 -> SA
    A -> B | S
    B -> b
    X -> a
    ```



# Greibach Normal Form (GNF)

- Greibach Normal Form (GNF) is a special form of context-free grammar (CFG) that has some restrictions on the right-hand side of the production rules.
- A CFG is in GNF if and only if all of its production rules are of the form: `A → aA1A2...An`, where `A, A1, A2, ..., An` are non-terminal symbols and `a` is a terminal symbol .
- GNF is useful for parsing algorithms, such as the top-down parsing algorithm, that require the first symbol of the right-hand side to be a terminal .
- GNF can also be used to prove that every context-free language can be accepted by a pushdown automaton.
- Every CFG can be converted to an equivalent GNF using a systematic algorithm . The algorithm consists of the following steps:
  - Step 1: If the start symbol `S` occurs on some right side, create a new start symbol `S'` and a new production `S' → S`.
  - Step 2: Remove null productions (productions of the form `A → ε`, where `ε` is the empty word) using the null production removal algorithm.
  - Step 3: Remove unit productions (productions of the form `A → B`, where `A` and `B` are non-terminal symbols) using the unit production removal algorithm.
  - Step 4: Eliminate terminals that are not at the beginning of the right-hand side using the following procedure:
    - For each production of the form `A → u1u2...un`, where `ui` is either a terminal or a non-terminal symbol, do the following:
      - If `u1` is a terminal, then leave the production unchanged.
      - If `u1` is a non-terminal, say `B`, then replace the production with `A → v1Av2...Avn`, where `v1, v2, ..., vn` are the first symbols of the right-hand sides of the productions for `B`.
  - Step 5: Eliminate non-terminals that are not at the end of the right-hand side using the following procedure:
    - For each production of the form `A → aB1B2...Bn`, where `a` is a terminal and `Bi` are non-terminal symbols, do the following:
      - If `n = 0` or `n = 1`, then leave the production unchanged.
      - If `n > 1`, then replace the production with `A → aB1C`, where `C` is a new non-terminal symbol, and add a new production `C → B2B3...Bn`.
- The algorithm terminates when no more changes can be made to the grammar, and the resulting grammar is in GNF.



# Chomsky Hierarchy

- The Chomsky hierarchy is a containment hierarchy of classes of formal grammars, as described by Noam Chomsky in 1956  .
- It is an essential tool used in formal language theory, computer science, and linguistics.
- This unique structure can be represented in the form of a pyramid, with type 0 at the base and type 3 at the peak.
- The following table summarizes each of Chomsky's four types of grammars, the class of language it generates, the type of automaton that recognizes it, and the form its rules must have .

| Type | Grammar | Language | Automaton | Rule Form |
| --- | --- | --- | --- | --- |
| 0 | Unrestricted | Recursively enumerable | Turing machine | α → β |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automaton | αAβ → αγβ |
| 2 | Context-free | Context-free | Pushdown automaton | A → γ |
| 3 | Regular | Regular | Finite automaton | A → aB |
|  |  |  |  | A → a |

- The Chomsky hierarchy shows that the classes of languages are nested in each other, meaning that every regular language is also context-free, every context-free language is also context-sensitive, and every context-sensitive language is also recursively enumerable .
- However, the converse is not true, meaning that there are languages that are not regular but context-free, not context-free but context-sensitive, and not context-sensitive but recursively enumerable .
- The Chomsky hierarchy also shows that the classes of grammars are not equivalent to the classes of automata, meaning that there are grammars that generate languages that cannot be recognized by any automaton, and there are automata that recognize languages that cannot be generated by any grammar .
- The Chomsky hierarchy is useful for studying the properties and limitations of different types of grammars, languages, and automata, and for designing efficient algorithms and systems for natural language processing .



# Programming problems based on the properties of CFGs

- A context-free grammar (CFG) is a set of rules that defines a language by specifying how to generate strings from a set of symbols.
- A CFG consists of four components: a set of terminals, a set of non-terminals, a start symbol, and a set of productions.
- A terminal is a symbol that appears in the strings of the language. A non-terminal is a symbol that represents a group of strings. A start symbol is a special non-terminal that represents the whole language. A production is a rule that specifies how to replace a non-terminal with a sequence of terminals and non-terminals.
- A CFG can generate a string by starting from the start symbol and applying productions repeatedly until only terminals are left. The sequence of productions used to generate a string is called a derivation. A language is context-free if it can be generated by some CFG.
- Some properties of CFGs are:

  - CFGs are closed under union, concatenation, and Kleene star operations. That is, if L1 and L2 are context-free languages, then so are L1 ∪ L2, L1L2, and L1*.
  - CFGs are not closed under intersection, complement, and set difference operations. That is, if L1 and L2 are context-free languages, then L1 ∩ L2, L1', and L1 - L2 may not be context-free.
  - CFGs can be converted into equivalent normal forms, such as Chomsky normal form (CNF) and Greibach normal form (GNF). A CFG is in CNF if every production is of the form A → BC or A → a, where A, B, and C are non-terminals and a is a terminal. A CFG is in GNF if every production is of the form A → aα, where A is a non-terminal, a is a terminal, and α is a sequence of non-terminals.
  - CFGs can be simplified by removing useless symbols, null productions, unit productions, and left recursion. A useless symbol is a non-terminal that does not appear in any derivation of a terminal string. A null production is a production of the form A → ε, where ε is the empty string. A unit production is a production of the form A → B, where A and B are non-terminals. Left recursion is a situation where a non-terminal A can derive a string that begins with A.
  - CFGs can be used to model the syntax of natural and programming languages. A parser is a program that takes a string and determines if it belongs to a context-free language, and if so, how it was derived by a CFG. A parser can be used to check the validity and structure of a program, and to translate it into an intermediate or executable form.

- Some programming problems based on the properties of CFGs are:

  - Given a CFG and a string, determine if the string belongs to the language generated by the CFG, and if so, find a derivation for it. This can be done by using a top-down or a bottom-up parsing algorithm, such as recursive descent, LL, LR, or LALR.
  - Given a CFG, convert it into an equivalent CFG in CNF or GNF. This can be done by applying a series of transformations, such as eliminating null and unit productions, introducing new non-terminals, and rearranging the right-hand sides of the productions.
  - Given a CFG, simplify it by removing useless symbols, null productions, unit productions, and left recursion. This can be done by using algorithms that identify and eliminate these elements from the grammar.
  - Given a CFG, determine if it is ambiguous or not. A CFG is ambiguous if there exists a string that can be derived in more than one way by the CFG. This can be done by using a technique called CYK algorithm, which constructs a table that shows all the possible ways to derive a string by the CFG.
  - Given a CFG, find its equivalent regular expression. A regular expression is a compact way of representing a regular language, which is a subset of context-free languages. This can be done by using a technique called state elimination, which converts the CFG into a finite automaton, and then eliminates the states one by one, replacing them with regular expressions.



# Unit 4 - Push Down Automata and Properties of Context Free Languages

- A **push down automaton (PDA)** is a finite automaton with an additional memory component called a **stack**.
- A stack is a data structure that allows only two operations: **push** (adding an element to the top) and **pop** (removing an element from the top).
- A PDA can use the stack to store and retrieve information that is needed to process the input string.
- A PDA can be either **deterministic** (DPDA) or **nondeterministic** (NPDA), depending on whether it has a unique next move for any given configuration.
- A **configuration** of a PDA consists of three components: the current state, the remaining input string, and the current stack content.
- A PDA can change its configuration by reading an input symbol, changing its state, and performing a stack operation (push, pop, or do nothing).
- A PDA accepts an input string if it reaches a **final state** with an empty stack or with a special symbol at the top of the stack.
- A **context free language (CFL)** is a language that can be generated by a **context free grammar (CFG)**.
- A CFG consists of a set of **variables**, a set of **terminals**, a **start variable**, and a set of **production rules**.
- A production rule has the form A -> α, where A is a variable and α is a string of variables and terminals.
- A CFG generates a string by starting from the start variable and applying production rules until only terminals are left.
- A CFL is the set of all strings that can be generated by a CFG.
- The relation between PDAs and CFLs is that a language is context free if and only if it is accepted by a PDA.
- Deterministic PDAs can recognize all deterministic CFLs, while nondeterministic PDAs can recognize all CFLs.
- Some properties of CFLs are:
  - CFLs are closed under union, concatenation, and Kleene star operations.
  - CFLs are not closed under intersection, complement, and set difference operations.
  - CFLs can be decided by algorithms that check whether a given string belongs to a CFL, whether a given CFG is empty, finite, or ambiguous, and whether two given CFGs are equivalent.
  - CFLs can be pumped by a lemma that states that any sufficiently long string in a CFL can be divided into five parts such that some of the parts can be repeated any number of times and the resulting string still belongs to the CFL.



# Nondeterministic Pushdown Automata (NPDA)

- A nondeterministic pushdown automaton (NPDA), or just pushdown automaton (PDA), is a variation of the nondeterministic finite automaton (NFA) that can use a stack as an auxiliary memory  .
- A stack is a data structure that allows only two operations: push (adding an element to the top) and pop (removing an element from the top).
- A NPDA can push and pop symbols from the stack during the transitions, and use the top symbol of the stack as an additional input.
- A NPDA can also make nondeterministic choices, meaning that it can have multiple possible transitions from a given configuration (state, input, and stack).
- A NPDA is formally defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite stack alphabet
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × (Γ ∪ {ε}) to a finite subset of Q × (Γ ∪ {ε})
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final or accepting states
- A NPDA accepts an input string w if there exists a sequence of transitions that leads from the initial configuration (q0, w, Z0) to a final configuration (qf, ε, α), where qf ∈ F and α ∈ Γ*.
- The language accepted by a NPDA is called a context-free language (CFL), and it is a proper subset of the recursively enumerable languages (REL).
- A NPDA can be represented by a state diagram, where each transition is labeled by an input symbol, a stack symbol to be popped, and a stack symbol to be pushed (separated by commas).
- A NPDA can also be simulated by a nondeterministic Turing machine (NTM) with a single tape, where the left end of the tape is used as the stack and the right end of the tape is used as the input.



# Definition for the notes of the Unit 4 - Push Down Automata and Properties of Context Free Languages in the subject of Theory of Automata and Formal Languages

- A **pushdown automaton (PDA)** is a type of automaton that employs a **stack** as an auxiliary memory .
- A stack is a data structure that allows operations of **push** (adding a symbol to the top) and **pop** (removing a symbol from the top).
- A PDA can read a given input string from left to right and manipulate the stack as part of performing a transition .
- A PDA can be defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where :
  - Q is a finite set of states
  - Σ is an alphabet of input symbols
  - Γ is an alphabet of stack symbols
  - δ is a transition function that maps Q × Σε × Γε to a finite subset of Q × Γε, where ε denotes the empty string
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final or accepting states
- A PDA can recognize **context-free languages (CFLs)**, which are languages that can be generated by a **context-free grammar (CFG)** .
- A CFG is a 4-tuple (V, Σ, R, S), where :
  - V is a finite set of variables or non-terminals
  - Σ is a finite set of terminals, disjoint from V
  - R is a finite set of rules or productions, each of the form A → α, where A ∈ V and α ∈ (V ∪ Σ)*
  - S is the start variable
- A CFG can generate a string by applying the rules recursively, starting from the start variable, until no more variables are left .
- A string is in the language of a CFG if it can be generated by the CFG .
- A language is context-free if there exists a CFG that generates it .
- CFLs have some properties that can be used to prove or disprove their context-freeness, such as :
  - Closure under union, concatenation, and Kleene star
  - Non-closure under intersection, complement, and set difference
  - Decidability of emptiness, finiteness, membership, and equivalence
  - Undecidability of ambiguity, containment, and minimality
  - Existence of normal forms, such as Chomsky normal form and Greibach normal form
  - Existence of pumping lemma, which states that any sufficiently long string in a CFL can be pumped or repeated without leaving the language



# Moves for the notes of the Unit 4 - Push Down Automata and Properties of Context Free Languages in the subject of Theory of Automata and Formal Languages

- A **push down automaton (PDA)** is a finite automaton with an additional memory component called a **stack**.
- A PDA can perform three operations on the stack: **push**, **pop**, and **read**.
- A PDA can be either **deterministic (DPDA)** or **nondeterministic (NPDA)**, depending on whether it has a unique transition for each input symbol and stack symbol or not.
- A **context free language (CFL)** is a language that can be generated by a **context free grammar (CFG)**, which is a set of production rules that describe how to form strings from a set of terminal and nonterminal symbols.
- A CFL can be accepted by a PDA using two methods: **acceptance by final state** or **acceptance by empty stack**.
- A DPDA can recognize all **deterministic context free languages (DCFL)**, which are a subset of CFLs that have a unique leftmost derivation for each string.
- An NPDA can recognize all CFLs, which are more expressive than DCFLs.
- Some properties of CFLs are:
  - CFLs are closed under union, concatenation, and Kleene star operations.
  - CFLs are not closed under intersection, complement, and set difference operations.
  - CFLs are decidable, meaning that there is an algorithm that can determine whether a given string belongs to a CFL or not.
  - CFLs are not enumerable, meaning that there is no algorithm that can list all the strings in a CFL in a systematic order.
  - CFLs have the pumping lemma, which is a necessary condition for a language to be context free. It states that for any sufficiently long string in a CFL, there exists a way to divide it into five parts such that repeating the middle two parts any number of times produces another string in the same CFL.



# A Language Accepted by NPDA

- A language is accepted by a non-deterministic pushdown automaton (NPDA) if there exists a sequence of transitions that leads the NPDA from the initial configuration to a final configuration for any input string in the language.
- A NPDA can accept any context-free language (CFL), but not all CFLs can be accepted by a deterministic pushdown automaton (DPDA).
- A NPDA can have multiple moves for a given input symbol and the current state, and it can also have moves without consuming any input symbol (called epsilon or lambda transitions).
- A NPDA can use the stack to store and retrieve symbols that can help it to recognize the structure of the input string.
- A NPDA can have multiple final states, or it can also accept by empty stack, or both.

## Example of a language accepted by NPDA

- Consider the language L = {a<sup>2n</sup>b<sup>n</sup> : n ≥ 0}, which consists of strings of a's followed by an equal number of b's.
- A NPDA that accepts this language is shown below:

NPDA for L

- The NPDA starts in the initial state q<sub>0</sub> with the stack symbol z. When it reads the first symbol a, it pushes two 1's on the stack (δ (q<sub>0</sub>, a, z) = { (q<sub>1</sub>, 11z)}).
- When it reads the second symbol a, it pushes two more 1's on the stack (δ (q<sub>1</sub>, a, 1) = { (q<sub>1</sub>, 111)}).
- When it reads the first symbol b, it pops one 1 from the stack (δ (q<sub>1</sub>, b, 1) = { (q<sub>1</sub>, λ)}).
- When it reads the second symbol b, it pops another 1 from the stack (δ (q<sub>1</sub>, b, 1) = { (q<sub>1</sub>, λ)}).
- When the stack becomes empty (i.e., when all the a's have been paired with b's), the NPDA transitions to the final state q<sub>f</sub> (δ (q<sub>1</sub>, λ, z) = { (q<sub>f</sub>, z)}).
- Therefore, the NPDA accepts the input string aabb by reaching a final state.



# Deterministic Pushdown Automata (DPDA)

- A deterministic pushdown automaton (DPDA) is a variation of the pushdown automaton (PDA) that accepts the deterministic context-free languages (DCFL), a proper subset of context-free languages (CFL) .
- A DPDA has a single computation from the initial configuration until an accepting one for all strings belonging to the language it accepts .
- A DPDA can be defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z, F) where :
  - Q is the set of states
  - Σ is the set of input symbols
  - Γ is the set of pushdown symbols (which can be pushed and popped from the stack)
  - δ is the transition function that maps Q × (Σ ∪ {ε}) × Γ to Q × Γ*
  - q0 is the initial state
  - Z is the initial pushdown symbol (which is initially present in the stack)
  - F is the set of final states
- A DPDA is different from a PDA in that the transition function δ is a function and not a relation, meaning that for each state, input symbol and stack symbol, there is at most one possible transition .
- A DPDA can accept a language by two modes: final state and empty stack. In the final state mode, the DPDA accepts a string if it reaches a final state after reading the entire input. In the empty stack mode, the DPDA accepts a string if it empties the stack after reading the entire input .
- A DPDA can simulate a deterministic finite automaton (DFA) by using an empty stack and a single state. However, a DPDA cannot simulate a nondeterministic finite automaton (NFA) or a nondeterministic pushdown automaton (NPDA) in general, as there are some CFLs that are not DCFLs .
- Some examples of DCFLs that can be accepted by DPDAs are:
  - The language of balanced parentheses: {w ∈ { (, ) }* | w is well-formed}
  - The language of palindromes over a binary alphabet: {w ∈ {0, 1}* | w = wR}
  - The language of arithmetic expressions with matching parentheses: {w ∈ { (, ), +, -, *, /, a, b, c }* | w is a valid expression}



# Deterministic Context Free Languages (DCFL)

- Deterministic context free languages (DCFL) are a proper subset of context free languages (CFL).
- They are the context free languages that can be accepted by a deterministic pushdown automaton (DPDA).
- A DPDA is a pushdown automaton (PDA) that has at most one transition for each combination of input symbol, current state, and top stack symbol.
- DCFLs are always unambiguous, meaning that they admit an unambiguous grammar. An unambiguous grammar is a grammar that generates only one parse tree for each string in the language.
- DCFLs have some properties that make them easier to process than general CFLs. For example:
  - DCFLs can be recognized by a deterministic Turing machine in polynomial time and O(log2 n) space.
  - DCFLs are closed under the following operations: union, intersection with a regular language, concatenation, Kleene star, reversal, and complement.
  - DCFLs have a unique minimal DPDA for each language, up to state renaming.
  - DCFLs can be parsed in linear time using a variant of the LR parsing algorithm.
- Some examples of DCFLs are:
  - The set of all palindromes over a finite alphabet.
  - The set of all strings of balanced parentheses.
  - The set of all strings of the form a^n b^n, where n is a positive integer.
  - The set of all strings of the form a^n b^m c^n, where n and m are positive integers.



# Pushdown Automata for Context Free Languages

- A **pushdown automaton** (PDA) is a finite automaton with an additional component called a **stack**, which is a data structure that allows operations of pushing (adding) and popping (removing) symbols at one end .
- A PDA can use the stack to store and retrieve information that is needed to process the input symbols. The stack can also be used to keep track of the structure of the input, such as matching parentheses or brackets .
- A PDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of stack symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ to a finite subset of Q × Γ*
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final states
- A PDA can operate in two modes: **acceptance by final state** or **acceptance by empty stack**. In the former, the PDA accepts an input if it reaches a final state after reading the entire input. In the latter, the PDA accepts an input if it empties the stack after reading the entire input .
- A PDA can also be **deterministic** or **nondeterministic**. A deterministic PDA (DPDA) has at most one possible move for any given configuration, while a nondeterministic PDA (NPDA) can have multiple possible moves for any given configuration .
- A **context-free language** (CFL) is a language that can be generated by a **context-free grammar** (CFG), which is a set of production rules that describe how to form strings from a set of terminal and nonterminal symbols .
- A CFL can also be characterized by a PDA, that is, a language is context-free if and only if there exists a PDA that accepts it  .
- The set of all CFLs is identical to the set of languages accepted by NPDA, and the set of regular languages is a subset of CFLs .
- A PDA can be used to parse a CFL by simulating the derivation of the input string from the start symbol of the CFG. The PDA pushes the start symbol onto the stack, and then repeatedly pops the top symbol of the stack and replaces it with the right-hand side of a production rule that matches the input symbol. If the PDA reaches the end of the input and the stack is empty, the input is accepted .
- A PDA can also be converted to a CFG by using a technique called the **state elimination method**, which involves introducing new nonterminal symbols that represent the possible configurations of the PDA, and then eliminating the states one by one until only the start and final states remain .



# Context Free Grammars for Pushdown Automata

- A **context-free grammar (CFG)** is a set of rewriting rules that can be used to generate or reproduce patterns/strings recursively.
- A **pushdown automaton (PDA)** is a finite-state machine with an additional stack memory that can store and retrieve symbols.
- A **context-free language (CFL)** is a language that can be generated by a CFG or accepted by a PDA.
- There is an equivalence between CFGs and PDAs, meaning that for every CFG there is a PDA that accepts the same language, and vice versa .
- The equivalence can be shown by two constructions: one that converts a CFG to a PDA, and another that converts a PDA to a CFG .

## CFG to PDA

- The idea of this construction is to simulate the derivation process of a CFG using the stack of the PDA .
- The PDA has only one state and two transitions: one for reading an input symbol and matching it with the top of the stack, and another for replacing the top of the stack with the right-hand side of a production rule .
- The PDA starts with the start symbol of the CFG on the stack, and accepts by empty stack when the input is exhausted and the stack is empty .
- Formally, given a CFG G = (V, Σ, R, S), where V is the set of variables, Σ is the set of terminals, R is the set of rules, and S is the start symbol, we can construct a PDA M = (Q, Σ, Γ, δ, q0, Z0, F), where Q = {q0} is the single state, Γ = V ∪ Σ is the stack alphabet, Z0 = S is the initial stack symbol, F = ∅ is the empty set of final states, and δ is the transition function defined as follows :

  - For every terminal symbol a ∈ Σ, δ(q0, a, a) = {(q0, ε)}, where ε is the empty string.
  - For every rule A → α ∈ R, where A ∈ V and α ∈ (V ∪ Σ)*, δ(q0, ε, A) = {(q0, α)}.

## PDA to CFG

- The idea of this construction is to generate a CFG that captures all the possible configurations and transitions of the PDA .
- The CFG has four types of variables: one for the start symbol, one for each state and stack symbol pair, one for each state pair, and one for each terminal symbol .
- The CFG has four types of rules: one for the initial configuration, one for the final configuration, one for the stack operations, and one for the input symbols .
- Formally, given a PDA M = (Q, Σ, Γ, δ, q0, Z0, F), where Q is the set of states, Σ is the input alphabet, Γ is the stack alphabet, δ is the transition function, q0 is the initial state, Z0 is the initial stack symbol, and F is the set of final states, we can construct a CFG G = (V, Σ, R, S), where V is the set of variables, Σ is the set of terminals, R is the set of rules, and S is the start symbol, as follows :

  - V = {S} ∪ {[qXp] | q, p ∈ Q, X ∈ Γ} ∪ {<qp> | q, p ∈ Q} ∪ {a | a ∈ Σ}.
  - S is the start symbol.
  - For every p ∈ F, R contains the rule S → [q0Z0p].
  - For every q, p, r ∈ Q, X, Y ∈ Γ, and a, b ∈ Σ ∪ {ε}, if δ(q, a, X) contains (r, Yb), then R contains the rule [qXp] → a[rYp]b.
  - For every q, p, r, s ∈ Q and X ∈



# Two stack Pushdown Automata

- A pushdown automaton (PDA) is a finite state machine that has an additional component called a stack, which can store and retrieve symbols according to the last-in first-out (LIFO) principle.
- A PDA can use the top of the stack to decide which transition to take, and it can manipulate the stack as part of performing a transition.
- A PDA with one stack can accept languages that are context-free, but not all recursively enumerable languages.
- A PDA with two stacks has the same computation power as a Turing machine, which can accept all recursively enumerable languages  .
- A two stack PDA is similar to a one stack PDA, but it has two stacks instead of one. In each transition, we must specify which stack to push or pop, or whether to leave both stacks unchanged.
- A two stack PDA can simulate a Turing machine by using one stack as the left part of the tape, and the other stack as the right part of the tape. The head of the Turing machine can be represented by the top symbols of the two stacks.
- A two stack PDA can also accept languages that are not context-free, such as $a^n b^n c^n$, by using one stack to match the $a$s and $b$s, and the other stack to match the $b$s and $c$s.



# Pumping Lemma for CFL

The pumping lemma for context-free languages (CFLs) is a tool to prove that a given language is not context-free. It states that if a language is context-free, then there exists a constant n (called the pumping length) such that any string w in the language of length at least n can be written as w = uvxyz, where:

- |vxy| ≤ n
- |vy| ≥ 1
- uv^nxy^nz is in the language for all n ≥ 0

The intuition behind the pumping lemma is that any sufficiently long string in a context-free language can be generated by a derivation tree that has a repeated variable along some path. This means that we can pump (repeat or remove) the substring corresponding to that variable and still get a string in the language.

To use the pumping lemma to show that a language is not context-free, we assume that it is context-free and derive a contradiction. We do this by choosing a string w in the language that is longer than the pumping length n, and showing that for any possible decomposition of w into uvxyz, there exists a value of n such that uv^nxy^nz is not in the language. This contradicts the pumping lemma and proves that the language is not context-free.

For example, consider the language L = {a^nb^nc^n | n ≥ 1}. To show that L is not context-free, we assume that it is and let n be the pumping length. We choose w = a^n b^n c^n, which is in L and has length 3n > n. Now, we consider any possible decomposition of w into uvxyz, where |vxy| ≤ n and |vy| ≥ 1. There are three cases:

- Case 1: vxy contains only one type of symbol, say a. Then, pumping v and y will change the number of a's in w, but not the number of b's or c's. This will result in a string that is not in L, since it does not have the form a^nb^nc^n.
- Case 2: vxy contains two types of symbols, say a and b. Then, pumping v and y will change the number of a's and b's in w, but not the number of c's. This will also result in a string that is not in L, since it does not have the form a^nb^nc^n.
- Case 3: vxy contains three types of symbols, say a, b and c. Then, pumping v and y will change the number of a's, b's and c's in w, but not in the same proportion. This will also result in a string that is not in L, since it does not have the form a^nb^nc^n.

In all cases, we have shown that there exists a value of n such that uv^nxy^nz is not in L, which contradicts the pumping lemma. Therefore, L is not context-free.



# Closure properties of CFL

- A language class is said to be closed under an operation if applying that operation on languages in the class results in a language that is also in the class.
- Context-free languages (CFL) are a class of languages that can be generated by context-free grammars (CFG).
- Some of the closure properties of CFL are:

  - **Union**: CFL are closed under union, which means that if L1 and L2 are CFL, then L1 ∪ L2 is also a CFL. This can be proved by constructing a CFG for L1 ∪ L2 using the CFGs for L1 and L2.
  - **Concatenation**: CFL are closed under concatenation, which means that if L1 and L2 are CFL, then L1 L2 is also a CFL. This can be proved by constructing a CFG for L1 L2 using the CFGs for L1 and L2.
  - **Kleene closure**: CFL are closed under Kleene closure, which means that if L is a CFL, then L* is also a CFL. This can be proved by constructing a CFG for L* using the CFG for L.
  - **Reversal**: CFL are closed under reversal, which means that if L is a CFL, then LR (the language obtained by reversing the strings in L) is also a CFL. This can be proved by constructing a CFG for LR using the CFG for L.
  - **Homomorphism**: CFL are closed under homomorphism, which means that if L is a CFL and h is a homomorphism (a function that maps each symbol in the alphabet to a string), then h(L) (the language obtained by applying h to each string in L) is also a CFL. This can be proved by constructing a CFG for h(L) using the CFG for L and the definition of h.
  - **Inverse homomorphism**: CFL are closed under inverse homomorphism, which means that if L is a CFL and h is a homomorphism, then h-1(L) (the language obtained by applying the inverse of h to each string in L) is also a CFL. This can be proved by constructing a CFG for h-1(L) using the CFG for L and the definition of h.

- Some of the non-closure properties of CFL are:

  - **Intersection**: CFL are not closed under intersection, which means that there exist CFL L1 and L2 such that L1 ∩ L2 is not a CFL. A counterexample is L1 = {an bn | n ≥ 0} and L2 = {an bn cn | n ≥ 0}, which are both CFL, but L1 ∩ L2 = {an bn cn | n ≥ 0}, which is not a CFL.
  - **Difference**: CFL are not closed under difference, which means that there exist CFL L1 and L2 such that L1 - L2 is not a CFL. A counterexample is L1 = {an bn cn | n ≥ 0} and L2 = {an bn | n ≥ 0}, which are both CFL, but L1 - L2 = {an bn cn | n > 0}, which is not a CFL.
  - **Complement**: CFL are not closed under complement, which means that there exists a CFL L such that Lc (the language containing all strings over the alphabet that are not in L) is not a CFL. A counterexample is L = {an bn | n ≥ 0}, which is a CFL, but Lc = {w | w is not of the form an bn for some n ≥ 0}, which is not a CFL.



# Decision Problems of CFL

- Decision problems are problems that ask whether a given statement is true or false, and can be solved by an algorithm that always terminates with a yes or no answer.
- Decision problems for CFLs are problems that involve context-free languages (CFLs) and context-free grammars (CFGs), such as:
  - Membership problem: Given a CFG G and a string w, decide if w belongs to L(G), the language generated by G.
  - Emptiness problem: Given a CFG G, decide if L(G) is empty, i.e., if G generates no strings at all.
  - Finiteness problem: Given a CFG G, decide if L(G) is finite, i.e., if G generates only a finite number of strings.
  - Equivalence problem: Given two CFGs G1 and G2, decide if L(G1) = L(G2), i.e., if they generate the same language.
  - Containment problem: Given two CFGs G1 and G2, decide if L(G1) is a subset of L(G2), i.e., if every string generated by G1 is also generated by G2.
  - Disjointness problem: Given two CFGs G1 and G2, decide if L(G1) and L(G2) are disjoint, i.e., if they have no strings in common.
- Some of these decision problems are decidable, meaning that there exists an algorithm that can solve them in finite time for any input. For example, the membership problem can be solved by using a pushdown automaton (PDA) that simulates the CFG and accepts the input string if it can be derived from the start symbol. The emptiness problem can be solved by using a bottom-up search that eliminates all the useless symbols from the CFG and checks if the start symbol is among them. The finiteness problem can be solved by using a pumping lemma for CFLs that shows that if a CFL is infinite, then it must contain a string that can be pumped to produce infinitely many strings.
- Some of these decision problems are undecidable, meaning that there is no algorithm that can solve them in finite time for any input. For example, the equivalence problem is undecidable, because it would imply that CFLs are closed under complement, which is a contradiction. The containment problem and the disjointness problem are also undecidable, because they can be reduced to the equivalence problem by using De Morgan's laws and the fact that CFLs are closed under union.



# Programming problems based on the properties of CFLs

- A context-free language (CFL) is a language generated by a context-free grammar (CFG) or accepted by a pushdown automaton (PDA).
- CFLs have many applications in programming languages, especially in parsing arithmetic expressions and nested structures.
- CFLs have some decidable and undecidable problems, which means that there are algorithms to answer some questions about them, but not all.
- Some of the decidable problems for CFLs are:
  - Membership problem: Given a CFL L and a string w, is w in L?
  - Emptiness problem: Given a CFL L, is L empty?
  - Finiteness problem: Given a CFL L, is L finite?
  - Equivalence problem: Given two CFLs L1 and L2, are they equal?
  - Subset problem: Given two CFLs L1 and L2, is L1 a subset of L2?
- Some of the undecidable problems for CFLs are:
  - Ambiguity problem: Given a CFL L, is it ambiguous?
  - Minimality problem: Given a CFL L, is there a smaller CFG that generates L?
  - Intersection problem: Given two CFLs L1 and L2, is their intersection empty?
  - Complement problem: Given a CFL L, is its complement a CFL?
  - Union problem: Given two CFLs L1 and L2, is their union a CFL?
- CFLs have some closure properties, which means that applying some operations on them results in another CFL. Some of the closure properties for CFLs are:
  - Closure under concatenation: If L1 and L2 are CFLs, then L1L2 is also a CFL.
  - Closure under Kleene star: If L is a CFL, then L* is also a CFL.
  - Closure under reversal: If L is a CFL, then LR is also a CFL, where LR is the set of strings obtained by reversing the strings in L.
  - Closure under homomorphism: If L is a CFL and h is a homomorphism, then h(L) is also a CFL, where h(L) is the set of strings obtained by applying h to each symbol in L.
  - Closure under inverse homomorphism: If L is a CFL and h is a homomorphism, then h-1(L) is also a CFL, where h-1(L) is the set of strings that map to L under h.
- CFLs have some non-closure properties, which means that applying some operations on them may not result in another CFL. Some of the non-closure properties for CFLs are:
  - Non-closure under intersection: If L1 and L2 are CFLs, then L1 ∩ L2 may not be a CFL.
  - Non-closure under complement: If L is a CFL, then Lc may not be a CFL, where Lc is the set of strings that are not in L.
  - Non-closure under set difference: If L1 and L2 are CFLs, then L1 - L2 may not be a CFL, where L1 - L2 is the set of strings that are in L1 but not in L2.



# Unit 5 - Turing Machines and Recursive Function Theory

- A **Turing machine** is a simple abstract computational device that can simulate any algorithm.
- A Turing machine consists of a finite set of states, a finite alphabet of symbols, a tape divided into cells, and a read-write head that can move along the tape and change the symbols on it .
- A Turing machine can be in one of the states at any time, and it can change its state according to a transition function that depends on the current state and the symbol read by the head .
- A Turing machine can accept, reject, or loop on an input string by reaching a special state or never halting .
- A Turing machine can be used to accept **recursive enumerable languages** (generated by Type-0 Grammar), which are the languages that can be enumerated by some algorithm.
- A Turing machine can also be used to compute **recursive functions**, which are the functions from natural numbers to natural numbers that can be computed by some algorithm.
- The theory of Turing machines and the theory of recursive functions are equivalent, and they are part of the theory of **computability**, which investigates the extent and limitations of what can be computed .
- Some important results in computability theory are:
  - The **Church-Turing thesis**, which states that any function that can be computed by an effective method can be computed by a Turing machine.
  - The **halting problem**, which states that there is no algorithm that can decide whether a given Turing machine halts on a given input.
  - The **recursion theorem**, which states that any Turing machine can obtain its own description as an input.
  - The **Rice's theorem**, which states that any non-trivial property of the languages accepted by Turing machines is undecidable.



# Basic Turing Machine Model

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It was invented by Alan Turing in 1936 to study the limits of computability.

A basic Turing machine consists of the following components :

- An **infinite tape** divided into cells, each cell containing a symbol from a finite alphabet. The tape serves as the input, output and memory of the machine.
- A **tape head** that can read and write symbols on the tape, and move one cell to the left or right at a time.
- A **finite state control** that stores the current state of the machine, and determines the next action based on the current state and the symbol read by the tape head.
- A **transition function** that specifies the rules for changing the state, writing a symbol and moving the tape head, given the current state and symbol.
- A **start state** that indicates the initial state of the machine before any computation.
- A **halt state** that indicates the termination of the computation.

A Turing machine operates as follows :

- The input string is placed on the tape, starting from the leftmost cell, and the rest of the tape is filled with a blank symbol.
- The tape head is positioned on the leftmost cell of the input, and the state control is set to the start state.
- The machine reads the symbol under the tape head, and consults the transition function to determine the next state, the symbol to write, and the direction to move the tape head.
- The machine updates the tape, the state control and the tape head according to the transition function.
- The machine repeats steps 3 and 4 until it reaches the halt state, or until it encounters an undefined transition.
- The output of the machine is the string on the tape after the computation ends, or the fact that the machine does not halt.

The following diagram illustrates a basic Turing machine model:

A basic Turing machine model

: https://www.tutorialspoint.com/automata_theory/turing_machine_introduction.htm
: https://www.javatpoint.com/automata-basic-model-of-turing-machine
: https://en.wikipedia.org/wiki/Turing_machine
: https://plato.stanford.edu/entries/turing-machine/
: https://www.britannica.com/technology/Turing-machine



# Representation of Turing Machines

- A Turing machine is a mathematical model of computation describing an abstract machine that manipulates symbols on a strip of tape according to a table of rules.
- A Turing machine can be specified by a five-tuple (Q, Σ, Γ, δ, q0), where
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of tape symbols, such that Σ ⊆ Γ and a special blank symbol ∈ Γ
  - δ is a transition function that maps Q × Γ to Q × Γ × {L, R}, where L and R denote left and right movements of the tape head
  - q0 is the initial state
- A Turing machine can be represented visually by state diagrams or machine tables.
- A state diagram is composed of state cells connected by arrows. Each state cell represents a state of the machine, and each arrow represents an instruction. The arrow is labeled with the current symbol, the new symbol, and the direction of movement. For example, the arrow labeled 0/1,R means that if the current symbol is 0, replace it with 1 and move the tape head to the right.
- A machine table has the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement. For example, the entry q1,1,L means that if the current state is q0 and the current symbol is 0, then the new state is q1, the new symbol is 1, and the tape head moves to the left.
- Here is an example of a Turing machine that increments a binary number by one, represented by both a state diagram and a machine table:

State diagram of a Turing machine that increments a binary number by one

| State \ Symbol | 0 | 1 | |
| --- | --- | --- | --- |
| q0 | q0,0,R | q0,1,R | |
| q1 | q1,0,L | q1,1,L | |
| q2 | q3,1,R | q2,0,L | |
| q3 | | | HALT |



# Language Acceptability of Turing Machines

- A Turing machine (TM) is a mathematical model of computation that can perform any computation that is possible by any other model of computation, such as a finite automaton, a pushdown automaton, or a lambda calculus.
- A TM consists of a finite control, an infinite tape divided into cells, and a tape head that can read and write symbols on the tape and move left or right.
- A TM can be in one of a finite number of states, including a special start state and one or more final or accepting states.
- A TM accepts a language if it enters into a final state for any input string w that belongs to the language. A language is recursively enumerable (generated by Type-0 grammar) if it is accepted by a TM .
- A TM decides a language if it accepts it and enters into a rejecting state for any input not in the language. A language is recursive (generated by Type-1 grammar) if it is decided by a TM.
- A TM can also be in a non-halting state, where it does not enter into a final or rejecting state for some input. A language is undecidable if there is no TM that decides it. A language is unrecognizable if there is no TM that accepts it.
- A TM can be deterministic or nondeterministic. A deterministic TM (DTM) has only one possible move for any given configuration of the tape and the state. A nondeterministic TM (NTM) can have more than one possible move for some configuration. A language is accepted by a DTM if and only if it is accepted by an NTM. A language is decided by a DTM if and only if it is decided by an NTM.
- A TM can be classified into different types based on the number of tapes, the size of the tape alphabet, the direction of the tape head movement, and the amount of time or space required to accept or decide a language. Some examples of TM types are single-tape TM, multi-tape TM, two-way infinite tape TM, one-way infinite tape TM, read-only TM, linear bounded automaton, etc. Each type of TM has a different computational power and can accept or decide different classes of languages.



# Techniques for Turing Machine Construction

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It consists of an infinite tape divided into cells, a head that can read and write symbols on the tape, and a finite set of states and transitions that determine the behavior of the machine.

There are different techniques for constructing Turing machines for various languages or problems. Some of the common techniques are:

- **Concatenation**: To construct a Turing machine for a language that is the concatenation of two languages, such as L = L1L2, we can use two Turing machines, one for L1 and one for L2, and connect them in series. The first machine will process the input until it reaches the end of L1, then move the head to the right and switch to the second machine, which will process the rest of the input as L2. If both machines accept, the combined machine accepts; otherwise, it rejects. For example, to construct a Turing machine for L = a<sup>n</sup>b<sup>n</sup>, we can use one machine that checks if the input is of the form a<sup>n</sup>, and another machine that checks if the input is of the form b<sup>n</sup>, and connect them in series.

- **Union**: To construct a Turing machine for a language that is the union of two languages, such as L = L1 ∪ L2, we can use two Turing machines, one for L1 and one for L2, and connect them in parallel. The input is given to both machines simultaneously, and the combined machine accepts if either of the machines accepts; otherwise, it rejects. For example, to construct a Turing machine for L = {0<sup>n</sup>1<sup>n</sup> | n ≥ 0} ∪ {1<sup>n</sup>0<sup>n</sup> | n ≥ 0}, we can use one machine that checks if the input is of the form 0<sup>n</sup>1<sup>n</sup>, and another machine that checks if the input is of the form 1<sup>n</sup>0<sup>n</sup>, and connect them in parallel.

- **Iteration**: To construct a Turing machine for a language that is the iteration of another language, such as L = L1<sup>*</sup>, we can use a Turing machine for L1 and repeat it as many times as needed. The machine will process the input from left to right, and each time it reaches the end of a substring that belongs to L1, it will move the head to the right and start over. If the input is exhausted and the machine is in an accepting state, the combined machine accepts; otherwise, it rejects. For example, to construct a Turing machine for L = {0, 1}<sup>*</sup>, we can use a Turing machine that accepts any single symbol 0 or 1, and repeat it as many times as needed.

- **Simulation**: To construct a Turing machine for a language that is defined by an algorithm or a function, we can simulate the algorithm or the function on the tape using the head and the states. The machine will perform the same steps as the algorithm or the function, and use the tape as a memory to store intermediate results or variables. If the algorithm or the function terminates and produces a valid output, the machine accepts; otherwise, it rejects. For example, to construct a Turing machine that computes the bitwise OR of its two binary inputs of length N, we can simulate the OR operation on the tape using the head and the states. The machine will read the two inputs from left to right, and write the result on the tape as it goes. If the inputs are valid and the operation is completed, the machine accepts; otherwise, it rejects.

- **Modification**: To construct a Turing machine for a language that is a modification of another language, such as L = L1 - L2, we can use a Turing machine for L1 and modify it to reject the inputs that belong to L2. The machine will process the input as if it belongs to L1, but if it encounters a symbol or a pattern that indicates that the input belongs to L2, it will switch to a rejecting state. For example, to construct a Turing machine for L = {0<sup>n</sup>1<sup>n</sup> | n ≥ 0} - {0<sup>2k</sup>1<sup>2k</



# Modifications of Turing Machine

A Turing machine is a mathematical model of computation that can perform any algorithmic task by reading and writing symbols on an infinite tape. A Turing machine consists of a finite set of states, a finite set of input symbols, a finite set of tape symbols, a transition function that maps the current state and tape symbol to a new state, tape symbol and head movement, and a start state and a set of final states.

There are several variations or modifications of Turing machines that are equivalent in terms of computational power, meaning that they can recognize the same class of languages or compute the same functions. Some of these modifications are:

- **Multiple track Turing machine**: A k-track Turing machine (for some k>0) has k-tracks and one R/W head that reads and writes all of them one by one. Each track can store one tape symbol, and the transition function depends on the symbols on all tracks. A multiple track Turing machine can simulate a single track Turing machine by using different symbols to encode the information on different tracks. 
- **Two-way infinite tape Turing machine**: A two-way infinite tape Turing machine has an infinite tape that extends in both directions, and a R/W head that can move left or right. A two-way infinite tape Turing machine can simulate a standard Turing machine by using a special symbol to mark the left end of the tape and ignoring any symbols beyond it. 
- **Multi-tape Turing machine**: A multi-tape Turing machine has k tapes (for some k>0) and k R/W heads, one for each tape. The transition function depends on the symbols on all tapes, and can change the symbols and move the heads independently. A multi-tape Turing machine can simulate a single tape Turing machine by using one tape to store the input and the rest to simulate the work tape. Conversely, a single tape Turing machine can simulate a multi-tape Turing machine by using different symbols to separate the contents of different tapes and a special symbol to mark the position of each head. 
- **Multi-tape multi-head Turing machine**: A multi-tape multi-head Turing machine has k tapes (for some k>0) and m R/W heads (for some m>0), where each head can access any tape. The transition function depends on the symbols on all tapes and heads, and can change the symbols and move the heads independently. A multi-tape multi-head Turing machine can simulate a multi-tape Turing machine by assigning one head to each tape. Conversely, a multi-tape Turing machine can simulate a multi-tape multi-head Turing machine by using different symbols to encode the information on different heads and tapes. 
- **Multi-dimensional tape Turing machine**: A multi-dimensional tape Turing machine has a tape that is a grid of cells, and a R/W head that can move in any direction. The transition function depends on the symbol in the current cell, and can change the symbol and move the head in any direction. A multi-dimensional tape Turing machine can simulate a standard Turing machine by using one row of the grid as the tape and moving the head only left or right. Conversely, a standard Turing machine can simulate a multi-dimensional tape Turing machine by using different symbols to encode the coordinates of the cells and the direction of the head. 
- **Multi-head Turing machine**: A multi-head Turing machine has one tape and k R/W heads (for some k>0), where each head can move left or right independently. The transition function depends on the symbols on all heads, and can change the symbols and move the heads independently. A multi-head Turing machine can simulate a standard Turing machine by using one head as the main head and the rest as auxiliary heads. Conversely, a standard Turing machine can simulate a multi-head Turing machine by using different symbols to mark the position of each head and moving them one by one. 
- **Non-deterministic Turing machine**: A non-deterministic Turing machine has a transition function that can map the current state and tape symbol to a set of possible new states, tape symbols and head movements, instead of a single one. A non-deterministic Turing machine accepts an input if there exists a sequence of transitions that leads to a final state. A non-deterministic Turing machine can simulate a deterministic Turing machine by choosing only one transition for each state and tape symbol. Conversely, a deterministic Turing machine can simulate a non-deterministic Turing machine by using a special symbol to mark the choices made and backtracking when necessary. 

: Variation of



# Turing Machine as Computer of Integer Functions

- A Turing machine is a simple abstract computational device that can simulate any algorithm or computation .
- A Turing machine can compute functions of the form f(x) or f(x,y) where x and y are integers.
- To compute a function, a Turing machine needs an input tape, a finite set of states, a transition function, and an output tape .
- The input tape contains the value of x or x and y, encoded in some way, such as unary or binary .
- The output tape contains the value of f(x) or f(x,y), encoded in the same way as the input, after the computation is done .
- The transition function specifies how the Turing machine moves from one state to another, reads and writes symbols on the tapes, and halts or loops .
- A Turing machine can compute any function that is computable, meaning that there is an algorithm or a finite set of rules that can produce the output from the input in a finite number of steps  .
- A Turing machine cannot compute functions that are uncomputable, meaning that there is no algorithm or a finite set of rules that can produce the output from the input in a finite number of steps, such as the halting problem or the busy beaver function  .
- A Turing machine can also be used to study the complexity and decidability of computational problems, such as the classes P, NP, and undecidable  .



# Universal Turing machine

- A universal Turing machine (UTM) is a Turing machine that can simulate an arbitrary Turing machine on arbitrary input .
- A UTM essentially achieves this by reading both the description of the machine to be simulated as well as the input to that machine from its own tape .
- A UTM can be used to model the notion of computability, as any function that can be computed by a Turing machine can also be computed by a UTM.
- A UTM can also be used to study the properties and limitations of Turing machines, such as decidability, undecidability, and complexity.
- A UTM can be constructed from a simple Turing machine by adding a special symbol to the tape alphabet, such as #, to separate the description of the machine to be simulated from the input to that machine.
- A UTM can then use a finite set of rules to decode the description of the machine to be simulated and execute its transitions on the input, while keeping track of the current state and head position of the simulated machine.
- A UTM can also be designed to accept a standard encoding of Turing machines, such as the Gödel number, and use a universal function to decode and simulate them.
- A UTM is not more powerful than any other Turing machine, as it can only compute what is computable, but it is more versatile and convenient, as it can simulate any Turing machine with a single fixed program.



# Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite amount of tape to work with.
- The tape is divided into cells, each containing a symbol from the tape alphabet.
- The tape alphabet includes two special symbols, called left and right endmarkers, that mark the boundaries of the tape.
- The LBA has a finite set of states and a transition function that determines how it moves from one state to another, depending on the current state and the symbol under the tape head.
- The LBA can also write a new symbol on the tape cell, replacing the old one, and move the tape head one cell to the left or right.
- The LBA can be deterministic or nondeterministic, meaning that it can have one or more possible transitions for a given state and symbol.
- The LBA can be multi-track, meaning that it can have more than one tape head and more than one symbol per cell.
- The LBA can accept or reject an input string by entering a special state, called an accepting or rejecting state, respectively.
- The LBA can also halt without accepting or rejecting, if it has no applicable transition for the current state and symbol.
- The LBA is said to recognize a language if it accepts all and only the strings that belong to that language.
- The LBA is more powerful than a finite automaton or a pushdown automaton, but less powerful than a general Turing machine.
- The LBA can recognize context-sensitive languages, which are a subset of recursively enumerable languages.
- The LBA can also decide context-sensitive languages, which are a subset of recursive languages.
- The LBA is equivalent to a Turing machine with a tape length that is a linear function of the input length.
- The LBA is also equivalent to a grammar that generates context-sensitive languages, called a linear bounded grammar.

: Linear bounded automaton - Wikipedia
: Linear Bounded Automata - tutorialspoint.com
: Introduction to Linear Bounded Automata (LBA) - GeeksforGeeks



# Church's Thesis

- Church's thesis, also called Church's theorem, is a principle formulated by the American logician Alonzo Church in 1935.
- It states that the recursive functions are the only functions that can be mechanically calculated.
- A recursive function is a function that can be defined by a finite set of rules, such as a formula, an algorithm, or a Turing machine.
- A mechanical calculation is a calculation that can be performed by a device that follows a fixed set of instructions, such as a computer.
- Church's thesis is not a mathematical theorem, but a hypothesis or a conjecture that cannot be proved or disproved.
- It is based on the intuitive notion of an effectively computable function, which is a function that can be computed by a human using a pencil and paper, given enough time and resources.
- Church's thesis claims that every effectively computable function is a recursive function, and vice versa.
- It also implies that there is no function that can be computed by a more powerful device than a Turing machine, which is a hypothetical machine that can simulate any algorithm.
- Church's thesis is widely accepted by mathematicians, logicians, and computer scientists, as no counterexample has ever been found.
- It is also supported by various formalizations of the notion of computability, such as lambda calculus, register machines, and Gödel's system T, which are all equivalent to recursive functions and Turing machines.
- However, Church's thesis is not universally accepted, as some constructivists and intuitionists reject the classical logic and the law of excluded middle that underlie the definition of recursive functions.
- They propose a stronger version of Church's thesis, which states that all total functions are computable functions.
- A total function is a function that is defined for every possible input, whereas a partial function may be undefined for some inputs.
- A computable function is a function that can be computed by a constructive method, which is a method that provides a proof of existence and a means of construction for every output.
- The constructivist version of Church's thesis is also an axiom that cannot be proved or disproved, but it is more restrictive than the classical version, as it excludes some partial recursive functions that are not total.



# Recursive and Recursively Enumerable Language

- A **recursive language** is a formal language for which there exists a Turing machine that accepts and halts on every input string, whether it belongs to the language or not.
- A **recursively enumerable language** is a formal language for which there exists a Turing machine that accepts and halts on every input string that belongs to the language, but may either reject or loop forever on input strings that do not belong to the language.
- Recursive languages are a subset of recursively enumerable languages, since a Turing machine that decides a language can also enumerate it by testing every possible input string in some order.
- Some properties of recursive languages are:
  - They are closed under union, intersection, complement, concatenation, Kleene star, reversal, homomorphism, and inverse homomorphism.
  - They are a proper subset of context-sensitive languages.
  - They are decidable by a Turing machine in finite time.
  - They are accepted by a linear bounded automaton.
- Some properties of recursively enumerable languages are:
  - They are closed under union, intersection, concatenation, Kleene star, and homomorphism, but not under complement, reversal, or inverse homomorphism.
  - They are a proper subset of recursively enumerable languages.
  - They are semi-decidable by a Turing machine, meaning that they can be accepted in finite time, but not rejected in finite time.
  - They are accepted by a Turing machine with unlimited tape.
- Some examples of recursive languages are:
  - The language of all palindromes over a finite alphabet.
  - The language of all strings over a finite alphabet that have an even number of symbols.
  - The language of all strings over a finite alphabet that are accepted by a finite automaton.
- Some examples of recursively enumerable languages that are not recursive are:
  - The language of all strings over a finite alphabet that encode a valid proof in some formal system, such as Peano arithmetic or Zermelo-Fraenkel set theory.
  - The language of all strings over a finite alphabet that encode a Turing machine that halts on the empty input.
  - The language of all strings over a finite alphabet that are accepted by a pushdown automaton, but not by a finite automaton.



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



# Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows: Given two lists of non-empty strings over Σ, M = (x1, x2, ..., xn) and N = (y1, y2, ..., yn), determine whether there exists a sequence of indices (i1, i2, ..., ik) such that x(i1) x(i2) ... x(ik) = y(i1) y(i2) ... y(ik), where x(i) and y(i) denote the ith elements of M and N respectively .
- The strings x(i) and y(i) are called the top and bottom strings of a domino, and the pair (x(i), y(i)) is called a domino. A solution to the PCP problem is a sequence of dominos whose top and bottom strings are equal .
- For example, consider the following instance of the PCP problem over the alphabet {a, b}:

  M = (ab, b, aab, abaa)
  N = (b, aa, a, aba)

  A possible solution is the sequence of indices (1, 3, 4, 2), which corresponds to the following sequence of dominos:

  |ab|aab|abaa|b|
  |b|a|aba|aa|

  The top and bottom strings are both abaababaaa.

- The PCP problem is undecidable, meaning that there is no algorithm that can always correctly answer yes or no for any given instance of the problem. This can be proved by reducing the halting problem to the PCP problem, i.e., by showing that if there were an algorithm for the PCP problem, then we could use it to solve the halting problem, which is known to be undecidable  .
- The PCP problem is often used in proofs of undecidability for other problems in logic or in formal language theory, such as the word problem for context-free grammars, the equivalence problem for regular expressions, or the satisfiability problem for first-order logic .
- The PCP problem is also related to some open problems in combinatorics and number theory, such as the Collatz conjecture, the abc conjecture, and the Erdős–Graham problem.



# Introduction to Recursive Function Theory

- Recursive function theory is a branch of mathematical logic that studies the class of functions on the natural numbers that can be defined by recursion .
- A function is recursive if it can be obtained from some basic functions (such as zero, successor, projection, etc.) by applying some rules of composition (such as substitution, primitive recursion, minimization, etc.) .
- Recursive functions are also called computable functions, because they can be computed by a Turing machine or an equivalent model of computation .
- Recursive functions can be classified into different types, such as primitive recursive functions, partial recursive functions, total recursive functions, etc., depending on their properties and limitations  .
- Recursive function theory is closely related to computability theory, which studies the notions of computability, decidability, and undecidability for various problems and languages  .
- Recursive function theory also explores the structure and properties of the recursively enumerable degrees, which measure the complexity of recursively enumerable sets and languages.

