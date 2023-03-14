A treebank is a parsed text corpus that annotates syntactic or semantic sentence structure. Treebanks are often used for natural language processing tasks such as part-of-speech tagging, parsing, semantic analysis and machine translation. Treebanks can be annotated with different types of syntactic structures, such as phrase structure or dependency structure. A phrase structure tree represents the hierarchical grouping of words into phrases and clauses, while a dependency structure tree represents the grammatical relations between words. Treebanks can be created manually, semi-automatically or automatically, and can vary in size, complexity and linguistic theory.

The following diagram illustrates the basic architecture of a treebank:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Raw corpus   +--->+   POS tagger   +--->+   Parser       |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
                                                   |
                                                   |
                                                   v
                                            +----------------+
                                            |                |
                                            |   Treebank    |
                                            |                |
                                            +----------------+
```

The raw corpus is a collection of natural language texts that are the input for the treebank. The POS tagger is a tool that assigns part-of-speech tags to each word in the corpus, such as noun, verb, adjective, etc. The parser is a tool that assigns syntactic structure to each sentence in the corpus, such as phrase structure or dependency structure. The treebank is the output of the parser, which contains the annotated sentences with syntactic structure. The treebank can be stored in different file formats, such as plain text, XML, JSON, etc. The treebank can also be enhanced with additional linguistic information, such as semantic roles, coreference, discourse relations, etc.