# Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probability of a rule is the conditional probability of expanding the left-hand side nonterminal into the right-hand side symbols, given the left-hand side nonterminal.
- The probability of a parse tree is the product of the probabilities of the rules used to derive it.
- The probability of a sentence is the sum of the probabilities of all possible parse trees for that sentence.
- PCFGs can be used to model natural languages and to perform syntactic analysis (parsing) of sentences.
- PCFGs can be learned from a corpus of annotated sentences (a treebank) by counting the occurrences of each rule and normalizing by the occurrences of each nonterminal.
- PCFGs can be parsed by using a modified version of the CKY algorithm, which is a bottom-up dynamic programming algorithm that finds the most probable parse tree for a given sentence and grammar.
- PCFGs have some advantages and disadvantages compared to standard CFGs:
  - Advantages:
    - They can handle ambiguity and preference by ranking parse trees according to their probabilities.
    - They can incorporate lexical information and statistical knowledge into the grammar rules.
    - They can be easily learned from data and adapted to different domains and genres.
  - Disadvantages:
    - They make unrealistic independence assumptions, such as the context-freeness of nonterminals and the independence of rules.
    - They are sensitive to data sparsity and overfitting, especially for rare or unseen words and structures.
    - They are computationally expensive to parse, as they require more memory and time than standard CFGs.