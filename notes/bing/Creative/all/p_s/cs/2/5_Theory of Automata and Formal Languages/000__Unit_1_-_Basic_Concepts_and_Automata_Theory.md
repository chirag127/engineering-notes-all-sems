## Unit 1 - Basic Concepts and Automata Theory

- Automata theory is the study of abstract machines and automata, as well as the computational problems that can be solved using them.
- An automaton is a self-operating machine that follows a predetermined sequence of instructions and operations.
- Automata theory is a branch of theoretical computer science that aims to understand the capabilities and limitations of different models of computation.
- Some applications of modern automata include robotics, spell checkers, text editors, artificial intelligence, and genetic programming.
- The four types of automata are:
  - Finite state machine: A machine that has a finite number of states and transitions between them based on the input symbols. It can accept or reject a string of symbols based on whether it reaches a final state or not.
  - Pushdown machine: A machine that has a finite state machine and a stack that can store symbols. It can push or pop symbols from the stack based on the input and the current state. It can accept or reject a string of symbols based on whether it reaches a final state and whether the stack is empty or not.
  - Turing machine: A machine that has a finite state machine and an infinite tape that can store symbols. It can read or write symbols on the tape and move the tape head left or right based on the input and the current state. It can accept or reject a string of symbols based on whether it halts or not.
  - Linear bounded automaton: A machine that is a restricted version of a Turing machine, where the tape is bounded by the length of the input. It can accept or reject a string of symbols based on whether it halts or not.

- The following diagram shows the hierarchy of automata and the classes of languages they can recognize:

```
+-----------------+     +-----------------+
| Turing machines | --> | Linear bounded  |
|                 |     | automata        |
+-----------------+     +-----------------+
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        |                      |
        v                      v
+-----------------+     +-----------------+
| Pushdown        | --> | Finite state    |
| machines        |     | machines        |
+-----------------+     +-----------------+
```

- The classes of languages they can recognize are:
  - Turing machines: Turing-recognizable languages (also called recursively enumerable languages)
  - Linear bounded automata: Context-sensitive languages
  - Pushdown machines: Context-free languages
  - Finite state machines: Regular languages

- The following table summarizes some of the properties of these classes of languages and automata:

| Class of language | Class of automaton | Closure properties | Decision properties |
|-------------------|--------------------|--------------------|---------------------|
| Regular           | Finite state       | Union, intersection, complement, concatenation, Kleene star | Emptiness, finiteness, membership, equivalence, minimization |
| Context-free      | Pushdown           | Union, concatenation, Kleene star | Emptiness, membership, ambiguity |
| Context-sensitive | Linear bounded     | Union, intersection, complement, concatenation, Kleene star | Emptiness, membership |
| Turing-recognizable| Turing            | Union, intersection, concatenation, Kleene star | Emptiness, membership (semi-decidable) |

- Some examples of regular languages are:
  - The set of all binary strings that end with 0
  - The set of all decimal numbers that are divisible by 3
  - The set of all strings over {a, b, c} that do not contain the substring "abc"

- Some examples of context-free languages are:
  - The set of all balanced parentheses
  - The set of all palindromes over {a, b}
  - The set of all arithmetic expressions with +, -, *, /, and parentheses

- Some examples of context-sensitive languages are:
  - The set of all strings of the form a^n b^n c^n, where n > 0
  - The set of all strings of the form w w^R, where w is any string and w^R is its reverse
  - The set of all strings of the form a^i b^j c^k, where i, j, k > 0 and i = j

Some possible mnemonics and learning tricks for the topic are:

- To remember the hierarchy of automata and languages, you can use the acronym FLPT (Finite, Pushdown, Linear, Turing) and think of it as "Flip the Tape".
- To remember the closure properties of regular languages, you can use the acronym UICCK (Union, Intersection, Complement, Concatenation, Kleene star) and think of it as "You I See, OK?".
- To remember the closure properties of context-free languages, you can use the acronym UCK (Union, Concatenation, Kleene star) and think of it as "You See, OK?".
- To remember the decision properties of regular languages, you can use the acronym EFMEM (Emptiness, Finiteness, Membership, Equivalence, Minimization) and think of it as "Eff 'em".
- To remember the decision properties of context-free languages, you can use the acronym EMA (Emptiness, Membership, Ambiguity) and think of it as "Emma".
- To remember the decision properties of context-sensitive languages, you can use the acronym EM (Emptiness, Membership) and think of it as "Em".
- To remember the decision properties of Turing-recognizable languages, you can use the acronym EM (Emptiness, Membership) and think of it as "Em", but with a question mark, since they are only semi-decidable.