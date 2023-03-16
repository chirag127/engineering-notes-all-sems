### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules .
- The probabilities of the rules are estimated from a corpus of sentences and their parse trees, called a treebank .
- The probability of a parse tree given a PCFG is the product of the probabilities of the rules used to derive the tree .
- PCFGs can be used to model natural languages and perform syntactic analysis, such as parsing and generation .
- PCFGs can capture some aspects of natural language syntax, such as word order, agreement, and subcategorization, but they cannot handle long-distance dependencies, such as wh-movement and coordination.
- PCFGs can be extended with features, such as lexicalization, annotation, and binarization, to improve their accuracy and coverage .
- PCFGs can be parsed efficiently using dynamic programming algorithms, such as the CKY algorithm, which builds a chart of possible sub-trees for each span of the input sentence .
- PCFGs can be evaluated using metrics, such as perplexity, which measures how well the grammar predicts new sentences, and F-score, which measures how well the grammar matches the gold-standard parse trees .