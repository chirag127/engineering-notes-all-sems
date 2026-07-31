### WSD using Supervised

Word Sense Disambiguation (WSD) is the task of identifying the correct sense of a word in a given context. Supervised WSD methods use labeled data to train a classifier that can then be used to disambiguate new instances.

1. **Training Data**: Supervised WSD methods require a large amount of labeled data, where each instance is a word in context, labeled with the correct sense. This data can be obtained from sense-annotated corpora or created manually.

2. **Feature Extraction**: Features are extracted from the training data to represent each instance. Common features used in WSD include the surrounding words, part-of-speech tags, and syntactic relations.

3. **Classification**: A classifier is trained on the labeled data using the extracted features. Common classifiers used in WSD include decision trees, Naive Bayes, and support vector machines.

4. **Disambiguation**: The trained classifier is used to disambiguate new instances by assigning the most likely sense based on the extracted features.

Supervised WSD methods can achieve high accuracy when a large amount of labeled data is available. However, creating labeled data can be time-consuming and expensive, and the performance of the classifier may not generalize well to new domains or languages.