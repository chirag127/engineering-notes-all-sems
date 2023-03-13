Word similarity is the task of measuring how similar two words are in terms of their meaning, usage, or association. There are two main methods for word similarity: thesaurus-based and distributional.

Thesaurus-based methods use a structured lexical resource, such as WordNet, to find synonyms, antonyms, hypernyms, hyponyms, and other semantic relations between words. These methods rely on human knowledge and expertise to create and maintain the thesaurus. They can capture fine-grained semantic distinctions and word senses, but they may suffer from incompleteness, ambiguity, and subjectivity.

Distributional methods use large corpora of text to find words that co-occur frequently or share similar contexts. These methods rely on the distributional hypothesis, which states that words that occur in similar contexts tend to have similar meanings. They can capture general semantic similarity and word usage, but they may ignore syntactic and pragmatic information and word senses.

The following diagram illustrates the basic architecture of a word similarity system using thesaurus and distributional methods:

```
+-----------------+     +-----------------+
|                 |     |                 |
|   Thesaurus     |     |   Corpus        |
|                 |     |                 |
+-----------------+     +-----------------+
        |                       |
        |                       |
        v                       v
+-----------------+     +-----------------+
|                 |     |                 |
| Thesaurus-based |     | Distributional  |
| similarity      |     | similarity      |
| measure         |     | measure         |
|                 |     |                 |
+-----------------+     +-----------------+
        |                       |
        |                       |
        +----------+------------+
                   |
                   v
           +-----------------+
           |                 |
           | Word similarity |
           | score           |
           |                 |
           +-----------------+
```