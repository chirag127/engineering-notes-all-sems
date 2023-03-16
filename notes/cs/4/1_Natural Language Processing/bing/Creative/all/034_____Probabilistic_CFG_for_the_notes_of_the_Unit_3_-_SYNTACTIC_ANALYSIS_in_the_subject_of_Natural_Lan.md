# Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules .
- The probabilities of the rules are estimated from a corpus of sentences and their parse trees, called a treebank .
- A PCFG can be used to model the syntactic structure of natural languages, and to perform probabilistic parsing .
- Probabilistic parsing is the task of finding the most likely parse tree for a given sentence under a PCFG .
- A PCFG can be defined as a tuple (N, Σ, R, S, P), where:
  - N is a finite set of nonterminal symbols
  - Σ is a finite set of terminal symbols (disjoint from N)
  - R is a finite set of production rules of the form A -> α, where A is a nonterminal and α is a string of symbols from (N ∪ Σ)*
  - S is a distinguished start symbol in N
  - P is a function that assigns a probability to each rule in R, such that for any nonterminal A, the sum of the probabilities of all rules with A on the left-hand side is 1
- A PCFG can be converted to Chomsky normal form (CNF), where each rule has at most two nonterminals on the right-hand side, by introducing new nonterminals and rules .
- A PCFG in CNF can be parsed efficiently using the CKY algorithm, which is a dynamic programming algorithm that fills a chart with the probabilities of all possible subtrees for each span of the sentence .
- The CKY algorithm can also return the most likely parse tree by keeping track of the backpointers that indicate which rules were used to create each subtree .
- The CKY algorithm has a time complexity of O(n^3 * |N|), where n is the length of the sentence and |N| is the number of nonterminals in the grammar .
- PCFGs have some limitations, such as ignoring the lexical and contextual information, and assuming independence among the rules .
- PCFGs can be extended or modified to overcome some of these limitations, such as using lexicalized PCFGs, latent variable PCFGs, or dependency-based PCFGs .