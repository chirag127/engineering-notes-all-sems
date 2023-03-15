### Languages

- In automata theory, a formal language is a set of strings of symbols drawn from a finite alphabet .
- A formal language can be specified either by a set of rules (such as regular expressions or a context-free grammar) that generates the language, or by a formal machine that accepts (recognizes) the language .
- A word is a finite string of symbols from the alphabet.
- A language is a set of words, possibly infinite.
- A formal language can be classified into different types based on the complexity and expressive power of the rules or machines that define or recognize it.
- The Chomsky hierarchy is a classification of formal languages into four types: regular, context-free, context-sensitive, and recursively enumerable.
- Regular languages are the simplest and most restricted type of formal languages. They can be defined by regular expressions or finite automata .
- Regular expressions are algebraic expressions that use symbols, concatenation, union, and Kleene star to construct regular languages .
- Finite automata are abstract machines that have a finite number of states and transitions, and can accept or reject an input word based on the state reached after reading the word .
- Finite automata can be either deterministic or nondeterministic. Deterministic finite automata (DFA) have exactly one transition for each state and input symbol, while nondeterministic finite automata (NFA) can have zero, one, or more transitions for each state and input symbol .
- Regular languages have the following closure properties: they are closed under union, concatenation, Kleene star, intersection, complement, and difference .
- Non-regular languages are formal languages that cannot be defined by regular expressions or finite automata. They are more complex and expressive than regular languages.
- Examples of non-regular languages are: the language of palindromes, the language of balanced parentheses, and the language of words with equal number of a's and b's.
- Non-regular languages can be defined by more powerful rules or machines, such as context-free grammars or pushdown automata.
- Context-free grammars are sets of rules that use variables, terminals, and productions to generate context-free languages.
- Pushdown automata are abstract machines that have a finite number of states, transitions, and a stack, and can accept or reject an input word based on the state and stack contents reached after reading the word.
- Non-regular languages have the following closure properties: they are closed under union, concatenation, Kleene star, and intersection with regular languages, but not under intersection, complement, or difference.