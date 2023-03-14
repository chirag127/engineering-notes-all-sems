Syntactic ambiguity is the presence of two or more possible meanings within a single sentence or sequence of words, due to ambiguous sentence structure. Syntactic ambiguity arises from the relationship between the words and clauses of a sentence, and the sentence structure underlying the word order therein. Syntactic ambiguity can be global or local, depending on whether the ambiguity persists or is resolved by the end of the sentence. Syntactic ambiguity can lead to misunderstanding, confusion, or humor, depending on the context and intention of the speaker or writer.

The following diagram illustrates the basic architecture of a syntactic analyzer:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Lexical       |     |  Syntactic     |     |  Semantic      |
|  Analyzer      |---->|  Analyzer      |---->|  Analyzer      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Converts      |     |  Checks the    |     |  Checks the    |
|  input stream  |     |  syntactic     |     |  semantic      |
|  of characters |     |  structure of  |     |  validity and  |
|  into tokens   |     |  the tokens    |     |  meaning of    |
|                |     |                |     |  the tokens    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```