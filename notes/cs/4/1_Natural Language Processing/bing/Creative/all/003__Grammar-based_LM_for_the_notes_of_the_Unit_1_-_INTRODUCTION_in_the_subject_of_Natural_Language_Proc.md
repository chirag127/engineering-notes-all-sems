### Grammar-based LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A grammar-based language model (LM) is a type of LM that uses a grammar to generate or parse sequences of words.
- A grammar is a set of rules that specify how words can be combined to form syntactically valid sentences in a language.
- A grammar can be formal or informal, depending on the level of rigor and precision in defining the rules.
- A formal grammar is a mathematical object that consists of a finite set of symbols (terminals and non-terminals), a start symbol, and a finite set of production rules that rewrite non-terminals into sequences of terminals and non-terminals.
- A formal grammar can be classified into different types according to the Chomsky hierarchy, such as regular, context-free, context-sensitive, or unrestricted grammars.
- A regular grammar is the simplest type of grammar that can generate regular languages, which are languages that can be recognized by finite automata or regular expressions.
- A context-free grammar (CFG) is a type of grammar that can generate context-free languages, which are languages that can be recognized by pushdown automata or parsed by recursive descent parsers.
- A context-sensitive grammar (CSG) is a type of grammar that can generate context-sensitive languages, which are languages that can be recognized by linear bounded automata or parsed by linear bounded parsers.
- An unrestricted grammar is the most general type of grammar that can generate recursively enumerable languages, which are languages that can be recognized by Turing machines or parsed by Turing parsers.
- A grammar-based LM can be probabilistic or non-probabilistic, depending on whether it assigns probabilities to the production rules or not.
- A probabilistic grammar-based LM assigns conditional probabilities to the production rules, such that the sum of the probabilities of all rules with the same left-hand side is one.
- A probabilistic grammar-based LM can be used to compute the probability of a word sequence by multiplying the probabilities of the production rules that generate it, and summing over all possible parse trees for that sequence.
- A probabilistic grammar-based LM can also be used to predict the next word in a sequence by computing the conditional probability of each possible word given the previous words and the grammar.
- A probabilistic grammar-based LM can be estimated from a corpus of sentences by counting the occurrences of the production rules and applying smoothing techniques to avoid zero probabilities.
- A non-probabilistic grammar-based LM does not assign probabilities to the production rules, but only checks whether a word sequence is grammatical or not according to the grammar.
- A non-probabilistic grammar-based LM can be used to filter out ungrammatical word sequences or to generate grammatical word sequences by applying the production rules.
- A non-probabilistic grammar-based LM can be constructed from a set of examples or from linguistic knowledge of the language.
- A grammar-based LM can be more complex or more expressive than a n-gram LM, which is a type of LM that only uses the previous n-1 words to predict the next word in a sequence.
- A grammar-based LM can capture the syntactic structure and the long-range dependencies of a language, while a n-gram LM can only capture the local and sequential patterns of a language.
- A grammar-based LM can be more accurate or more robust than a n-gram LM, depending on the quality and the size of the grammar and the corpus.
- A grammar-based LM can be more precise or more general than a n-gram LM, depending on the type and the level of the grammar and the n-gram.
- A grammar-based LM can be more efficient or more complex than a n-gram LM, depending on the algorithms and the data structures used to implement and apply the grammar and the n-gram.

Some examples of grammar-based LMs are:

- Probabilistic context-free grammars (PCFGs), which are CFGs with probabilities assigned to the production rules. PCFGs can be used for tasks like speech recognition, spelling correction, and machine translation.
- Probabilistic context-sensitive grammars (PCSGs), which are CSGs with probabilities assigned to the production rules. PCSGs can be used for tasks like natural language generation, semantic parsing, and information extraction.
- Probabilistic regular grammars (PRGs), which are regular grammars with probabilities assigned to the production rules. PRGs can be used for tasks like text classification, sentiment analysis, and named entity recognition.
- Non-probabilistic context-free grammars (NCFGs),