### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule in a CFG, such that the sum of the probabilities of all rules with the same left-hand side is 1 .
- The probability of a derivation or a parse tree in a PCFG is the product of the probabilities of all the rules used in the derivation .
- PCFGs can be used to model the syntactic structure of natural language sentences, and to perform parsing tasks such as finding the most likely parse tree for a given sentence .
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the non-terminal symbols of the grammar.
- L-PCFGs can capture the dependencies between words and syntactic categories, and improve the accuracy and efficiency of parsing natural language sentences.
- L-PCFGs use a head-driven annotation scheme, where each non-terminal symbol is annotated with the head word of its subtree.
- For example, the rule S -> NP VP can be lexicalized as S[book] -> NP[John] VP[book], where book is the head word of the S node, John is the head word of the NP node, and book is the head word of the VP node.
- The probabilities of the rules in L-PCFGs are conditioned on the head words of the left-hand side and the right-hand side symbols.
- For example, the probability of the rule S[book] -> NP[John] VP[book] is P(S[book] -> NP[John] VP[book] | S[book], NP[John], VP[book]).
- L-PCFGs can be learned from a treebank, which is a corpus of sentences annotated with parse trees and head words.
- L-PCFGs can also be extended with other features, such as parent annotation, gap annotation, and bi-lexicalization .
- Parent annotation adds the parent symbol of each non-terminal to its annotation, to capture the influence of the context on the syntactic category.
- Gap annotation marks the position of the gap in a non-terminal that dominates a trace, to handle long-distance dependencies.
- Bi-lexicalization adds the head word of the sibling symbol to the annotation of each non-terminal, to model the interactions between adjacent words.