### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule in a CFG.
- The probability of a rule A -> α is the conditional probability of expanding A to α given A, written as P(A -> α | A) or P(A -> α).
- The probability of a derivation or a parse tree is the product of the probabilities of all the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences, and to perform parsing tasks such as finding the most probable parse tree for a given sentence.
- Lexicalized PCFGs (L-PCFGs) are a type of PCFGs that incorporate lexical information into the nonterminal symbols of the grammar.
- L-PCFGs use a head-driven annotation scheme, where each nonterminal symbol is annotated with the head word of its subtree.
- The head word is the most important word in a phrase that determines its syntactic and semantic properties.
- For example, in the phrase "the big red car", the head word is "car", and the nonterminal symbol for the phrase is NP(car).
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs, and can improve the accuracy of parsing natural language sentences.
- Neural bi-lexicalized PCFGs (NBL-PCFGs) are a type of L-PCFGs that use neural networks to model the probabilities of the rules and the head words.
- NBL-PCFGs use two types of head words: the left head word and the right head word, which are the head words of the left and right children of a nonterminal symbol respectively.
- NBL-PCFGs use a neural network to compute the probability of a rule A -> BC given the left head word of A and the right head word of A, written as P(A -> BC | A.l, A.r).
- NBL-PCFGs also use a neural network to compute the probability of a head word given the rule and the head words of the children, written as P(A.l | A -> BC, B.l, C.l) and P(A.r | A -> BC, B.r, C.r).
- NBL-PCFGs can learn more complex and expressive syntactic representations than L-PCFGs, and can achieve state-of-the-art results on unsupervised grammar induction.