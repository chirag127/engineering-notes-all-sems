```markdown
### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probability of a rule is the conditional probability of expanding the left-hand side nonterminal into the right-hand side symbols, given the left-hand side nonterminal.
- The probability of a parse tree is the product of the probabilities of the rules used to generate it.
- The probability of a sentence is the sum of the probabilities of all possible parse trees for that sentence.
- PCFGs can be used to model natural languages and perform syntactic analysis, such as parsing and disambiguation.
- PCFGs can be learned from a corpus of annotated sentences, such as the Penn Treebank, by counting the occurrences of each rule and normalizing by the occurrences of each nonterminal.
- PCFGs can be parsed by algorithms such as the CKY algorithm, which is a bottom-up dynamic programming algorithm that finds the most probable parse tree for a given sentence and grammar.
- PCFGs have some limitations, such as the independence assumption, which ignores the dependencies between different parts of the sentence, and the sparsity problem, which results from the lack of data for some rare rules or words.
- PCFGs can be improved by adding more features, such as lexicalization, subcategorization, and annotation, which can capture more syntactic and semantic information and reduce ambiguity.
```