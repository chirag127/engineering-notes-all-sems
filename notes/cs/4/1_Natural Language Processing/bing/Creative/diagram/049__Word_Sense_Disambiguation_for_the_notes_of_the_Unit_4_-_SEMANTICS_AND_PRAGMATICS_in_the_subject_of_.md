Word Sense Disambiguation (WSD) is the process of identifying which sense of a word is meant in a sentence or other segment of context. For example, the word "bank" can have different meanings depending on the context, such as a financial institution, a river shore, or a verb meaning to tilt or lean.

A basic architecture of a WSD system can be represented as follows:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Input text     |---->|  Preprocessing  |---->|  Disambiguation |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                                                    |
                                                    |
                                                    V
                                               +-----------------+
                                               |                 |
                                               |  Output sense  |
                                               |                 |
                                               +-----------------+
```

The input text is the text that contains the word to be disambiguated. The preprocessing step can involve various tasks, such as tokenization, part-of-speech tagging, lemmatization, and syntactic parsing. The disambiguation step is the core of the WSD system, where different methods and algorithms can be applied to assign the most appropriate sense to the word. The output sense can be a label from a predefined sense inventory, such as WordNet, or a cluster of similar words or contexts, depending on the approach used.