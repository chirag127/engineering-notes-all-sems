WSD using Supervised is a method of word sense disambiguation that relies on sense-annotated training data to learn a classifier for each ambiguous word. The classifier is then applied to new instances of the word in context to predict the correct sense. Supervised WSD methods typically use features such as the surrounding words, part-of-speech tags, syntactic dependencies, and semantic relations to represent the context of the word. Supervised WSD methods can achieve high accuracy, but they require a large amount of labeled data, which is costly and time-consuming to obtain.

The following diagram illustrates the basic architecture of a supervised WSD system using a naive Bayes classifier:

```
+-----------------+     +-----------------+     +-----------------+
| Sense-annotated |     | Feature         |     | Naive Bayes     |
| training corpus | --> | extraction      | --> | classifier      | --> Sense
+-----------------+     +-----------------+     +-----------------+
                                    |                  ^
                                    |                  |
                                    v                  |
                               +-----------------+     |
                               | Feature         |     |
                               | extraction      | ----+
                               +-----------------+
                                    |
                                    v
                               +-----------------+
                               | Unlabeled       |
                               | test corpus     |
                               +-----------------+
```