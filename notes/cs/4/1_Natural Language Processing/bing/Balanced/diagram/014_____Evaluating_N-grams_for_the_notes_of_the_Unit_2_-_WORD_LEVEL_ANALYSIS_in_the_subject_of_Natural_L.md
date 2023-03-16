Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of evaluating n-grams for the notes of the unit 2 - word level analysis in the subject of natural language processing.

### Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams are useful for tasks such as language modeling, text generation, machine translation, speech recognition, and information retrieval.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical properties of natural language and how well they perform on the downstream tasks.
- There are two main types of evaluation methods for n-grams: intrinsic and extrinsic.

#### Intrinsic Evaluation

- Intrinsic evaluation measures the internal characteristics of n-grams, such as how well they fit the training data, how diverse they are, and how coherent they are.
- Intrinsic evaluation is usually faster and cheaper than extrinsic evaluation, but it may not reflect the actual performance of n-grams on the real-world tasks.
- Some common intrinsic evaluation metrics for n-grams are:

  - Perplexity: the inverse of the average probability of the test data given the n-gram model. It measures how well the n-gram model predicts the next word in a text. Lower perplexity means better fit and generalization.
  - Coverage: the percentage of n-grams in the test data that are also in the training data. It measures how diverse the n-gram model is. Higher coverage means more vocabulary and less data sparsity.
  - Coherence: the degree of semantic and syntactic relatedness among the words in an n-gram. It measures how meaningful and natural the n-gram model is. Higher coherence means more sense and fluency.

#### Extrinsic Evaluation

- Extrinsic evaluation measures the impact of n-grams on the performance of the downstream tasks, such as text generation, machine translation, speech recognition, and information retrieval.
- Extrinsic evaluation is usually more realistic and reliable than intrinsic evaluation, but it may also be more time-consuming and expensive.
- Some common extrinsic evaluation metrics for n-grams are:

  - BLEU: the geometric mean of the n-gram precision scores multiplied by a brevity penalty. It measures how similar the generated text is to the reference text in terms of n-grams. Higher BLEU means better quality and accuracy.
  - ROUGE: the recall-oriented metric that compares the n-grams in the generated text to the n-grams in the reference text. It measures how much information the generated text contains in terms of n-grams. Higher ROUGE means better completeness and relevance.
  - WER: the word error rate that counts the number of word substitutions, insertions, and deletions needed to match the generated text to the reference text. It measures how many errors the generated text has in terms of words. Lower WER means better correctness and intelligibility.