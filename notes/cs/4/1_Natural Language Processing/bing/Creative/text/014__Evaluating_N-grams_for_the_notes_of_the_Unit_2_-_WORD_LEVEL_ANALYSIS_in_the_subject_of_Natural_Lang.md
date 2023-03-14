### Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams can be used for various natural language processing tasks, such as language modeling, text generation, spelling correction, machine translation, speech recognition, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical regularities of natural language and how well they generalize to unseen data.
- There are two main types of evaluation methods for n-grams: intrinsic and extrinsic.

#### Intrinsic evaluation

- Intrinsic evaluation measures the internal properties of n-grams, such as their frequency, coverage, perplexity, etc.
- Frequency is the number of times an n-gram occurs in a given corpus. It reflects how common or rare an n-gram is in a language.
- Coverage is the percentage of words in a corpus that can be predicted by an n-gram model. It reflects how comprehensive an n-gram model is in a language.
- Perplexity is the inverse of the average probability assigned by an n-gram model to a word given its previous words. It reflects how uncertain or surprised an n-gram model is by a language.
- Intrinsic evaluation is useful for comparing different n-gram models or tuning their parameters, such as the value of n, the smoothing technique, the vocabulary size, etc.
- However, intrinsic evaluation does not directly measure how well n-grams perform on a specific natural language processing task or application.

#### Extrinsic evaluation

- Extrinsic evaluation measures the impact of n-grams on a specific natural language processing task or application, such as text generation, spelling correction, machine translation, speech recognition, etc.
- Extrinsic evaluation requires a predefined metric or criterion that reflects the quality or performance of the task or application, such as accuracy, precision, recall, F1-score, BLEU, ROUGE, etc.
- Extrinsic evaluation is useful for assessing how useful or effective n-grams are for a specific natural language processing task or application.
- However, extrinsic evaluation is more costly and time-consuming than intrinsic evaluation, as it requires a large amount of annotated data, a baseline system, and a test set.