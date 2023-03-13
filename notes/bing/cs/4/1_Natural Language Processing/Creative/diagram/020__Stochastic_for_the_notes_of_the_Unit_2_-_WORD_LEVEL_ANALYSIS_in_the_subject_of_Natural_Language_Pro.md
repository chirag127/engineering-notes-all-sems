Stochastic is a term that refers to the use of probabilistic and statistical methods in natural language processing (NLP). Stochastic methods can help to deal with the ambiguity and complexity of natural language, especially when processing longer sentences with realistic grammars .

One example of a stochastic method in NLP is a stochastic grammar, which is a grammar framework that assigns probabilities to different grammatical structures or rules. A stochastic grammar can be used to model the likelihood of a sentence being grammatical or to generate sentences from a given language.

The following diagram illustrates the basic architecture of a stochastic grammar:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Grammar rules  |     |  Probability    |     |  Sentence       |
|  with symbols   |     |  distribution   |     |  generation     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Grammar rules  |     |  Probability    |     |  Sentence       |
|  with numbers   |     |  calculation    |     |  selection      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows how a stochastic grammar can generate sentences from a given language. The steps are:

- The grammar rules with symbols are assigned numerical probabilities based on some data or criteria.
- The probability distribution is calculated for each possible sentence that can be derived from the grammar rules.
- The sentence generation is done by selecting the most probable sentence or by sampling from the probability distribution.