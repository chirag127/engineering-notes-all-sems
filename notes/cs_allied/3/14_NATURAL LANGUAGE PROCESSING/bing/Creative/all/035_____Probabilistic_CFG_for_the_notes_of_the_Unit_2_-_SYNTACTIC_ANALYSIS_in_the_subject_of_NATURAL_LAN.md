# Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probabilities of the rules are estimated from a corpus of sentences and their parse trees, called a treebank.
- A PCFG can be used to model the syntactic structure of natural languages, and to parse new sentences with a probabilistic parser.
- A probabilistic parser finds the most likely parse tree for a given sentence, or the probability distribution over all possible parse trees.
- A PCFG can be defined as a tuple (N, T, S, R, P), where:
  - N is a set of nonterminal symbols
  - T is a set of terminal symbols
  - S is the start symbol
  - R is a set of production rules of the form A -> B, where A is a nonterminal and B is a sequence of terminals and/or nonterminals
  - P is a function that assigns a probability to each rule in R, such that for each nonterminal A, the sum of the probabilities of all rules with A on the left-hand side is 1.
- A PCFG can be converted to Chomsky Normal Form (CNF), where each rule has at most two symbols on the right-hand side, by introducing new nonterminals and rules.
- A PCFG in CNF can be parsed efficiently with the CKY algorithm, which is a bottom-up dynamic programming algorithm that fills a chart with the probabilities of all possible sub-trees for each span of the sentence.
- The CKY algorithm can also be extended to handle unary rules, which have only one symbol on the right-hand side, by collapsing them into a single nonterminal.
- The CKY algorithm can also be modified to output the most likely parse tree, or the k-best parse trees, or the inside and outside probabilities of each nonterminal in the chart.
- The inside probability of a nonterminal A at a span (i, j) is the probability of generating the substring w(i)...w(j) from A, denoted by beta(A, i, j).
- The outside probability of a nonterminal A at a span (i, j) is the probability of generating the rest of the sentence from the start symbol, given that A is at (i, j), denoted by alpha(A, i, j).
- The inside and outside probabilities can be computed recursively using the rules and their probabilities, and can be used to calculate the marginal probability of any sub-tree in the chart.