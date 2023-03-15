### Recursive and Recursively Enumerable language

- A **recursive language** is a formal language for which there exists a Turing machine (or other computable function) that will halt and accept when presented with any string in the language as input and will halt and reject when presented with any string not in the language .
- A **recursively enumerable language** is a formal language for which there exists a Turing machine (or other computable function) that will halt and accept when presented with any string in the language as input but may either halt and reject or loop forever when presented with a string not in the language  .
- A recursive language is also a recursively enumerable language, but the converse is not true .
- A recursively enumerable language is also called a **semi-decidable language** or a **Turing-recognizable language** .
- A recursive language is also called a **decidable language** or a **Turing-decidable language** .
- A language is recursive if and only if it is both recursively enumerable and co-recursively enumerable, where the co-language is the complement of the language .
- A language is recursively enumerable if and only if there exists an enumeration procedure that generates all the strings in the language in some order .
- A language is recursive if and only if there exists a decision procedure that determines whether a given string belongs to the language or not in a finite amount of time .
- Examples of recursive languages are the language of palindromes over a finite alphabet, the language of well-formed arithmetic expressions, and the language of syntactically correct programs in a given programming language .
- Examples of recursively enumerable languages that are not recursive are the language of theorems in a given formal system, the language of halting Turing machines, and the language of prime numbers  .