

## Unit 1 - Basic Concepts and Automata Theory

- This unit introduces the basic concepts and terminology of formal languages, grammars, and automata theory, which are the foundations of theoretical computer science and natural language processing.
- Formal languages are sets of strings over a finite alphabet, which can be defined by rules or operations. For example, the set of all binary strings is a formal language over the alphabet {0, 1}.
- Grammars are systems of rules that generate formal languages. For example, a grammar for arithmetic expressions can generate strings like "2 + 3 * 4" or "(5 - 1) / 2".
- Automata are abstract machines that can recognize or process formal languages. For example, a finite automaton is a simple model of computation that has a finite number of states and transitions between them, and can accept or reject strings based on whether they reach a final state or not.
- There are different types of formal languages, grammars, and automata, depending on their expressive power and complexity. For example, regular languages are the simplest class of formal languages, which can be defined by regular expressions or recognized by finite automata. Context-free languages are a larger class of formal languages, which can be defined by context-free grammars or recognized by pushdown automata. There are also context-sensitive languages, recursive languages, recursively enumerable languages, and so on, which correspond to different types of grammars and automata.
- This unit covers the basic definitions, properties, and examples of formal languages, grammars, and automata, as well as some important theorems and algorithms related to them. For example, the pumping lemma is a technique to prove that a language is not regular or not context-free. The Chomsky hierarchy is a classification of formal languages and grammars based on their generative power. The equivalence and conversion of different models of computation, such as regular expressions, finite automata, and regular grammars, are also discussed.



# Introduction to Theory of Computation

- Theory of computation (TOC) is a branch of computer science that is concerned with how problems can be solved using algorithms and how efficiently they can be solved.
- TOC includes the fundamental mathematical properties of computer hardware, software and their applications.
- TOC deals with what problems can be solved on a model of computation, using an algorithm, how efficiently they can be solved or to what degree (e.g., approximate solutions versus precise ones).
- A model of computation is an abstract representation of a computing device that defines its capabilities and limitations.
- Some examples of models of computation are Turing machines, finite automata, pushdown automata, and lambda calculus.
- TOC also studies the concepts of computability, decidability, reducibility, recursive function theory, complexity classes, completeness, hierarchy theorems, and oracles .
- Computability theory is the branch of TOC that investigates the limitations of algorithmic problem solving and the classes of problems that are solvable or unsolvable by different models of computation.
- Decidability theory is the branch of TOC that studies the existence of effective methods for solving problems and the properties of decidable and undecidable problems.
- Reducibility theory is the branch of TOC that explores the relationships between different problems and the possibility of transforming one problem into another by using algorithms.
- Recursive function theory is the branch of TOC that deals with the formalization and classification of computable functions and their properties.
- Complexity theory is the branch of TOC that measures the resources (such as time and space) required by algorithms to solve problems and the classes of problems that can be solved within certain resource bounds.
- Completeness theory is the branch of TOC that identifies the hardest problems in a given complexity class and the implications of their existence.
- Hierarchy theorems are the results in TOC that establish the existence of distinct levels of complexity within a given complexity class.
- Inherently complex problems are the problems in TOC that are provably hard to solve or approximate by any algorithm, regardless of the model of computation.
- Oracles are the hypothetical devices in TOC that can answer questions that are otherwise undecidable or intractable by any algorithm.

## Basic Concepts and Automata Theory

- Automata theory is the branch of TOC that studies the abstract machines that can perform computations on inputs and produce outputs.
- An automaton is a mathematical model of a machine that can change its state according to some rules and accept or reject an input based on its final state.
- Automata theory investigates the properties and limitations of different types of automata and the languages that they can recognize or generate.
- A language is a set of strings over some alphabet, where an alphabet is a finite set of symbols.
- Automata theory also explores the relations between automata and formal languages, such as regular expressions, grammars, and parsing.
- Some examples of automata are finite automata, pushdown automata, linear bounded automata, and Turing machines.
- Finite automata are the simplest type of automata that have a finite number of states and can recognize regular languages.
- Pushdown automata are a type of automata that have a stack as an auxiliary memory and can recognize context-free languages.
- Linear bounded automata are a type of automata that have a tape of bounded length as an auxiliary memory and can recognize context-sensitive languages.
- Turing machines are the most powerful type of automata that have an unbounded tape as an auxiliary memory and can recognize recursively enumerable languages.
- Automata theory is useful for modeling and analyzing various aspects of computation, such as compilers, parsers, pattern matching, cryptography, artificial intelligence, and logic.



# Automata for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages

- Automata theory is a branch of computer science and mathematics that studies abstract computing devices, or machines, that can perform certain tasks automatically  .
- An automaton is an abstract model of a machine that has a finite number of states and can change its state according to some input symbols and a transition function  .
- Automata theory can be used to model and analyze various aspects of computation, such as complexity, decidability, and expressiveness  .
- There are different types of automata, such as finite automata, pushdown automata, and Turing machines, that have different capabilities and limitations    .
- Finite automata are the simplest type of automata that can recognize regular languages, which are the languages that can be described by regular expressions    .
- Pushdown automata are a type of automata that have a stack as an additional memory and can recognize context-free languages, which are the languages that can be described by context-free grammars    .
- Turing machines are the most powerful type of automata that can simulate any algorithm and can recognize recursively enumerable languages, which are the languages that can be generated by a Turing machine    .
- The Church-Turing thesis states that any function that can be computed by an algorithm can also be computed by a Turing machine, and vice versa .
- Some problems are undecidable, meaning that there is no algorithm or Turing machine that can always give a correct answer for them, such as the halting problem  .
- Automata theory is closely related to other fields of computer science, such as formal languages, computability, complexity, and logic   .



# Computability

Computability is the study of what can and cannot be computed by following specific rules or procedures. It is also known as recursion theory .

Some of the main topics in computability theory are:

- **Computable functions**: These are functions that can be calculated by a finite set of instructions, such as arithmetic operations, logical operations, or string manipulations. Examples of computable functions are addition, multiplication, factorial, or the Fibonacci sequence.
- **Computing models**: These are abstract machines or formal systems that can perform computations, such as Turing machines, lambda calculus, or cellular automata. Different models of computation may have different capabilities and limitations, but they are all equivalent in the sense that they can compute the same class of functions, known as the **recursive functions** .
- **Decidability and undecidability**: A problem is decidable if there is an algorithm that can always give a correct yes or no answer for any input. A problem is undecidable if there is no such algorithm. Examples of decidable problems are checking whether a given string belongs to a regular language, or whether two natural numbers are relatively prime. Examples of undecidable problems are the halting problem, which asks whether a given program will ever stop on a given input, or the word problem for groups, which asks whether two given words in a group are equal .
- **Reducibility and completeness**: A problem A is reducible to a problem B if there is an algorithm that can transform any instance of A into an instance of B, such that the answer for A is the same as the answer for B. This means that A is no harder than B, and B is at least as hard as A. A problem is complete for a class of problems if it belongs to that class and every other problem in that class is reducible to it. This means that the complete problem is the hardest problem in that class. Examples of complete problems are the halting problem for the class of undecidable problems, or the satisfiability problem for the class of NP problems .
- **Recursive function theory**: This is the study of the properties and structure of the recursive functions, which are the functions that can be computed by any model of computation. Recursive functions can be classified into different levels of complexity, such as primitive recursive functions, which are defined by using only basic operations and recursion, or partial recursive functions, which are defined by using also unbounded minimization or the mu-operator. Recursive function theory also explores the notions of computable sets, computable enumerations, and computable structures .
- **Time and space measures**: These are the study of how much time or space is required to compute a function or solve a problem on a given model of computation. Time and space measures can be used to compare the efficiency and feasibility of different algorithms or problems. For example, a problem is polynomial-time solvable if there is an algorithm that can solve it in a number of steps that is bounded by a polynomial function of the input size. A problem is exponential-time solvable if there is an algorithm that can solve it in a number of steps that is bounded by an exponential function of the input size. Polynomial-time problems are generally considered to be tractable, while exponential-time problems are generally considered to be intractable .
- **Hierarchy theorems**: These are theorems that show that there are different levels of complexity within a class of problems or functions, and that these levels are distinct and incomparable. For example, the time hierarchy theorem states that there are problems that can be solved in polynomial time, but not in linear time, and problems that can be solved in exponential time, but not in polynomial time. The space hierarchy theorem states that there are problems that can be solved in polynomial space, but not in logarithmic space, and problems that can be solved in exponential space, but not in polynomial space .
- **Inherently complex problems**: These are problems that are provably hard or impossible to solve efficiently on any model of computation, regardless of the specific algorithm or implementation. For example, the busy beaver function, which gives the maximum number of steps that a Turing machine with a given number of states can perform before halting, is an inherently complex function, as it grows faster than any computable function. The Kolmogorov complexity of a string, which gives the



# Complexity

Complexity is a measure of the resources required to perform a computation by an abstract machine, such as an automaton. Complexity theory is a branch of computer science and mathematics that studies the limits and trade-offs of various computational models and problems.

Some of the topics covered in complexity theory are:

- Classes of abstract machines, such as finite automata, pushdown automata, Turing machines, circuits, etc.
- Classes of computational problems, such as decision problems, function problems, optimization problems, etc.
- Classes of computational resources, such as time, space, nondeterminism, randomness, parallelism, communication, etc.
- Relations and reductions between classes of machines, problems, and resources, such as equivalence, simulation, mapping, completeness, hardness, etc.
- Hierarchy theorems and separation results that show the existence or nonexistence of gaps between classes of machines, problems, and resources, such as the time hierarchy theorem, the space hierarchy theorem, the P versus NP problem, etc.

Complexity theory aims to understand the inherent difficulty of computational tasks, and to classify them according to their complexity. Complexity theory also explores the connections and implications of complexity results for other fields of computer science, such as algorithms, cryptography, logic, programming languages, etc.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of alphabet for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages.

# Alphabet
- An alphabet is a finite, non-empty set of symbols, usually denoted by Σ.
- The symbols in an alphabet are called letters or characters.
- Examples of alphabets are:
  - Σ = {0, 1} (the binary alphabet)
  - Σ = {a, b, c, ..., z} (the lowercase English alphabet)
  - Σ = {a, b} (a simple alphabet with two letters)
- An alphabet can be used to form strings or words by concatenating the symbols in the alphabet.
- A string over an alphabet Σ is a finite sequence of symbols from Σ.
- Examples of strings over the binary alphabet are:
  - 0 (a string of length 1)
  - 101 (a string of length 3)
  - 00100110 (a string of length 8)
- The length of a string w is the number of symbols in w, denoted by |w|.
- The empty string is the string of length 0, denoted by ε or λ.
- The set of all strings over an alphabet Σ is denoted by Σ*.
- Examples of subsets of Σ* are:
  - Σ+ = Σ* - {ε} (the set of all non-empty strings over Σ)
  - Σ^n = {w ∈ Σ* | |w| = n} (the set of all strings of length n over Σ)
  - Σ^≤n = {w ∈ Σ* | |w| ≤ n} (the set of all strings of length at most n over Σ)
- The concatenation of two strings u and v is the string obtained by appending v to the end of u, denoted by uv or u⋅v.
- Examples of concatenation are:
  - 0⋅1 = 01
  - 101⋅001 = 101001
  - ε⋅0 = 0⋅ε = 0
- The concatenation of a string w with itself n times is denoted by w^n, where w^0 = ε and w^1 = w.
- Examples of exponentiation are:
  - 0^3 = 000
  - 10^2 = 1010
  - ε^5 = ε
- The reversal of a string w is the string obtained by reversing the order of the symbols in w, denoted by w^R.
- Examples of reversal are:
  - 0^R = 0
  - 101^R = 101
  - 00100110^R = 01100100
- A language over an alphabet Σ is a subset of Σ*, that is, a set of strings over Σ.
- Examples of languages over the binary alphabet are:
  - L = {0, 1, 00, 01, 10, 11} (a finite language with 6 strings)
  - L = {0^n1^n | n ≥ 0} (an infinite language with strings of the form 0^k1^k for some k ≥ 0)
  - L = Σ* (the universal language that contains all strings over Σ)
  - L = ∅ (the empty language that contains no strings)



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some symbols for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages.

# Symbols for the notes of the Unit 1 - Basic Concepts and Automata Theory

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
- **L<sub>1</sub> = L<sub>2</sub>**: The equality relation, the two languages are equal if they have the same strings.
- **L<sup>*</sup>**: The Kleene star of a language, the set of strings obtained by concatenating zero or more strings from the language.
- **L<sup>+</sup>**: The positive closure of a language, the set of strings obtained by concatenating one or more strings from the language.
- **L<sup>n</sup>**: The nth power of a language, the set of strings obtained by concatenating n strings from the language.
- **M**: A machine, an abstract model of computation.
- **Q**: The set of states of a machine, a finite set of labels.
- **q<sub>0</sub>**: The initial state of a machine, a state from which the computation starts.
- **F**: The set of final or accepting states of a machine, a subset of states that indicate successful computation.
- **δ**: The transition function of a machine, a rule that defines how the machine changes its state and output based on its input and current state.
- **(q, w) ⇒ (p, x)**: The transition relation of a machine, a relation that indicates that the machine can go from state q to state p and produce output x when reading input w.
- **M(w)**: The output of a machine M on input w, the result of applying the transition function or relation to the input and the initial state.
- **L(M)**: The language recognized or accepted by a machine M, the set of inputs for which the machine produces a successful output or reaches a final state.



# String

- A string is a finite sequence of symbols from a given alphabet.
- An alphabet is a finite set of symbols, such as {0, 1}, {a, b, c, ..., z}, or {+, -, x, /, (, )}.
- A string can be denoted by enclosing its symbols in double quotes, such as "0101", "hello", or "+(x/x)".
- The length of a string is the number of symbols in it, denoted by |s| for a string s.
- The empty string is the string with no symbols, denoted by ε or λ. It has length zero, i.e., |ε| = 0.
- A string s is a substring of another string t if s occurs as a consecutive sequence of symbols in t, such as "ell" is a substring of "hello".
- A string s is a prefix of another string t if s occurs at the beginning of t, such as "he" is a prefix of "hello".
- A string s is a suffix of another string t if s occurs at the end of t, such as "lo" is a suffix of "hello".
- A string s is a subsequence of another string t if s can be obtained from t by deleting some symbols, such as "hl" is a subsequence of "hello".
- The concatenation of two strings s and t is the string obtained by appending t to the end of s, denoted by s⋅t or simply st, such as "hello"⋅"world" = "helloworld".
- The reverse of a string s is the string obtained by reversing the order of its symbols, denoted by s^R, such as "hello"^R = "olleh".
- The power of a string s to the n-th exponent, denoted by s^n, is the string obtained by concatenating n copies of s, such as "ab"^3 = "ababab". The zero-th power of any string is the empty string, i.e., s^0 = ε.
- A language is a set of strings over a given alphabet, such as {0, 1}* is the language of all binary strings, or {a^n b^n | n ≥ 0} is the language of all strings with equal numbers of a's and b's.
- A language can be specified by a set of rules, such as a grammar, a regular expression, or an automaton, which define how to generate or recognize the strings in the language.



# Formal Languages

- A **formal language** is a set of strings over a finite alphabet.
- A **string** is a finite sequence of symbols from an alphabet.
- An **alphabet** is a finite set of symbols.
- A **symbol** is a character, an abstraction that is meaningless by itself.
- Examples of formal languages are:
  - The set of all binary strings that start with 1.
  - The set of all valid arithmetic expressions over the symbols +, -, *, /, (, ), and the digits 0-9.
  - The set of all syntactically correct programs in a given programming language.
- Formal languages are used to model and study various aspects of computation, such as syntax, semantics, logic, algorithms, and complexity .

# Automata Theory

- **Automata theory** is the study of abstract machines that can process inputs and produce outputs according to some rules.
- An **automaton** is a mathematical model of a machine that can recognize or generate strings over an alphabet.
- Automata are often classified by the class of formal languages they can recognize or generate, as in the **Chomsky hierarchy**, which describes a nesting relationship between major classes of automata.
- Examples of automata are:
  - **Finite automata**, which have a finite number of states and can recognize regular languages.
  - **Pushdown automata**, which have a finite number of states and a stack and can recognize context-free languages.
  - **Turing machines**, which have an infinite tape and can recognize recursively enumerable languages.
  - **Cellular automata**, which consist of a grid of cells that change state according to local rules and can model complex phenomena.
- Automata theory provides a simple, elegant view of the complex machine that we call a computer and helps us understand the limits and possibilities of computation .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of Deterministic Finite Automaton (DFA) for the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages.

# Deterministic Finite Automaton (DFA)

- A deterministic finite automaton (DFA) is a mathematical model of a machine that accepts or rejects a given input string based on its current state and the symbols in the input.
- A DFA has a finite set of states, a finite set of input symbols (called the alphabet), a transition function that maps each state and input symbol to a next state, a start state, and a set of final or accepting states.
- A DFA can be represented by a five-tuple (Q, Σ, δ, q0, F), where
  - Q is the set of states
  - Σ is the alphabet
  - δ is the transition function
  - q0 is the start state
  - F is the set of final states
- A DFA can also be represented by a state diagram, which is a directed graph where each node is a state, each edge is labeled by an input symbol, and there is a special start state and a set of final states marked by double circles.
- A DFA processes an input string from left to right, starting from the start state, and following the edges labeled by the input symbols. If the DFA reaches a final state after reading the entire input, the input is accepted; otherwise, the input is rejected.
- A DFA is deterministic because for each state and input symbol, there is exactly one next state. There is no ambiguity or choice in the transition function.
- A DFA recognizes a regular language, which is a set of strings that can be accepted by some DFA. Regular languages have many properties and applications in computer science, such as regular expressions, lexical analysis, pattern matching, etc.



# Unit 1 - Basic Concepts and Automata Theory

## Definition

- Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them.
- An automaton is a self-acting, self-willed, self-moving device that can process information and perform tasks according to a definite procedure.
- Automata theory is a branch of theoretical computer science that explores the capabilities and limitations of different types of automata and their applications .
- Automata theory has connections with mathematics, logic, linguistics, philosophy, and engineering .
- Automata theory can be divided into several subfields, such as finite automata, pushdown automata, Turing machines, cellular automata, and quantum automata . Each subfield studies a different class of automata and the languages they can recognize or generate .



# Representation for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages

- The unit covers the following topics:
  - Introduction to formal languages and automata theory
  - Alphabets, strings, and languages
  - Operations on strings and languages
  - Finite automata and regular languages
  - Deterministic and nondeterministic finite automata
  - Equivalence and minimization of finite automata
  - Regular expressions and regular grammars
  - Closure and decidability properties of regular languages
