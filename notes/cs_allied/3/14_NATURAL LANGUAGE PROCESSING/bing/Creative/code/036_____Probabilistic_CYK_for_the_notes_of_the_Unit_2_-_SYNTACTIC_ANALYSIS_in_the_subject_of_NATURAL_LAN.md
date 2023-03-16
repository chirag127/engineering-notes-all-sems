### Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence in a table.
- The algorithm works as follows:

  - Initialize the table with the probabilities of the terminal symbols for each word in the sentence.
  - For each substring of length 2 or more, consider all possible ways of splitting it into two smaller substrings, and all possible rules of the form A -> BC that can generate the substring.
  - For each rule A -> BC, compute the probability of the substring as the product of the probability of the rule and the probabilities of the two smaller substrings, and store the maximum probability and the corresponding rule in the table.
  - Repeat until the table is filled.
  - The probability of the whole sentence is the probability of the start symbol S for the entire sentence, and the most likely parse tree can be reconstructed by tracing back the rules stored in the table.

- The probabilistic CYK algorithm can handle ambiguous grammars, where more than one parse tree is possible for a given sentence, by choosing the most probable one.
- The probabilistic CYK algorithm can also handle unknown words, by assigning them a default probability and a default part-of-speech tag.