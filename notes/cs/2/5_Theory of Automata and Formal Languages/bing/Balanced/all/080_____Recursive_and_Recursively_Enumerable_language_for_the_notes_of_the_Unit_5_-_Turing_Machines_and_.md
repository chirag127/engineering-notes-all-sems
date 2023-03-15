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