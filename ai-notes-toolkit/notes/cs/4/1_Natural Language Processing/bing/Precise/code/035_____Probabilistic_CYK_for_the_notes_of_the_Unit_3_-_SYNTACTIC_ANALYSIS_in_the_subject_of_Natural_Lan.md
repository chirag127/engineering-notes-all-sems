### Probabilistic CYK

The Probabilistic Cocke–Younger–Kasami (CYK) algorithm is an inference algorithm that utilizes dynamic programming to find the most likely parse tree of a given sentence according to production probabilities for given probabilistic context-free grammars (PCFGs).

When the probabilistic CYK algorithm is applied to a long string, the splitting probability can become very small due to multiplying many probabilities together. This can be dealt with by summing log-probability instead of multiplying probabilities.

In informal terms, this algorithm considers every possible substring of the input string and sets to be true if the substring of length starting from can be generated from the nonterminal.
