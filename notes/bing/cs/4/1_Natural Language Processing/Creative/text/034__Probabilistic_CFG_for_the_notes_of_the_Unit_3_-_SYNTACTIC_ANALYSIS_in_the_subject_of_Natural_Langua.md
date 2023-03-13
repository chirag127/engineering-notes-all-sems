### Probabilistic CFG

- A probabilistic CFG (PCFG) is a CFG that assigns a probability to each of its rules.
- The probability of a rule reflects how likely it is to be used in a derivation of a sentence.
- The probability of a sentence is the product of the probabilities of the rules used in its derivation.
- A PCFG can be used to model the syntactic structure of natural language sentences and to disambiguate between multiple possible parses.
- A PCFG can be learned from a corpus of annotated sentences (a treebank) by counting the occurrences of each rule and normalizing by the occurrences of each left-hand side nonterminal.
- A PCFG can be parsed using algorithms such as the CKY algorithm or the Earley algorithm, which are extensions of the standard CFG parsing algorithms that take into account the rule probabilities.
- A PCFG can be evaluated by comparing its predictions to a gold standard of annotated sentences, using metrics such as precision, recall, and F1-score.