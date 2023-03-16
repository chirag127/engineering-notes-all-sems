### Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams can be used for various natural language processing tasks, such as language modeling, text generation, spelling correction, machine translation, speech recognition, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical regularities of natural language and how well they generalize to unseen data.
- There are two main types of evaluation methods for n-grams: intrinsic and extrinsic.

#### Intrinsic evaluation

- Intrinsic evaluation measures the internal properties of n-grams, such as how well they fit the training data and how diverse they are.
- Intrinsic evaluation can be done by using metrics such as perplexity, entropy, and coverage.

  - Perplexity is a measure of how uncertain the n-gram model is about predicting the next word in a sequence. It is defined as the inverse of the average probability assigned by the model to each word in a test set. A lower perplexity means a better fit and a higher predictive power.
  - Entropy is a measure of how much information is contained in a text. It is defined as the average number of bits needed to encode each word in a text using the n-gram model. A higher entropy means a more diverse and complex text.
  - Coverage is a measure of how many words in a test set are seen in the training set. It is defined as the ratio of the number of words in the test set that are also in the training set to the total number of words in the test set. A higher coverage means a better generalization and a lower data sparsity.

#### Extrinsic evaluation

- Extrinsic evaluation measures the impact of n-grams on the performance of a downstream task, such as text generation, machine translation, speech recognition, etc.
- Extrinsic evaluation can be done by using metrics such as BLEU, ROUGE, WER, etc.

  - BLEU (bilingual evaluation understudy) is a metric for evaluating the quality of machine translation output. It is defined as the geometric mean of the n-gram precision scores multiplied by a brevity penalty. A higher BLEU score means a better translation quality and a higher similarity to the reference translation.
  - ROUGE (recall-oriented understudy for gisting evaluation) is a metric for evaluating the quality of text summarization output. It is defined as the F1-score of the n-gram overlap between the summary and the reference text. A higher ROUGE score means a better summary quality and a higher informativeness and relevance.
  - WER (word error rate) is a metric for evaluating the quality of speech recognition output. It is defined as the ratio of the number of errors (substitutions, deletions, and insertions) to the number of words in the reference transcription. A lower WER means a better speech recognition quality and a higher accuracy.