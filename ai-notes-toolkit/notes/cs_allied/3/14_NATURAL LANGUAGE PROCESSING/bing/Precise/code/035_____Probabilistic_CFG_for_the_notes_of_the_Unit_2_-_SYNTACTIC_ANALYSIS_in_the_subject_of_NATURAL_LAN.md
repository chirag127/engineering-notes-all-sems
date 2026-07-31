### Probabilistic CFG

Probabilistic Context-Free Grammar (PCFG) is a type of Context-Free Grammar (CFG) that associates a probability with each production rule. The probabilities of the production rules are used to compute the probability of a parse tree, and the most probable parse tree is chosen as the best parse for a given sentence.

Some key points to remember about PCFG are:

- PCFG is an extension of CFG, where each production rule is assigned a probability.
- The probability of a parse tree is computed as the product of the probabilities of the production rules used to derive the tree.
- The most probable parse tree is chosen as the best parse for a given sentence.
- PCFG can be used for disambiguation, where multiple parse trees are possible for a given sentence.
- The probabilities of the production rules can be estimated from a training corpus.
