### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probability of a rule is the conditional probability of expanding the left-hand side nonterminal into the right-hand side symbols, given the left-hand side nonterminal.
- The probability of a parse tree is the product of the probabilities of the rules used to generate it.
- The probability of a sentence is the sum of the probabilities of all possible parse trees for that sentence.
- PCFGs can be used to model natural languages and perform syntactic analysis (parsing).
- PCFGs can be learned from a corpus of annotated sentences (treebank) by counting the occurrences of each rule and normalizing by the occurrences of each nonterminal.
- PCFGs can be parsed by algorithms such as the CKY algorithm, which is a bottom-up dynamic programming algorithm that finds the most probable parse tree for a given sentence and grammar.
- PCFGs have some advantages over standard CFGs, such as being able to handle ambiguity and capture linguistic preferences and tendencies.
- PCFGs also have some limitations, such as being unable to model long-distance dependencies, word order variations, and lexical influences.