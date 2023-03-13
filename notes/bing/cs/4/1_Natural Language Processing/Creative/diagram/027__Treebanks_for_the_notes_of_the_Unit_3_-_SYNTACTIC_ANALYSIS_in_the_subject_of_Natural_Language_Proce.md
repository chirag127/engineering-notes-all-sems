A treebank is a collection of syntactically annotated sentences in which the annotation has been manually checked  . Treebanks have become valuable resources in natural language processing (NLP) for engineering and training various systems such as parsers, taggers, semantic analyzers and machine translation systems  .

The following diagram illustrates the basic architecture of a treebank in markdown:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Raw corpus    |    |   POS tagging   |    |   Parsing       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   A collection  |    |   Assigning     |    |   Assigning     |
|   of sentences  |    |   part-of-speech|    |   syntactic     |
|   in a natural  |    |   tags to each  |    |   structure to  |
|   language      |    |   word in the   |    |   each sentence |
|                 |    |   corpus        |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +---------------------->                      |
                                |                      |
                                |                      |
                                |                      |
                                +---------------------->
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |