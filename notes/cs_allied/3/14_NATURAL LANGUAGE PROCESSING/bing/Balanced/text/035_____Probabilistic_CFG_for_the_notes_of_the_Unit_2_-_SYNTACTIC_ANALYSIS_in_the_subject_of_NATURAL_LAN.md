### Probabilistic CFG

- A probabilistic context-free grammar (PCFG) is a context-free grammar that assigns probabilities to each of its production rules.
- The probabilities of the rules are estimated from a corpus of annotated sentences, called a treebank.
- The sum of the probabilities of all the rules with the same left-hand side must be equal to one.
- A PCFG can be used to model the syntactic structure of natural language sentences, and to assign probabilities to different possible parses of a sentence.
- A PCFG can also be used to generate random sentences from a given grammar, by randomly choosing rules according to their probabilities.
- A PCFG can be parsed by a modified version of the CKY algorithm, which is a bottom-up dynamic programming algorithm that finds the most probable parse tree for a given sentence and grammar.
- The CKY algorithm works by filling a triangular chart with the probabilities of all possible constituents that span a substring of the sentence, and then backtracking to find the best parse tree.
- The CKY algorithm requires the PCFG to be in Chomsky Normal Form (CNF), which means that every rule has either two nonterminal symbols or one terminal symbol on the right-hand side.
- A PCFG can be converted to CNF by introducing new nonterminal symbols and adding new rules that preserve the original probabilities.
- A PCFG can capture some aspects of natural language syntax, such as word order, agreement, and subcategorization, but it cannot capture long-distance dependencies, such as wh-movement, or semantic constraints, such as selectional restrictions.