### Tokenization

Tokenization is the process of breaking down the given text in natural language processing into the smallest unit in a sentence called a token. Punctuation marks, words, and numbers can be considered tokens. Tokenization helps in understanding the context or developing the model for the NLP. 

Some of the reasons why we need tokenization are:

- To reduce the dimensionality of the feature space by removing irrelevant or redundant words.
- To normalize the text by converting it to a standard format that can be easily processed by the NLP algorithms.
- To extract meaningful information from the text by identifying the keywords, phrases, entities, etc.
- To perform further analysis on the text such as stemming, lemmatization, part-of-speech tagging, etc.

There are different methods and libraries available to perform tokenization. NLTK, Gensim, Keras are some of the libraries that can be used to accomplish the task. Tokenization can be done to either separate words or sentences. If the text is split into words using some separation technique it is called word tokenization and same separation done for sentences is called sentence tokenization.

There are various tokenization techniques available which can be applicable based on the language and purpose of modeling. Below are a few of the tokenization techniques used in NLP:

- White Space Tokenization: This is the simplest tokenization technique. Given a sentence or paragraph it tokenizes into words by splitting the input whenever a white space in encountered. This is the fastest tokenization technique but will work for languages in which the white space breaks apart the sentence into meaningful words. Example: English.
- Dictionary Based Tokenization: In this method the tokens are found based on the tokens already existing in the dictionary. If the token is not found, then special rules are used to tokenize it. It is an advanced technique compared to whitespace tokenizer.
- Rule Based Tokenization: In this technique a set of rules are created for the specific problem. These rules can be based on regular expressions, grammar, syntax, etc. This technique can handle complex cases such as abbreviations, contractions, hyphenated words, etc. Example: English, French, German.
- Subword Tokenization: In this technique the tokens are not necessarily words, but smaller units that can be combined to form words. This technique is useful for languages that have a large vocabulary or are morphologically rich. Example: Chinese, Japanese, Turkish. Some of the subword tokenization methods are:
  - Byte Pair Encoding (BPE): This method starts with a set of characters as tokens and iteratively merges the most frequent pair of tokens to form a new token. This way it creates a vocabulary of subword tokens that can represent any word in the text.
  - WordPiece: This method is similar to BPE, but instead of merging the most frequent pair of tokens, it merges the pair of tokens that maximizes the likelihood of the text given the vocabulary. This way it creates a more optimal vocabulary of subword tokens.
  - Unigram Language Model: This method starts with a large vocabulary of subword tokens and iteratively removes the tokens that have the lowest probability of occurring in the text. This way it creates a smaller and more efficient vocabulary of subword tokens.