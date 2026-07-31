### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule in a CFG.
- The probability of a rule A -> α is the conditional probability of expanding A to α given A, written as P(A -> α | A) or P(A -> α).
- The probability of a derivation or a parse tree is the product of the probabilities of all the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences, and to perform parsing tasks such as finding the most probable parse tree for a given sentence.
- Lexicalized PCFGs (L-PCFGs) are a type of PCFGs that incorporate lexical information into the nonterminal symbols of the grammar.
- L-PCFGs use a head-driven approach, where each nonterminal symbol is annotated with the head word of its constituent, and the probabilities of the rules depend on the head words of the parent and the children.
- L-PCFGs can capture more fine-grained syntactic and semantic dependencies between words, and can improve the accuracy and efficiency of parsing.
- Neural bi-lexicalized PCFGs (NBL-PCFGs) are a type of L-PCFGs that use neural networks to parameterize the probabilities of the rules based on the embeddings of the head words.
- NBL-PCFGs can learn richer and more expressive representations of the head words, and can handle unseen words and rare rules better than traditional L-PCFGs.
- NBL-PCFGs can also perform unsupervised grammar induction, where they learn the grammar rules and the probabilities from unannotated sentences.