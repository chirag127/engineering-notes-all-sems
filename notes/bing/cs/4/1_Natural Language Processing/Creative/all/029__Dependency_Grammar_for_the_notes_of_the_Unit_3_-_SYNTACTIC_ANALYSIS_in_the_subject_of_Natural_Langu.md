### Dependency Grammar for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Dependency grammar is a segment of syntactic text analysis that determines the relationship among the words in a sentence.
- In dependency grammar, the words are connected to each other by directed links, called dependencies, that indicate the syntactic function of each word .
- The verb is considered the center of the clause structure, and every other syntactic unit is connected to the verb in terms of a directed link.
- Each dependency has a head (or governor) and a dependent (or modifier). The head is the word that determines the syntactic category and the semantic role of the dependent .
- For example, in the sentence "She likes apples", the verb "likes" is the head of the whole sentence, and it has two dependents: the subject "she" and the object "apples". The dependency relation between "likes" and "she" is labeled as "nsubj" (nominal subject), and the relation between "likes" and "apples" is labeled as "obj" (object).
- Dependency grammar can be represented in different ways, such as dependency trees, dependency graphs, or CoNLL format .
- A dependency tree is a tree structure where the nodes are the words and the edges are the dependencies. The root of the tree is the head of the sentence, and the leaves are the words that have no dependents .
- A dependency graph is a directed graph where the nodes are the words and the edges are the dependencies. A dependency graph can have cycles or multiple heads, unlike a dependency tree.
- CoNLL format is a tabular format where each row represents a word and each column represents a feature, such as word form, part-of-speech tag, head index, or dependency label.
- For example, the sentence "She likes apples" can be represented as follows:

| Word | POS | Head | Label |
|------|-----|------|-------|
| She  | PRP | 2    | nsubj |
| likes| VBZ | 0    | root  |
| apples| NNS | 2    | obj   |

- Dependency grammar has some advantages over constituency grammar, such as being more compact, more flexible, and more suitable for languages with free word order.
- Dependency grammar also has some disadvantages, such as being less expressive, less consistent, and less compatible with phrase structure rules.
- Dependency grammar is widely used for syntactic analysis of natural language texts, especially for tasks such as dependency parsing, semantic role labeling, and machine translation  .
- Dependency parsing is the task of automatically extracting the dependency structure of a given sentence, using either rule-based or data-driven methods .
- Semantic role labeling is the task of identifying the semantic roles of the arguments of a predicate, such as agent, patient, instrument, etc., using either dependency-based or constituency-based methods.
- Machine translation is the task of translating a text from one natural language to another, using either rule-based, statistical, or neural methods. Dependency grammar can help to capture the syntactic and semantic similarities and differences between languages.

: Dependency Parsing in NLP [Explained with Examples] - upGrad blog
: Syntactical Parsing in NLP - Analytics Vidhya
: Part 12: Step by Step Guide to Master NLP - Analytics Vidhya
: Annual Review of Linguistics Dependency Grammar
: Dependency grammar - Wikipedia