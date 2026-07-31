# Tokenization

- Tokenization is the process of breaking down a piece of text into small units called tokens.
- A token may be a word, part of a word or just characters like punctuation.
- Tokenization is the first step in any natural language processing (NLP) pipeline.
- Tokenization is used in NLP to split paragraphs and sentences into smaller units that can be more easily assigned meaning.
- Tokenization is useful for a number of tasks in NLP, including sentiment analysis, topic modeling, and machine translation.
- One of the main advantages of tokenization is that it can help to improve the accuracy of these tasks by providing more context for each word.
- The token occurrences in a document can be used directly as a vector representing that document.

## Types of Tokenization

- There are different types of tokenization, depending on the level of granularity and the language of the text.
- Some of the common types of tokenization are:

  - **Word Tokenization**: This is the most basic type of tokenization, where the text is split into words based on whitespace and punctuation. For example, the sentence "Hello, world!" would be tokenized into two tokens: "Hello" and "world".
  - **Sentence Tokenization**: This is the type of tokenization where the text is split into sentences based on punctuation and capitalization. For example, the paragraph "Hello, world! This is a test." would be tokenized into two tokens: "Hello, world!" and "This is a test.".
  - **Subword Tokenization**: This is the type of tokenization where the text is split into smaller units than words, such as syllables, morphemes, or n-grams. For example, the word "tokenization" could be tokenized into four tokens: "tok", "en", "iz", and "ation".
  - **Character Tokenization**: This is the type of tokenization where the text is split into individual characters. For example, the word "tokenization" would be tokenized into 12 tokens: "t", "o", "k", "e", "n", "i", "z", "a", "t", "i", "o", and "n".

## Challenges of Tokenization

- Tokenization is a crucial step in many NLP tasks, but it is also a difficult one, because every language has its own grammatical constructs, which are often difficult to write down as rules.
- Some of the challenges of tokenization are:

  - **Ambiguity**: Some words or punctuation marks can have multiple meanings or functions, depending on the context. For example, the word "can" can be a noun, a verb, or a modal auxiliary. The dot (.) can be a period, a decimal point, or an ellipsis.
  - **Contractions**: Some words are formed by combining two or more words, such as "don't", "I'm", or "we'll". These words need to be split into their original components, such as "do not", "I am", or "we will".
  - **Abbreviations**: Some words are shortened forms of longer words, such as "Mr.", "Dr.", or "U.S.A.". These words need to be treated as single tokens, and not split into their constituent letters.
  - **Non-standard Words**: Some words are not part of the standard vocabulary of a language, such as slang, jargon, or foreign words. These words need to be recognized and handled appropriately, depending on the task and the domain.
  - **Multi-word Expressions**: Some words are composed of more than one word, but have a single meaning, such as "New York", "hot dog", or "red herring". These words need to be treated as single tokens, and not split into their individual words.

## Examples of Tokenization

- Here are some examples of tokenization using different types and languages:

  - Word Tokenization (English): "The quick brown fox jumps over the lazy dog." -> ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "."]
  - Sentence Tokenization (English): "Hello, world! This is a test." -> ["Hello, world!", "This is