- The notes can be represented using the following format:
  - Each topic can have a brief introduction, followed by definitions, examples, theorems, proofs, and exercises.
  - Definitions can be highlighted using bold text, such as **finite automaton**.
  - Examples can be illustrated using diagrams, tables, or pseudocode, such as the following diagram of a finite automaton that accepts the language of all strings over {0,1} that end with 1:

  Finite automaton example

  - Theorems can be stated using italic text, such as *Theorem 1.1: Every regular language is accepted by some finite automaton*.
  - Proofs can be presented using logical steps, such as the following proof of Theorem 1.1:

  Proof: Let L be a regular language. By definition, there exists a regular expression R that denotes L. We can construct a finite automaton M that accepts L using the following algorithm:

  1. Convert R to an equivalent nondeterministic finite automaton (NFA) N using the rules given in the textbook.
  2. Convert N to an equivalent deterministic finite automaton (DFA) D using the subset construction algorithm.
  3. Minimize D using the partition refinement algorithm.

  The resulting DFA D is the finite automaton that accepts L. Hence, the theorem is proved.

  - Exercises can be given at the end of each topic, with solutions provided in a separate document, such as the following exercise:

  Exercise 1.1: Design a finite automaton that accepts the language of all strings over {a,b} that contain at least two a's and at most one b.

  Solution: One possible finite automaton is shown below:

  Finite automaton solution



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of acceptability of a string and language for the notes of the unit 1 - basic concepts and automata theory in the subject of theory of automata and formal languages.

# Acceptability of a String and Language

- A string is a finite sequence of symbols from a given alphabet.
- A language is a set of strings over a given alphabet.
- An alphabet is a finite, non-empty set of symbols.
- For example, if the alphabet is {a, b}, then some possible strings are a, b, ab, ba, aaa, bbb, etc. and some possible languages are {a, b}, {ab, ba}, {a^n b^n | n >= 0}, etc.
- An automaton is a mathematical model of a machine that can process strings and accept or reject them based on some rules.
- There are different types of automata, such as finite automata, pushdown automata, Turing machines, etc. Each type of automaton has a different power and limitation in recognizing languages.
- A string is accepted by an automaton if the automaton can reach a final state after processing the string.
- A language is accepted by an automaton if the automaton can accept all the strings in the language and reject all the strings not in the language.
- For example, a finite automaton can accept the language {a^n b^n | n >= 0} by having two states, one initial and final, and one intermediate, and having transitions from the initial state to the intermediate state on a, from the intermediate state to the final state on b, and from the final state to itself on b. The automaton can reject any string that has a b before an a, or has more a's than b's, or has more b's than a's, by not having any transition for those cases.
- The acceptability of a string or a language by an automaton depends on the type of the automaton, the alphabet, the states, the transitions, and the final states of the automaton. Different types of automata can accept different classes of languages. For example, finite automata can accept regular languages, pushdown automata can accept context-free languages, and Turing machines can accept recursively enumerable languages.



# Non Deterministic Finite Automaton (NFA)

