### Probabilistic Lexicalized CFGs

- Probabilistic context-free grammars (PCFGs) are context-free grammars (CFGs) that assign probabilities to each production rule.
- The probability of a rule A -> α is the conditional probability of expanding A to α given A, denoted as P(A -> α | A) or P(A -> α).
- The probability of a parse tree is the product of the probabilities of all the rules used to construct it.
- The probability of a sentence is the sum of the probabilities of all the parse trees for that sentence.
- PCFGs can be used to model the syntactic structure of natural language and to find the most likely parse for a given sentence.
- Lexicalized PCFGs (L-PCFGs) are PCFGs that incorporate lexical information into the non-terminal symbols.
- Each non-terminal symbol is annotated with a head word that represents the semantic and syntactic core of the constituent.
- For example, the symbol VP(saw) indicates a verb phrase headed by the word saw.
- L-PCFGs can capture more fine-grained syntactic distinctions and dependencies than PCFGs, and can improve the accuracy of parsing.