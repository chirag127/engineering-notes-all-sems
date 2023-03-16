# Detecting and Correcting Spelling Errors

- Spelling errors are a common source of noise and ambiguity in natural language processing (NLP) and information retrieval (IR) tasks.
- Spelling errors can be classified into two types: non-word errors and real-word errors.
- Non-word errors are those that result in a word that does not exist in the language, such as *teh* for *the* or *recieve* for *receive*.
- Real-word errors are those that result in a word that exists in the language, but is not the intended one, such as *form* for *from* or *their* for *there*.
- Non-word errors can be detected by checking the word against a predefined lexicon or dictionary, and corrected by using edit distance, n-gram models, or deep learning methods.
- Real-word errors are more difficult to detect and correct, as they require semantic and contextual information to identify the intended word. Some methods for real-word error correction are:
  - Statistical methods, such as the noisy channel model proposed by Mays, Damerau and Mercer, which uses a language model and an error model to estimate the probability of a word given its context and the error type.
  - Rule-based methods, such as the one proposed by Hirst and Budanitsky, which uses a set of linguistic rules and a thesaurus to identify and correct confusable words.
  - Hybrid methods, such as the one proposed by Alotaibi and Alharbi, which combines the noisy channel model with a rule-based method to improve the accuracy and coverage of real-word error correction.
  - Deep learning methods, such as the one proposed by Awasthi et al., which uses a pre-trained contextual language model (BERT) to generate and rank candidate corrections based on the similarity and coherence with the context.

: Hirst, G., & Budanitsky, A. (2005). Correcting real-word spelling errors by restoring lexical cohesion. Natural Language Engineering, 11(1), 87-111.

: Alotaibi, M., & Alharbi, A. (2023). Correcting Real-Word Spelling Errors: A New Hybrid Approach. arXiv preprint arXiv:2302.06407.

: Awasthi, A., Gupta, A., & Mathur, P. (2021). Misspelling Correction with Pre-trained Contextual Language Model. arXiv preprint arXiv:2101.03204.