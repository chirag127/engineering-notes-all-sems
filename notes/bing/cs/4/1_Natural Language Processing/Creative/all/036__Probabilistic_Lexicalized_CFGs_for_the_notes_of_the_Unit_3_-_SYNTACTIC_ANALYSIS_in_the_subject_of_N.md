### Probabilistic Lexicalized CFGs for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Probabilistic context-free grammars (PCFGs) are a type of context-free grammars (CFGs) that assign probabilities to each production rule.
- The probabilities of the rules are conditional on the left-hand side nonterminal symbol and sum to one for each nonterminal symbol.
- The probability of a parse tree is the product of the probabilities of the rules used to derive it.
- The probability of a sentence is the sum of the probabilities of all the parse trees that can generate it.
- PCFGs can be used to model the syntactic structure of natural language and to perform statistical parsing tasks, such as finding the most likely parse tree for a given sentence or ranking the possible parse trees according to their probabilities.
- Lexicalized PCFGs (L-PCFGs) are a type of PCFGs that incorporate lexical information into the nonterminal symbols of the grammar.
- Each nonterminal symbol is annotated with a head word, which is the most important word in the phrase or constituent represented by that symbol.
- The head word is inherited from the head word of the right-hand side symbol that is marked as the head child in the production rule.
- The head child is determined by a set of head rules that specify which symbol is the head for each type of phrase or constituent.
- The head word annotation helps to capture the syntactic and semantic dependencies between words and phrases in a sentence, and to reduce the sparsity and ambiguity problems of PCFGs.
- L-PCFGs can be learned from a treebank, which is a corpus of sentences annotated with their parse trees and head words.
- The parameters of L-PCFGs can be estimated by counting the occurrences of the production rules and applying the maximum likelihood estimation method.
- L-PCFGs can be used to perform the same statistical parsing tasks as PCFGs, but with improved accuracy and efficiency.

Some examples of PCFGs and L-PCFGs are shown below:

PCFG:

S -> NP VP [1.0]
NP -> DT NN [0.6] | PRP [0.4]
VP -> VBD NP [0.7] | VBD [0.3]
DT -> the [0.8] | a [0.2]
NN -> dog [0.5] | cat [0.5]
PRP -> he [0.6] | she [0.4]
VBD -> saw [0.4] | chased [0.6]

L-PCFG:

S^saw -> NP^dog VP^saw [1.0]
NP^dog -> DT^dog NN^dog [0.6] | PRP^dog [0.4]
VP^saw -> VBD^saw NP^cat [0.7] | VBD^saw [0.3]
DT^dog -> the^dog [0.8] | a^dog [0.2]
NN^dog -> dog^dog [0.5] | cat^dog [0.5]
PRP^dog -> he^dog [0.6] | she^dog [0.4]
VBD^saw -> saw^saw [0.4] | chased^saw [0.6]

The parse tree for the sentence "He saw the cat" using the PCFG is:

S
 / \
NP  VP
|  /  \
PRP VBD NP
|  |  /  \
he saw DT NN
      |  |
      the cat

The probability of this parse tree is:

P(S -> NP VP) * P(NP -> PRP) * P(PRP -> he) * P(VP -> VBD NP) * P(VBD -> saw) * P(NP -> DT NN) * P(DT -> the) * P(NN -> cat)
= 1.0 * 0.4 * 0.6 * 0.7 * 0.4 * 0.6 * 0.8 * 0.5
= 0.003456

The parse tree for the same sentence using the L-PCFG is:

S^saw
 /    \
NP^dog VP^saw
|    /    \
PRP^dog VBD^saw NP^cat
|      |    /    \
he^dog saw^saw DT^cat NN