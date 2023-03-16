### WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings.
- Supervised WSD methods use sense-annotated corpora to train machine learning models that can predict the sense of a word based on its features, such as the surrounding words, part-of-speech tags, syntactic dependencies, etc  .
- The most widely used training corpus for supervised WSD is SemCor, which contains 226,036 sense annotations from 352 documents manually annotated with WordNet senses .
- Some of the common supervised WSD algorithms are:
  - Naive Bayes: This is a probabilistic classifier that assigns the most likely sense to a word based on the frequencies of the features in the training data.
  - Decision Trees: This is a rule-based classifier that splits the feature space into regions based on the values of the features, and assigns the most frequent sense in each region to the word.
  - Support Vector Machines: This is a linear classifier that finds the optimal hyperplane that separates the feature vectors of different senses, and assigns the sense that corresponds to the side of the hyperplane where the word's feature vector lies.
  - Neural Networks: This is a non-linear classifier that learns a complex function that maps the feature vectors to the senses, and assigns the sense that has the highest output value for the word's feature vector.
- Supervised WSD methods have the advantage of being able to learn from large amounts of data and achieve high accuracy, but they also have some limitations, such as:
  - They require a lot of manually annotated data, which is costly and time-consuming to obtain .
  - They suffer from the data sparsity problem, which means that they may not have enough examples for rare or fine-grained senses, or for new words that are not in the training data .
  - They are domain-dependent, which means that they may not generalize well to different domains or genres of text, where the word usage and sense distribution may vary .

: http://nlpprogress.com/english/word_sense_disambiguation.html
: https://www.ijsr.net/archive/v4i2/SUB151598.pdf
: https://aclanthology.org/2020.textgraphs-1.6.pdf
: http://www.scholarpedia.org/article/Word_sense_disambiguation
: https://www.tutorialspoint.com/natural_language_processing/natural_language_processing_word_sense_disambiguation.htm
: https://link.springer.com/article/10.1007/s12046-019-1206-x