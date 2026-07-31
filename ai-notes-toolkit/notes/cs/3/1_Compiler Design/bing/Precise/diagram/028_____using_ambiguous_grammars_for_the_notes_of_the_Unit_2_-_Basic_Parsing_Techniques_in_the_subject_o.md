### Unit 2 - Basic Parsing Techniques: Using Ambiguous Grammars

- An ambiguous grammar is a context-free grammar that generates a sentence for which there are two or more distinct parse trees.
- Ambiguity in a grammar can cause problems in parsing, as it can lead to multiple interpretations of the same sentence.
- To resolve ambiguity, one approach is to use disambiguation techniques such as precedence and associativity rules to select a preferred parse tree.
- Another approach is to rewrite the grammar to remove the ambiguity, by introducing new non-terminals and production rules.
- It is important to note that not all ambiguous grammars can be rewritten to be unambiguous, and some languages are inherently ambiguous.
- In such cases, parsing techniques such as GLR (Generalized LR) parsing or Earley parsing can be used to handle ambiguous grammars.
- These parsing techniques can generate all possible parse trees for an ambiguous sentence, allowing the parser to choose the most appropriate interpretation based on additional information or heuristics.