- A Non Deterministic Finite Automaton (NFA) is a type of finite automaton that can have more than one possible transition from a given state for a given input symbol.
- An NFA can be defined as a 5-tuple (Q, Σ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × Σε to 2^Q, where Σε = Σ ∪ {ε} and ε is the empty string
  - q0 is the initial state
  - F is a subset of Q that contains the final or accepting states
- An NFA accepts an input string if there exists at least one sequence of transitions from the initial state to a final state that consumes the entire input string.
- An NFA can be represented by a transition diagram, where each state is a node, each transition is an edge labeled by the input symbol, and the initial and final states are marked by arrows and double circles, respectively.
- An example of an NFA that accepts the language L = {xa | x ∈ {a,b}*} is shown below:

NFA example

- An NFA can be converted to an equivalent Deterministic Finite Automaton (DFA) using the subset construction method, which constructs a DFA that simulates all possible moves of the NFA for each input symbol .
- An NFA can be more expressive and concise than a DFA, but a DFA can be more efficient and easier to implement than an NFA.



# Equivalence of DFA and NFA

- A DFA (deterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another is uniquely determined by the current state and the input symbol.
- An NFA (nondeterministic finite automaton) is a finite state machine that accepts or rejects a given string of symbols, where each move from a state to another is not uniquely determined by the current state and the input symbol. An NFA can have zero, one or more than one move from a given state on a given input symbol, and can also have null moves (moves without input symbol).
- A DFA and an NFA are equivalent if they recognize the same language, that is, if they accept the same set of strings.
- The equivalence of DFA and NFA can be proved by showing that for any DFA, there is an equivalent NFA, and vice versa.
- To construct an equivalent NFA from a given DFA, we can simply copy the states, transitions, initial state and final states of the DFA to the NFA. The resulting NFA will have the same behavior as the DFA, since there is no nondeterminism or null moves involved.
- To construct an equivalent DFA from a given NFA, we can use the subset construction algorithm, which is as follows:

  - Let the NFA be M1 = (Q1, E, q1,0, delta1, A1), where Q1 is the set of states, E is the input alphabet, q1,0 is the initial state, delta1 is the transition function, and A1 is the set of final states.
  - Let the DFA be M2 = (Q2, E, q2,0, delta2, A2), where Q2 is the set of states, E is the input alphabet, q2,0 is the initial state, delta2 is the transition function, and A2 is the set of final states.
  - The states of the DFA are subsets of the states of the NFA, that is, Q2 = 2^Q1, where 2^Q1 is the power set of Q1.
  - The initial state of the DFA is the epsilon-closure of the initial state of the NFA, that is, q2,0 = epsilon-closure(q1,0), where epsilon-closure(q) is the set of states that can be reached from q by following zero or more null moves.
  - The final states of the DFA are those subsets of the states of the NFA that contain at least one final state of the NFA, that is, A2 = {S | S is a subset of Q1 and S intersects A1 is not empty}.
  - The transition function of the DFA is defined as follows: for any state S in Q2 and any symbol a in E, delta2(S, a) = epsilon-closure(union of delta1(q, a) for all q in S), where delta1(q, a) is the set of states that can be reached from q by following one move on a in the NFA, and union is the set union operation.
  - The subset construction algorithm ensures that the DFA simulates the behavior of the NFA on any input string, by keeping track of all the possible states that the NFA can be in after reading each symbol of the input. Therefore, the DFA and the NFA accept the same language.



# NFA with ε-Transition

- An NFA with ε-transition is a type of non-deterministic finite automaton (NFA) that allows transitions from one state to another without consuming any input symbol. These transitions are labeled with ε, which denotes the empty string.
- An NFA with ε-transition can be formally defined as a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps Q × (Σ ∪ {ε}) to 2^Q, the power set of Q
  - q0 is the initial state
  - F is a subset of Q that contains the final or accepting states
- An NFA with ε-transition accepts an input string x if there exists a sequence of states q0, q1, ..., qn such that:
  - q0 is the initial state
  - qn is a final state
  - For each i (0 ≤ i < n), either qi+1 ∈ δ(qi, xi+1) or qi+1 ∈ δ(qi, ε)
- The ε-closure of a state q, denoted by ε-closure(q), is the set of all states that can be reached from q by following only ε-transitions. The ε-closure of a set of states S, denoted by ε-closure(S), is the union of the ε-closures of all states in S.
- The language accepted by an NFA with ε-transition is the set of all strings that are accepted by the automaton. It can be shown that any NFA with ε-transition can be converted to an equivalent NFA without ε-transition, and vice versa. Therefore, NFAs with ε-transition are equivalent in expressive power to NFAs without ε-transition, and to regular expressions and regular grammars.



# Equivalence of NFA's with and without ε-Transition

- An NFA (Non-deterministic Finite Automaton) is a finite state machine that can have multiple transitions for the same input symbol and state.
- An ε-transition is a special transition that does not consume any input symbol and can be taken spontaneously.
- An ε-NFA is an NFA that has one or more ε-transitions.
- An NFA without ε-transitions is also called a DFA (Deterministic Finite Automaton), since it has a unique transition for each input symbol and state.
- An NFA and an ε-NFA are equivalent if they accept the same language, i.e., the set of strings that make them reach a final state.
- To prove the equivalence of NFA and ε-NFA, we need to show that for any NFA, there exists an equivalent ε-NFA, and vice versa.

## Converting NFA to ε-NFA

- Given an NFA, we can construct an equivalent ε-NFA by adding ε-transitions from each state to itself, and from the initial state to all the final states.
- This way, the ε-NFA can simulate the behavior of the NFA by taking the same transitions as the NFA, or by skipping some states using the ε-transitions.
- For example, consider the following NFA that accepts the language {0, 01, 001}:

NFA

- We can convert it to an equivalent ε-NFA by adding ε-transitions as shown below:

ε-NFA

- The ε-NFA accepts the same language as the NFA, since it can take the same transitions as the NFA, or use the ε-transitions to skip some states.

## Converting ε-NFA to NFA

- Given an ε-NFA, we can construct an equivalent NFA by removing the ε-transitions and replacing them with appropriate transitions for each input symbol.
- To do this, we need to find the ε-closure of each state, which is the set of states that can be reached from that state by taking only ε-transitions.
- Then, for each state and input symbol, we find the set of states that can be reached from the ε-closure of that state by taking that input symbol, and add a transition for that symbol to that set of states.
- We also make the initial state of the NFA the ε-closure of the initial state of the ε-NFA, and make any state that contains a final state of the ε-NFA a final state of the NFA.
- For example, consider the following ε-NFA that accepts the language {a, ab, abb}:

ε-NFA

- We can convert it to an equivalent NFA by removing the ε-transitions and adding appropriate transitions as shown below:

NFA

- The NFA accepts the same language as the ε-NFA, since it can reach the same set of states as the ε-NFA for any input string.



# Finite Automata with Output

- Finite automata with output are similar to finite automata, except that they have the additional capability of producing output .
- Finite automata with output are also known as finite state machines (FSM) or transducers .
- Finite automata with output can be classified into two types: Moore machines and Mealy machines  .
- Moore machines are finite automata with output where the output depends only on the current state  .
- Mealy machines are finite automata with output where the output depends on both the current state and the input symbol  .
- Finite automata with output can be used to model various systems that have discrete inputs, outputs, states and transitions  .
- Finite automata with output can be represented by state diagrams, state tables or transition functions  .
- Finite automata with output can be converted from one type to another by adding or removing states and transitions .
- Finite automata with output can be analyzed for properties such as completeness, minimality, equivalence and regularity  .



# Moore Machine

- A Moore machine is a type of finite state machine (FSM) that has an output value associated with each state    .
- The output value of a Moore machine depends only on the current state, not on the input symbols    .
- A Moore machine can be formally defined as a 6-tuple (Q, Σ, Γ, δ, ω, q0) where    :
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite output alphabet
  - δ is a transition function that maps Q × Σ to Q
  - ω is an output function that maps Q to Γ
  - q0 is the initial state
- A Moore machine can be represented by a state diagram, where each state is labeled with its output value and each transition is labeled with an input symbol    .
- A Moore machine can be used to model systems that produce outputs based on their current states, such as traffic lights, vending machines, counters, etc    .
- An example of a Moore machine is shown below:

Moore machine example

- This Moore machine has four states: A, B, C, and D, with output values 0, 1, 0, and 1 respectively.
- The input alphabet is {0, 1} and the output alphabet is {0, 1}.
- The initial state is A.
- The transition function is defined as follows:
  - δ(A, 0) = B
  - δ(A, 1) = C
  - δ(B, 0) = B
  - δ(B, 1) = D
  - δ(C, 0) = B
  - δ(C, 1) = C
  - δ(D, 0) = B
  - δ(D, 1) = D
- The output function is defined as follows:
  - ω(A) = 0
  - ω(B) = 1
  - ω(C) = 0
  - ω(D) = 1
- The behavior of this Moore machine can be described as follows:
  - If the input is 0, the machine moves to state B and outputs 1.
  - If the input is 1, the machine moves to state C and outputs 0.
  - If the machine is in state B or D, it stays in the same state and outputs 1 for any input.
  - If the machine is in state C, it stays in the same state and outputs 0 for any input.



# Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input symbol. It is also known as a **deterministic finite-state transducer**  because it can transform an input sequence into an output sequence.

A Mealy machine can be formally defined by a 6-tuple (Q, q0, ∑, O, δ, λ') where:

- Q is a finite set of states
- q0 is the initial state
- ∑ is a finite input alphabet
- O is a finite output alphabet
- δ: Q × ∑ → Q is the transition function
- λ': Q × ∑ → O is the output function

A Mealy machine can be represented by a state diagram, where each state is labeled with its name and each transition is labeled with the input symbol and the output symbol separated by a slash. For example, the following state diagram shows a Mealy machine that detects the sequence 101 in the input and outputs 1 whenever it is detected:

Mealy machine example

Some properties of Mealy machines are :

- They are more efficient than Moore machines, as they require fewer states to implement the same functionality.
- They are more expressive than Moore machines, as they can produce different outputs for the same state depending on the input symbol.
- They are equivalent to Moore machines in terms of computational power, as any Mealy machine can be converted into a Moore machine and vice versa.



# Equivalence of Moore and Mealy Machine

- A Moore machine is a finite state machine where the output depends only on the current state.
- A Mealy machine is a finite state machine where the output depends on the current state and the input.
- The equivalence of the Moore and Mealy machine means that both the machines produce the same output for the same input.
- A Mealy machine can always be converted to a Moore machine, with the possible addition of extra states .
- A Moore machine can also be converted to a Mealy machine, with the possible reduction of states .

## Conversion from Mealy to Moore Machine

- The general method to convert a Mealy machine to a Moore machine is as follows :

  - Step 1: Identify the states that have more than one output associated with them.
  - Step 2: Create new states for each distinct output of the original states.
  - Step 3: Distribute the incoming and outgoing transitions of the original states among the new states.
  - Step 4: Assign the output of each new state according to the original state's output.
  - Step 5: Remove any unreachable or redundant states.

- For example, consider the following Mealy machine:

  Mealy machine

  - Step 1: The states q1 and q2 have more than one output associated with them.
  - Step 2: We create four new states: q1a, q1b, q2a, and q2b.
  - Step 3: We distribute the transitions as follows:

    - q0 -> q1a on input 0
    - q0 -> q2a on input 1
    - q1a -> q1b on input 0
    - q1a -> q2a on input 1
    - q1b -> q1b on input 0
    - q1b -> q2a on input 1
    - q2a -> q1a on input 0
    - q2a -> q2b on input 1
    - q2b -> q1a on input 0
    - q2b -> q2b on input 1

  - Step 4: We assign the output of each new state as follows:

    - q1a and q2a have output 0
    - q1b and q2b have output 1

  - Step 5: We remove any unreachable or redundant states. In this case, there are none.

  - The resulting Moore machine is:

    Moore machine

## Conversion from Moore to Mealy Machine

- The general method to convert a Moore machine to a Mealy machine is as follows :

  - Step 1: Identify the states that have the same output and are reachable from each other by the same input.
  - Step 2: Merge those states into one state and assign the output to the corresponding transition.
  - Step 3: Remove any unreachable or redundant states.

- For example, consider the following Moore machine:

  Moore machine

  - Step 1: The states q1 and q2 have the same output 0 and are reachable from each other by input 0. The states q3 and q4 have the same output 1 and are reachable from each other by input 1.
  - Step 2: We merge q1 and q2 into one state q12 and assign the output 0 to the transition on input 0. We merge q3 and q4 into one state q34 and assign the output 1 to the transition on input 1.
  - Step 3: We remove any unreachable or redundant states. In this case, there are none.

  - The resulting Mealy machine is:

    Mealy machine

: https://math.stackexchange.com/questions/268888/my-moore-and-mealy-machines-look-the-same-why



# Minimization of Finite Automata

Minimization of finite automata is the process of finding an equivalent finite automaton with the minimum number of states for a given finite automaton. Minimizing a finite automaton can reduce the complexity and size of the automaton, and improve the efficiency of operations such as recognition, equivalence checking, and conversion to regular expressions.

There are different methods for minimizing finite automata, such as the partitioning method, the table-filling method, and the Hopcroft's algorithm. These methods are based on the concept of equivalence classes of states, which are sets of states that have the same behavior for any input string.

The partitioning method is a simple and intuitive method that iteratively divides the set of states into smaller subsets based on their equivalence. The initial partition consists of two subsets: the set of final states and the set of non-final states. Then, for each subset, the method checks if there are any states that can be distinguished by some input symbol, and splits the subset accordingly. This process is repeated until no more splits are possible, and the final partition represents the equivalence classes of states. The minimized automaton is obtained by replacing each subset with a single state, and preserving the transitions and final states.

The table-filling method is a more efficient method that uses a two-dimensional table to store the information about the distinguishability of states. The table has one entry for each pair of states, and is initially filled with zeros. The method marks the pairs of states that are obviously distinguishable, such as final and non-final states, with ones. Then, for each pair of states that are not marked, the method checks if there is any input symbol that leads them to a marked pair of states, and marks them accordingly. This process is repeated until no more changes are made to the table, and the unmarked pairs of states represent the equivalence classes of states. The minimized automaton is obtained by merging each unmarked pair of states into a single state, and preserving the transitions and final states.

Hopcroft's algorithm is a more advanced method that uses a data structure called a partition refinement to store the information about the equivalence classes of states. The algorithm starts with the same initial partition as the partitioning method, and then refines it by splitting each subset based on the transitions to other subsets. The algorithm uses a queue to store the subsets that need to be processed, and a hash table to store the inverse transitions for each subset. The algorithm terminates when the queue is empty, and the final partition represents the equivalence classes of states. The minimized automaton is obtained by replacing each subset with a single state, and preserving the transitions and final states.

The benefits of minimizing a finite automaton are:

- It reduces the compile time, as it removes identical or redundant operations.
- It simplifies the analysis and verification of the automaton, as it eliminates unreachable or useless states.
- It facilitates the conversion of the automaton to other representations, such as regular expressions or grammars, as it reduces the number of symbols and rules.



# Myhill-Nerode Theorem

- The Myhill-Nerode theorem is a fundamental result in the theory of regular languages. It provides a necessary and sufficient condition for a language to be regular  .
- The theorem is based on the notion of **equivalence classes** of strings with respect to a language. Two strings are said to be **equivalent** with respect to a language if they can be extended by the same set of strings to form words in the language  .
- Formally, for a language L, we define an equivalence relation ~L on the set of all strings as follows:

  - For any two strings x and y, x ~L y if and only if for all strings z, xz is in L if and only if yz is in L  .

- The equivalence relation ~L partitions the set of all strings into disjoint subsets called **equivalence classes**. Each equivalence class contains all the strings that are equivalent to each other with respect to L  .
- The Myhill-Nerode theorem states that:

  - A language L is regular if and only if it has a finite number of equivalence classes under ~L, and moreover, that this number is equal to the number of states in the minimal deterministic finite automaton (DFA) accepting L  .

- The Myhill-Nerode theorem can be used to:

  - Prove that a language L is regular by showing that it has a finite number of equivalence classes under ~L. This can be done by an exhaustive case analysis in which, beginning from the empty string, distinguishing extensions are used to find additional equivalence classes until no more can be found  .
  - Prove that a language L is not regular by showing that it has an infinite number of equivalence classes under ~L. This can be done by finding an infinite set of strings that are pairwise inequivalent with respect to L  .
  - Find the minimal number of states in a DFA that recognizes L by finding the number of equivalence classes under ~L. This can be done by constructing a DFA that has one state for each equivalence class, and transitions that correspond to the extensions that preserve the equivalence  .



# Simulation of DFA and NFA

- A **deterministic finite automaton (DFA)** is a finite state machine that accepts or rejects a given string of symbols, by running through a state sequence uniquely determined by the string.
- A **nondeterministic finite automaton (NFA)** is a finite state machine where, from each state, there can be more than one possible next state for a given input symbol, or no next state at all.
- Both DFA and NFA can be used to recognize the same set of regular languages, but they may differ in the number of states and transitions they require.
- To simulate a DFA, we need to keep track of the current state and the input string, and follow the transition function for each input symbol until we reach the end of the string or a state with no outgoing transition. Then we check if the final state is an accepting state or not.
- To simulate an NFA, we need to keep track of all the possible current states and the input string, and follow all the possible transitions for each input symbol until we reach the end of the string or no more transitions are possible. Then we check if any of the final states is an accepting state or not.
- To convert an NFA to an equivalent DFA, we can use the **subset construction** algorithm, which creates a new state in the DFA for each subset of states in the NFA, and defines the transition function based on the union of the transitions of the NFA states in each subset.
- To convert a DFA to an equivalent NFA, we can simply copy the states, transitions, and accepting states of the DFA, since every DFA is also an NFA.



## Unit 2 - Regular Expressions and Languages

- A regular expression is a concise way of describing a set of strings that share a common pattern.
- A regular expression can be used to specify the syntax of a language, to search for patterns in a text, or to validate user input.
- A regular expression consists of symbols that represent characters, sets of characters, or operations on sets of characters.
- The basic symbols of regular expressions are:

  - **Literals**: Any character that represents itself, such as `a`, `b`, `1`, `#`, etc.
  - **Wildcards**: A special character that matches any character, such as `.` (dot).
  - **Character classes**: A set of characters enclosed in square brackets that matches any character in the set, such as `[abc]`, `[0-9]`, `[A-Z]`, etc. A character class can also be negated by using a caret (`^`) as the first character, such as `[^abc]`, which matches any character except `a`, `b`, or `c`.
  - **Quantifiers**: Symbols that specify how many times a character or a group of characters can be repeated, such as `*` (zero or more times), `+` (one or more times), `?` (zero or one time), `{n}` (exactly n times), `{n,m}` (at least n and at most m times), etc.
  - **Grouping**: Parentheses that enclose a subexpression and treat it as a single unit, such as `(ab)+`, which matches one or more repetitions of `ab`.
  - **Alternation**: A vertical bar (`|`) that separates two or more alternatives, such as `a|b`, which matches either `a` or `b`.
  - **Anchors**: Symbols that indicate the position of a match, such as `^` (beginning of a line), `$` (end of a line), `\b` (word boundary), etc.

- A regular expression can be converted into a finite automaton, which is a mathematical model of computation that consists of a finite set of states, a finite set of input symbols, a transition function that maps a state and an input symbol to a new state, a start state, and a set of final states.
- A finite automaton can be either deterministic (DFA) or nondeterministic (NFA). A DFA has exactly one transition for each state and input symbol, while an NFA can have zero, one, or more transitions for each state and input symbol. An NFA can also have epsilon transitions, which are transitions that do not consume any input symbol.
- A DFA can recognize a regular language, which is a set of strings that can be described by a regular expression. A regular language can also be defined by using closure properties, such as union, concatenation, star, complement, intersection, etc.
- An NFA can also recognize a regular language, and every NFA can be converted into an equivalent DFA using the subset construction algorithm, which constructs a new state for each subset of states of the NFA, and defines the transitions and final states accordingly.
- A regular expression can also be converted into an NFA using the Thompson's construction algorithm, which constructs a new NFA for each symbol or operation of the regular expression, and combines them using epsilon transitions.



Hello, I am Sydney, your AI assistant. I can help you with your study material on regular expressions and languages. Here are some notes for Unit 2:

# Regular Expressions and Languages

- A regular expression is a concise and flexible way to describe patterns of strings.
- A regular expression can be defined recursively as follows:
  - The empty set Ø, the empty string ε, and any single symbol a are regular expressions.
  - If r and s are regular expressions, then so are (r + s), (r · s), and (r*), where + denotes union, · denotes concatenation, and * denotes Kleene closure.
  - Nothing else is a regular expression.
- A regular expression r denotes a language L(r) defined as follows:
  - L(Ø) = Ø, the empty set.
  - L(ε) = {ε}, the set containing only the empty string.
  - L(a) = {a}, the set containing only the symbol a.
  - L(r + s) = L(r) ∪ L(s), the union of the languages denoted by r and s.
  - L(r · s) = L(r) · L(s), the concatenation of the languages denoted by r and s.
  - L(r*) = L(r)*, the Kleene closure of the language denoted by r.
- A language is called regular if it is denoted by some regular expression.
- Regular expressions can be simplified and manipulated using some algebraic laws, such as:
  - r + s = s + r (commutativity of union)
  - (r + s) + t = r + (s + t) (associativity of union)
  - r + r = r (idempotence of union)
  - r + Ø = r (identity for union)
  - r · s = s · r (commutativity of concatenation)
  - (r · s) · t = r · (s · t) (associativity of concatenation)
  - r · ε = ε · r = r (identity for concatenation)
  - r · Ø = Ø · r = Ø (annihilation for concatenation)
  - (r + s)* = r* · s* (distributivity of closure over union)
  - (r*)* = r* (closure of closure)
  - ε* = ε (closure of identity)
  - Ø* = ε (closure of empty set)
- Regular expressions can be represented by finite automata, which are abstract machines that can recognize regular languages.
- A finite automaton consists of a finite set of states, a finite set of input symbols, a transition function that maps states and symbols to states, a start state, and a set of final states.
- A finite automaton can be either deterministic (DFA) or nondeterministic (NFA). A DFA has exactly one transition for each state and symbol, while an NFA can have zero, one, or more transitions for each state and symbol.
- A finite automaton accepts an input string if there is a sequence of transitions from the start state to a final state that matches the input string. The language accepted by a finite automaton is the set of all strings that it accepts.
- Every NFA can be converted to an equivalent DFA using the subset construction algorithm, which constructs a new DFA whose states are subsets of the states of the NFA, and whose transitions are defined by the union of the transitions of the NFA states in each subset.
- Every DFA can be converted to an equivalent regular expression using the state elimination algorithm, which eliminates states one by one and replaces the transitions with regular expressions that denote the same language.



Hello, I am Sydney, your AI assistant. I can help you with your query.

# Transition Graph for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- A transition graph is a special kind of flowchart for language analysis that represents a finite automaton  .
- A transition graph consists of three things:
  - A finite set of states, at least one of which is designated the start state and some of which are designated as final states.
  - An alphabet Σ of possible input symbols from which the input strings are formed.
  - A set of transitions, each of which is a directed edge from one state to another, labeled with an input symbol or ε (the empty string).
- A transition graph can be interpreted as an algorithm that recognizes a language by starting from the start state and following the transitions according to the input symbols until reaching a final state or a dead state.
- A dead state is a state that has no outgoing transitions or only has transitions to itself.
- A transition graph can also be represented using a transition table, which is a table that shows the next state for each state and input symbol.
- A transition graph can be used to visualize and analyze the behavior and properties of a finite automaton, such as its accepted language, its equivalence or minimization, its determinism or nondeterminism, etc    .
- Here is an example of a transition graph and its corresponding transition table for a finite automaton that accepts the language L = {w | w contains at least two 0s and at most one 1} over the alphabet Σ = {0, 1}:

transition graph

| State | 0 | 1 |
| ----- | - | - |
| q0    | q1| q3|
| q1    | q2| q4|
| q2    | q2| q4|
| q3    | q4| q5|
| q4    | q4| q5|
| q5    | q5| q5|

- In this transition graph, q0 is the start state, q2 and q4 are the final states, and q5 is the dead state.
- For example, the input string 0010 is accepted by this finite automaton, because it follows the transitions q0 -> q1 -> q2 -> q4 -> q5, and q4 is a final state.
- However, the input string 0101 is not accepted by this finite automaton, because it follows the transitions q0 -> q3 -> q4 -> q5 -> q5, and q5 is not a final state.



# Kleene's Theorem

- Kleene's theorem is a fundamental result in the theory of automata and formal languages that shows the equivalence between regular languages, regular expressions, and finite automata.
- Kleene's theorem consists of two parts: 
  - Part 1: For any regular expression of a language, there exists a finite automaton (either deterministic or nondeterministic) that recognizes the same language.
  - Part 2: For any finite automaton (either deterministic or nondeterministic) that recognizes a language, there exists a regular expression that describes the same language.
- Kleene's theorem can be used to prove that various operations on regular languages, such as union, intersection, complement, concatenation, and Kleene star, are also regular.
- Kleene's theorem can also be used to show that some languages are not regular, by showing that there is no regular expression or finite automaton that can describe them.
- Kleene's theorem can be proved by constructing algorithms that can convert any regular expression to a finite automaton, and vice versa, using the following steps:
  - To convert a regular expression to a finite automaton, use the following rules:
    - For the empty set ∅, construct a finite automaton with one state and no transitions.
    - For the empty string ε, construct a finite automaton with two states and one transition labeled ε from the initial state to the final state.
    - For any symbol a, construct a finite automaton with two states and one transition labeled a from the initial state to the final state.
    - For any two regular expressions R and S, construct a finite automaton for R + S (union) by creating a new initial state and a new final state, and adding ε-transitions from the new initial state to the initial states of R and S, and from the final states of R and S to the new final state.
    - For any two regular expressions R and S, construct a finite automaton for RS (concatenation) by connecting the final state of R to the initial state of S with an ε-transition.
    - For any regular expression R, construct a finite automaton for R* (Kleene star) by creating a new initial state and a new final state, and adding ε-transitions from the new initial state to the initial state of R, from the final state of R to the new final state, and from the new final state to the new initial state.
  - To convert a finite automaton to a regular expression, use the following steps:
    - Eliminate all ε-transitions by replacing them with equivalent transitions labeled with symbols or regular expressions.
    - Eliminate all states except the initial state and the final state by applying the following rule: for any state q that is neither the initial state nor the final state, and has incoming transitions labeled R1, R2, ..., Rn from states p1, p2, ..., pn, and outgoing transitions labeled S1, S2, ..., Sm from states q1, q2, ..., qm, replace each pair of transitions pi → q → qj with a single transition pi → qj labeled with Ri(Sq)*Sj, where Sq is the regular expression on the self-loop of q, if any, or ε otherwise. Repeat this process until only the initial state and the final state remain.
    - The regular expression that describes the language of the finite automaton is the union of all the labels on the transitions from the initial state to the final state.



# Finite Automata and Regular Expression

- Finite automata are abstract machines that can recognize patterns in strings and accept or reject them based on some rules .
- Regular expressions are algebraic notations that can describe the set of strings accepted by finite automata .
- Regular expressions and finite automata are equivalent in expressive power, meaning that for every regular expression, there exists a finite automaton that accepts the same language, and vice versa   .
- There are two types of finite automata: deterministic finite automata (DFA) and nondeterministic finite automata (NFA). DFA have only one transition for each input symbol and state, while NFA can have multiple transitions or no transition for the same input symbol and state .
- NFA can also have epsilon transitions, which are transitions that do not consume any input symbol and can be taken spontaneously .
- Every NFA can be converted to an equivalent DFA using the subset construction algorithm, which creates a new state for each subset of states in the NFA .
- DFA can be minimized by eliminating unreachable states and merging equivalent states, which are states that have the same behavior for all input strings .
- Regular expressions can be constructed from finite automata using the state elimination method, which removes states one by one and replaces the transitions with equivalent regular expressions until only the initial and final states remain.
- Finite automata can be constructed from regular expressions using the state decomposition method, which breaks down the regular expression into simpler components and creates states and transitions accordingly.
- Regular expressions can be defined recursively using the following rules :
  - The empty set ∅, the empty string ε, and any single symbol a are regular expressions.
  - If r and s are regular expressions, then so are (r + s), (r.s), and (r*), where + denotes union, . denotes concatenation, and * denotes Kleene closure.
  - Nothing else is a regular expression.
- Regular languages are the languages that can be described by regular expressions or accepted by finite automata .
- Regular languages are closed under the regular operations of union, concatenation, and Kleene closure, meaning that applying these operations to regular languages results in another regular language.



# Arden's Theorem for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

- Arden's Theorem is a mathematical statement that helps to find the regular expression equivalent to a given finite automaton  .
- Arden's Theorem states that, if P and Q are two regular expressions over an alphabet , and if P does not contain the empty string , then the following equation in R given by R = Q + RP has a unique solution, that is, R = QP*  .
- The proof of Arden's Theorem is based on the following steps:
  - Show that R = QP* is a solution of R = Q + RP by substituting R = QP* in the equation and simplifying it.
  - Show that R = QP* is the only solution of R = Q + RP by assuming that there is another solution S and deriving a contradiction.
- Arden's Theorem can be used to find the regular expression of a finite automaton by following these steps :
  - Convert the finite automaton into a system of equations, where each equation corresponds to a state and has the form R = Q + RP, where R is the regular expression for the language accepted by that state, Q is the regular expression for the transitions from that state to itself, and P is the regular expression for the transitions from that state to other states.
  - Solve the system of equations using Arden's Theorem, starting from the final states and moving backwards to the initial state.
  - The regular expression for the language accepted by the finite automaton is the regular expression for the initial state.
- An example of using Arden's Theorem to find the regular expression of a finite automaton is given below:

Finite automaton

The system of equations for this finite automaton is:

q1 = q1.0 + q2.1

q2 = q1.1 + q2.0 + q3.0

q3 = q2.1 + q3.0 + q3.1

Using Arden's Theorem, we can solve the equations as follows:

q3 = (q2.1 + q3.0 + q3.1)*

q2 = (q1.1 + q2.0 + q3.0)*

q1 = q1.0 + q2.1

q1 = (q1.0 + q2.1)*

q1 = (0 + (q1.1 + q2.0 + q3.0)*.1)*

q1 = (0 + (0 + (q1.1 + q2.0 + q3.0)*.1)*.1 + (q2.1 + q3.0 + q3.1)*.0)*

q1 = (0 + 1(0 + 1)*.1 + (1(0 + 1)*.1 + 0 + 1)*.0)*

The regular expression for the language accepted by the finite automaton is q1, which is:

(0 + 1(0 + 1)*.1 + (1(0 + 1)*.1 + 0 + 1)*.0)*



# Algebraic Method Using Arden’s Theorem

- Arden’s theorem is a mathematical statement that can be used to find the regular expression of a finite automaton.
- Arden’s theorem states that if P and Q are two regular expressions over an alphabet Σ, and if P does not contain the empty string ε, then the following equation in R given by R = Q + RP has a unique solution, i.e., R = QP*  .
- That means, whenever we get any equation in the form of R = Q + RP, then we can directly replace it with R = QP*.
- Arden’s theorem can be proved by using the properties of regular expressions and induction.
- Arden’s theorem can be applied to convert a given finite automaton to a regular expression by following these steps :
  - Step 1: Write the transition function of the finite automaton as a system of equations in terms of regular expressions. For example, if δ(qi, a) = qj, then write qi = qi.a + qj.
  - Step 2: Eliminate the states one by one using Arden’s theorem, until only the initial and final states remain. For example, if qk = qk.b + ql, then replace qk with ql.b* in all other equations.
  - Step 3: The regular expression of the finite automaton is the solution of the equation corresponding to the initial state. For example, if q0 is the initial state and qf is the final state, then the regular expression is q0.qf*.
- Arden’s theorem can also be used to solve some challenging problems involving regular expressions and finite automata. For example, finding the number of strings accepted by a finite automaton, finding the shortest string accepted by a finite automaton, finding the intersection or union of two regular expressions, etc.



# Regular and Non-Regular Languages

- A **regular language** is a language that can be expressed with a **regular expression** or a **finite automaton**.
- A **regular expression** is a sequence of symbols that defines a **pattern** for matching strings.
- A **finite automaton** is a mathematical model of computation that has a finite number of **states** and can change its state based on the input symbols.
- A **non-regular language** is a language that **cannot** be expressed with a regular expression or a finite automaton.
- A non-regular language may require **infinite memory** or **unbounded counting** to recognize .
- Examples of regular languages are:
  - All strings of length 2 over {a, b}* i.e. L = {aa, ab, ba, bb}
  - All strings that start and end with the same symbol over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaa, bbb, ...}
  - All strings that contain an even number of 0s over {0, 1}* i.e. L = {1, 01, 10, 11, 001, 010, 100, 101, 110, 111, ...}
- Examples of non-regular languages are:
  - All strings that have equal number of a's and b's over {a, b}* i.e. L = {ab, ba, aabb, abab, baba, bbaa, ...}
  - All strings that are palindromes over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaaa, bbbb, abba, baab, ...}
  - All strings of the form a^n b^n over {a, b}* i.e. L = {ab, aabb, aaabbb, aaaabbbb, ...}



# Closure properties of Regular Languages

- Closure properties on regular languages are defined as certain operations on a language, resulting in a new language that is of the same "type" as the original language, i.e., regular  .
- Regular languages are closed under the following operations  :
  - Union: If L1 and L2 are regular languages, then L1 ∪ L2 is also regular.
  - Intersection: If L1 and L2 are regular languages, then L1 ∩ L2 is also regular.
  - Complement: If L is a regular language, then L is also regular.
  - Difference: If L1 and L2 are regular languages, then L1 - L2 is also regular.
  - Concatenation: If L1 and L2 are regular languages, then L1L2 is also regular.
  - Kleene star: If L is a regular language, then L* is also regular.
  - Kleene plus: If L is a regular language, then L+ is also regular.
  - Reversal: If L is a regular language, then LR is also regular, where LR is the language obtained by reversing the strings of L.
  - Homomorphism: If L is a regular language and h is a homomorphism, then h(L) is also regular, where h(L) is the language obtained by applying h to each string of L.
  - Inverse homomorphism: If L is a regular language and h is a homomorphism, then h-1(L) is also regular, where h-1(L) is the language obtained by applying the inverse of h to each string of L.
- To prove the closure properties of regular languages, we can use any of its representations, such as regular expressions, finite automata, or regular grammars, and show that the operation on the languages can be performed using the corresponding representation.



# Pigeonhole Principle

The pigeonhole principle is a simple but powerful idea that can be used to prove the existence of certain mathematical facts. It can also be applied to problems in computer science, cryptography, combinatorics, and other fields.

The basic idea of the pigeonhole principle is that if we have more items than containers, then at least one container must hold more than one item. For example, if we have 10 pigeons and 9 holes, then at least one hole must have more than one pigeon. This is illustrated in the figure below.

Pigeonhole principle example

The pigeonhole principle can be stated formally as follows:

- If n items are put into m containers, with n > m, then at least one container must contain more than one item.

The pigeonhole principle can also be generalized to different situations, such as:

- If n items are put into m containers, with n > km, where k is a positive integer, then at least one container must contain more than k items.
- If n items are put into m containers, and n/k is not an integer, where k is a positive integer, then at least one container must contain strictly more than n/k items.

Some examples of applying the pigeonhole principle are:

- If 5 people have birthdays in a year, then at least two of them have their birthdays in the same month, since there are 12 months and 5 > 12.
- If 13 cards are drawn from a standard 52-card deck, then at least two of them have the same suit, since there are 4 suits and 13 > 4.
- If 10 points are placed within a unit equilateral triangle, then there exists two points with distance at most 1/3 apart, since we can divide the triangle into 9 smaller equilateral triangles of side length 1/3, and 10 > 9.

The pigeonhole principle is a useful tool for proving the existence of certain mathematical objects or properties, but it does not tell us how to find them or construct them. For example, the pigeonhole principle tells us that there must be two people in the world with the same number of hairs on their head, but it does not tell us who they are or how to find them.



# Pumping Lemma for Regular Languages

- The pumping lemma for regular languages is a theorem that describes a property of all regular languages.
- A regular language is a language that can be recognized by a finite automaton or generated by a regular expression.
- The pumping lemma states that for any regular language L, there exists a constant p (called the pumping length) such that any string w in L with length at least p can be divided into three substrings, w = xyz, where:
  - |y| > 0 (y is not empty)
  - |xy| <= p (y is a prefix of w)
  - xy^i z is in L for all i >= 0 (y can be repeated any number of times)
- The pumping lemma can be used to prove that a language is not regular by showing a contradiction. That is, by finding a string w in the language that does not satisfy the pumping lemma property for any choice of x, y, and z.
- For example, consider the language L = {a^n b^n | n >= 0} over the alphabet {a, b}. This language is not regular, and we can prove it using the pumping lemma as follows:
  - Assume L is regular, and let p be the pumping length.
  - Choose w = a^p b^p, which is in L and has length 2p >= p.
  - By the pumping lemma, w can be written as xyz, where |y| > 0, |xy| <= p, and xy^i z is in L for all i >= 0.
  - Since |xy| <= p, y must consist of only a's, say y = a^k, where 0 < k <= p.
  - Then, x = a^m, z = a^(p-m-k) b^p, where 0 <= m < p and m + k <= p.
  - Now, consider xy^2 z = xyyz = a^m a^k a^k a^(p-m-k) b^p = a^(p+k) b^p, which has length 2p + k > 2p.
  - This string is not in L, because it has more a's than b's, which contradicts the pumping lemma.
  - Therefore, L is not regular.



# Application of Pumping Lemma

- The pumping lemma is a property of regular languages that states that any sufficiently long string in a regular language can be divided into three parts, such that the middle part can be repeated any number of times and the resulting string will still belong to the language  .
- The pumping lemma can be used to prove that certain languages are not regular, by showing a contradiction. If a language is regular, it must satisfy the pumping lemma, but if it does not satisfy the pumping lemma, it is non-regular  .
- The pumping lemma can also be used to find the minimum number of states in a deterministic finite automaton (DFA) that recognizes a regular language, by using the pumping length as a lower bound.
- The pumping lemma can also be used to compare the expressive power of different classes of languages, such as context-free languages and context-sensitive languages, by showing that some languages that satisfy the pumping lemma for regular languages do not satisfy the pumping lemma for other classes of languages.

## Example of using the pumping lemma to prove a language is non-regular

- Consider the language L = {a^n b^n | n >= 0} over the alphabet {a, b}. We will show that L is not regular by using the pumping lemma.
- Suppose L is regular, then there exists a pumping length p such that any string in L of length at least p can be divided into three parts, x, y, and z, such that xy^i z is in L for any i >= 0, and |xy| <= p and |y| > 0.
- Let s = a^p b^p be a string in L of length 2p >= p. Then s can be divided into x, y, and z as described above. Since |xy| <= p, x and y must consist of only a's. Let x = a^k and y = a^l, where k + l <= p and l > 0. Then z = a^(p-k-l) b^p.
- Now consider the string xy^2 z, which is obtained by repeating y once. This string is equal to a^(k+2l) a^(p-k-l) b^p = a^(p+l) b^p. This string is not in L, because the number of a's and b's are not equal. This contradicts the pumping lemma, which says that xy^2 z should be in L.
- Therefore, we have shown that L does not satisfy the pumping lemma, and hence L is not regular.



# Decidability

- Decidability is the property of a problem that can be solved by an algorithm in a finite number of steps.
- In terms of automata theory, decidability refers to the problem of testing whether a given model of computation, such as a finite automaton, a Turing machine, or a grammar, accepts a given input string or generates a given language.
- A problem is decidable if there exists a Turing machine that halts on every input and gives a correct answer (yes or no) for the problem.
- A language is decidable or recursive if there exists a Turing machine that accepts and halts on every string in the language, and rejects and halts on every string not in the language.
- A decidable language corresponds to an algorithmically solvable decision problem.
- Some examples of decidable problems in automata theory are:
  - A DFA: Given a deterministic finite automaton (DFA) and an input string, does the DFA accept the string?
  - A NFA: Given a nondeterministic finite automaton (NFA) and an input string, does the NFA accept the string?
  - E DFA: Given a DFA, is the language accepted by the DFA empty?
  - E Q DFA: Given two DFAs, do they accept the same language?
  - A CFG: Given a context-free grammar (CFG) and an input string, does the CFG generate the string?
- Some examples of undecidable problems in automata theory are:
  - A TM: Given a Turing machine and an input string, does the Turing machine accept the string?
  - E TM: Given a Turing machine, is the language accepted by the Turing machine empty?
  - E Q TM: Given two Turing machines, do they accept the same language?
  - A RE: Given a regular expression and an input string, does the regular expression match the string?
  - A CS: Given a context-sensitive grammar and an input string, does the grammar generate the string?
- Decidability is related to the concept of computability, which studies what kinds of functions can be computed by different models of computation.
- Decidability is also related to the concept of complexity, which studies how efficiently a problem can be solved by an algorithm, given the available resources such as time and space.



# Decision Properties for the Notes of the Unit 2 - Regular Expressions and Languages in the Subject of Theory of Automata and Formal Languages

- Decision properties are questions that can be answered yes or no for a given language or a class of languages.
- For example, given a regular expression R, is the language L(R) empty? Or, given two regular expressions R1 and R2, are the languages L(R1) and L(R2) equal?
- Decision properties are important for analyzing and manipulating languages and their representations, such as regular expressions and finite automata.
- Some common decision properties for regular languages are:

  - Emptiness: Given a regular expression R, is L(R) = ∅?
  - Non-emptiness: Given a regular expression R, is L(R) ≠ ∅?
  - Finiteness: Given a regular expression R, is L(R) finite?
  - Infiniteness: Given a regular expression R, is L(R) infinite?
  - Membership: Given a regular expression R and a string w, is w ∈ L(R)?
  - Equality: Given two regular expressions R1 and R2, is L(R1) = L(R2)?
  - Containment: Given two regular expressions R1 and R2, is L(R1) ⊆ L(R2)?
  - Disjointness: Given two regular expressions R1 and R2, is L(R1) ∩ L(R2) = ∅?

- All these decision properties are decidable for regular languages, meaning that there exists an algorithm that can answer them in finite time.
- One way to decide these properties is to convert the regular expressions to deterministic finite automata (DFA) and use the properties and operations of DFA to answer the questions.
- For example, to decide emptiness, we can convert R to a DFA A and check if the set of final states of A is empty or not.
- To decide equality, we can convert R1 and R2 to DFA A1 and A2 and check if the symmetric difference of L(A1) and L(A2) is empty or not. This can be done by constructing a DFA for L(A1) ∆ L(A2) and applying the emptiness test.
- To decide membership, we can convert R to a DFA A and simulate the input w on A and check if it reaches a final state or not.



# Finite Automata and Regular Languages

- A **regular language** is a set of strings that can be described by a simple pattern, such as a sequence of characters, a repetition of a substring, or a choice between alternatives.
- A **finite automaton** is a mathematical model of a machine that can recognize regular languages by moving through a finite number of states according to the input symbols.
- Finite automata and regular expressions are different ways to represent regular languages.
- A **regular expression** is a notation that uses symbols and operators to describe a regular language in a concise and algebraic way.
- The languages accepted by some regular expression are referred to as **regular languages**.
- Finite automata can be used to generate strings in a regular language. A finite automaton for a particular language is “programmed,” in a way, to generate the strings of a given language through its states and transition functions.
- There are two types of finite automata: **deterministic finite automata (DFA)** and **nondeterministic finite automata (NFA)**.
- A **DFA** is a finite automaton that has exactly one transition for each state and input symbol, and can be in only one state at a time.
- An **NFA** is a finite automaton that can have more than one transition for each state and input symbol, and can be in multiple states at a time.
- Every NFA can be converted to an equivalent DFA that accepts the same language, using a process called **subset construction** or **powerset construction**.
- Every DFA can be converted to an equivalent regular expression that describes the same language, using a process called **state elimination** or **Kleene's algorithm**.
- Every regular expression can be converted to an equivalent NFA that accepts the same language, using a process called **Thompson's construction**.
- Regular languages and finite automata can model computational problems that require a very small amount of memory. For example, a finite automaton can generate a regular language to describe if a light switch is on or off, but it cannot keep track of how many times the light was switched on or off.
- Regular languages and finite automata have limitations in their expressive power. They cannot recognize languages that require unbounded memory or recursion, such as the language of balanced parentheses or the language of palindromes.
- A language that is not regular is called a **non-regular language**. A tool to prove that a language is non-regular is the **pumping lemma for regular languages**, which states that if a language is regular, then there exists a constant p such that any string in the language of length at least p can be pumped, or repeated, without leaving the language.



# Regular Languages and Computers

- A regular language is a formal language that can be defined by a regular expression, in the strict sense in theoretical computer science.
- A regular expression is a sequence of symbols that specifies a pattern of characters to be matched in a text.
- A formal language is a set of strings over a finite alphabet.
- An alphabet is a finite set of symbols, such as {0, 1} or {a, b, c, ..., z}.
- A string is a finite sequence of symbols from an alphabet, such as 0101 or hello.
- A regular language can be recognized by a finite automaton, which is a mathematical model of computation that has a finite number of states and transitions between them .
- A finite automaton can be deterministic or nondeterministic, depending on whether it has at most one transition for each state and input symbol or not.
- A deterministic finite automaton (DFA) can be represented by a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states
  - Σ is a finite alphabet
  - δ is a transition function that maps Q × Σ to Q
  - q0 is the initial state
  - F is a subset of Q that contains the final or accepting states
- A nondeterministic finite automaton (NFA) can be represented by a 5-tuple (Q, Σ, δ, q0, F), where:
  - Q is a finite set of states
  - Σ is a finite alphabet
  - δ is a transition function that maps Q × Σ to P(Q), where P(Q) is the power set of Q
  - q0 is the initial state
  - F is a subset of Q that contains the final or accepting states
- A finite automaton accepts a string if there is a sequence of transitions from the initial state to a final state that corresponds to the symbols of the string.
- A finite automaton recognizes a language if it accepts all and only the strings that belong to the language.
- A language is regular if and only if it can be recognized by a finite automaton.
- Regular languages have many applications in computer science, such as :
  - Parsing and designing programming languages
  - Searching and matching text patterns
  - Encoding and compressing data
  - Modeling and verifying finite-state systems
  - Solving combinatorial problems with regular constraints



# Simulation of Transition Graph and Regular Language

- A transition graph is a graphical representation of a finite automaton, which consists of a set of states, a set of input symbols, a start state, a set of final states, and a transition function that maps each state and input symbol to a next state.
- A regular language is a language that can be recognized by a finite automaton, or equivalently, that can be described by a regular expression.
- A regular expression is a notation for specifying a set of strings using symbols, operators, and parentheses.
- The simulation of a transition graph and a regular language is the process of checking whether a given string belongs to the language accepted by the graph, by following the transitions from the start state to a final state according to the input symbols.
- The simulation can be done in two ways: by using a transition table or by using a generalized transition graph .

## Transition Table

- A transition table is a tabular representation of a transition graph, where each row corresponds to a state, each column corresponds to an input symbol, and each entry shows the next state for that state and symbol.
- A transition table can be used to simulate a transition graph and a regular language by following these steps:
  - Start from the row that corresponds to the start state of the graph.
  - Read the input string from left to right, and for each symbol, move to the row that corresponds to the next state given by the entry in the current row and column.
  - If the input string is exhausted and the current row corresponds to a final state of the graph, then the string is accepted by the graph and belongs to the language. Otherwise, the string is rejected by the graph and does not belong to the language.

## Generalized Transition Graph

- A generalized transition graph is an extension of a transition graph, where the labels on the transitions can be regular expressions instead of single symbols.
- A generalized transition graph can be used to simulate a transition graph and a regular language by following these steps:
  - Start from the initial state of the graph.
  - Read the input string from left to right, and for each symbol, find a transition from the current state that has a label that matches the symbol or a prefix of the remaining input string. If there is more than one such transition, choose any one of them.
  - Move to the next state given by the chosen transition, and remove the matched prefix from the input string.
  - If the input string is empty and the current state is a final state of the graph, then the string is accepted by the graph and belongs to the language. Otherwise, the string is rejected by the graph and does not belong to the language.



## Unit 3 - Regular and Non-Regular Grammars

- A grammar is a set of rules that defines how a language is generated from a finite alphabet of symbols.
- A grammar consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- A production rule is of the form A -> B, where A is a non-terminal symbol and B is a string of terminal and/or non-terminal symbols.
- A grammar can be used to derive strings of the language by starting from the start symbol and applying production rules until only terminal symbols are left.
- A grammar is said to be regular if it has only production rules of the form A -> a or A -> aB, where A and B are non-terminal symbols and a is a terminal symbol.
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton.
- A grammar is said to be non-regular if it has production rules that are not of the form A -> a or A -> aB.
- A non-regular grammar can generate a non-regular language, which is a language that cannot be recognized by a finite automaton.
- An example of a regular grammar is G = ({a, b}, {S, A}, S, {S -> aA, A -> b, A -> bA}), which generates the language L(G) = {ab, abb, abbb, ...}.
- An example of a non-regular grammar is G = ({a, b}, {S}, S, {S -> aSb, S -> epsilon}), which generates the language L(G) = {a^n b^n | n >= 0}, where epsilon is the empty string.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of context free grammar (CFG) for the notes of the unit 3 - regular and non-regular grammars in the subject of theory of automata and formal languages.

# Context Free Grammar (CFG)

- A context free grammar (CFG) is a set of rules that defines a language by specifying how any valid string can be derived from a special symbol called the start symbol.
- A CFG consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- Terminal symbols are the basic symbols that appear in the strings of the language. They cannot be further divided or replaced by any rules.
- Non-terminal symbols are placeholders that can be replaced by a combination of terminal and non-terminal symbols according to the production rules.
- The start symbol is a special non-terminal symbol that represents the whole language. Every valid string of the language can be derived from the start symbol by applying the production rules repeatedly.
- Production rules are the rules that specify how a non-terminal symbol can be replaced by a sequence of terminal and non-terminal symbols. They have the form A -> α, where A is a non-terminal symbol and α is a string of terminal and non-terminal symbols (possibly empty).
- A derivation is a sequence of strings that shows how a start symbol can be transformed into a terminal string by applying the production rules. Each string in the derivation is derived from the previous one by replacing one non-terminal symbol with its right-hand side in a production rule.
- A language is said to be context free if it can be generated by a CFG. That is, if there exists a CFG such that every string in the language can be derived from the start symbol of the CFG, and every string that can be derived from the start symbol of the CFG is in the language.
- CFGs are more expressive than regular grammars, which are a subset of CFGs that have more restrictions on the form of the production rules. Regular grammars can only generate regular languages, which are a proper subset of context free languages.
- CFGs can be used to model the syntax of natural languages, programming languages, and other structured data. They can also be used to define parsing algorithms that can check if a given string belongs to a language and construct a parse tree that shows the structure of the string.



# Definition for the notes of the Unit 3 - Regular and Non-regular Grammars in the subject of Theory of Automata and Formal Languages

- A **regular grammar** is a formal grammar that can generate only regular languages, which are a subset of context-free languages.
- A regular grammar can be either **right-regular** or **left-regular**, depending on the position of the non-terminal symbol in the production rules.
- A **right-regular grammar** has production rules of the form `A -> a`, `A -> aB`, or `A -> ε`, where `A` and `B` are non-terminal symbols, `a` is a terminal symbol, and `ε` is the empty string.
- A **left-regular grammar** has production rules of the form `A -> a`, `A -> Ba`, or `A -> ε`, where `A` and `B` are non-terminal symbols, `a` is a terminal symbol, and `ε` is the empty string.
- A regular grammar is **unambiguous** if there is only one production rule for each non-terminal symbol, and **ambiguous** otherwise.
- A **non-regular grammar** is a formal grammar that can generate languages that are not regular, such as context-free languages, context-sensitive languages, or recursively enumerable languages.
- A non-regular grammar can have production rules that do not follow the restrictions of regular grammars, such as `A -> aBb`, `A -> BC`, or `A -> a^n b^n`, where `A`, `B`, and `C` are non-terminal symbols, `a` and `b` are terminal symbols, and `n` is a positive integer.
- A non-regular grammar can be **ambiguous** if there is more than one way to derive a string from the start symbol, or **unambiguous** otherwise.



# Derivations for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A **derivation** is a process of generating a string from a grammar by applying production rules.
- A **derivation tree** is a graphical representation of a derivation, where each node is a symbol and each branch is a production rule.
- A **regular grammar** is a type of grammar that can generate only regular languages, which are languages that can be recognized by finite automata.
- A **non-regular grammar** is a type of grammar that can generate languages that are not regular, which are languages that cannot be recognized by finite automata.
- A regular grammar can be either **left-regular** or **right-regular**, depending on whether the production rules have the non-terminal symbol on the left or right side of the arrow.
- A left-regular grammar has the following form: A -> aB | a | epsilon, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A right-regular grammar has the following form: A -> Ba | a | epsilon, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A regular grammar can be converted to a finite automaton by following these steps:
  - The number of states in the automaton will be equal to the number of non-terminals plus one.
  - Each state in the automaton represents each non-terminal in the regular grammar.
  - The additional state will be the final state of the automaton.
  - The initial state of the automaton will be the state corresponding to the start symbol of the grammar.
  - The transitions of the automaton will be determined by the production rules of the grammar.
  - If A -> aB is a rule, then there will be a transition from state A to state B labeled with a.
  - If A -> a is a rule, then there will be a transition from state A to the final state labeled with a.
  - If A -> epsilon is a rule, then state A will be a final state as well.
- A finite automaton can be converted to a regular grammar by following these steps:
  - The set of non-terminals of the grammar will be the set of states of the automaton.
  - The start symbol of the grammar will be the initial state of the automaton.
  - The production rules of the grammar will be determined by the transitions of the automaton.
  - If there is a transition from state A to state B labeled with a, then A -> aB will be a rule.
  - If state A is a final state, then A -> epsilon will be a rule as well.
- A **regular expression** is another way of describing a regular language, using symbols and operators to construct strings that belong to the language.
- A regular expression can be converted to a finite automaton by using the **Thompson's construction** algorithm, which builds a non-deterministic finite automaton (NFA) for each subexpression and combines them using epsilon transitions.
- A finite automaton can be converted to a regular expression by using the **Kleene's theorem**, which states that for any finite automaton, there exists a regular expression that generates the same language, and vice versa.
- A regular expression can be converted to a regular grammar by using the **Brzozowski's algorithm**, which constructs a right-regular grammar for each subexpression and combines them using non-terminals.
- A regular grammar can be converted to a regular expression by using the **Arden's lemma**, which states that for any equation of the form X = AX + B, where X, A, and B are sets of strings, there exists a unique solution X = A* B, where A* is the Kleene star operator.



# Languages

- In automata theory, a formal language is a set of strings of symbols drawn from a finite alphabet .
- A formal language can be specified either by a set of rules (such as regular expressions or a context-free grammar) that generates the language, or by a formal machine that accepts (recognizes) the language .
- A word is a finite string of symbols from the alphabet.
- A language is a set of words, which may be finite or infinite.
- A formal language is a mathematical object that can be studied and analyzed using various tools and techniques.
- Formal languages are classified into different types based on their expressive power and the complexity of the machines or rules that define them.
- Regular languages are the simplest and most restricted type of formal languages .
- Regular languages can be defined by regular expressions, finite automata, or regular grammars .
- Regular languages have many closure properties, such as being closed under union, intersection, complement, concatenation, and Kleene star.
- Non-regular languages are formal languages that are not regular.
- Non-regular languages cannot be defined by regular expressions, finite automata, or regular grammars.
- Non-regular languages can be recognized by more powerful machines, such as pushdown automata or Turing machines.
- Non-regular languages can be defined by more expressive rules, such as context-free grammars or recursively enumerable grammars.
- Non-regular languages have fewer closure properties than regular languages, such as being closed under union, concatenation, and Kleene star, but not under intersection or complement.
- Non-regular languages can be proved to be non-regular by using the pumping lemma or other methods.



# Derivation Trees and Ambiguity

- A derivation tree or parse tree is a graphical representation of the derivation of a string by a context-free grammar (CFG).
- A derivation tree shows how the start symbol of the grammar generates the string by applying the production rules in a hierarchical manner.
- A derivation tree has the following properties:
  - The root node is labeled with the start symbol of the grammar.
  - The internal nodes are labeled with the non-terminal symbols of the grammar.
  - The leaf nodes are labeled with the terminal symbols or the empty string of the grammar.
  - The order of the children of a node corresponds to the order of the symbols in the right-hand side of the production rule used to expand the node.
  - The concatenation of the labels of the leaf nodes from left to right gives the derived string.
- A derivation tree can be obtained from either a leftmost derivation or a rightmost derivation of the string, where the leftmost (or rightmost) non-terminal symbol is replaced at each step.
- A derivation tree is unique for a given derivation, but a string may have more than one derivation and hence more than one derivation tree by a CFG.
- A CFG is said to be ambiguous if there exists at least one string that has more than one derivation tree by the grammar.
- Ambiguity is a property of grammars, not languages. A language may have both ambiguous and unambiguous grammars.
- Some languages are inherently ambiguous, meaning that there is no unambiguous grammar for them.
- Ambiguity can cause problems in parsing and interpretation of strings, as different derivations may lead to different meanings or structures.
- Ambiguity can be resolved or reduced by using precedence rules, associativity rules, parentheses, or other conventions to disambiguate the grammar or the string.



# Regular Grammars

- A regular grammar is a grammar that is right-regular or left-regular.
- A grammar is right-regular if all production rules have at most one non-terminal symbol and that symbol is always at the end of the rule's right-hand side.
- A grammar is left-regular if all production rules have at most one non-terminal symbol and that symbol is always at the start of the rule's right-hand side.
- A regular grammar can be formally defined as a mathematical object, G, with four components, G = (N, Σ, P, S), where :
  - N is a nonempty, finite set of non-terminal symbols
  - Σ is a finite set of terminal symbols, or alphabet, symbols
  - P is a finite set of production rules of the form A → xB or A → x, where A and B are non-terminal symbols and x is a string of terminal symbols
  - S is a special non-terminal symbol called the start symbol
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton.
- A regular grammar can be converted to a regular expression, which is a concise way of describing a regular language using symbols and operators.
- A regular grammar can also be converted to a right-linear grammar or a left-linear grammar, which are equivalent forms of regular grammar with different conventions for the placement of non-terminal symbols.



# Right Linear and Left Linear Grammars

- A **linear grammar** is a type of context-free grammar in which the right-hand side of every production rule consists of at most one non-terminal symbol, possibly preceded and/or followed by some terminal symbols.
- A **right linear grammar** is a linear grammar in which the non-terminal symbol, if present, is always at the right end of the right-hand side of every production rule. For example, A -> aB | a | epsilon is a right linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- A **left linear grammar** is a linear grammar in which the non-terminal symbol, if present, is always at the left end of the right-hand side of every production rule. For example, A -> Ba | a | epsilon is a left linear grammar, where A and B are non-terminals, a is a terminal, and epsilon is the empty string.
- Right linear and left linear grammars are equivalent in expressive power, meaning that they can generate the same set of languages, which are precisely the **regular languages** .
- To convert a right linear grammar to a left linear grammar, we can use the following steps :
  - Reverse every terminal symbol in the right-hand side of every production rule. For example, A -> aB becomes A -> Ba, and B -> ab becomes B -> ba.
  - Replace every non-terminal symbol in the right-hand side of every production rule with a new non-terminal symbol that corresponds to the reverse of the original non-terminal symbol. For example, A -> Ba becomes A -> aB', and B -> ba becomes B -> abB'.
  - Add a new start symbol S and a new production rule S -> aA', where A' is the reverse of the original start symbol A.
  - Eliminate any epsilon productions by removing them and adding new production rules that skip the non-terminal symbol that produces epsilon. For example, if B -> epsilon, then remove it and add A -> a for every production rule of the form A -> aB.
- To convert a left linear grammar to a right linear grammar, we can use the same steps but in reverse order :
  - Eliminate any epsilon productions by removing them and adding new production rules that skip the non-terminal symbol that produces epsilon. For example, if B -> epsilon, then remove it and add A -> a for every production rule of the form A -> Ba.
  - Add a new start symbol S and a new production rule S -> A'a, where A' is the reverse of the original start symbol A.
  - Replace every non-terminal symbol in the left-hand side of every production rule with a new non-terminal symbol that corresponds to the reverse of the original non-terminal symbol. For example, A -> Ba becomes B' -> aA, and B -> ab becomes B' -> bA.
  - Reverse every terminal symbol in the left-hand side of every production rule. For example, B' -> aA becomes B' -> Aa, and B' -> bA becomes B' -> Ab.



# Conversion of FA into CFG and Regular grammar into FA

## FA into CFG

- A finite automaton (FA) is a model of computation that accepts or rejects a string based on its transitions between a finite set of states and a finite alphabet of symbols.
- A context-free grammar (CFG) is a set of production rules that generate a language by applying substitutions to a start symbol.
- To convert a FA into a CFG, we can follow these steps:
  - For each state q of the FA, introduce a new variable Q in the CFG.
  - The variable corresponding to the starting state of the FA will be the starting variable of the CFG.
  - For each transition q -> r labeled by a symbol a in the FA, add a production rule Q -> aR in the CFG, where Q and R are the variables corresponding to q and r, respectively.
  - For each final state q of the FA, add a production rule Q -> epsilon in the CFG, where Q is the variable corresponding to q and epsilon is the empty string.
- Example: Consider the following FA that accepts the language of all strings over {0,1} that end with 1.

FA

- By applying the above algorithm, we get the following CFG with the starting variable S and the following rules:

```
S -> 0E | 1D
E -> 0E | 1D
D -> 0E | 1D | epsilon
```

- To derive a word in the CFG, we can follow the transitions of the FA and apply the corresponding rules. For example, to derive the word 011, we can do:

```
S -> 0E -> 01D -> 011
```

## Regular grammar into FA

- A regular grammar is a special type of CFG that has the following restrictions on its production rules:
  - The left-hand side must be a single variable.
  - The right-hand side must be either a single terminal, a single terminal followed by a single variable, or epsilon.
- To convert a regular grammar into a FA, we can follow these steps:
  - For each variable A in the grammar, create a state q_A in the FA.
  - The state corresponding to the starting variable of the grammar will be the starting state of the FA.
  - For each production rule A -> aB in the grammar, where a is a terminal and B is a variable, create a transition q_A -> q_B labeled by a in the FA.
  - For each production rule A -> a in the grammar, where a is a terminal, create a transition q_A -> q_F labeled by a in the FA, where q_F is a new final state.
  - For each production rule A -> epsilon in the grammar, where epsilon is the empty string, make q_A a final state in the FA.
- Example: Consider the following regular grammar that generates the language of all strings over {a,b} that contain at least one a.

```
S -> aA | bS
A -> aA | bA | epsilon
```

- By applying the above algorithm, we get the following FA with the starting state q_S and the final states q_A and q_F.

FA

- To accept a word in the FA, we can follow the transitions of the FA and match the symbols of the word. For example, to accept the word bab, we can do:

```
q_S -> b -> q_S -> a -> q_A -> b -> q_A
```



# Simplification of CFG

- A context-free grammar (CFG) is a set of production rules that generate strings belonging to a language.
- A CFG may contain some redundant or unnecessary productions and symbols that do not affect the language generated by the grammar.
- Simplification of CFGs is the process of removing these productions and symbols to obtain an equivalent grammar that is simpler and more concise.
- Simplification of CFGs consists of the following steps:

  - **Removal of useless productions**: These are the productions that can never take part in the derivation of any string, or that can never lead to a terminal string. There are two types of useless productions:

    - **Non-generating productions**: These are the productions that have a non-terminal on the right-hand side that cannot be replaced by any terminal string. For example, in the grammar `S -> AB | a, A -> aA | b, B -> bB | c`, the production `B -> bB` is non-generating because `B` cannot be replaced by any terminal string.
    - **Non-reachable productions**: These are the productions that have a non-terminal on the left-hand side that cannot be derived from the start symbol. For example, in the grammar `S -> AB | a, A -> aA | b, B -> bB | c, C -> cC | d`, the production `C -> cC` is non-reachable because `C` cannot be derived from `S`.

  - To remove useless productions, we can use the following algorithm:

    - Step 1: Find all the non-generating non-terminals and remove them and the productions that contain them from the grammar.
    - Step 2: Find all the non-reachable non-terminals and remove them and the productions that contain them from the grammar.

  - **Removal of null productions**: These are the productions that have an empty string (`ε`) on the right-hand side. For example, in the grammar `S -> AB | a, A -> aA | ε, B -> bB | ε`, the productions `A -> ε` and `B -> ε` are null productions.
  - To remove null productions, we can use the following algorithm:

    - Step 1: Find all the nullable non-terminals, i.e., the non-terminals that can derive `ε` directly or indirectly.
    - Step 2: For each production that contains a nullable non-terminal on the right-hand side, add a new production without that non-terminal. For example, if `A` is nullable and we have a production `S -> AB`, we add a new production `S -> B`.
    - Step 3: Remove all the null productions from the grammar, except for the case where the start symbol is nullable. In that case, we keep the production `S -> ε` and make sure that `S` does not appear on the right-hand side of any other production.

  - **Removal of unit productions**: These are the productions that have a single non-terminal on the right-hand side. For example, in the grammar `S -> AB | a, A -> aA | B, B -> bB | c`, the production `A -> B` is a unit production.
  - To remove unit productions, we can use the following algorithm:

    - Step 1: For each non-terminal `A`, find all the non-terminals that can be reached from `A` by a sequence of unit productions, and store them in a set `U(A)`. For example, if we have the productions `A -> B, B -> C, C -> D, D -> E`, then `U(A) = {B, C, D, E}`.
    - Step 2: For each non-terminal `A`, replace all the unit productions of the form `A -> B` with the productions of the form `B -> α`, where `α` is any string of terminals and non-terminals, and `B` belongs to `U(A)`. For example, if we have the productions `A -> B, B -> aB | b`, then we replace `A -> B` with `A -> aB | b`.
    - Step 3: Remove all the unit productions from the grammar.



Hello, I am Sydney, your AI assistant. I can help you with your topic of normal forms in formal languages. Here are some notes that you can use for your study material:

# Normal Forms for the Unit 3 - Regular and Non-Regular Grammars in the Subject of Theory of Automata and Formal Languages

- A normal form is a standard way of writing a grammar that has certain desirable properties, such as simplicity, efficiency, or uniqueness.
- There are different types of normal forms for different types of grammars, such as regular, context-free, context-sensitive, or unrestricted grammars.
- In this unit, we will focus on two normal forms for context-free grammars: Chomsky normal form and Greibach normal form.

## Chomsky Normal Form

- A context-free grammar is in Chomsky normal form if all of its production rules are of the form:

  - A → BC, where A, B, and C are nonterminal symbols
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string

- Any context-free grammar can be converted to an equivalent grammar in Chomsky normal form by applying a series of transformations, such as eliminating ε-rules, unit rules, and useless symbols, and introducing new nonterminal symbols.
- Chomsky normal form is useful for proving properties of context-free languages, such as the pumping lemma, and for designing parsing algorithms, such as the CYK algorithm.

## Greibach Normal Form

- A context-free grammar is in Greibach normal form if all of its production rules are of the form:

  - A → aα, where A is a nonterminal symbol, a is a terminal symbol, and α is a string of nonterminal symbols

- Any context-free grammar can be converted to an equivalent grammar in Greibach normal form by applying a series of transformations, such as eliminating left recursion, left factoring, and introducing new nonterminal symbols.
- Greibach normal form is useful for designing parsing algorithms, such as recursive-descent parsing, and for generating strings of a context-free language in a systematic way.



# Chomsky Normal Form (CNF)

- Chomsky Normal Form (CNF) is a special form of context-free grammar (CFG) that has a simple and restricted structure.
- A CFG is in CNF if all its production rules are of the form:
  - A → BC, where A, B, and C are non-terminal symbols
  - A → a, where A is a non-terminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string
- CNF is useful for simplifying the parsing and analysis of context-free languages, as well as proving some properties of CFGs.
- Every CFG can be converted into an equivalent CNF grammar, that is, a CNF grammar that generates the same language as the original CFG.
- The conversion algorithm consists of the following steps:
  - Step 1: If the start symbol S occurs on the right-hand side of any production, create a new start symbol S' and add the production S' → S.
  - Step 2: Remove all ε-productions, that is, productions of the form A → ε, where A is not the start symbol. This can be done by replacing each occurrence of A on the right-hand side of any production with either A or ε, and eliminating any resulting ε-productions.
  - Step 3: Remove all unit productions, that is, productions of the form A → B, where A and B are non-terminal symbols. This can be done by replacing each occurrence of A on the right-hand side of any production with the right-hand side of B, and eliminating any resulting unit productions.
  - Step 4: Convert all remaining productions into the form A → BC or A → a, where A, B, and C are non-terminal symbols and a is a terminal symbol. This can be done by introducing new non-terminal symbols for each combination of terminal and non-terminal symbols on the right-hand side of any production, and adding new productions for them.
- The conversion algorithm preserves the language generated by the original CFG, and produces a CNF grammar whose size is at most the square of the original CFG's size.



# Greibach Normal Form (GNF)

- Greibach Normal Form (GNF) is a special form of context-free grammar (CFG) that has some restrictions on the right-hand side of the production rules.
- A CFG is in GNF if and only if all of its production rules are of the form: A → aA1A2...An, where A, A1, A2, ..., An are non-terminal symbols and a is a terminal symbol .
- GNF is useful for parsing algorithms, such as the top-down parsing algorithm, that require the first symbol of the right-hand side to be a terminal symbol .
- Any CFG can be converted into an equivalent GNF using a systematic algorithm that involves the following steps :
  - Step 1: If the start symbol S occurs on some right side, create a new start symbol S' and a new production S' → S.
  - Step 2: Remove null productions (productions of the form A → ε) using the null production removal algorithm.
  - Step 3: Remove unit productions (productions of the form A → B) using the unit production removal algorithm.
  - Step 4: Eliminate left recursion (direct or indirect) using the left recursion elimination algorithm.
  - Step 5: For each production of the form A → u1 | u2 | ... | un, where ui are strings of terminals and non-terminals, do the following:
    - If ui starts with a terminal symbol, say ai, then replace ui with aiBi, where Bi is a new non-terminal symbol, and add a new production Bi → ui / ai.
    - If ui starts with a non-terminal symbol, say Aj, then replace ui with the right-hand side of Aj, and repeat this process until ui starts with a terminal symbol.
  - Step 6: Simplify the grammar by removing any useless symbols or productions.



# Chomsky Hierarchy

- The Chomsky hierarchy is a containment hierarchy of classes of formal grammars, as described by Noam Chomsky in 1956 .
- It is an essential tool used in formal language theory, computer science, and linguistics .
- It can be represented in the form of a pyramid, with type 0 at the base and type 3 at the peak.
- Each type of grammar generates a class of language and is recognized by a type of automaton .
- The following table summarizes the four types of grammars, the languages they generate, the automata they recognize, and the form of their rules .

| Type | Grammar | Language | Automaton | Rule Form |
| --- | --- | --- | --- | --- |
| 0 | Unrestricted | Recursively enumerable | Turing machine | `α → β` |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automaton | `αAβ → αγβ` |
| 2 | Context-free | Context-free | Pushdown automaton | `A → γ` |
| 3 | Regular | Regular | Finite state automaton | `A → aB` or `A → a` |

- The Chomsky hierarchy shows the relation between the complexity of the grammar and the language it generates.
- The higher the type, the more restricted the grammar and the simpler the language.
- The lower the type, the more expressive the grammar and the richer the language.
- The Chomsky hierarchy also shows the relation between the power of the automaton and the language it recognizes.
- The higher the type, the less powerful the automaton and the easier the recognition.
- The lower the type, the more powerful the automaton and the harder the recognition.
- The Chomsky hierarchy is useful for studying the properties and limitations of different classes of languages and grammars.
- It also helps to compare and contrast different models of computation and formalisms.
- It is relevant to natural language processing, as natural languages are often modeled by context-free grammars or their extensions.



# Programming problems based on the properties of CFGs

- A context-free grammar (CFG) is a set of rules that defines a language by specifying how to generate strings from a set of symbols.
- A CFG consists of four components: a set of terminals, a set of non-terminals, a start symbol, and a set of productions.
- A terminal is a symbol that appears in the strings of the language. A non-terminal is a symbol that represents a group of strings. A start symbol is a special non-terminal that represents the whole language. A production is a rule that specifies how to replace a non-terminal with a sequence of terminals and non-terminals.
- A CFG can generate a string by starting from the start symbol and applying productions repeatedly until only terminals are left. The sequence of productions used to generate a string is called a derivation. A language is context-free if it can be generated by some CFG.
- Some properties of CFGs are:

  - CFGs are closed under union, concatenation, and Kleene star operations. That is, if L1 and L2 are context-free languages, then L1 ∪ L2, L1L2, and L1* are also context-free languages.
  - CFGs are not closed under intersection, complement, and set difference operations. That is, if L1 and L2 are context-free languages, then L1 ∩ L2, L1', and L1 - L2 may not be context-free languages.
  - CFGs can be converted into equivalent normal forms, such as Chomsky normal form and Greibach normal form, which have certain restrictions on the form of the productions. Normal forms are useful for simplifying the analysis and parsing of CFGs.
  - CFGs can be recognized by pushdown automata, which are finite automata with an additional stack memory. Pushdown automata can simulate the derivations of CFGs by pushing and popping symbols from the stack according to the productions.
  - CFGs can be classified into different classes based on the complexity of parsing them. For example, deterministic context-free languages (DCFLs) are a subclass of context-free languages that can be recognized by deterministic pushdown automata, which have only one possible transition for each input symbol and stack symbol. DCFLs can be parsed in linear time using algorithms such as LR parsing. However, not all context-free languages are deterministic, and some may require non-deterministic or even unbounded pushdown automata to recognize them.

- Some programming problems based on the properties of CFGs are:

  - Given a CFG, determine whether it is ambiguous, i.e., whether it can generate the same string in more than one way. This problem is undecidable in general, meaning that there is no algorithm that can solve it for all CFGs. However, some special cases can be decided, such as when the CFG is in Chomsky normal form or when it is unambiguous by construction.
  - Given a CFG, determine whether it is in Chomsky normal form, i.e., whether all its productions are of the form A → BC or A → a, where A, B, and C are non-terminals and a is a terminal. This problem is decidable and can be solved by checking the form of each production. If the CFG is not in Chomsky normal form, it can be converted into an equivalent CFG in Chomsky normal form using a standard algorithm.
  - Given a CFG, determine whether it is in Greibach normal form, i.e., whether all its productions are of the form A → aB1B2...Bn, where A and Bi are non-terminals and a is a terminal. This problem is decidable and can be solved by checking the form of each production. If the CFG is not in Greibach normal form, it can be converted into an equivalent CFG in Greibach normal form using a standard algorithm.
  - Given a CFG, determine whether it is deterministic, i.e., whether it can be recognized by a deterministic pushdown automaton. This problem is decidable and can be solved by checking whether the CFG satisfies certain conditions, such as having no ε-productions, no left recursion, and no common prefixes. If the CFG is not deterministic, it can be converted into an equivalent CFG that is deterministic using a standard algorithm.
  - Given a CFG and a string, determine whether the string belongs to the language generated by the CFG, i.e., whether there exists a derivation of the string from the start symbol of the CFG. This problem is decidable and can be solved by



# Unit 4 - Push Down Automata and Properties of Context Free Languages

- A push down automaton (PDA) is a finite automaton with an additional component called a stack, which can store and retrieve symbols according to the last-in first-out (LIFO) principle.
- A PDA can use the stack to store information that can help it recognize a language. For example, a PDA can use the stack to match parentheses or brackets in an expression.
- A PDA can be deterministic (DPDA) or nondeterministic (NPDA). A DPDA has at most one possible transition for any given input symbol and stack symbol, while a NPDA can have multiple possible transitions.
- A context free language (CFL) is a language that can be generated by a context free grammar (CFG), which is a set of rules that specify how to form strings from a finite set of symbols.
- A CFG consists of a set of variables, a set of terminals, a start variable, and a set of production rules. A production rule has the form A -> B, where A is a variable and B is a string of variables and terminals.
- A CFL can be accepted by a PDA, and vice versa. This means that for any CFL, there exists a PDA that accepts it, and for any PDA, there exists a CFL that it accepts.
- The properties of CFLs include the following:
  - CFLs are closed under union, concatenation, and Kleene star operations. This means that if L1 and L2 are CFLs, then L1 U L2, L1 L2, and L1* are also CFLs.
  - CFLs are not closed under intersection, complement, and set difference operations. This means that if L1 and L2 are CFLs, then L1 ∩ L2, L1', and L1 - L2 may not be CFLs.
  - CFLs are not closed under reversal operation. This means that if L is a CFL, then L^R may not be a CFL.
  - CFLs are not closed under homomorphism and inverse homomorphism operations. This means that if L is a CFL and h is a homomorphism, then h(L) and h^-1(L) may not be CFLs.
  - CFLs are decidable. This means that there exists an algorithm that can determine whether a given string belongs to a CFL or not.
  - CFLs are not enumerable. This means that there is no algorithm that can list all the strings in a CFL in a systematic order.



# Nondeterministic Pushdown Automata (NPDA)

- A nondeterministic pushdown automaton (NPDA) is a variation of the nondeterministic finite automaton (NDFA) that has access to a stack (hence the name pushdown)   .
- A stack is a data structure that allows only two operations: push (adding an element to the top) and pop (removing an element from the top).
- A NPDA can use the stack to store and retrieve information during the computation, which gives it more power than a NDFA.
- A NPDA is formally defined by a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where  :
  - Q is a finite set of states
  - Σ is an input alphabet
  - Γ is a stack alphabet
  - δ is a transition function that maps Q x (Σ ∪ {ε}) x (Γ ∪ {ε}) to a finite subset of Q x (Γ ∪ {ε})
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final states
- A NPDA can make transitions based on the current state, the input symbol, and the top of the stack. It can also change the state and the stack by popping and pushing symbols.
- A NPDA can have multiple possible transitions from a given configuration, or no transitions at all. Any of these transitions can be chosen in a computation. A NPDA accepts an input if there exists a computation that leads to a final state.
- The class of languages accepted by NPDA is called the context-free languages (CFL), which is a proper superset of the regular languages. A CFL can also be defined by a context-free grammar (CFG). There is an algorithm to convert a CFG to a NPDA and vice versa.



# Definition for the notes of the Unit 4 - Push Down Automata and Properties of Context Free Languages in the subject of Theory of Automata and Formal Languages

- A **pushdown automaton** (PDA) is a type of automaton that employs a **stack** as an auxiliary memory.
- A stack is a data structure that allows operations of **push** (adding a symbol to the top) and **pop** (removing a symbol from the top).
- A PDA can use the stack to store and retrieve information that is needed to process the input symbols.
- A PDA can recognize **context-free languages** (CFLs), which are a class of languages that can be generated by **context-free grammars** (CFGs).
- A CFG is a set of rules that describe how to form strings from a finite set of symbols called **terminals** and a finite set of symbols called **non-terminals**.
- A CFG consists of four components: a set of non-terminals (N), a set of terminals (Σ), a set of rules (R), and a start symbol (S).
- A rule has the form A → α, where A is a non-terminal and α is a string of terminals and/or non-terminals.
- A PDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where :
  - Q is a finite set of states
  - Σ is the input alphabet
  - Γ is the stack alphabet
  - δ is the transition function, which maps Q × Σε × Γε to a finite subset of Q × Γε, where ε denotes the empty string
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is the set of final or accepting states
- A PDA can operate in two modes: **accept by final state** or **accept by empty stack**.
  - In the first mode, a PDA accepts an input string if it reaches a final state after reading the entire input and performing zero or more stack operations.
  - In the second mode, a PDA accepts an input string if it empties the stack after reading the entire input and performing zero or more stack operations.



Hello, I am Sydney, your AI assistant. I can help you with writing the notes for the Unit 4 - Push Down Automata and Properties of Context Free Languages in the subject of Theory of Automata and Formal Languages. Here is the content in markdown format:

# Unit 4 - Push Down Automata and Properties of Context Free Languages

## Push Down Automata (PDA)

- A push down automata (PDA) is a finite automata with an additional stack memory.
- A stack is a data structure that allows only two operations: push and pop.
- Push operation adds a symbol to the top of the stack, and pop operation removes the symbol from the top of the stack.
- A PDA can use the stack to store and retrieve information that is needed to recognize the input string.
- A PDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where
  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite stack alphabet
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ to a finite subset of Q × Γ*
  - q0 is the initial state
  - Z0 is the initial stack symbol
  - F is a set of final states
- A PDA can be deterministic (DPDA) or nondeterministic (NPDA).
- A DPDA has at most one move from any configuration, and it cannot have both a move on ε and a move on any input symbol from the same configuration.
- A NPDA can have zero, one, or more moves from any configuration, and it can have both a move on ε and a move on any input symbol from the same configuration.
- A PDA can accept an input string by two methods: final state and empty stack.
- In the final state method, a PDA accepts an input string if it reaches a final state after reading the entire input string. The stack may or may not be empty.
- In the empty stack method, a PDA accepts an input string if it empties the stack after reading the entire input string. The state may or may not be final.
- The language accepted by a PDA by final state method is denoted by L(P), and the language accepted by a PDA by empty stack method is denoted by N(P).
- A PDA can be represented by a state diagram, where each transition is labeled by a/x, y, where a is the input symbol, x is the stack symbol to be popped, and y is the string of stack symbols to be pushed.
- A PDA can also be represented by an instantaneous description (ID), which is a triplet (q, w, α), where q is the current state, w is the remaining input string, and α is the current stack content.

## Properties of Context Free Languages (CFLs)

- A context free language (CFL) is a language that can be generated by a context free grammar (CFG).
- A CFG is a 4-tuple (V, Σ, R, S), where
  - V is a finite set of variables (or nonterminals)
  - Σ is a finite set of terminals (or alphabet)
  - R is a finite set of rules (or productions) of the form A → α, where A ∈ V and α ∈ (V ∪ Σ)*
  - S is the start variable
- A CFG can be used to derive a string in the language by applying the rules in R, starting from S, until no variables are left.
- A derivation can be represented by a derivation tree, where each node is labeled by a variable or a terminal, and each branch corresponds to a rule application.
- A derivation can be leftmost or rightmost, depending on whether the leftmost or the rightmost variable is replaced at each step.
- A CFG is ambiguous if it can generate more than one derivation tree for some string in the language.
- A CFL is inherently ambiguous if every CFG that generates it is ambiguous.
- A CFG is in Chomsky normal form (CNF) if every rule is of the form A → BC or A → a, where A, B, C ∈ V and a ∈ Σ, except for the rule S → ε, where S is the start variable and ε is the empty string.
- A CFG is in Greibach normal form (GNF) if every rule is of the form A → aα, where A ∈ V, a ∈ Σ, and α ∈ V*.
- Every CFL can be generated by a CFG in CN



# A Language Accepted by NPDA

- A language is accepted by a nondeterministic pushdown automaton (NPDA) if there exists a sequence of moves that leads the NPDA from the initial configuration to a final configuration for any input string in the language.
- A NPDA can accept any context-free language (CFL), but not all CFLs can be accepted by a deterministic pushdown automaton (DPDA).
- A NPDA can have multiple transitions for the same input symbol and stack symbol, and it can also have transitions without consuming any input symbol (called epsilon or lambda transitions).
- A NPDA can accept a language by either empty stack or final state, or both. However, for any NPDA that accepts by empty stack, there exists an equivalent NPDA that accepts by final state, and vice versa.
- A NPDA can simulate a nondeterministic finite automaton (NFA) by using the stack as a memory, but it cannot simulate a nondeterministic Turing machine (NTM), since the stack has only one end and is not infinite in both directions.
- A NPDA can be represented by a 7-tuple (Q, Σ, Γ, δ, q0, Z, F), where Q is a finite set of states, Σ is a finite input alphabet, Γ is a finite stack alphabet, δ is a transition function, q0 is the initial state, Z is the initial stack symbol, and F is a set of final states.
- A NPDA can be converted to an equivalent context-free grammar (CFG) by using a standard algorithm that generates a production rule for each possible transition of the NPDA.
- A NPDA can be used to recognize various languages that are not regular, such as {a^n b^n | n >= 0}, {w w^R | w ∈ (a,b)*}, {a^n b^m c^n | m,n >= 1}, etc.



# Deterministic Pushdown Automata (DPDA)

- A deterministic pushdown automaton (DPDA) is a variation of the pushdown automaton (PDA) that accepts the deterministic context-free languages (DCFL), a proper subset of context-free languages (CFL) .
- A DPDA has a single computation from the initial configuration to an accepting one for all strings belonging to the language it accepts .
- A DPDA can be formally defined as a 6-tuple (Q, Σ, Γ, δ, q0, F), where :
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - Γ is a finite set of pushdown symbols (which can be pushed and popped from the stack)
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ to Q × Γ*
  - q0 is the initial state
  - F is a set of final states
- A DPDA is deterministic if for every state q, input symbol a, and stack symbol X, there is at most one transition of the form (q, a, X) → (p, γ) in δ .
- A DPDA can accept a string by two modes: final state and empty stack .
  - In the final state mode, a DPDA accepts a string if it reaches a final state after reading the entire input and possibly modifying the stack.
  - In the empty stack mode, a DPDA accepts a string if it empties the stack after reading the entire input and possibly changing the state.
- A DPDA can be converted to an equivalent context-free grammar (CFG) and vice versa .
- A DPDA can simulate a deterministic finite automaton (DFA) by using an empty stack, but not all CFLs can be accepted by a DPDA .
- A DPDA can be represented by a state diagram, where each transition is labeled by an input symbol, a stack symbol to be popped, and a stack symbol (or string) to be pushed . For example, the following state diagram shows a DPDA that accepts the language {a^n b^n | n ≥ 0} by empty stack :

DPDA example



# Deterministic Context Free Languages (DCFL)

- A deterministic context free language (DCFL) is a context free language (CFL) that can be accepted by a deterministic pushdown automaton (DPDA).
- A DPDA is a pushdown automaton (PDA) that has at most one possible transition for any given input symbol and stack symbol.
- DCFLs are always unambiguous, meaning that they have only one possible derivation tree for any given string in the language.
- DCFLs are a proper subset of CFLs, meaning that every DCFL is also a CFL, but not every CFL is a DCFL.
- DCFLs have some advantages over CFLs, such as being easier to parse and having more efficient algorithms for recognition and decision problems.
- DCFLs also have some limitations, such as not being closed under union, intersection, or complementation, and not being able to express some natural languages or programming languages that are CFLs.
- Some examples of DCFLs are:
  - The set of all palindromes over a finite alphabet.
  - The set of all balanced parentheses.
  - The set of all strings of the form a^n b^n c^n, where n is a positive integer.
  - The set of all strings of the form a^n b^m, where n and m are positive integers and n is greater than m.



# Pushdown Automata for Context Free Languages

- A **pushdown automaton** (PDA) is a computational model that can recognize **context free languages** (CFLs) by using a **stack** as an auxiliary memory .
- A stack is a data structure that allows only two operations: **push** (adding an element to the top) and **pop** (removing an element from the top).
- A PDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z, F), where:
  - Q is a finite set of **states**.
  - Σ is a finite set of **input symbols**.
  - Γ is a finite set of **stack symbols**.
  - δ is a **transition function** that maps Q × (Σ ∪ {ε}) × Γ to a finite subset of Q × Γ*.
  - q0 is the **initial state**.
  - Z is the **initial stack symbol**.
  - F is a set of **final states**.
