# Probabilistic CYK

- Probabilistic CYK is an extension of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- Probabilistic CYK uses dynamic programming to store and reuse the probabilities of subtrees in a table, similar to the CYK algorithm.
- The algorithm works as follows:

  - Initialize a table T of size n x n, where n is the length of the input sentence.
  - For each word in the sentence, fill the corresponding diagonal cell in T with the nonterminals that can generate that word, along with their probabilities.
  - For each span of length 2 to n, consider every possible split point and every possible pair of nonterminals that can generate the span, according to the PCFG rules. Calculate the probability of the span as the product of the probabilities of the two subspans and the probability of the rule. Store the maximum probability and the corresponding nonterminal in the cell of T for that span.
  - The most likely parse tree is the one that corresponds to the nonterminal with the highest probability in the top-right cell of T. This can be retrieved by backtracking from the cell and following the pointers to the subspans.

- The probabilistic CYK algorithm can be improved by using log-probabilities instead of probabilities, to avoid underflow issues when multiplying many small numbers.
- The probabilistic CYK algorithm can be used for natural language parsing, speech recognition, machine translation, and other applications that involve finding the most likely structure of a given input.