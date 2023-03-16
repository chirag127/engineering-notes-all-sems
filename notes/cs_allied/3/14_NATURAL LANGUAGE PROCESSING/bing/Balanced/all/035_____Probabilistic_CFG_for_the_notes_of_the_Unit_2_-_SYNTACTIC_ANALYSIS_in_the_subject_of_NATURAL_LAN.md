# Probabilistic CFG

- Probabilistic Context Free Grammar (PCFG) is an extension of Context Free Grammar (CFG) with a probability for each production rule .
- The probability of a production rule is the conditional probability of the right-hand side given the left-hand side, i.e. P(α → β) = P(β | α) where α is a nonterminal and β is a sequence of terminals and/or nonterminals .
- The probability of a derivation (parse) is then the product of the probabilities of the productions used in that derivation .
- The probability of a sentence is the sum of the probabilities of all possible derivations (parses) of that sentence .
- PCFGs can be used to model natural language syntax and resolve ambiguity by assigning higher probabilities to more likely parses  .
- PCFGs can also be used to model other domains such as RNA structures, where each feature has a production rule that is assigned a probability estimated from a training set of RNA structures.