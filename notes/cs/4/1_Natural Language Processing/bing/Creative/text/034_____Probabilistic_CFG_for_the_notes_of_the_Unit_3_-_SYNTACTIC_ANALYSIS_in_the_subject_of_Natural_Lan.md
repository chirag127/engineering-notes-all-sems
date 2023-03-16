### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules .
- The probability of a rule is the conditional probability of expanding the left-hand side nonterminal into the right-hand side symbols, given the left-hand side nonterminal.
- The probability of a parse tree is the product of the probabilities of the rules used to generate it .
- The probability of a sentence is the sum of the probabilities of all possible parse trees for that sentence .
- PCFGs can be used to model natural languages and perform syntactic analysis .
- PCFGs can be learned from a corpus of annotated sentences using the maximum likelihood estimation (MLE) method .
- PCFGs can be parsed using algorithms such as the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up dynamic programming algorithm that finds all possible parse trees for a sentence under a PCFG in Chomsky Normal Form (CNF) .
- PCFGs have some advantages and disadvantages compared to other models of natural language syntax :
  - Advantages:
    - PCFGs can capture some aspects of syntactic ambiguity and preference by assigning different probabilities to different parse trees for the same sentence.
    - PCFGs can be easily extended to incorporate lexical information, semantic features, or other linguistic constraints by adding more nonterminals or rules to the grammar.
    - PCFGs can be efficiently parsed using polynomial-time algorithms such as CKY.
  - Disadvantages:
    - PCFGs are still limited by the expressive power of context-free grammars, which cannot handle some complex syntactic phenomena such as cross-serial dependencies, long-distance dependencies, or coordination.
    - PCFGs are sensitive to the choice of nonterminals and rules, which may affect the accuracy and coverage of the model.
    - PCFGs are often trained on small and domain-specific corpora, which may not generalize well to other domains or genres of natural language.