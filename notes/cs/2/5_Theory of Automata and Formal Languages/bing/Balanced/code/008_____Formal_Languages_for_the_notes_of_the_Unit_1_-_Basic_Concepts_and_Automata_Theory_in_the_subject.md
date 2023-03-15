# Formal Languages

- A formal language is a set of strings over a finite alphabet.
- An alphabet is a finite, non-empty set of symbols, usually denoted by $\Sigma$.
- A string is a finite sequence of symbols from an alphabet, also called a word or a sentence.
- The length of a string $w$, denoted by $|w|$, is the number of symbols in $w$.
- The empty string, denoted by $\epsilon$, is the string of length zero.
- A language $L$ over an alphabet $\Sigma$ is a subset of $\Sigma^*$, the set of all possible strings over $\Sigma$.
- A language can be finite or infinite, depending on the number of strings it contains.
- A language can be described by various means, such as regular expressions, grammars, or automata.

# Automata Theory

- Automata theory is the study of abstract machines that can recognize or generate formal languages.
- An automaton is a mathematical model of a system that can change its state in response to some inputs.
- A finite automaton is an automaton that has a finite number of states and a finite alphabet of inputs.
- A deterministic finite automaton (DFA) is a finite automaton that has exactly one transition for each state and input symbol.
- A nondeterministic finite automaton (NFA) is a finite automaton that can have zero, one, or more transitions for each state and input symbol.
- A DFA or an NFA can accept or reject a string by starting from an initial state and following the transitions according to the input symbols, and ending in a final or accepting state or a non-final or rejecting state.
- The set of strings that a DFA or an NFA can accept is called the language recognized or accepted by the automaton.
- A regular language is a language that can be recognized by some DFA or NFA.
- A regular expression is a compact notation for describing a regular language using symbols, concatenation, union, and Kleene star operations.
- A regular grammar is a grammar that can generate a regular language using rules of the form $A \rightarrow a$ or $A \rightarrow aB$, where $A$ and $B$ are variables and $a$ is a terminal symbol.