### Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence in a table.
- The algorithm works as follows:

  - Initialize the table with the probabilities of the terminal symbols for each word in the sentence.
  - For each substring of length 2 or more, consider all possible ways of splitting it into two smaller substrings, and all possible rules of the form A -> BC that can generate the substring.
  - For each such rule, multiply the probabilities of the subtrees for B and C, and the probability of the rule itself, and store the maximum value in the table for A.
  - Repeat until the table is filled.
  - The probability of the most likely parse tree for the whole sentence is the maximum value in the table for the start symbol of the grammar.
  - The most likely parse tree can be reconstructed by tracing back the table entries from the start symbol to the terminal symbols.