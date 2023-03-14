Shallow parsing, also known as chunking or light parsing, is an analysis of a sentence that identifies and groups its constituent parts into higher-level units that have discrete grammatical meanings, such as noun phrases, verb phrases, prepositional phrases, etc.  It is a technique widely used in natural language processing, especially for tasks that do not require full syntactic analysis, such as information extraction, named entity recognition, sentiment analysis, etc. 

Shallow parsing can be seen as a simplified version of deep parsing, which aims to produce a complete and detailed representation of the syntactic structure of a sentence, such as a parse tree or a dependency graph. Deep parsing is more computationally intensive and requires more linguistic knowledge and resources than shallow parsing.  

A basic architecture of a shallow parser consists of the following components:

- A tokenizer that splits the input text into tokens, such as words, punctuation marks, etc.
- A part-of-speech (POS) tagger that assigns a POS tag to each token, such as noun, verb, adjective, etc.
- A chunker that applies rules or machine learning models to identify and label the chunks in the sentence, such as NP for noun phrase, VP for verb phrase, PP for prepositional phrase, etc.
- An optional post-processor that modifies or refines the chunk labels based on some criteria, such as semantic consistency, syntactic agreement, etc.

The following diagram illustrates the basic architecture of a shallow parser using ASCII art:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|    Tokenizer   | --> |  POS Tagger   | --> |    Chunker     | --> | Post-Processor |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```

An example of the input and output of a shallow parser is given below:

Input: He reckons the current account deficit will narrow to only # 1.8 billion in September.

Output: [NP He ] [VP reckons ] [NP the current account deficit ] [VP will narrow ] [PP to ] [NP only # 1.8 billion ] [PP in ] [NP September ].