### WSD using Supervised

Word Sense Disambiguation (WSD) is the task of identifying the correct sense of a word in context. Supervised WSD methods use labeled data to train a classifier to predict the correct sense of a word in context.

1. **Training Data**: Supervised WSD methods require labeled data, where each instance of a word is annotated with its correct sense. This data is used to train a classifier to predict the correct sense of a word in context.
2. **Feature Extraction**: Features are extracted from the context of the word to be disambiguated. These features can include the surrounding words, part-of-speech tags, and syntactic dependencies.
3. **Classification**: A classifier is trained on the labeled data using the extracted features. The classifier can be a decision tree, a support vector machine, or a neural network, among others.
4. **Evaluation**: The performance of the classifier is evaluated on a separate test set, where the true senses of the words are known. Common evaluation metrics include accuracy, precision, recall, and F1-score.

Supervised WSD methods can achieve high accuracy when there is a large amount of labeled data available. However, creating labeled data can be time-consuming and expensive, and the performance of supervised methods may suffer when there is a limited amount of labeled data available. Additionally, supervised methods may not generalize well to new domains or languages, where the distribution of senses may be different.