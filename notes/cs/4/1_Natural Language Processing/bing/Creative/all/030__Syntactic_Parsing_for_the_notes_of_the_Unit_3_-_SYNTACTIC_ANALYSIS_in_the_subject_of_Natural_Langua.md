### Syntactic Parsing for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Syntactic parsing is the automatic analysis of syntactic structure of natural language, especially syntactic relations (in dependency grammar) and labelling spans of constituents (in constituency grammar).
- Syntactic parsing is motivated by the problem of structural ambiguity in natural language: a sentence can be assigned multiple grammatical parses, so some kind of knowledge beyond computational grammar rules are needed to tell which parse is intended.
- Syntactic parsing is one of the important tasks in computational linguistics and natural language processing, and has been a subject of research since the mid-20th century with the advent of computers.
- Syntactic parsing can also serve as the basis for semi-supervised and transfer learning of syntactic parsers when there exist both unannotated sentences and (in-domain or out-of-domain) annotated sentences.
- Syntactic parsing can also be useful for downstream tasks such as semantic parsing, relation extraction, and machine translation.
- Different theories of grammar propose different formalisms for describing the syntactic structure of sentences. For computational purposes, these formalisms can be grouped under constituency grammars and dependency grammars.
- Constituency grammars assume that sentences are composed of nested phrases, each of which has a head word and a syntactic category. Constituency grammars use context-free grammars (CFGs) or probabilistic context-free grammars (PCFGs) to encode rules for constituent formation and merging.
- Dependency grammars assume that sentences are composed of words that are linked by binary asymmetric relations called dependencies. Dependency grammars use dependency structures or graphs to represent the syntactic structure of sentences.
- Parsers for either class of grammars call for different types of algorithms, and approaches to the two problems have taken different forms.
- The most popular algorithm for constituency parsing is the Cocke–Kasami–Younger algorithm (CKY), which is a dynamic programming algorithm that constructs a parse in worst-case time, on a sentence of words and is the size of a CFG given in Chomsky Normal Form.
- The most popular algorithm for dependency parsing is the Eisner algorithm, which is also a dynamic programming algorithm that constructs a projective dependency parse in worst-case time, on a sentence of words.
- Given the issue of ambiguity leading to multiple acceptable parses, it is necessary to be able to score the probability of parses to pick the most probable one. One way to do this is by using PCFGs or probabilistic dependency grammars (PDGs) which have a probability of each rule or dependency, and modifying CKY or Eisner to maximise probabilities when parsing bottom-up.
- Another way to do this is by using discriminative models such as conditional random fields (CRFs) or neural networks, which can learn feature weights or parameters from annotated data, and use them to score parses.
- A major challenge faced by supervised parsing is that syntactically annotated sentences are not always available for a target language or domain and building high-quality annotated corpus is very expensive and time-consuming.
- A radical solution to this challenge is unsupervised parsing, sometimes also called grammar induction, which learns a parser from training sentences without parse tree annotations.
- Unsupervised parsing can be done by using generative models such as PCFGs or PDGs, and applying unsupervised learning techniques such as expectation-maximization (EM) or variational inference (VI) to estimate the model parameters from unannotated data.
- Unsupervised parsing can also be done by using discriminative models such as neural networks, and applying self-training or pre-training techniques such as auto-encoding, contrastive learning, or masked language modeling to learn the model parameters from unannotated data.
- Unsupervised parsing can also be done by using external sources of information such as visual input, cross-lingual data, or BERT embeddings to guide the learning of syntactic structure from unannotated data.

: Syntactic parsing (computational linguistics) - Wikipedia
: Unsupervised Natural Language Parsing (Introductory Tutorial)