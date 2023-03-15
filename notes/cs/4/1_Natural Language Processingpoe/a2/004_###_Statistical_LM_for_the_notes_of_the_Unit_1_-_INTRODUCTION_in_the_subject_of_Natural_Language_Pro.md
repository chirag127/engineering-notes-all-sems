 Here is the content in markdown format for the topic ### Statistical LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing:

### Statistical LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Statistical Language Models (SLM) compute the probability of a sequence of words. They are trained on a large corpus of text data.
- Some commonly used SLMs are:
	- Unigram model: Probability of a word only depends on the previous word. P(w|w_-1)
	- Bigram model: Probability of a word depends on the previous 2 words. P(w|w_-2, w_-1)
	- Trigram model: Probability of a word depends on the previous 3 words. P(w|w_-3, w_-2, w_-1)
	- N-gram model: Probability of a word depends on the previous N words.
- Higher order N-gram models (like Trigram and higher) lead to better results but have data sparsity issues as the number of parameters to estimate increases exponentially.
- Good Memory Mnemonic: The more 'Grams' the better the 'Jam' (probability estimates).
- Smoothing techniques are used to tackle data sparsity like:
	- Add-one smoothing: Replace zeros with 1.
	- Linear interpolation: Interpolate with lower-order models.
	- Kneser-Ney smoothing: More suitable for higher-order N-grams.
- Applications of SLMs: Speech recognition, Machine translation, Spell checkers, Predictive text, etc.
- Advantages: Simple to implement and train. Capture local contextual information.
- Disadvantages: Do not capture long-range dependencies. Suffer from data sparsity for higher orders.

[Detailed diagrams and code snippets can be added here if required to explain the concepts better.]