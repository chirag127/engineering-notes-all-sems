### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that assign probabilities to each production rule, such that the sum of the probabilities of all rules with the same left-hand side is 1.
- PCFGs can be used to model the likelihood of different syntactic structures for a given sentence, and to select the most probable parse tree among the possible ones.
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the non-terminal symbols, such that each non-terminal is associated with a head word that determines its subcategorization and selectional preferences.
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs, and can improve the accuracy of parsing and disambiguation.
- L-PCFGs can be learned from a treebank of annotated sentences, by extracting the head words of each non-terminal node and estimating the rule probabilities from the relative frequencies of the rules in the corpus.
- L-PCFGs can be parsed using the same algorithms as PCFGs, such as the CKY algorithm or the Earley algorithm, with some modifications to handle the lexicalization of the non-terminals.