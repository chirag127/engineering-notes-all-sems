### Finite-State Automata for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Finite-state automata (FSA) are abstract machines that can recognize and generate patterns of symbols, such as strings of characters or words .
- FSA have a finite number of states, a set of input symbols, a set of output symbols (optional), a start state, and a set of final states .
- FSA can be deterministic (DFA) or non-deterministic (NFA). DFA have exactly one transition for each input symbol and state, while NFA can have zero, one, or more transitions for each input symbol and state .
- FSA can be used for various natural language processing (NLP) tasks, such as tokenization, morphological analysis, part-of-speech tagging, named entity recognition, and text normalization    .
- FSA can also be extended to finite-state transducers (FST), which can produce some output for a given input. FST can be used for tasks such as spelling correction, text generation, speech recognition, and machine translation   .
- FSA and FST have several advantages for NLP, such as:
  - They are simple and intuitive to design and implement .
  - They are efficient and fast to execute, as they only require a constant amount of memory and a linear scan of the input   .
  - They are expressive and powerful, as they can capture regular languages and regular relations, which are suitable for many NLP tasks    .
  - They are compositional and modular, as they can be combined using operations such as union, concatenation, intersection, complement, and inversion    .
  - They are robust and flexible, as they can handle noise, ambiguity, and variation in natural language    .

- Here is an example of a DFA that recognizes the language of all strings over the alphabet {a, b} that end with the substring "ab":

```
    a     b
  +---+  +---+
  |   |  |   |
  |   v  v   |
+---+---+---+---+---+
| q0| q1| q2| q3| q4|
+---+---+---+---+---+
  ^   |   |   |   |
  |   |   |   |   |
  +---+---+---+---+
    a     b
```

- The states are q0, q1, q2, q3, and q4. The start state is q0 and the final state is q4. The input symbols are a and b. The output symbols are not shown, as this is a recognizer and not a transducer.
- The transitions are labeled with the input symbols that trigger them. For example, if the current state is q0 and the input symbol is a, then the next state is q1. If the current state is q1 and the input symbol is b, then the next state is q4, which is the final state.
- The DFA accepts a string if it reaches a final state after reading the entire string. For example, the DFA accepts the string "aab" but rejects the string "aba".
- Here is a possible mnemonic to remember the DFA: "Start with q0, then follow the arrows. If you see ab at the end, you win. Otherwise, you lose."