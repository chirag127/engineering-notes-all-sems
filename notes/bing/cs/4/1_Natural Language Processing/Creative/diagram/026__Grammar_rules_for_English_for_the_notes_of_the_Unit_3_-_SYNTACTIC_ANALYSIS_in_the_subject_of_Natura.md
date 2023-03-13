### Grammar rules for English for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

The following diagram illustrates the basic architecture of a syntactic analyzer for English sentences, based on the grammar rules of the language :

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Tokenizer     | --> |  Part-of-Speech| --> |  Syntactic     |
|                |     |  Tagger        |     |  Parser        |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The tokenizer splits the input sentence into individual words or tokens, such as nouns, verbs, adjectives, etc.

The part-of-speech tagger assigns a grammatical category to each token, such as noun, verb, adjective, etc.

The syntactic parser analyzes the structure and meaning of the sentence, based on the grammar rules of the language, and produces a parse tree or a syntactic representation of the sentence.

Some of the grammar rules for English are  :

- A complete sentence must include a subject and a verb.
- The first word in a sentence must start with a capital letter.
- A subject and a verb must agree in number (singular or plural).
- A comma should be used to separate independent clauses joined by a conjunction or a semicolon.
- A singular subject needs a singular verb, and a plural subject needs a plural verb.
- An adjective modifies a noun, and an adverb modifies a verb, an adjective, or another adverb.
- A pronoun must agree in number, gender, and case with its antecedent (the noun it refers to).
- A noun phrase consists of a noun and its modifiers, such as articles, adjectives, or prepositional phrases.
- A verb phrase consists of a verb and its complements, such as objects, adverbs, or prepositional phrases.
- A clause is a group of words that contains a subject and a verb, and can be either independent or dependent.
- A sentence can be either simple, compound, complex, or compound-complex, depending on the number and type of clauses it contains.
- A modifier should be placed as close as possible to the word it modifies, to avoid ambiguity or confusion.