# Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams can be used for various natural language processing tasks, such as language modeling, text generation, spelling correction, machine translation, speech recognition, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical regularities of natural language and how well they generalize to unseen data.
- There are two main types of evaluation metrics for n-grams: intrinsic and extrinsic.

## Intrinsic evaluation

- Intrinsic evaluation measures the internal properties of n-grams, such as how well they fit the training data and how diverse they are.
- Intrinsic evaluation is usually faster and easier to perform than extrinsic evaluation, but it does not directly reflect the performance of n-grams on downstream tasks.
- Some common intrinsic evaluation metrics for n-grams are:

  - Perplexity: the inverse of the average probability assigned by the n-gram model to each word in a test set. Lower perplexity means higher probability and better fit.
  - Entropy: the average amount of information or uncertainty in the n-gram model. Higher entropy means more diversity and less predictability.
  - Coverage: the percentage of n-grams in a test set that are also present in the training set. Higher coverage means better generalization and less data sparsity.

## Extrinsic evaluation

- Extrinsic evaluation measures the impact of n-grams on the performance of a specific downstream task, such as text generation, machine translation, speech recognition, etc.
- Extrinsic evaluation is usually more costly and time-consuming than intrinsic evaluation, but it reflects the actual usefulness of n-grams for a given application.
- Some common extrinsic evaluation metrics for n-grams are:

  - BLEU: the geometric mean of the precision of n-grams in a generated text compared to one or more reference texts. Higher BLEU means higher similarity and better quality.
  - ROUGE: the recall of n-grams in a generated summary compared to one or more reference summaries. Higher ROUGE means higher coverage and better informativeness.
  - WER: the percentage of word errors (insertions, deletions, substitutions) in a transcribed speech compared to a reference transcription. Lower WER means higher accuracy and better recognition.