- A PDA can be either **deterministic** (DPDA) or **nondeterministic** (NPDA), depending on whether the transition function δ is a function or a relation.
- A DPDA can recognize all **deterministic context free languages** (DCFLs) while an NPDA can recognize all CFLs, with the former often used in parser design.
- A PDA can accept an input string in two ways:
  - By **final state**: the PDA reaches a final state after reading the entire input and emptying the stack.
  - By **empty stack**: the PDA empties the stack after reading the entire input, regardless of the current state.
- There is a direct way to construct a PDA for a given **context free grammar** (CFG), and vice versa, which shows the equivalence between CFLs and PDAs .
- A CFG is a 4-tuple (V, Σ, R, S), where:
  - V is a finite set of **variables** or **nonterminals**.
  - Σ is a finite set of **terminals** that is disjoint from V.
  - R is a finite set of **rules** or **productions** of the form A → α, where A ∈ V and α ∈ (V ∪ Σ)*.
  - S is the **start symbol**.
- A CFG generates a CFL by applying the rules recursively, starting from the start symbol, until no more variables can be replaced.
- A CFL is a language that can be generated by a CFG, or equivalently, accepted by a PDA .
- A CFL has some properties that distinguish it from other classes of languages, such as:
  - A CFL is **closed** under union, concatenation, Kleene star, reversal, and homomorphism, but not under intersection, complement, or difference.
  - A CFL can be **pumped** by a pumping lemma that states that for any sufficiently long string in the language, there exists a way to divide it into five parts such that some of the middle parts can be repeated any number of times and the resulting string still belongs to the language.
  - A CFL can be **decided** by an algorithm that determines whether a given string belongs to the language or not, or whether a given CFG is empty, finite, or ambiguous.



