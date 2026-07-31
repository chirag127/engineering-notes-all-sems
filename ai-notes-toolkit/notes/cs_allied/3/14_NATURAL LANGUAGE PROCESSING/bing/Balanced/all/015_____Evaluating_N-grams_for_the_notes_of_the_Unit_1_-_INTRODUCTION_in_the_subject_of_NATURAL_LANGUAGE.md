# Evaluating N-grams

- N-grams are sequences of n words or tokens that are used to model the probability of a word given its previous words in a text.
- N-grams are useful for natural language processing tasks such as language modeling, text generation, machine translation, speech recognition, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical properties of natural language and how well they generalize to unseen data.
- There are two main types of evaluation methods for n-grams: intrinsic and extrinsic.

## Intrinsic evaluation

- Intrinsic evaluation measures the internal characteristics of n-grams, such as how well they fit the training data, how diverse they are, how coherent they are, etc.
- Intrinsic evaluation is usually faster and cheaper than extrinsic evaluation, but it may not reflect the actual performance of n-grams in real-world applications.
- Some common intrinsic evaluation metrics for n-grams are:

  - **Perplexity**: Perplexity is a measure of how uncertain the n-gram model is about predicting the next word in a text. It is defined as the inverse of the average probability assigned by the model to each word in the text. Lower perplexity means higher probability and lower uncertainty. Perplexity can be used to compare different n-gram models on the same test data, but it may not be comparable across different test data or different languages.
  - **Entropy**: Entropy is a measure of how much information is contained in a text. It is defined as the average amount of bits needed to encode each word in the text using the n-gram model. Higher entropy means more information and more diversity. Entropy can be used to measure the richness and variety of n-grams, but it may not capture the semantic or syntactic coherence of the text.
  - **Coverage**: Coverage is a measure of how many words or tokens in a text are recognized by the n-gram model. It is defined as the ratio of the number of words or tokens in the text that have a non-zero probability assigned by the model to the total number of words or tokens in the text. Higher coverage means better vocabulary and less out-of-vocabulary words. Coverage can be used to measure the completeness and robustness of n-grams, but it may not reflect the accuracy or relevance of the predictions.

## Extrinsic evaluation

- Extrinsic evaluation measures the external performance of n-grams, such as how well they improve the quality of a downstream task or application that uses them as a component or a feature.
- Extrinsic evaluation is usually more realistic and meaningful than intrinsic evaluation, but it may also be more complex and costly, depending on the task or application.
- Some common extrinsic evaluation tasks or applications for n-grams are:

  - **Text generation**: Text generation is the task of producing natural language text from a given input, such as a prompt, a keyword, a topic, etc. N-grams can be used to generate text by sampling or selecting the most probable words according to the model. The quality of the generated text can be evaluated by human or automatic metrics, such as fluency, coherence, relevance, originality, etc.
  - **Machine translation**: Machine translation is the task of translating natural language text from one language to another. N-grams can be used to model the source and target languages, as well as the translation probabilities between them. The quality of the translation can be evaluated by human or automatic metrics, such as adequacy, fluency, accuracy, etc.
  - **Speech recognition**: Speech recognition is the task of converting speech signals into natural language text. N-grams can be used to model the language of the speech, as well as the acoustic features of the speech signals. The quality of the recognition can be evaluated by human or automatic metrics, such as word error rate, accuracy, etc.