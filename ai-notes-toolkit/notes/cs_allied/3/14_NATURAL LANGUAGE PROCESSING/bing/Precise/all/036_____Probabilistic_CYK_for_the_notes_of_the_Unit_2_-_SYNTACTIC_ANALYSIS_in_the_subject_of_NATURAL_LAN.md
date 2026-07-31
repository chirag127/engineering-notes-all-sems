# Probabilistic CYK

Probabilistic CYK is an algorithm used for parsing sentences in natural language processing. It is a variant of the Cocke-Younger-Kasami (CYK) algorithm that incorporates probabilities to determine the most likely parse tree for a given sentence.

1. The algorithm uses a probabilistic context-free grammar (PCFG) to assign probabilities to different parse trees.
2. The algorithm works by filling in a parse chart, which is a two-dimensional table that stores the probabilities of different sub-trees for each substring of the input sentence.
3. The algorithm starts by filling in the bottom row of the parse chart with the probabilities of the terminal symbols (words) in the sentence.
4. The algorithm then fills in the rest of the parse chart by considering all possible combinations of sub-trees and selecting the one with the highest probability.
5. Once the parse chart is filled, the algorithm can backtrack to find the most likely parse tree for the entire sentence.

Probabilistic CYK is useful for dealing with ambiguity in natural language sentences, as it allows the algorithm to select the most likely interpretation of a sentence based on the probabilities assigned by the PCFG. It is commonly used in natural language processing tasks such as syntactic analysis and machine translation.