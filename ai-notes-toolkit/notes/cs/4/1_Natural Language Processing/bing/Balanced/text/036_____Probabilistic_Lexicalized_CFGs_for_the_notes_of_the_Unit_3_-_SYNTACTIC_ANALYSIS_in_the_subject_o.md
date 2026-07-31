### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule, such that the sum of the probabilities of all rules with the same left-hand side is 1.
- PCFGs can be used to model the likelihood of different syntactic structures for a given sentence, and to select the most probable parse tree among the possible ones.
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the non-terminal symbols, such that each non-terminal is associated with a head word that determines its subcategorization and selectional preferences.
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs, and can improve the accuracy of parsing.
- Neural bi-lexicalized PCFGs (NBL-PCFGs) are a recent approach that uses neural networks to learn the parameters of L-PCFGs from data, and to encode the bi-directional context of each word in the sentence.
- NBL-PCFGs can achieve state-of-the-art results on unsupervised grammar induction, and can handle long-distance dependencies and rare words better than previous methods.