# Context Free Grammars for Pushdown Automata

- A **context-free grammar (CFG)** is a set of rewriting rules that can be used to generate or reproduce patterns/strings recursively.
- A **pushdown automaton (PDA)** is a finite-state machine with an added stack that can store and retrieve symbols.
- A **context-free language (CFL)** is a language that can be generated by a CFG or accepted by a PDA.
- There is a **correspondence** between CFGs and PDAs: for every CFG, there is an equivalent PDA, and vice versa  .
- The correspondence can be established by the following **conversions**:
  - **CFG to PDA**: Given a CFG in Chomsky normal form, construct a PDA that simulates the leftmost derivation of the input string by pushing and popping symbols from the stack .
  - **PDA to CFG**: Given a PDA, construct a CFG that generates the strings that cause the PDA to go from the initial state to the final state with an empty stack.
- The conversions are **constructive**, meaning that they provide an algorithm to obtain the equivalent CFG or PDA from the given PDA or CFG  .
- The conversions are also **correct**, meaning that they preserve the language accepted or generated by the original CFG or PDA  .
- The conversions are useful for **proving** properties of CFLs, such as closure under certain operations, decidability of certain problems, and pumping lemma for CFLs .



# Two Stack Pushdown Automata

- A pushdown automaton (PDA) is a finite state machine augmented with a stack. A stack is a data structure that allows only two operations: push and pop. Push adds a symbol to the top of the stack, and pop removes the symbol from the top of the stack. A PDA can use the top of the stack to decide which transition to take, and it can manipulate the stack as part of performing a transition.
- A two stack pushdown automaton (2-PDA) is a PDA that has two stacks instead of one. In each transition, it must specify which stack to push or pop, or whether to leave both stacks unchanged. A 2-PDA can simulate a queue by using one stack as the front and the other as the rear of the queue.
- A 2-PDA has the same computation power as a Turing machine, which is a more powerful model of computation than a PDA. A Turing machine can accept languages that are not accepted by any PDA with one stack, such as the language {a^n b^n c^n | n >= 0}. A 2-PDA can accept this language by using one stack to count the number of a's and the other stack to count the number of b's, and then compare them with the number of c's .
- A 2-PDA can be formally defined as a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where:

  - Q is a finite set of states
  - Σ is a finite input alphabet
  - Γ is a finite stack alphabet
  - δ is a transition function that maps Q × (Σ ∪ {ε}) × Γ × Γ to a subset of Q × {push, pop, ε} × {push, pop, ε}
  - q0 is the initial state
  - Z0 is the initial stack symbol for both stacks
  - F is a set of final states

