# Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probabilities of the rules are estimated from a corpus of annotated sentences, called a treebank.
- A PCFG can be used to model the syntactic structure of natural languages, and to parse new sentences with a probabilistic parser.
- A probabilistic parser finds the most likely parse tree for a given sentence, or the probability distribution over all possible parse trees.
- A PCFG can be defined as a tuple (N, Σ, R, S, P), where:
  - N is a set of nonterminal symbols
  - Σ is a set of terminal symbols (words)
  - R is a set of production rules of the form A -> α, where A is a nonterminal and α is a string of nonterminals and terminals
  - S is the start symbol
  - P is a function that assigns a probability to each rule, such that for each nonterminal A, the sum of the probabilities of all rules with A on the left-hand side is 1.
- A PCFG can be converted to Chomsky Normal Form (CNF), where each rule has at most two nonterminals on the right-hand side, by introducing new nonterminals and rules.
- A PCFG in CNF can be parsed efficiently with the CKY algorithm, which is a dynamic programming algorithm that fills a chart with the probabilities of all possible sub-trees for each span of the sentence.
- The CKY algorithm can also be extended to handle unary rules, which have only one nonterminal on the right-hand side, by collapsing them into a single nonterminal with a combined probability.