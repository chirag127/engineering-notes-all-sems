### Dependency Grammar for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity. It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- Dependency grammar is based on the idea that syntactic structure consists of words linked by binary, asymmetrical relations called dependency relations (or dependencies for short). A dependency relation holds between a syntactically subordinate word, called the dependent, and another word on which it depends, called the head.
- Dependency grammar differs from phrase structure grammar, which is the most widely used type of syntactic representation in both theoretical and computational linguistics. Phrase structure grammar represents the grouping of words into phrases, classified by structural categories such as noun phrase (NP) and verb phrase (VP). Dependency grammar, on the other hand, represents head-dependent relations between words, classified by functional categories such as subject (SBJ) and object (OBJ).
- A dependency structure for a sentence can be represented by a labeled directed graph, where nodes correspond to words (including an artificial word root before the first word of the sentence) and labeled arcs correspond to typed dependency relations. For example, the dependency structure for the sentence "The news had an effect on the economy" can be represented as follows:

```
root
  |
  |SBJ
  v
 news
  |ATT
  v
Economic
  ^
  |OBJ
  |
 had
  |
  |ATT
  v
  an
  |
  |ATT
  v
effect
  |
  |PC
  v
  on
  |
  |PNC
  v
the
  |
  |ATT
  v
economy
```

- Dependency grammar has some advantages over phrase structure grammar, such as simplicity, parsimony, and flexibility. Dependency grammar is simpler because it does not require the notion of phrase or constituent, which can be problematic for some languages that have free word order or discontinuous constituents. Dependency grammar is more parsimonious because it has fewer nodes and labels than phrase structure grammar, which can reduce the complexity and ambiguity of syntactic analysis. Dependency grammar is more flexible because it can capture various syntactic phenomena that phrase structure grammar cannot, such as long-distance dependencies, coordination, and ellipsis .
- Dependency grammar also has some disadvantages, such as lack of standardization, difficulty of parsing, and limited expressiveness. Dependency grammar lacks a standard set of dependency types and labels, which can lead to inconsistency and confusion among different frameworks and applications. Dependency grammar is more difficult to parse than phrase structure grammar, because it requires more sophisticated algorithms and models that can handle non-projective dependencies and multiple heads. Dependency grammar is less expressive than phrase structure grammar, because it cannot represent hierarchical and recursive structures that are common in natural languages .
- Dependency grammar has many applications in natural language processing, such as syntactic parsing, semantic parsing, information extraction, machine translation, and natural language generation. Dependency grammar can provide a rich and compact representation of the syntactic and semantic information of a sentence, which can facilitate various natural language processing tasks. Dependency grammar can also be integrated with other linguistic theories and resources, such as lexical functional grammar, head-driven phrase structure grammar, and WordNet, to enhance the performance and accuracy of natural language processing systems .

Some mnemonics and learning tricks for dependency grammar are:

- Remember that dependency grammar is based on the idea of head-dependent relations, where the head is the word that determines the syntactic and semantic properties of the dependent. A useful acronym to remember the head-dependent relation is HDL, which stands for Head-Dependent Link.
- Remember that dependency grammar differs from phrase structure grammar, which is based on the idea of grouping words into phrases. A useful way to remember the difference is to think of dependency grammar as a tree with branches, where each branch connects a head word with a dependent word, and phrase structure grammar as a nest with boxes, where each box contains a phrase with a structural category.
- Remember that dependency grammar has some advantages and disadvantages over phrase structure grammar. A useful way to remember them is to use the mnemonic SPADEL, which stands for Simplicity, Parsimony, and Flexibility (advantages) and Standardization, Parsing, and Expressiveness (