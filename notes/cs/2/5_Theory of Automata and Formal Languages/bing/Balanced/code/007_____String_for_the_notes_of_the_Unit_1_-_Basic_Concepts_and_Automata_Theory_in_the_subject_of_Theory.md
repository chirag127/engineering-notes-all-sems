# String

- A string is a finite sequence of symbols chosen from a finite set called an alphabet.
- For example, if the alphabet is {0, 1}, then some possible strings are 0, 1, 01, 10, 001, 1010, etc.
- The empty string, denoted by ε, is the string that contains no symbols at all.
- The length of a string, denoted by |s|, is the number of symbols in the string.
- For example, |0| = 1, |01| = 2, |ε| = 0.
- The concatenation of two strings s and t, denoted by s⋅t or simply st, is the string obtained by appending t to the end of s.
- For example, if s = 01 and t = 10, then st = 0110.
- The reverse of a string s, denoted by s^R, is the string obtained by reversing the order of the symbols in s.
- For example, if s = 0110, then s^R = 0110.
- A string s is a prefix of a string t if there exists a string u such that t = su.
- For example, 0, 01, and 011 are prefixes of 0110.
- A string s is a suffix of a string t if there exists a string u such that t = us.
- For example, 0, 10, and 110 are suffixes of 0110.
- A string s is a substring of a string t if there exists strings u and v such that t = usv.
- For example, 1, 11, and 110 are substrings of 0110.
- A string s is a subsequence of a string t if there exists a sequence of indices i_1 < i_2 < ... < i_k such that s = t[i_1]t[i_2]...t[i_k].
- For example, 0, 01, and 010 are subsequences of 0110.

# Formal Language

- A formal language is a set of strings over a given alphabet.
- For example, the set of all binary strings that start with 0 is a formal language over the alphabet {0, 1}.
- A formal language can be finite or infinite, depending on the size of the set.
- For example, the set of all binary strings of length 3 is a finite language, while the set of all binary strings is an infinite language.
- A formal language can be defined by various methods, such as regular expressions, grammars, or automata.
- For example, the language of all binary strings that start with 0 can be defined by the regular expression 0(0 + 1)*, or by the grammar S -> 0A, A -> 0A | 1A | ε, or by the automaton shown below:

![automaton](https://i.imgur.com/8f8ZwZw.png)

# Automata Theory

- Automata theory is the study of abstract machines that can process strings and recognize formal languages.
- An automaton consists of a finite set of states, a finite set of input symbols, a transition function that maps states and symbols to states, an initial state, and a set of final or accepting states.
- For example, the automaton shown above has four states, {q0, q1, q2, q3}, two input symbols, {0, 1}, a transition function defined by the arrows, an initial state q0, and a final state q3.
- An automaton can process a string by starting from the initial state and following the transitions according to the input symbols. If the automaton reaches a final state after reading the whole string, the string is accepted by the automaton. Otherwise, the string is rejected by the automaton.
- For example, the automaton above accepts the string 0110, but rejects the string 1100.
- There are different types of automata, depending on the power and complexity of the transition function and the memory available to the automaton.
- Some common types of automata are:

  - Finite automata (FA): These are the simplest type of automata, where the transition function depends only on the current state and the current input symbol. They have no memory other than the current state. They can recognize regular languages, which are the languages that can be defined by regular expressions or regular grammars.
  -