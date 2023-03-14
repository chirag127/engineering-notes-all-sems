### Tokenization for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Tokenization is the process of breaking down a text into smaller units called tokens    .
- Tokens are usually words or punctuation marks, but they can also be parts of words or characters   .
- Tokenization is a crucial step in many NLP tasks, such as part-of-speech tagging, text classification, sentiment analysis, topic modeling, and machine translation  .
- Tokenization can help to improve the accuracy of these tasks by providing more context for each word.
- Tokenization can be done at different levels, such as sentence level or word level .
- Sentence level tokenization splits the text into sentences, while word level tokenization splits the text into words .
- There are different methods and libraries available to perform tokenization, such as NLTK, Gensim, Keras, etc .
- There are various tokenization techniques available, which can be applicable based on the language and purpose of modeling.
- Some of the tokenization techniques are:
  - White space tokenization: This is the simplest tokenization technique, which splits the text into words by using white space as a separator. This is the fastest tokenization technique, but it only works for languages that use white space to separate words, such as English.
  - Dictionary based tokenization: This is a more advanced technique, which splits the text into words by using a predefined dictionary of tokens. If the token is not found in the dictionary, then special rules are used to tokenize it. This technique can handle more complex languages and cases, such as abbreviations, contractions, compound words, etc.
  - Rule based tokenization: This is a technique that uses a set of rules to split the text into tokens. The rules can be based on regular expressions, grammar, syntax, etc. This technique can be customized for specific problems and domains, such as dates, numbers, email addresses, etc.
  - Subword tokenization: This is a technique that splits the text into smaller units than words, such as syllables, morphemes, or n-grams . This technique can help to deal with rare words, out-of-vocabulary words, and morphologically rich languages, such as German, Turkish, or Arabic .

- A possible mnemonic to remember the tokenization techniques is: **WDRS** (White space, Dictionary, Rule, Subword).
- A possible learning trick to understand the tokenization process is to use online tools or libraries to tokenize some sample texts and compare the results of different techniques. For example, one can use the NLTK library in Python to perform different types of tokenization and see the output. Here is a sample code snippet:

```python
# Import the NLTK library
import nltk

# Define a sample text
text = "I'm going to buy a new iPhone 14 today."

# Perform white space tokenization
white_space_tokens = text.split()
print("White space tokens:", white_space_tokens)

# Perform dictionary based tokenization using NLTK's word_tokenize function
dictionary_tokens = nltk.word_tokenize(text)
print("Dictionary tokens:", dictionary_tokens)

# Perform rule based tokenization using NLTK's regexp_tokenize function
rule_tokens = nltk.regexp_tokenize(text, pattern='\w+|\$[\d\.]+|\S+')
print("Rule tokens:", rule_tokens)

# Perform subword tokenization using NLTK's TweetTokenizer function
subword_tokenizer = nltk.TweetTokenizer()
subword_tokens = subword_tokenizer.tokenize(text)
print("Subword tokens:", subword_tokens)
```

The output of the code is:

```
White space tokens: ["I'm", 'going', 'to', 'buy', 'a', 'new', 'iPhone', '14', 'today.']
Dictionary tokens: ['I', "'m", 'going', 'to', 'buy', 'a', 'new', 'iPhone', '14', 'today', '.']
Rule tokens: ['I', "'m", 'going', 'to