Word sense disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context. WSD using supervised methods relies on sense-annotated training data, where each word is labeled with its correct sense from a predefined sense inventory, such as WordNet. A classifier is then trained on the labeled data to learn the features that distinguish different senses of a word. The classifier can then be applied to new data to predict the sense of a word based on its context.

The following diagram illustrates the basic architecture of a supervised WSD system using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
| Sense-annotated |     | Feature         |     | Trained         |
| training data   | --> | extraction      | --> | classifier      |
+-----------------+     +-----------------+     +-----------------+
                                                    |
                                                    |
                                                    V
+-----------------+     +-----------------+     +-----------------+
| New data        |     | Feature         |     | Sense           |
| (unlabeled)     | --> | extraction      | --> | prediction      |
+-----------------+     +-----------------+     +-----------------+
```

The feature extraction module is responsible for extracting relevant features from the word and its context, such as part-of-speech tags, surrounding words, syntactic dependencies, etc. The trained classifier uses these features to assign a sense to the word based on the learned patterns from the training data. The sense prediction module outputs the predicted sense for the word, which can be used for downstream applications such as machine translation, information retrieval, text mining, etc.