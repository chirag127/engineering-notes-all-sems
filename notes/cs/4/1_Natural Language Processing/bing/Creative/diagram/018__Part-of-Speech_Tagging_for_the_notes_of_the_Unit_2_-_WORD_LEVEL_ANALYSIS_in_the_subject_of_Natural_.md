Part-of-speech tagging is the process of marking up a word in a text as corresponding to a particular part of speech, based on both its definition and its context. For example, in the sentence "John likes the blue house at the end of the street", the word "likes" is tagged as a verb, the word "blue" is tagged as an adjective, and the word "house" is tagged as a noun.

There are different methods and algorithms for part-of-speech tagging, such as rule-based, stochastic, and neural network-based. A basic architecture of a part-of-speech tagger consists of the following components:

- A tokenizer, which splits the input text into tokens (words, punctuation, etc.).
- A lexicon, which contains a list of words and their possible parts of speech.
- A tagger, which assigns a part of speech to each token based on the lexicon and some rules or probabilities.
- A post-processor, which corrects or modifies the tags based on the context and some heuristics.

The following diagram illustrates the basic architecture of a part-of-speech tagger using ASCII art:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|    Tokenizer   | --> |     Lexicon    | --> |     Tagger     | --> | Post-processor |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```