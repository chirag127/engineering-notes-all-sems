Syntactic parsing is the process of analyzing the syntactic structure of natural language, especially syntactic relations (in dependency grammar) and labeling spans of constituents (in constituency grammar) . Syntactic parsing is one of the important tasks in natural language processing, and has been a subject of research since the mid-20th century with the advent of computers. Different theories of grammar propose different formalisms for describing the syntactic structure of sentences.

The following diagram illustrates the basic architecture of a syntactic parser:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input text    +---->+  Tokenizer     +---->+  Morphological |
|                |     |                |     |  Analyzer      |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Grammar       +---->+  Parser        +---->+  Parse tree    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Lexicon       +---->+  Semantic      +---->+  Semantic      |
|                |     |  Analyzer      |     |  Representation|
+----------------+     +----------------+     +----------------+
```

The input text is a natural language sentence that needs to be parsed. The tokenizer splits the input text into tokens, which are the smallest units of meaning in a language, such as words, punctuation marks, numbers, etc. The morphological analyzer assigns part-of-speech tags and other morphological features to each token, such as tense, number, gender, case, etc. The grammar is a set of rules that define the syntactic structure of the language, such as how words can be combined into phrases and sentences. The parser applies the grammar rules to the tokens and generates a parse tree, which is a hierarchical representation of the syntactic structure of the sentence. The lexicon is a collection of words and their meanings, such as synonyms, antonyms, hyponyms, etc. The semantic analyzer uses the lexicon and the parse tree to derive the semantic representation of the sentence, which is a formal representation of the meaning of the sentence, such as a logical expression, a semantic network, a frame, etc.