## Unit 2 - Regular Expressions and Languages

1. **Regular Expressions**: A regular expression is a pattern that describes a set of strings. It is a way to describe and parse text. Regular expressions are used in many programming languages, text editors, and command line tools.

2. **Regular Languages**: A regular language is a formal language that can be expressed using a regular expression. Regular languages are a subset of the set of all formal languages. They have a simple structure and can be recognized by a finite automaton.

3. **Finite Automata**: A finite automaton is a mathematical model of computation used to recognize regular languages. It consists of a finite set of states, a set of input symbols, a transition function, an initial state, and a set of accepting states.

4. **Deterministic Finite Automata (DFA)**: A DFA is a type of finite automaton where for each state and input symbol, there is a unique next state. DFAs can be used to recognize regular languages.

5. **Nondeterministic Finite Automata (NFA)**: An NFA is a type of finite automaton where for each state and input symbol, there can be multiple next states. NFAs can also be used to recognize regular languages.

6. **Conversion of NFA to DFA**: An NFA can be converted to an equivalent DFA using the powerset construction. This involves creating a new DFA state for each subset of NFA states and defining the transitions of the new DFA based on the transitions of the NFA.

7. **Regular Grammars**: A regular grammar is a type of formal grammar that can generate a regular language. Regular grammars have a simple structure and can be used to define regular languages.

8. **Closure Properties of Regular Languages**: Regular languages are closed under several operations, including union, concatenation, and Kleene star. This means that if two languages are regular, then the language resulting from applying one of these operations to the two languages is also regular.

9. **Pumping Lemma for Regular Languages**: The pumping lemma for regular languages is a property that can be used to prove that a language is not regular. It states that for any regular language, there exists a constant `p` such that any string in the language of length at least `p` can be divided into three substrings that satisfy certain conditions.

10. **Decision Problems for Regular Languages**: There are several decision problems for regular languages, including the emptiness problem, the membership problem, and the equivalence problem. These problems can be solved using algorithms that operate on finite automata or regular expressions.