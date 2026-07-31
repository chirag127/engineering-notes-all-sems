### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule, such that the sum of the probabilities of all rules with the same left-hand side is 1.
- The probability of a derivation or a parse tree is the product of the probabilities of all the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences, and to perform parsing tasks such as finding the most probable parse tree for a given sentence.
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the non-terminal symbols, such that each non-terminal is associated with a head word that determines its syntactic and semantic properties.
- L-PCFGs can capture long-distance dependencies and subcategorization preferences that are not easily modeled by standard PCFGs.
- L-PCFGs can be learned from a treebank, a corpus of sentences annotated with parse trees, by using the head-finding rules to assign head words to each non-terminal, and then estimating the rule probabilities by counting the occurrences of each rule in the treebank.
- Neural bi-lexicalized PCFGs (NBL-PCFGs) are a recent extension of L-PCFGs that use neural networks to parameterize the rule probabilities as a function of both the head word and the dependent word of each rule.
- NBL-PCFGs can learn richer and more expressive representations of the syntactic categories and the lexical dependencies, and achieve state-of-the-art results on unsupervised grammar induction.