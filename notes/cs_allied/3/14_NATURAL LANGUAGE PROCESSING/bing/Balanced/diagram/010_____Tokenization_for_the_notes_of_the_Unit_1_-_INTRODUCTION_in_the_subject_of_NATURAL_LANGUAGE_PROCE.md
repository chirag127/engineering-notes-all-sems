### Tokenization

- Tokenization is the process of breaking down a piece of text into small units called tokens.
- A token may be a word, part of a word or just characters like punctuation.
- Tokenization is the first step in any NLP pipeline. It has an important effect on the rest of your pipeline.
- A tokenizer breaks unstructured data and natural language text into chunks of information that can be considered as discrete elements.
- The token occurrences in a document can be used directly as a vector representing that document.
- Tokenization is useful for a number of tasks in natural language processing, including sentiment analysis, topic modeling, and machine translation.
- One of the main advantages of tokenization is that it can help to improve the accuracy of these tasks by providing more context for each word.

#### Types of Tokenization

- There are different types of tokenization, depending on the level of granularity and the language of the text.
- Some common types of tokenization are:

  - **Word Tokenization**: This is the most basic type of tokenization, where the text is split into words based on whitespace and punctuation. For example, the sentence "I love NLP." would be tokenized into ["I", "love", "NLP", "."].
  - **Subword Tokenization**: This is a type of tokenization where the words are further split into smaller units based on some criteria, such as frequency or morphology. For example, the word "tokenization" could be split into ["token", "iz", "ation"] or ["tok", "en", "iz", "at", "ion"].
  - **Character Tokenization**: This is a type of tokenization where the text is split into individual characters. For example, the word "token" would be split into ["t", "o", "k", "e", "n"].
  - **Sentence Tokenization**: This is a type of tokenization where the text is split into sentences based on punctuation and other cues. For example, the paragraph "Hello. How are you? I am fine." would be split into ["Hello.", "How are you?", "I am fine."].

#### Challenges of Tokenization

- Tokenization is a crucial step in many NLP tasks, but it is not a trivial one. There are many challenges and complexities involved in tokenizing natural language text, such as:

  - **Language Variation**: Different languages have different rules and conventions for word formation and sentence structure. For example, some languages, such as Chinese and Japanese, do not use whitespace to separate words, while some languages, such as German and Turkish, have long compound words that may need to be split. Therefore, a tokenizer needs to be aware of the language and its characteristics to perform tokenization correctly.
  - **Ambiguity**: Sometimes, the same piece of text can be tokenized in different ways, depending on the context and the intended meaning. For example, the word "can" can be a noun, a verb, or a modal auxiliary, and the punctuation mark "." can be a period, a decimal point, or an abbreviation marker. Therefore, a tokenizer needs to resolve the ambiguity and choose the most appropriate tokenization for the given text.
  - **Noise**: Sometimes, the text may contain errors, typos, slang, emoticons, or other non-standard forms that may affect the tokenization process. For example, the text "lol, ur so funny :)" may not be easily tokenized by a standard word tokenizer. Therefore, a tokenizer needs to handle the noise and normalize the text before tokenizing it.

#### Examples of Tokenization

- Here are some examples of tokenization using different types of tokenizers and different languages:

  - Word Tokenization:

    - English: "I love NLP." -> ["I", "love", "NLP", "."]
    - French: "Je t'aime." -> ["Je", "t'", "aime", "."]
    - Hindi: "मुझे नलप पसंद है।" -> ["मुझे", "नलप", "पसंद", "है", "।"]

  - Subword Tokenization:

    - English