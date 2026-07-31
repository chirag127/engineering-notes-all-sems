# Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that attach probabilities to each production rule in a CFG.
- The probabilities of the rules are conditional on the left-hand side nonterminal and form a valid categorical distribution .
- The probability of a derivation or a parse tree is the product of the probabilities of the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences and to perform statistical parsing .
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the nonterminal symbols .
- L-PCFGs use a head-driven approach, where each nonterminal is annotated with the head word of its subtree.
- The head word is the most important word in a phrase that determines its syntactic and semantic properties.
- L-PCFGs can capture long-distance dependencies and subcategorization preferences that are not easily modeled by standard PCFGs .
- L-PCFGs can also improve the accuracy and efficiency of parsing by reducing the sparsity and ambiguity of the grammar .
- L-PCFGs can be learned from a treebank, a corpus of sentences annotated with parse trees, by applying a head-finding algorithm and estimating the rule probabilities from the frequency counts.
- Neural L-PCFGs are a recent extension of L-PCFGs that use neural networks to parameterize the rule probabilities and to encode the lexical and syntactic information.
- Neural L-PCFGs can leverage the distributed representations of words and phrases to capture more fine-grained and context-sensitive features.
- Neural L-PCFGs can also overcome some of the limitations of traditional L-PCFGs, such as the fixed vocabulary size and the independence assumptions.