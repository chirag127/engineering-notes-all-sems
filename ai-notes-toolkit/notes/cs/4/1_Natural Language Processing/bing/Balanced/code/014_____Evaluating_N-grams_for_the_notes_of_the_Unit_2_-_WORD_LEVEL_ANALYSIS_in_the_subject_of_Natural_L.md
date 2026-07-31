### Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams can be used for various natural language processing tasks, such as language modeling, text generation, machine translation, speech recognition, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical regularities of natural language and how well they generalize to unseen data.
- One common way to evaluate n-grams is to use perplexity, which is the inverse of the average probability of a word given its previous words in a test set.
- Perplexity measures how surprised or uncertain the n-gram model is when predicting the next word in a text. A lower perplexity means a better fit and a higher generalization.
- Another way to evaluate n-grams is to use intrinsic and extrinsic methods. Intrinsic methods compare the n-gram model with a reference model, such as a human judgment or a gold standard corpus. Extrinsic methods measure the impact of the n-gram model on a downstream task, such as text summarization or sentiment analysis.
- Intrinsic methods are easier and faster to perform, but they may not reflect the actual performance of the n-gram model in a real-world application. Extrinsic methods are more realistic and meaningful, but they are more expensive and time-consuming to conduct.
- Some examples of intrinsic methods are:

  - Likelihood ratio test: compares the likelihood of two n-gram models on the same data and determines if the difference is statistically significant.
  - Goodness-of-fit test: compares the observed and expected frequencies of n-grams in a corpus and determines if they follow a certain distribution, such as Zipf's law or power law.
  - Coverage test: measures the percentage of n-grams in a test set that are also present in a training set and determines if the n-gram model is overfitting or underfitting.
  - Entropy test: measures the average amount of information or uncertainty in a text and determines if the n-gram model is capturing the diversity and complexity of natural language.

- Some examples of extrinsic methods are:

  - BLEU score: compares the n-gram overlap between a machine-generated translation and a human reference translation and determines the quality of the translation.
  - ROUGE score: compares the n-gram overlap between a machine-generated summary and a human reference summary and determines the quality of the summary.
  - Accuracy score: measures the percentage of correct predictions made by a n-gram model on a classification or recognition task and determines the accuracy of the model.