- A configuration of a 2-PDA is a triple (q, w, αβ), where q is the current state, w is the remaining input, and αβ is the content of the two stacks, with α being the top of the first stack and β being the top of the second stack. The initial configuration is (q0, w, Z0Z0), where w is the input string. The final configuration is (q, ε, εε), where q is a final state and both stacks are empty.
- A 2-PDA can make a transition from one configuration to another according to the transition function δ. For example, if δ(q, a, X, Y) = {(p, push, pop)}, then the 2-PDA can move from (q, aw, Xα, Yβ) to (p, w, aXα, β) by reading an input symbol a, pushing it to the first stack, and popping the second stack. If δ(q, ε, X, Y) = {(p, ε, ε)}, then the 2-PDA can move from (q, w, Xα, Yβ) to (p, w, Xα, Yβ) by making an ε-transition without changing the stacks.



# Pumping Lemma for CFL

The pumping lemma for context-free languages (CFLs) is a tool to prove that a given language is not context-free. It states that if a language is context-free, then there exists a constant n (called the pumping length) such that any string w in the language of length at least n can be written as w = uvxyz, where:

- |vxy| ≤ n
- |vy| ≥ 1
- uv^nxy^nz is in the language for all n ≥ 0

The intuition behind the pumping lemma is that any sufficiently long string in a context-free language can be generated by a derivation tree that has a repeated variable along some path. This means that we can "pump" the string by repeating or deleting the substring generated by that variable, and still get a string in the language.

