### Evaluating N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

N-grams are contiguous sequences of n items from a given sample of text or speech. Evaluating N-grams is an important part of word level analysis in Natural Language Processing (NLP). N-grams can be used to extract language patterns and predict the likelihood of certain words occurring in a given context.

Here are some important points to keep in mind while evaluating N-grams for word level analysis in NLP:

1. **Choosing the right value of n**: The value of n determines the size of the N-grams to be evaluated. A higher value of n will result in larger N-grams, which may capture more context but can also lead to sparsity of data. On the other hand, a lower value of n will result in smaller N-grams, which may not capture enough context but can result in more dense data. It is important to strike a balance between these two factors and choose the right value of n depending on the task at hand.

2. **Calculating N-gram frequency**: The frequency of each N-gram in the sample text can be calculated to understand its importance and relevance to the task at hand. This can be done using formulas such as the Maximum Likelihood Estimation (MLE) or the Laplace smoothing technique.

3. **Measuring N-gram perplexity**: Perplexity is a measure of how well a language model predicts a given text. It is calculated by taking the inverse of the geometric mean of the probabilities assigned to each word in the text by the language model. N-gram perplexity is a popular method of evaluating language models based on N-grams.

4. **Using N-grams for language modelling**: Language modelling is the process of predicting the probability of a given sequence of words occurring in a given context. N-grams can be used for language modelling by calculating the conditional probability of each word in the sequence given its preceding N-1 words.

5. **Advantages of using N-grams**: N-grams can capture important language patterns and context, making them useful for tasks such as language modelling, speech recognition, and text classification. They are also computationally efficient and can be easily implemented using existing libraries and tools.

6. **Disadvantages of using N-grams**: N-grams may not capture long-term dependencies between words, resulting in less accurate predictions. They can also lead to sparse data and overfitting if the sample size is too small or if the value of n is too high.

Mnemonics and learning tricks for evaluating N-grams:

- Remember the formula for calculating N-gram perplexity: perplexity = 2^(-log P(w1,w2,...,wn)/N), where P(w1,w2,...,wn) is the probability of the given sequence of words and N is the total number of words in the text.
- A useful way to remember the advantages of N-grams is to think of them as capturing "snapshots" of language patterns at different scales, allowing for more accurate predictions and analysis.
- To avoid overfitting when using N-grams, try using cross-validation techniques such as k-fold or leave-one-out validation to evaluate the performance of the model on different samples of data.