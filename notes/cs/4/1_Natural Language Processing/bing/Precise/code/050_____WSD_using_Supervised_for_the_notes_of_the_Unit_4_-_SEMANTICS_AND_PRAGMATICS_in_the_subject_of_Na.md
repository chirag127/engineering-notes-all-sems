### WSD using Supervised

Word Sense Disambiguation (WSD) is the task of identifying the correct sense of a word in a given context. Supervised WSD methods use labeled data to train a classifier that can then be used to disambiguate new instances.

1. **Training Data**: Supervised WSD methods require a large amount of labeled data, where each instance is a word in context, and the label is the correct sense of the word. This data can be obtained from sense-annotated corpora or by manually annotating data.

2. **Feature Extraction**: Features are extracted from the context of the word to be disambiguated. Common features include the surrounding words, their part-of-speech tags, and their syntactic relations.

3. **Classification**: A classifier is trained on the labeled data using the extracted features. Common classifiers used for WSD include decision trees, naive Bayes, and support vector machines.

4. **Disambiguation**: The trained classifier is used to predict the sense of new instances. The features are extracted from the context of the word to be disambiguated, and the classifier assigns a sense based on these features.

Supervised WSD methods can achieve high accuracy when a large amount of labeled data is available. However, obtaining labeled data can be time-consuming and expensive. Additionally, supervised methods may not generalize well to new domains or languages.