To use the pumping lemma to show that a language is not context-free, we assume that the language is context-free and derive a contradiction. We do this by choosing a string w in the language that is longer than the pumping length n, and showing that for any possible decomposition of w into uvxyz, there exists a value of n such that uv^nxy^nz is not in the language. This contradicts the pumping lemma, and hence the language is not context-free.

For example, consider the language L = {a^nb^nc^n | n ≥ 1}. We want to show that L is not context-free. Suppose, for a contradiction, that L is context-free. Then there exists a pumping length n such that any string w in L of length at least n can be pumped. Let w = a^nb^nc^n, where n is the pumping length. Then w can be written as w = uvxyz, where |vxy| ≤ n and |vy| ≥ 1. There are three possible cases for the decomposition of w:

- Case 1: vxy contains only one type of symbol, such as a, b, or c. Then pumping v and y will change the number of that symbol, and the resulting string will not be in L. For example, if vxy = a^k for some k > 0, then uv^2xy^2z = a^(n+k)b^nc^n, which is not in L.
- Case 2: vxy contains two types of symbols, such as ab, bc, or ca. Then pumping v and y will change the order of the symbols, and the resulting string will not be in L. For example, if vxy = a^kb^l for some k, l > 0, then uv^2xy^2z = a^(n+k)b^(n+l)c^n, which is not in L.
- Case 3: vxy contains all three types of symbols, such as abc, bca, or cab. Then pumping v and y will create a gap between the symbols, and the resulting string will not be in L. For example, if vxy = a^kb^lc^m for some k, l, m > 0, then uv^2xy^2z = a^(n+k)b^(n+l)c^(n+m), which is not in L.

In all cases, we can find a value of n such that uv^nxy^nz is not in L, which contradicts the pumping lemma. Therefore, L is not context-free.



# Closure properties of CFL

- A closure property of a class of languages is a property that says that if we apply a certain operation to the languages in the class, we get another language in the same class.
- For example, the closure property of union for CFLs says that if we take the union of two CFLs, we get another CFL.
- Closure properties are useful for proving that certain languages are or are not CFLs, and for constructing CFGs for languages that are CFLs.
- Some of the common closure properties of CFLs are:

  - **Union**: If L1 and L2 are CFLs, then L1 ∪ L2 is also a CFL. To prove this, we can construct a CFG for L1 ∪ L2 by adding a new start symbol S and two new productions S → S1 | S2, where S1 and S2 are the start symbols of the CFGs for L1 and L2, respectively   .
  - **Concatenation**: If L1 and L2 are CFLs, then L1 L2 is also a CFL. To prove this, we can construct a CFG for L1 L2 by adding a new start symbol S and a new production S → S1 S2, where S1 and S2 are the start symbols of the CFGs for L1 and L2, respectively   .
  - **Kleene closure**: If L is a CFL, then L* is also a CFL. To prove this, we can construct a CFG for L* by adding a new start symbol S and two new productions S → ε | S1 S, where S1 is the start symbol of the CFG for L   .
  - **Reversal**: If L is a CFL, then LR is also a CFL, where LR is the language obtained by reversing the strings in L. To prove this, we can construct a CFG for LR by reversing the right-hand sides of all the productions in the CFG for L .
  - **Homomorphism**: If L is a CFL and h is a homomorphism, then h(L) is also a CFL, where h(L) is the language obtained by applying h to each string in L. A homomorphism is a function that maps each symbol in an alphabet to a string over another alphabet. To prove this, we can construct a CFG for h(L) by replacing each symbol in the right-hand sides of the productions in the CFG for L with the corresponding string given by h .
  - **Inverse homomorphism**: If L is a CFL and h is a homomorphism, then h-1(L) is also a CFL, where h-1(L) is the language obtained by applying the inverse of h to each string in L. The inverse of h is a function that maps each string over the target alphabet of h to a string over the source alphabet of h, such that h(h-1(x)) = x for all x in the target alphabet. To prove this, we can construct a CFG for h-1(L) by replacing each string in the right-hand sides of the productions in the CFG for L with the corresponding symbol given by h-1 .

- Some of the properties that CFLs are not closed under are:

  - **Intersection**: If L1 and L2 are CFLs, then L1 ∩ L2 may or may not be a CFL. A counterexample is L1 = {an bn cn | n ≥ 0} and L2 = {an bn | n ≥ 0}, which are both CFLs, but their intersection L1 ∩ L2 = {an bn bn | n ≥ 0} is not a CFL .
  - **Difference**: If L1 and L2 are CFLs, then L1 - L2 may or may not be a CFL. A counterexample is L1 = {an bn cn | n ≥ 0} and L2 = {an bn | n ≥ 0}, which are both CFLs, but their difference L1 - L2 = {an bn cn | n > 0} is not a CFL .
  - **Complement**: If



# Decision Problems of CFL

- Decision problems are questions that can be answered by yes or no, such as whether a given string belongs to a language, or whether a language is empty or infinite.
- Decision problems for CFLs are important because they can help us determine the properties and limitations of CFLs and their corresponding models, such as CFGs and PDAs.
- Some common decision problems for CFLs are:

  - **Membership problem**: Given a CFG G and a string w, decide if w belongs to L(G).
    - This problem can be solved by using a PDA that simulates G and accepts w by empty stack or final state, or by using the CYK algorithm that checks if w can be derived from the start symbol of G.
    - This problem is decidable and has polynomial time complexity.
  - **Emptiness problem**: Given a CFG G, decide if L(G) is empty.
    - This problem can be solved by using a bottom-up search that marks all the symbols that can produce some terminal string, and then checking if the start symbol is marked or not.
    - This problem is decidable and has linear time complexity.
  - **Infiniteness problem**: Given a CFG G, decide if L(G) is infinite.
    - This problem can be solved by using the pumping lemma for CFLs, which states that if L(G) is infinite, then there exists some integer p such that any string w in L(G) with length at least p can be pumped, i.e., written as w = uvxyz such that |vxy| <= p, |vy| > 0, and uv^nxy^nz belongs to L(G) for any n >= 0.
    - This problem is decidable and has polynomial time complexity.
  - **Equivalence problem**: Given two CFGs G1 and G2, decide if L(G1) = L(G2).
    - This problem can be reduced to the emptiness problem by constructing a CFG G such that L(G) = L(G1) symmetric difference L(G2), i.e., the set of strings that belong to either L(G1) or L(G2) but not both, and then checking if L(G) is empty or not.
    - This problem is undecidable, i.e., there is no algorithm that can solve it for all possible inputs. This is because CFLs are not closed under complement, and if this problem were decidable, then we could also decide the complement problem, which is given a CFG G, decide if L(G) is the complement of L(G), i.e., the set of strings that do not belong to L(G).
  - **Containment problem**: Given two CFGs G1 and G2, decide if L(G1) is a subset of L(G2).
    - This problem can be reduced to the emptiness problem by constructing a CFG G such that L(G) = L(G1) intersection L(G2) complement, i.e., the set of strings that belong to L(G1) but not to L(G2), and then checking if L(G) is empty or not.
    - This problem is undecidable, for the same reason as the equivalence problem.



# Programming problems based on the properties of CFLs

- A context-free language (CFL) is a language that can be generated by a context-free grammar (CFG).
- A CFG consists of a set of variables, a set of terminals, a start variable, and a set of production rules of the form A -> α, where A is a variable and α is a string of variables and terminals.
- A CFL has some properties that can be used to design programming problems, such as:
  - Closure properties: A CFL is closed under union, concatenation, Kleene star, reversal, and homomorphism, but not under intersection, complement, or difference.
  - Decision properties: It is decidable whether a given CFG is ambiguous, whether a given CFG generates a given string, whether a given CFG generates the empty language, whether a given CFG generates a finite language, and whether two given CFGs generate the same language.
  - Pumping lemma: If L is a CFL, then there exists a constant n such that for any string w in L with |w| >= n, there exist strings u, v, x, y, z such that w = uvxyz, |vxy| <= n, |vy| > 0, and for any k >= 0, u(v^k)x(y^k)z is also in L.
- Some examples of programming problems based on the properties of CFLs are:
  - Given a CFG G and a string w, write a program that determines whether w is in L(G), the language generated by G, using a pushdown automaton (PDA) or a parsing algorithm such as CYK or Earley.
  - Given two CFGs G1 and G2, write a program that constructs a CFG G3 such that L(G3) = L(G1) ∪ L(G2), using the closure property of union and the standard construction of CFGs from PDAs.
  - Given a CFG G, write a program that checks whether G is ambiguous, using the decision property of ambiguity and a method such as generating two different parse trees for the same string or finding a string that satisfies the pumping lemma for two different decompositions.
  - Given a CFL L, write a program that generates a random string in L, using a method such as randomly selecting production rules from a CFG for L or randomly simulating a PDA for L.



## Unit 5 - Turing Machines and Recursive Function Theory

- A Turing machine is a simple abstract computational device that can simulate any algorithm  .
- A Turing machine consists of a finite set of states, a finite alphabet of symbols, a tape divided into cells that can store symbols, and a head that can read and write symbols on the tape and move left or right .
- A Turing machine can be in one of the states at any time, and the state determines how the machine behaves on the current symbol on the tape .
- A Turing machine can change its state, write a new symbol on the tape, and move the head according to a transition function that specifies the rules of the machine .
- A Turing machine can accept or reject an input string by entering a special accepting or rejecting state, or it can loop indefinitely .
- A Turing machine can be deterministic or nondeterministic, depending on whether the transition function is a function or a relation .
- A Turing machine can be universal, meaning that it can simulate any other Turing machine given its description and input .
- A Turing machine can be used to accept recursive enumerable languages, which are the languages generated by type-0 grammars.
- A recursive function is a function from natural numbers to natural numbers that can be computed by a Turing machine.
- A recursive function can be defined by primitive recursion, which is a way of constructing new functions from simpler ones using a base case and a recursive step.
- A recursive function can also be defined by the μ-operator, which is a way of finding the smallest natural number that satisfies a given property.
- A recursive function can also be defined by composition, which is a way of combining existing functions into new ones.
- A recursive function can also be defined by recursion theorem, which is a way of creating self-referential functions.
- A recursive function can be partial or total, depending on whether it is defined for all natural numbers or not.
- A recursive function can be primitive recursive or general recursive, depending on whether it can be defined without using the μ-operator or not.
- A recursive function can be computable or uncomputable, depending on whether there exists a Turing machine that can compute it or not.
- The theory of Turing machines and the theory of recursive functions are equivalent, meaning that they can express the same set of computable functions .
- The Church-Turing thesis is a conjecture that states that any function that can be computed by an effective method can also be computed by a Turing machine.
- The Church-Turing thesis has implications for the limits of computation, such as the undecidability of the halting problem and the existence of uncomputable functions.



# Basic Turing Machine Model

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It was proposed by Alan Turing in 1936 as a way of studying the limits of computability .

A basic Turing machine consists of the following components :

- An infinite tape divided into cells, each cell containing a symbol from a finite alphabet. The tape serves as the input and output of the machine, as well as its memory.
- A tape head that can read and write symbols on the tape, and move one cell to the left or right at a time.
- A finite set of states, one of which is designated as the initial state, and some of which are designated as accepting or rejecting states. The state of the machine determines its behavior at each step.
- A transition function that specifies, for each state and tape symbol, what the machine should do next: write a new symbol on the tape, move the head left or right, and change to a new state.

The machine starts in the initial state with the input string on the tape, and the head positioned on the leftmost cell. It then follows the transition function until it reaches an accepting or rejecting state, or loops indefinitely. The output of the machine is the final configuration of the tape, or undefined if the machine does not halt.

A Turing machine can be represented by a diagram, a table, or a formal notation. Here is an example of a Turing machine that decides whether a binary string is a palindrome (a string that is the same when reversed):

Turing machine diagram

The diagram shows the states as circles, the tape symbols as letters, and the transitions as arrows. The transition function is written as (write symbol, move direction, new state) on each arrow. For example, the transition from state q0 to q1 on symbol 0 is (0, R, q1), which means write 0, move right, and change to state q1. The initial state is marked with an arrow, and the accepting state is marked with a double circle.

The table shows the same information in a tabular form, with the rows corresponding to the states, and the columns corresponding to the tape symbols. The blank symbol is denoted by B. For example, the entry in row q0 and column 0 is (0, R, q1), which means the same as above.

| State | 0 | 1 | B |
| ----- | - | - | - |
| q0 | (0, R, q1) | (1, R, q2) | (B, R, qa) |
| q1 | (0, R, q1) | (1, R, q2) | (B, L, q3) |
| q2 | (0, R, q1) | (1, R, q2) | (B, L, q4) |
| q3 | (0, L, q3) | (1, L, q5) | (B, R, q6) |
| q4 | (0, L, q5) | (1, L, q4) | (B, R, q6) |
| q5 | (B, L, q5) | (B, L, q5) | (B, R, q0) |
| q6 | (B, R, q6) | (B, R, q6) | (B, R, qa) |
| qa | (0, R, qr) | (1, R, qr) | (B, R, qa) |
| qr | (0, R, qr) | (1, R, qr) | (B, R, qr) |

The formal notation shows the same information in a compact form, using a semicolon to separate the transitions for each state, and a comma to separate the transitions for each symbol. For example, the notation for state q0 is q0: 0->0, R, q1; 1->1, R, q2; B->B, R, qa, which means the same as the diagram and the table.

q0: 0->0, R, q1; 1->1, R, q2; B->B, R, qa
q1: 0->0, R, q1; 1->1



# Representation of Turing Machines

- A Turing machine is a theoretical model of computation that can perform any algorithmic task by manipulating symbols on an infinite tape according to a finite set of rules.
- A Turing machine consists of four components: a tape, a tape head, a state register, and a transition function.
- The tape is divided into cells, each of which can hold one symbol from a finite alphabet. The tape is infinite in both directions, and the tape head can move left or right along the tape.
- The state register stores the current state of the machine, which is one of a finite number of possible states. The initial state is usually denoted by q0, and the final state by qf.
- The transition function is a set of instructions that specify how the machine should change its state, symbol, and tape head movement based on the current state and symbol. The transition function can be represented by a table, a diagram, or a formula.
- A table representation of a Turing machine has the tape alphabet displayed on the x-axis, and the set of machine states across the y-axis. Inside the table, at the intersection of each state and symbol, is written the rest of the instruction—the new state, new symbol, and direction of movement. For example, the table below represents a Turing machine that adds one to a binary number.

| | 0 | 1 | B |
|---|---|---|---|
| q0 | q0, 0, R | q0, 1, R | q1, B, L |
| q1 | q2, 1, L | q1, 0, L | qf, B, R |
| q2 | q2, 0, L | q2, 1, L | q0, B, R |

- A diagram representation of a Turing machine has state cells connected by arrows. Each state cell represents a state of the machine, and each arrow represents a transition rule. The arrow is labeled with the input symbol, the output symbol, and the direction of movement. For example, the diagram below represents the same Turing machine as the table above.

Turing machine diagram

- A formula representation of a Turing machine uses a mathematical notation to describe the transition function. For example, the formula below represents the same Turing machine as the table and the diagram above.

δ(q0, 0) = (q0, 0, R)  
δ(q0, 1) = (q0, 1, R)  
δ(q0, B) = (q1, B, L)  
δ(q1, 0) = (q2, 1, L)  
δ(q1, 1) = (q1, 0, L)  
δ(q1, B) = (qf, B, R)  
δ(q2, 0) = (q2, 0, L)  
δ(q2, 1) = (q2, 1, L)  
δ(q2, B) = (q0, B, R)

- A Turing machine can be in one of three modes: accepting, rejecting, or looping. An accepting mode means that the machine has reached the final state and has successfully completed its task. A rejecting mode means that the machine has reached a state that is not the final state and has no applicable transition rule. A looping mode means that the machine is stuck in an infinite cycle of states and symbols and never reaches the final state.



# Language Acceptability of Turing Machines

