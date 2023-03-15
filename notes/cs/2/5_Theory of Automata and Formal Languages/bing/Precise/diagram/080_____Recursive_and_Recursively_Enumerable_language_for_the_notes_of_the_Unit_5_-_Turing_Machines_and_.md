### Recursive and Recursively Enumerable language

Unit 5 - Turing Machines and Recursive Function Theory

Subject: Theory of Automata and Formal Languages

- A **recursive language** is a formal language for which there exists a Turing machine that, when presented with any finite input string, halts and accepts if the string is in the language, and halts and rejects otherwise.
- A **recursively enumerable language** is a formal language for which there exists a Turing machine that, when presented with any finite input string, halts and accepts if the string is in the language, and runs forever otherwise.
- Recursive languages are also known as **decidable languages**, while recursively enumerable languages are also known as **semi-decidable languages** or **Turing-recognizable languages**.
- Every recursive language is also recursively enumerable, but not every recursively enumerable language is recursive.
- The set of all recursive languages is a proper subset of the set of all recursively enumerable languages.
- The complement of a recursive language is also recursive, while the complement of a recursively enumerable language is not necessarily recursively enumerable.
- The halting problem is an example of a problem that is recursively enumerable but not recursive.