# Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that attach probabilities to each production rule in a CFG.
- The probabilities of the rules are conditional on the left-hand side nonterminal and form a valid categorical distribution .
- The probability of a derivation or a parse tree is the product of the probabilities of the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences and to perform statistical parsing.
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the nonterminal symbols.
- L-PCFGs associate each nonterminal with a head word that determines its syntactic and semantic properties.
- L-PCFGs can capture long-distance dependencies and subcategorization preferences that are not easily modeled by PCFGs.
- L-PCFGs can be learned from treebanks using various methods, such as the inside-outside algorithm, the expectation-maximization algorithm, or neural networks .
- L-PCFGs can achieve better parsing accuracy and efficiency than PCFGs, especially for languages with rich morphology and free word order .