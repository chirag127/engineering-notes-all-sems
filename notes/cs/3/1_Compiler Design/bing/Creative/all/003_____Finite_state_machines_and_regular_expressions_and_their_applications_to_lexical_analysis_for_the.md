# Finite state machines and regular expressions and their applications to lexical analysis

- Finite state machines (FSMs) are abstract models of computation that can process a sequence of inputs and change their state accordingly.
- Regular expressions (REs) are algebraic notations that can specify a set of strings, called a regular language, using symbols and operators.
- Lexical analysis is the first phase of a compiler, where the source code is scanned and divided into meaningful units, called tokens.
- The applications of FSMs and REs to lexical analysis are:
  - FSMs can be used as recognizers for REs, that is, they can determine whether a given input string belongs to the language specified by a RE.
  - REs can be used as generators for FSMs, that is, they can provide a concise and convenient way of describing the structure and syntax of tokens.
  - Algorithms exist to convert REs to FSMs and vice versa, which can facilitate the design and implementation of lexical analyzers.
  - FSMs can be implemented using lookup tables or transition diagrams, which can be easily encoded and executed by a computer program.
  - REs and FSMs can handle common lexical patterns, such as identifiers, keywords, literals, operators, comments, etc.