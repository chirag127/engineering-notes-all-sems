### Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence in a table.
- The algorithm works as follows:
  - Initialize the table with the probabilities of the terminal symbols for each word in the sentence.
  - For each substring of length 2 or more, consider all possible ways of splitting it into two smaller substrings, and check if there is a rule of the form A -> BC that can generate the substring from the two smaller substrings.
  - If there is such a rule, compute the probability of the subtree rooted at A as the product of the probabilities of the subtrees rooted at B and C, and the probability of the rule A -> BC.
  - Store the maximum probability and the corresponding rule for each nonterminal symbol that can generate the substring in the table.
  - Repeat until the table is filled.
  - The most likely parse tree for the whole sentence is the one with the highest probability in the top-right cell of the table, and it can be reconstructed by tracing back the rules stored in the table.
- The probabilistic CYK algorithm can be used for parsing natural language sentences, as well as other applications that involve probabilistic modeling of context-free structures.