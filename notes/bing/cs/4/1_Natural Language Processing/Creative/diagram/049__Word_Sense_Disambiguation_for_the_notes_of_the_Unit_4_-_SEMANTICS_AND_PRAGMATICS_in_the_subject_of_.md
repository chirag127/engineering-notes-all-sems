Word Sense Disambiguation (WSD) is the process of identifying which sense of a word is meant in a sentence or other segment of context. There are different approaches and methods to WSD, such as dictionary-based, supervised, semi-supervised, and unsupervised methods.

The following diagram illustrates the basic architecture of a WSD system:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input text    +---->+  Preprocessing +---->+  Disambiguation|
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                         |
                                         |
                                         v
                                 +----------------+
                                 |                |
                                 |  Sense output  |
                                 |                |
                                 +----------------+
```

The input text is the text that contains the ambiguous word(s) that need to be disambiguated. The preprocessing step involves tokenizing, lemmatizing, and tagging the text with part-of-speech tags. The disambiguation step involves applying one or more methods to assign the most appropriate sense to each ambiguous word, based on the context and a sense inventory (such as WordNet). The sense output is the result of the disambiguation, which can be a sense identifier, a definition, or a synonym of the word.