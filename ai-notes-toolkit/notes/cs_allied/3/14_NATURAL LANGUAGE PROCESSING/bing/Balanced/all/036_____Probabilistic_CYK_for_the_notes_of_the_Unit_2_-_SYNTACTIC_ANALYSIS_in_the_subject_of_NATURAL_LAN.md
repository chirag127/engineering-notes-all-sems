# Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree for a given sentence and a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence, and then combines them to find the most probable parse tree.
- The algorithm works as follows:

  - Initialize a table T of size n x n, where n is the length of the input sentence, and fill it with zeros.
  - For each word w_i in the sentence, find all the nonterminals A that can generate w_i with some probability P(A -> w_i), and set T[i, i] = P(A -> w_i).
  - For each span length l from 2 to n, and for each start position i from 1 to n - l + 1, do the following:
    - Set j = i + l - 1, and initialize T[i, j] = 0.
    - For each split position k from i to j - 1, find all the nonterminals A that can generate the substring from i to j with some probability P(A -> BC), where B and C are the nonterminals that generate the substrings from i to k and from k + 1 to j, respectively.
    - Update T[i, j] = max(T[i, j], P(A -> BC) * T[i, k] * T[k + 1, j]).
  - The most probable parse tree for the sentence is the one that corresponds to the nonterminal A that maximizes T[1, n].