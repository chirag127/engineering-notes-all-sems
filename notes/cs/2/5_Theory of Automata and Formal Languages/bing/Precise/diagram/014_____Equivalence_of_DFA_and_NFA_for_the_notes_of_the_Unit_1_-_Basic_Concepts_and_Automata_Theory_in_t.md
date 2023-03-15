### Equivalence of DFA and NFA

A Deterministic Finite Automaton (DFA) is a type of finite state machine that accepts or rejects a given string of symbols, based on whether the sequence of states it goes through ends in an accepting state or not. A Non-deterministic Finite Automaton (NFA) is similar to a DFA, but it allows for multiple possible transitions from a single state for a given input symbol, including the possibility of no transition at all.

The equivalence of DFA and NFA means that for any given NFA, there exists a DFA that recognizes the same language as the NFA. This is known as the **NFA to DFA conversion** or **subset construction**.

The subset construction algorithm works by creating a new DFA state for each possible subset of NFA states. The transition function of the new DFA is defined such that, for each input symbol, the new DFA state corresponding to a given subset of NFA states transitions to the new DFA state corresponding to the set of NFA states that can be reached from the original subset of NFA states by following transitions on the given input symbol.

The start state of the new DFA is the set containing only the start state of the NFA, and the accepting states of the new DFA are the sets that contain at least one accepting state of the NFA.

In summary, the equivalence of DFA and NFA means that any language that can be recognized by an NFA can also be recognized by a DFA, and vice versa. This is an important concept in the study of automata theory and formal languages.