# Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probability of a rule is the conditional probability of expanding the left-hand side nonterminal into the right-hand side symbols, given the left-hand side nonterminal.
- The probability of a parse tree is the product of the probabilities of the rules used to derive it.
- The probability of a sentence is the sum of the probabilities of all possible parse trees for that sentence.
- PCFGs can be used to model natural languages and perform syntactic analysis, such as parsing and generation.
- PCFGs can be learned from a corpus of annotated sentences, such as the Penn Treebank, by counting the occurrences of each rule and normalizing by the occurrences of each nonterminal.
- PCFGs can be parsed efficiently using dynamic programming algorithms, such as the CKY algorithm, which builds a chart of possible constituents for each span of the sentence and selects the most probable ones.
- PCFGs can capture some aspects of natural language syntax, such as word order, agreement, and subcategorization, but they have limitations, such as the independence assumption, the sparsity problem, and the lack of lexicalization.