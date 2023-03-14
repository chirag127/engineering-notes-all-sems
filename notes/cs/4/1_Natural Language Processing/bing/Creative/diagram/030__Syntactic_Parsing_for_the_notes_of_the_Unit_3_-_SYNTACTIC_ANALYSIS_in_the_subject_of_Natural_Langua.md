Syntactic parsing is the process of analyzing the syntactic structure of natural language, especially syntactic relations (in dependency grammar) and labeling spans of constituents (in constituency grammar).  It is one of the important tasks in natural language processing and has been a subject of research since the mid-20th century with the advent of computers. 

Different theories of grammar propose different formalisms for describing the syntactic structure of sentences. For computational purposes, these formalisms can be grouped under constituency grammars and dependency grammars. Parsers for either class call for different types of algorithms, and approaches to the two problems have taken different forms. 

The following diagram illustrates the basic architecture of a syntactic parser:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input text    | --> |  Tokenizer     | --> |  POS tagger    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Constituency  | <-- |  Constituency  | <-- |  Constituency  |
|  grammar       |     |  parser        |     |  parse tree    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Dependency    | <-- |  Dependency    | <-- |  Dependency    |
|  grammar       |     |  parser        |     |  parse tree    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The input text is first tokenized into words and punctuation marks. Then, a part-of-speech (POS) tagger assigns a POS tag to each token, such as noun, verb, adjective, etc. The POS tags are used as features for the syntactic parsers.

A constituency parser analyzes the input text according to a constituency grammar, such as the formalism of the Penn Treebank. It produces a constituency parse tree, which shows the hierarchical structure of phrases and clauses in the sentence. A constituency parse tree can be converted to a dependency parse tree using a set of rules or a machine learning model.

A dependency parser analyzes the input text according to a dependency grammar, such as the Universal Dependencies. It produces a dependency parse tree, which shows the syntactic relations between words in the sentence, such as subject, object, modifier, etc. A dependency parse tree can be used for information extraction, semantic role labeling, entity labeling, and other downstream tasks.     

: https://en.wikipedia.org/wiki/Syntactic_parsing_(computational_linguistics)
: https://en.wikipedia.org/wiki/Parsing
: https://www.tutorialspoint.com/natural_language_processing/natural_language_processing_syntactic_analysis.htm
: https://knowledgeburrow.com/what-is-syntactic-parsing-in-nlp/
: https://nlp.stanford.edu/software/lex-parser.shtml