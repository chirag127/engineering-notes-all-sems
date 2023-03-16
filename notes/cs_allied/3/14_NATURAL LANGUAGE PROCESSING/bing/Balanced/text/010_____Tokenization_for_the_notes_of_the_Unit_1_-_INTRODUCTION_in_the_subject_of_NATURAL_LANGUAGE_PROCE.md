### Tokenization

- Tokenization is the process of breaking down a piece of text into small units called tokens.
- A token may be a word, part of a word or just characters like punctuation.
- Tokenization is the first step in any natural language processing (NLP) pipeline.
- Tokenization is used in NLP to split paragraphs and sentences into smaller units that can be more easily assigned meaning.
- Tokenization is useful for a number of tasks in NLP, including sentiment analysis, topic modeling, and machine translation.
- One of the main advantages of tokenization is that it can help to improve the accuracy of these tasks by providing more context for each word.
- The token occurrences in a document can be used directly as a vector representing that document.

### Types of Tokenization

- There are different types of tokenization depending on the level of granularity and the language of the text.
- Some of the common types of tokenization are:

  - **Word Tokenization**: This is the most basic type of tokenization, where the text is split into words based on whitespace and punctuation. For example, the sentence "Hello, world!" would be tokenized into two tokens: "Hello" and "world".
  - **Sentence Tokenization**: This is the type of tokenization where the text is split into sentences based on punctuation and capitalization. For example, the paragraph "Hi. How are you? I'm fine." would be tokenized into three sentences: "Hi.", "How are you?" and "I'm fine.".
  - **Subword Tokenization**: This is the type of tokenization where the text is split into smaller units than words, such as syllables, morphemes, or n-grams. For example, the word "tokenization" could be tokenized into four subwords: "tok", "en", "iz", and "ation".
  - **Character Tokenization**: This is the type of tokenization where the text is split into individual characters. For example, the word "hello" would be tokenized into five characters: "h", "e", "l", "l", and "o".

### Challenges of Tokenization

- Tokenization is a crucial step in many NLP tasks, but it is also a difficult one, because every language has its own grammatical constructs, which are often difficult to write down as rules.
- Some of the challenges of tokenization are:

  - **Ambiguity**: Sometimes, the same text can be tokenized in different ways depending on the context or the intended meaning. For example, the sentence "She saw a man on a hill with a telescope." can be tokenized into different phrases depending on who has the telescope and where they are located.
  - **Contractions**: Some languages, such as English, have contractions, where two words are combined into one with an apostrophe. For example, "don't" is a contraction of "do not". Tokenizing contractions can be tricky, because sometimes they should be split into two tokens, and sometimes they should be kept as one token depending on the task.
  - **Multiword Expressions**: Some languages, such as Chinese, have multiword expressions, where a group of words form a single unit of meaning. For example, "红烧肉" (red braised pork) is a multiword expression in Chinese. Tokenizing multiword expressions can be challenging, because sometimes they should be treated as one token, and sometimes they should be split into multiple tokens depending on the task.
  - **Non-standard Text**: Some texts, such as social media posts, emails, or chats, may contain non-standard spelling, grammar, or punctuation. For example, "lol" is a non-standard abbreviation for "laugh out loud". Tokenizing non-standard text can be difficult, because sometimes they should be normalized, and sometimes they should be preserved depending on the task.

### Examples of Tokenization

- Here are some examples of tokenization using different types and languages:

  - Word Tokenization (English): "I love NLP." -> ["I", "love", "NLP", "."]
  - Sentence Tokenization (English): "Hello. How are you?" -> ["Hello.", "How are you?"]
  - Subword Tokenization (English): "