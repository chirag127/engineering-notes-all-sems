### Probabilistic Lexicalized CFGs

- Probabilistic Lexicalized CFGs (PLCFGs) are a type of probabilistic context-free grammars (PCFGs) that incorporate lexical information into the syntactic rules.
- PLCFGs assign a probability to each rule in the grammar, based on the frequency of its occurrence in a corpus of parsed sentences. The probability of a parse tree is the product of the probabilities of the rules used to derive it.
- PLCFGs also associate each non-terminal symbol in the grammar with a lexical head, which is a word that determines the syntactic and semantic properties of the phrase. The lexical head is inherited from the head of the rightmost child in the rule, unless specified otherwise by a head table.
- PLCFGs can capture more fine-grained syntactic distinctions than PCFGs, by taking into account the lexical dependencies between words and phrases. For example, PLCFGs can distinguish between different types of noun phrases (NPs), such as NPs headed by a proper noun, a common noun, or a pronoun, and assign different probabilities to them.
- PLCFGs can also handle long-distance dependencies, such as wh-movement and topicalization, by introducing special non-terminal symbols that mark the position of the extracted element and its trace. For example, the sentence "What did John buy?" can be parsed by a PLCFG as follows:

```
S[+WH] -> NP[+WH] S[-WH]
NP[+WH] -> what
S[-WH] -> NP VP
NP -> John
VP -> V NP[-WH]
V -> buy
NP[-WH] -> t
```

- The symbol S[+WH] indicates a sentence with a wh-element, NP[+WH] indicates a noun phrase with a wh-element, and NP[-WH] indicates a noun phrase without a wh-element. The symbol t represents the trace of the wh-element, which is co-indexed with it.
- PLCFGs can be learned from a corpus of parsed sentences, by applying the expectation-maximization (EM) algorithm, which iteratively estimates the rule probabilities and the parse trees, until convergence. The EM algorithm can also handle incomplete or noisy data, by assigning probabilities to all possible parse trees, and choosing the most likely one.