### Evaluating N-grams

- N-grams are sequences of words or characters that are used to model natural language.
- N-grams can be used for various tasks, such as text generation, spelling correction, machine translation, speech recognition, etc.
- N-grams are typically extracted from a large corpus of text, and their probabilities are estimated based on their frequency of occurrence.
- N-grams can be evaluated based on different criteria, such as:

  - **Coverage**: the percentage of n-grams in a test set that are also present in a training set. Higher coverage means better generalization and less data sparsity.
  - **Perplexity**: the inverse of the average probability of a test set, given a trained n-gram model. Lower perplexity means better fit and less uncertainty.
  - **Entropy**: the average amount of information contained in an n-gram. Higher entropy means more diversity and richness of language.
  - **Likelihood**: the probability of a test set, given a trained n-gram model. Higher likelihood means better fit and more evidence.
  - **Cross-entropy**: the average amount of information needed to encode a test set, given a trained n-gram model. Lower cross-entropy means better fit and less redundancy.

- N-grams can be evaluated using different methods, such as:

  - **Held-out estimation**: a portion of the training data is set aside as a validation set, and the n-gram model is trained on the remaining data. The n-gram model is then evaluated on the validation set using one or more of the criteria mentioned above.
  - **Bootstrap sampling**: the n-gram model is trained on the entire training data, and then a number of samples are drawn from the training data with replacement. The n-gram model is then evaluated on each sample using one or more of the criteria mentioned above, and the results are averaged.
  - **Cross-validation**: the training data is divided into k folds, and the n-gram model is trained on k-1 folds and evaluated on the remaining fold. This process is repeated for each fold, and the results are averaged.
  - **Extrinsic evaluation**: the n-gram model is used as a component of a larger system, such as a machine translation system or a speech recognition system, and the performance of the system is measured on a test set using some task-specific metric, such as BLEU score or word error rate.