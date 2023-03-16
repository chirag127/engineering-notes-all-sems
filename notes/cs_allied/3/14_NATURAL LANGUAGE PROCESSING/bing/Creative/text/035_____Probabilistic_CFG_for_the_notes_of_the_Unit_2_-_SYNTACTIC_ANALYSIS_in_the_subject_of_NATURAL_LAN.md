### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probabilities of the rules are estimated from a corpus of sentences and their parse trees, called a treebank.
- A PCFG can be used to model the syntactic structure of natural languages, and to perform probabilistic parsing, which is the task of finding the most likely parse tree for a given sentence.
- A PCFG is defined by a tuple (N, Σ, R, S, P), where:
  - N is a set of nonterminal symbols (also called syntactic categories or labels)
  - Σ is a set of terminal symbols (also called words or tokens)
  - R is a set of production rules of the form A → α, where A ∈ N and α ∈ (N ∪ Σ)*
  - S ∈ N is the start symbol
  - P is a function that assigns a probability to each rule in R, such that for any A ∈ N, the sum of P(A → α) over all α ∈ (N ∪ Σ)* is 1.
- A PCFG generates a sentence w ∈ Σ* and its parse tree t by applying a sequence of rules starting from S, such that the yield of t is w and the product of the probabilities of the rules is the probability of t.
- The probability of a sentence w is the sum of the probabilities of all possible parse trees for w.
- A PCFG can be converted to Chomsky normal form (CNF), which is a restricted form of CFG where each rule has either two nonterminals or one terminal on the right-hand side. This simplifies the parsing algorithm and reduces the number of parameters to estimate.
- A common algorithm for probabilistic parsing with PCFGs is the CKY algorithm, which is a bottom-up dynamic programming algorithm that fills a chart with the probabilities of all possible subtrees for each span of the sentence, and then backtracks to find the most probable parse tree.