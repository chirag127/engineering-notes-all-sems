# Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are a type of weighted CFGs that attach probabilities to each production rule in a CFG.
- The probabilities of the rules are conditional on the left-hand side nonterminal and form a valid categorical distribution.
- The probability of a derivation or a parse tree is the product of the probabilities of the rules used in the derivation.
- PCFGs can be used to model the syntactic structure of natural language sentences and to perform statistical parsing.
- Lexicalized PCFGs (L-PCFGs) are a variant of PCFGs that incorporate lexical information into the nonterminal symbols.
- Each nonterminal in an L-PCFG is annotated with a head word that represents the most important word in the constituent.
- The head word is propagated bottom-up from the preterminal rules to the higher-level rules in the parse tree.
- The probabilities of the rules in an L-PCFG depend on the head words of the nonterminals as well as their categories.
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs and achieve better parsing accuracy.
- L-PCFGs can be learned from a treebank of annotated sentences using the maximum likelihood estimation or the expectation-maximization algorithm.