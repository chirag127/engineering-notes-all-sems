Part-of-Speech Tagging is the process of marking up a word in a text as corresponding to a particular part of speech, based on both its definition and its context . The most common parts of speech are noun, verb, adjective, adverb, pronoun, preposition, and conjunction . There are also a few less common ones, such as interjection and article.

The basic architecture of a Part-of-Speech Tagging system consists of three main components :

- A **tokenizer** that splits the input text into tokens (words, punctuation, etc.)
- A **tagger** that assigns a part of speech tag to each token based on a set of rules or a statistical model
- A **tag dictionary** that stores the possible tags for each token and their probabilities

The following diagram illustrates the basic architecture of a Part-of-Speech Tagging system using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Tokenizer    | --> |     Tagger      | --> |  Tag Dictionary |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```