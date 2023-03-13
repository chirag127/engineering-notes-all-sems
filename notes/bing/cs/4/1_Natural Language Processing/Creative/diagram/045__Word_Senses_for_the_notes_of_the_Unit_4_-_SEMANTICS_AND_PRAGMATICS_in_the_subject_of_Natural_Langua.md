Word senses are the different meanings that a word can have in natural language. For example, the word "bank" can mean a financial institution, a sloping mound, a biological repository, or a building where a bank does its business, depending on the context. Word sense disambiguation (WSD) is the task of assigning the correct sense to a word in a given text or discourse. WSD is a challenging problem in natural language processing (NLP) because natural language is ambiguous and many words can be interpreted in multiple ways.

The following diagram illustrates the basic architecture of a word sense disambiguation system in NLP:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Input text     |---->| Preprocessing  |---->| Feature        |
|                |     |                |     | extraction     |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 |
                                                 V
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Sense          |<----| Disambiguation |<----| Feature        |
| inventory      |     | algorithm      |     | representation |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                                 |
                                                 |
                                                 V
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Sense          |<----| Evaluation     |<----| Output         |
| annotated text |     | metrics        |     | text           |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The input text is the raw text that contains the word to be disambiguated. The preprocessing step involves tokenizing, lemmatizing, and part-of-speech tagging the text. The feature extraction step involves selecting relevant features that can help distinguish the word senses, such as the surrounding words, the syntactic structure, the domain, or the topic of the text. The feature representation step involves encoding the features in a suitable format, such as a vector, a graph, or a matrix. The sense inventory is a collection of possible senses for the word, such as a dictionary, a thesaurus, or a knowledge base. The disambiguation algorithm is the method that assigns the most likely sense to the word, based on the features and the sense inventory. The output text is the text with the word sense annotated, such as with a sense identifier or a definition. The evaluation metrics are the measures that assess the accuracy and the quality of the disambiguation, such as precision, recall, or F1-score. The sense annotated text is the text with the word sense annotated and evaluated, which can be used for further analysis or applications.