## Unit 2 - Regular Expressions and Languages

1. **Regular Expressions**: A regular expression is a pattern that describes a set of strings. It is a way to describe and parse text. Regular expressions are used in many programming languages, text editors, and other tools to search and manipulate text.

2. **Regular Languages**: A regular language is a formal language that can be expressed using a regular expression. Regular languages are recognized by finite automata and are closed under the operations of union, concatenation, and Kleene star.

3. **Kleene Star**: The Kleene star is an operation on a set of strings, denoted by `*`, that results in the set of all possible strings that can be formed by concatenating zero or more strings from the original set.

4. **Finite Automata**: A finite automaton is a mathematical model of computation used to recognize regular languages. It consists of a finite set of states, a set of input symbols, a transition function, an initial state, and a set of accepting states.

5. **Deterministic Finite Automata (DFA)**: A DFA is a type of finite automaton where, for each state and input symbol, there is a unique transition to a next state. DFAs can be used to recognize regular languages.

6. **Nondeterministic Finite Automata (NFA)**: An NFA is a type of finite automaton where, for each state and input symbol, there may be multiple transitions to next states. NFAs can also be used to recognize regular languages.

7. **Conversion of NFA to DFA**: An NFA can be converted to an equivalent DFA using the powerset construction. This involves creating a new DFA state for each subset of NFA states and defining the transitions of the new DFA based on the transitions of the NFA.

8. **Regular Grammar**: A regular grammar is a type of formal grammar that generates a regular language. It consists of a finite set of production rules that describe how strings in the language can be generated from a set of terminal and nonterminal symbols.

9. **Pumping Lemma for Regular Languages**: The pumping lemma for regular languages is a property that can be used to prove that a language is not regular. It states that for any regular language, there exists a constant `p` such that any string in the language of length at least `p` can be divided into three substrings, `xyz`, such that `|xy| <= p`, `|y| > 0`, and `xy^iz` is in the language for all `i >= 0`.

10. **Closure Properties of Regular Languages**: Regular languages are closed under the operations of union, concatenation, and Kleene star. This means that if `L1` and `L2` are regular languages, then `L1 U L2`, `L1L2`, and `L1*` are also regular languages. Regular languages are also closed under complementation and intersection.