- A Turing machine (TM) is a mathematical model of computation that can perform any algorithmic task by manipulating symbols on an infinite tape according to a finite set of rules.
- A TM can accept or reject an input string based on whether it reaches a final state or not after processing the input.
- A TM can also decide an input string by halting on either a final state or a rejecting state for any input.
- A language is a set of strings over some alphabet. A language is accepted by a TM if the TM accepts every string in the language and rejects every string not in the language.
- A language is decided by a TM if the TM decides every string in the language and every string not in the language.
- A language is Turing-acceptable if there exists a TM that accepts it. Turing-acceptable languages are also called recursively enumerable languages, and they are generated by Type-0 grammars in the Chomsky hierarchy.
- A language is Turing-decidable if there exists a TM that decides it. Turing-decidable languages are also called recursive languages, and they are a proper subset of Turing-acceptable languages.



# Techniques for Turing Machine Construction

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It consists of an infinite tape divided into cells, a head that can read and write symbols on the tape, and a finite set of states and transitions that determine the behavior of the machine.

There are different techniques for constructing Turing machines for various languages or problems. Some of the common techniques are:

- **Concatenation**: To construct a Turing machine for a language that is the concatenation of two languages, such as L = L1L2, we can use two Turing machines, one for L1 and one for L2, and connect them in sequence. The first machine will process the input until it reaches a special symbol that marks the end of L1, and then switch to the second machine that will process the rest of the input. If both machines accept, the whole input is accepted. For example, to construct a Turing machine for L = {a^n b^n | n >= 1}, we can use a Turing machine for L1 = {a^n | n >= 1} that marks the last a with a special symbol X, and a Turing machine for L2 = {b^n | n >= 1} that checks if the number of b's matches the number of a's (excluding X).

- **Union**: To construct a Turing machine for a language that is the union of two languages, such as L = L1 U L2, we can use two Turing machines, one for L1 and one for L2, and run them in parallel on two copies of the input. The input is accepted if either machine accepts. For example, to construct a Turing machine for L = {a^n | n is odd} U {b^n | n is even}, we can use a Turing machine for L1 = {a^n | n is odd} that counts the number of a's and accepts if it is odd, and a Turing machine for L2 = {b^n | n is even} that counts the number of b's and accepts if it is even.

- **Iteration**: To construct a Turing machine for a language that is the iteration of another language, such as L = L1*, we can use a Turing machine for L1 and repeat it as many times as needed until the input is exhausted or rejected. The input is accepted if it is empty or if it is a concatenation of one or more strings from L1. For example, to construct a Turing machine for L = {a^n b^n | n >= 0}*, we can use a Turing machine for L1 = {a^n b^n | n >= 0} that checks if the input has equal number of a's and b's, and repeat it until the tape is empty or the input is invalid.

- **Simulation**: To construct a Turing machine for a language that is recognized by another model of computation, such as a finite automaton, a pushdown automaton, or a recursive function, we can simulate the behavior of that model using the tape, the head, and the states of the Turing machine. For example, to construct a Turing machine for L = {w | w is a palindrome}, we can simulate a pushdown automaton that pushes the first half of the input onto a stack (represented by a portion of the tape), and then pops and compares it with the second half of the input.



# Modifications of Turing Machine

A Turing machine is a theoretical model of computation that can read and write symbols on an infinite tape according to a set of rules. A Turing machine can be modified in various ways to enhance its power or efficiency, but these modifications do not change the class of languages that can be accepted by a Turing machine. Some of the common modifications of Turing machine are:

- **Multiple track Turing machine**: A k-track Turing machine (for some k>0) has k-tracks and one R/W head that reads and writes all of them one by one. Each track can store a symbol from a finite alphabet. A multiple track Turing machine can simulate a single track Turing machine by using different symbols to represent the combinations of symbols on different tracks.
- **Two-way infinite tape Turing machine**: A two-way infinite tape Turing machine has an infinite tape that extends in both directions. The tape is divided into cells, each of which can store a symbol from a finite alphabet. A two-way infinite tape Turing machine can simulate a standard Turing machine by using a special symbol to mark the left end of the tape.
- **Multi-tape Turing machine**: A multi-tape Turing machine has k tapes (for some k>0) and k R/W heads, one for each tape. The tapes are initially filled with the input string on the first tape and blanks on the other tapes. The machine can read and write symbols on any tape and move the heads independently. A multi-tape Turing machine can simulate a single tape Turing machine by using a single tape to store the contents of all the tapes and using special symbols to separate them and indicate the positions of the heads.
- **Multi-tape multi-head Turing machine**: A multi-tape multi-head Turing machine has k tapes (for some k>0) and m heads (for some m>0) that can access any tape. The tapes are initially filled with the input string on the first tape and blanks on the other tapes. The machine can read and write symbols on any tape and move the heads independently. A multi-tape multi-head Turing machine can simulate a multi-tape Turing machine by using a single tape to store the contents of all the tapes and using special symbols to separate them and indicate the positions of the heads.
- **Multi-dimensional tape Turing machine**: A multi-dimensional tape Turing machine has a tape that is a grid of cells, each of which can store a symbol from a finite alphabet. The machine has a R/W head that can move in any direction on the grid. A multi-dimensional tape Turing machine can simulate a single tape Turing machine by using a one-dimensional tape to store the contents of the grid and using special symbols to indicate the boundaries and the position of the head.
- **Multi-head Turing machine**: A multi-head Turing machine has a single tape and k R/W heads (for some k>0) that can move independently on the tape. The tape is initially filled with the input string and blanks. The machine can read and write symbols on the tape and move the heads in either direction. A multi-head Turing machine can simulate a single tape Turing machine by using a single head and marking the positions of the other heads with special symbols on the tape.
- **Non-deterministic Turing machine**: A non-deterministic Turing machine has a set of rules that can specify more than one possible action for a given state and symbol. The machine can choose any of the possible actions and proceed with the computation. A non-deterministic Turing machine can simulate a deterministic Turing machine by following the same rules. A deterministic Turing machine can simulate a non-deterministic Turing machine by using a multi-tape Turing machine to keep track of all the possible branches of computation and exploring them one by one.

: Variation of Turing Machine - GeeksforGeeks



# Turing Machine as Computer of Integer Functions

- A Turing machine is a simple abstract computational device that can simulate any algorithm or computation .
- A Turing machine can compute functions of the form y = f(x), where x and y are integers or pairs of integers .
- To compute a function, a Turing machine needs an input tape, a finite control, a read-write head, and an output tape .
- The input tape contains the value of x, encoded in some way, such as unary or binary .
- The finite control contains the states and transitions of the Turing machine, which determine how the machine behaves based on the current state and the symbol read by the head .
- The read-write head can move left or right along the input tape, read the symbol at the current position, and write a new symbol or erase the old one .
- The output tape contains the value of y, encoded in the same way as x, after the Turing machine has performed the computation .
- The computation starts with the head at the leftmost position of the input tape, and the finite control in the initial state .
- The computation ends when the finite control reaches a final state, or when the Turing machine enters an infinite loop .
- The computation is successful if the output tape contains the correct value of y, and the head returns to the leftmost position of the output tape .
- The computation is unsuccessful if the output tape contains an incorrect value of y, or the head does not return to the leftmost position of the output tape .
- A Turing machine can compute any function that is computable, meaning that there exists an algorithm or a finite set of rules that can produce the correct output for any given input .
- A Turing machine cannot compute any function that is uncomputable, meaning that there is no algorithm or a finite set of rules that can produce the correct output for any given input .
- Examples of computable functions are addition, subtraction, multiplication, division, factorial, Fibonacci, etc .
- Examples of uncomputable functions are the halting problem, the busy beaver function, the Kolmogorov complexity, etc .



# Universal Turing machine

- A universal Turing machine (UTM) is a Turing machine that can simulate any other Turing machine on any input.
- A UTM essentially achieves this by reading both the description of the machine to be simulated and the input to that machine from its own tape .
- A UTM can also compute everything that a real computer can compute. For example, a UTM can simulate any function used in a programming language.
- A UTM was introduced by Alan Turing in 1936-1937 as a mathematical tool to investigate the extent and limitations of what can be computed.
- A UTM can also be used to prove the undecidability of some problems, such as the halting problem. The halting problem asks whether there exists an algorithm that can determine, given any Turing machine and any input, whether the machine will eventually halt or run forever.
- A UTM can be constructed from a finite number of states and symbols, depending on the encoding scheme used for the descriptions of the machines and the inputs. For example, one possible UTM has 22 states and 18 symbols.
- A UTM can be represented by a transition table, a transition diagram, or a set of instructions, similar to any other Turing machine.
- A UTM operates by reading the description of the machine to be simulated and the input to that machine from the left end of the tape, and then executing the instructions of the simulated machine on the input, using the rest of the tape as its work area.
- A UTM can be modified to accept multiple inputs, output the results of the simulation, or perform other tasks, by adding more states and symbols to the original UTM.



# Linear Bounded Automata

- A linear bounded automaton (LBA) is a type of Turing machine that has a finite amount of tape to work with.
- The tape is divided into cells, each containing a symbol from a finite alphabet.
- The tape has two special symbols, called left and right endmarkers, that mark the boundaries of the tape.
- The LBA has a finite set of states and a transition function that determines how it moves from one state to another, depending on the current state and the symbol under the tape head.
- The LBA can also change the symbol under the tape head, except for the endmarkers.
- The LBA can move the tape head left or right, but not beyond the endmarkers.
- The LBA can be deterministic or nondeterministic, meaning that it can have one or more possible transitions for a given state and symbol.
- The LBA can accept or reject an input string by entering a special state, called an accepting or rejecting state, respectively.
- The LBA can also halt without accepting or rejecting, by entering a state that has no transitions defined.
- The LBA is a restricted model of computation, since it cannot use more tape than the length of the input string, multiplied by a constant factor.
- The LBA can recognize a class of languages, called context-sensitive languages, that are more expressive than context-free languages, but less expressive than recursively enumerable languages.
- The LBA can be defined formally as an 8-tuple (Q, X, ∑, q0, ML, MR, δ, F), where:

  - Q is a finite set of states
  - X is the tape alphabet, which includes the endmarkers ML and MR
  - ∑ is the input alphabet, which is a subset of X without the endmarkers
  - q0 is the initial state
  - ML and MR are the left and right endmarkers, respectively
  - δ is the transition function, which maps Q × X to a subset of Q × X × {L, R}, where L and R are the left and right tape head movements, respectively
  - F is the set of accepting states, which is a subset of Q

- An example of an LBA that accepts the language {a^n b^n c^n | n ≥ 1} is shown below:

LBA example

- The LBA starts with the input string between the endmarkers, and then scans the tape from left to right, marking each a with an A, each b with a B, and each c with a C, while checking that the number of a's, b's, and c's are equal.
- If the LBA finds a mismatch or an invalid symbol, it rejects the input by entering the state qR.
- If the LBA reaches the right endmarker without finding any errors, it accepts the input by entering the state qF.



# Church's Thesis

- Church's thesis, also known as the Church-Turing thesis, is a statement about the nature and scope of computable functions.
- It asserts that any function that can be computed by an effective or systematic or mechanical method, i.e., a finite sequence of precise and unambiguous instructions, can also be computed by a Turing machine, i.e., a hypothetical device that manipulates symbols on an infinite tape according to a set of rules.
- The thesis is not a formal theorem, but rather a conjecture or a hypothesis that is widely accepted by the scientific community as a foundational principle of computability theory, the branch of mathematics and computer science that studies the limits of computation.
- The thesis was independently proposed by Alonzo Church and Alan Turing in the 1930s, based on their respective definitions of computable functions using lambda calculus and Turing machines. They also showed that their definitions were equivalent, i.e., that any function that can be computed by a lambda expression can also be computed by a Turing machine, and vice versa.
- The thesis has several implications and applications, such as:
  - It provides a precise and universal notion of what it means for a problem to be solvable by an algorithm or a program, regardless of the specific model of computation or programming language used.
  - It implies that there are problems that are inherently unsolvable by any algorithm or program, such as the halting problem, the Entscheidungsproblem, and the incompleteness theorems.
  - It suggests that any physical system that can perform computation, such as a digital computer, a neural network, or a quantum computer, is subject to the same limitations and capabilities as a Turing machine, unless it can exploit some form of hypercomputation that goes beyond the standard model of computation.
  - It serves as a basis for exploring the connections and differences between human intelligence and artificial intelligence, and the possibility of creating machines that can think, learn, and reason.



# Recursive and Recursively Enumerable Language

- A **recursive language** is a formal language for which there exists a Turing machine that accepts and halts on every input string, whether it belongs to the language or not.
- A **recursively enumerable language** is a formal language for which there exists a Turing machine that accepts and halts on every input string that belongs to the language, but may either reject or loop forever on input strings that do not belong to the language.
- Recursive languages are a subset of recursively enumerable languages, since a Turing machine that decides a language can also enumerate it by testing every possible input string in some order.
- Recursively enumerable languages are also called **Turing-recognizable languages** or **semi-decidable languages**.
- Some examples of recursive languages are:
  - The language of all palindromes over a finite alphabet.
  - The language of all strings over a finite alphabet that have an even number of symbols.
  - The language of all strings over a finite alphabet that are accepted by a finite automaton.
- Some examples of recursively enumerable languages that are not recursive are:
  - The language of all strings over a finite alphabet that are accepted by a pushdown automaton.
  - The language of all strings over a finite alphabet that encode a valid proof in some formal system.
  - The language of all strings over a finite alphabet that encode a Turing machine that halts on the empty input.



# Halting Problem

- The halting problem is a decision problem about properties of computer programs on a fixed Turing-complete model of computation, i.e., all programs that can be written in some given programming language that is general enough to be equivalent to a Turing machine.
- The problem is to determine, from a description of an arbitrary computer program and an input, whether the program will finish running, or continue to run forever.
- Alan Turing proved in 1936 that a general algorithm to solve the halting problem for all possible program–input pairs cannot exist.
- The proof is based on a contradiction: suppose there exists a program H that can decide the halting problem, then we can construct a program P that uses H as a subroutine and does the opposite of what H predicts, leading to a paradox.
- The halting problem is an early example of a decision problem, and also a good example of the limits of determinism in computer science.
- The halting problem is also related to other undecidable problems, such as the universal halting problem, which is the problem of determining whether a given computer program will halt for every input. This problem is not only undecidable, but highly undecidable, meaning that there is no algorithm that can even partially solve it.
- The halting problem and its variants illustrate the fundamental limitations of computability and decidability, and have important implications for the theory of computation and formal languages .



# Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows: Given two lists, M and N, of non-empty strings over Σ, such as:

  M = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ..., x<sub>n</sub>)

  N = (y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>, ..., y<sub>n</sub>)

  Find a sequence of indices (i<sub>1</sub>, i<sub>2</sub>, i<sub>3</sub>, ..., i<sub>k</sub>) such that:

  x<sub>i1</sub>x<sub>i2</sub>x<sub>i3</sub>...x<sub>ik</sub> = y<sub>i1</sub>y<sub>i2</sub>y<sub>i3</sub>...y<sub>ik</sub>

  If such a sequence exists, the PCP problem has a solution. Otherwise, it has no solution.

- The PCP problem can be visualized using dominoes, where each domino has a top string and a bottom string. The goal is to arrange the dominoes horizontally such that the top string and the bottom string are equal .

  For example, given the following dominoes:

  | 1 | 2 | 3 |
  |:-:|:-:|:-:|
  | a | ab | baa |
  | ba | a | aa |

  A possible solution is:

  | 2 | 3 | 1 | 3 |
  |:-:|:-:|:-:|:-:|
  | ab | baa | a | baa |
  | a | aa | ba | aa |

  Because:

  abbabaa = aaaabaa

- The PCP problem is undecidable, meaning that there is no algorithm that can determine whether a given instance of the PCP problem has a solution or not for all possible instances  .
- The PCP problem is often used in proofs of undecidability, because it is simpler than the halting problem and the Entscheidungsproblem .
- The PCP problem can be generalized to the Modified Post Correspondence Problem (MPCP), where the first domino in the sequence must have the same index as the last domino. The MPCP problem is also undecidable, and can be used to prove the undecidability of other problems, such as the emptiness problem for context-free grammars.



# Introduction to Recursive Function Theory

- Recursive function theory is a branch of mathematical logic that studies the class of functions on the natural numbers that can be defined by recursion .
- Recursion is a process of defining a function by applying the same function to its own arguments .
- A function that calls itself directly or indirectly is called a recursive function.
- Recursive functions are closely related to computability theory, which investigates the limits of what can be computed by machines such as Turing machines  .
- A recursive function is called total if it is defined for every input, or equivalently, if it can be computed by a total Turing machine.
- A recursive function is called partial if it is not defined for some inputs, or equivalently, if it can be computed by a partial Turing machine.
- A recursive function is called primitive recursive if it can be defined using only basic arithmetic operations, zero, successor, and bounded recursion  .
- A recursive function is called general recursive or simply recursive if it can be defined using unbounded recursion, or equivalently, if it can be computed by a Turing machine  .
- A recursive function is called computable if it can be computed by an algorithm, or equivalently, if it is general recursive  .
- A recursive function is called uncomputable if it cannot be computed by any algorithm, or equivalently, if it is not general recursive  .
- A set of natural numbers is called recursive or computable if its characteristic function (which returns 1 if the input belongs to the set and 0 otherwise) is recursive  .
- A set of natural numbers is called recursively enumerable or semi-computable if its enumeration function (which lists the elements of the set in some order) is recursive  .
- A set of natural numbers is called co-recursively enumerable or co-semi-computable if its complement is recursively enumerable  .
- A set of natural numbers is called decidable if it is recursive, and undecidable if it is not recursive  .
- A set of natural numbers is called semi-decidable if it is recursively enumerable, and co-semi-decidable if it is co-recursively enumerable  .
- A set of natural numbers is called creative if it is recursively enumerable but not recursive, and its complement is not recursively enumerable  .
- A set of natural numbers is called simple if it is recursively enumerable but not recursive, and its complement is infinite and recursive  .
- A set of natural numbers is called m-complete if it is recursively enumerable but not recursive, and every recursively enumerable set is reducible to it  .
- A set of natural numbers is called m-intermediate if it is recursively enumerable but not recursive, and neither reducible to nor from any m-complete set  .
- A set of natural numbers is called m-simple if it is recursively enumerable but not recursive, and its complement is infinite and co-recursively enumerable  .
- A set of natural numbers is called productive if it is recursively enumerable but not recursive, and there is a recursive function that produces an element of the set from any recursive function that enumerates a subset of the set  .
- A set of natural numbers is called immune if it is infinite and recursive, and none of its infinite subsets is recursively enumerable  .
- A set of natural numbers is called hyperimmune if it is infinite and recursive, and there is no recursive function that dominates its enumeration function  .
- A set of natural numbers is called hyperimmune-free if it is

