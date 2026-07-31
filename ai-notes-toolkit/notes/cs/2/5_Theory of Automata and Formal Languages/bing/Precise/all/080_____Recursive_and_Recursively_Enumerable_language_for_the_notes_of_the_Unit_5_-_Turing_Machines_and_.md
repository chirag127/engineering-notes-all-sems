# Recursive and Recursively Enumerable Language

## Unit 5 - Turing Machines and Recursive Function Theory

### Theory of Automata and Formal Languages

- A **recursive language** is a formal language for which there exists a Turing machine that, when presented with any finite input string, halts and accepts if the string is in the language, and halts and rejects otherwise.
- A **recursively enumerable language** is a formal language for which there exists a Turing machine that, when presented with any finite input string, halts and accepts if the string is in the language, and runs forever otherwise.
- Recursive languages are also known as **decidable languages**, as there is an algorithm (in the form of a Turing machine) that can decide whether a given string is in the language or not.
- Recursively enumerable languages are also known as **semi-decidable languages** or **Turing-recognizable languages**, as there is an algorithm (in the form of a Turing machine) that can recognize whether a given string is in the language or not, but may not halt if the string is not in the language.
- All recursive languages are recursively enumerable, but not all recursively enumerable languages are recursive.
- The set of recursive languages is a proper subset of the set of recursively enumerable languages.
- The complement of a recursive language is also recursive, while the complement of a recursively enumerable language is not necessarily recursively enumerable.
- The halting problem is an example of a problem that is recursively enumerable but not recursive.