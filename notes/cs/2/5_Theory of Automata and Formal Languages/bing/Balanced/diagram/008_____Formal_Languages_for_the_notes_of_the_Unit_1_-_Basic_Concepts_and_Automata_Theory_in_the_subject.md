### Formal Languages

- A formal language is a set of strings over a finite alphabet.
- An alphabet is a finite set of symbols, such as {0, 1} or {a, b, c, ..., z}.
- A string is a finite sequence of symbols from an alphabet, such as 0101 or hello.
- The length of a string is the number of symbols in it, denoted by |s|.
- The empty string is the string with no symbols, denoted by ε or λ.
- A language is a set of strings over an alphabet, such as {0, 1, 10, 11} or {a, ab, aba, abab, ...}.
- A language can be finite or infinite, depending on the number of strings in it.
- A language can be defined by a rule, such as L = {0n1n | n ≥ 0} or L = {w | w is a palindrome}.
- A language can also be defined by a grammar, which is a set of rules for generating strings in the language.
- A grammar consists of a set of variables, a set of terminals, a start variable, and a set of production rules.
- A variable is a symbol that can be replaced by a string, such as S or A.
- A terminal is a symbol that cannot be replaced, such as 0 or 1.
- A start variable is a special variable that represents the whole string, such as S.
- A production rule is a rule of the form A → α, where A is a variable and α is a string of variables and terminals, such as S → 0S1 or A → aA | ε.
- A grammar generates a string by starting from the start variable and applying production rules until no variables are left, such as S → 0S1 → 00S11 → 0011.
- A grammar defines a language by generating all and only the strings in the language, such as L = {0n1n | n ≥ 0} or L = {w | w is a palindrome}.

### Automata Theory

- Automata theory is the study of abstract machines that can recognize and process formal languages.
- An automaton is a mathematical model of a machine that has a finite number of states, a finite set of inputs, and a transition function that defines how the machine changes states based on the inputs.
- An automaton can also have an output function that defines what the machine produces as output based on the states and inputs.
- An automaton can be deterministic or nondeterministic, depending on whether the transition function is a function or a relation.
- A deterministic automaton has a unique next state for each state and input, such as a deterministic finite automaton (DFA) or a deterministic pushdown automaton (DPDA).
- A nondeterministic automaton has a set of possible next states for each state and input, such as a nondeterministic finite automaton (NFA) or a nondeterministic pushdown automaton (NPDA).
- A nondeterministic automaton can be converted to an equivalent deterministic automaton using the subset construction or the powerset construction.
- An automaton can be finite or infinite, depending on whether the machine has a finite or infinite memory, such as a finite automaton (FA) or a Turing machine (TM).
- A finite automaton has a finite memory that consists of the current state, such as a DFA or an NFA.
- A finite automaton can recognize regular languages, which are the languages that can be defined by regular expressions or regular grammars.
- A regular expression is a notation for describing regular languages using symbols, concatenation, union, and Kleene star, such as 0*1* or (a|b)*abb.
- A regular grammar is a grammar that has production rules of the form A → a or A → aB, where A and B are variables and a is a terminal, such as S → aS | bA | ε or A → bA | b.
- A finite automaton can be converted to an equivalent regular expression using the state elimination method or the Kleene's theorem.
- A finite automaton can also be converted to an equivalent regular grammar using the state labeling method or the right linear grammar method.

- An infinite automaton has an infinite memory that consists of the current state and an auxiliary storage, such as a stack or a tape, such as a PDA or a TM.
- An infinite automaton can recognize more powerful languages than finite automata, such as context