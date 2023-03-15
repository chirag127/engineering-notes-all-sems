 Here is the content in markdown format for the topic - ### Dependency Grammar for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing:

### Dependency Grammar

- Dependency Grammar is a syntactic theory that considers syntactic structure in terms of relations between words (rather than constituents).
- In Dependency Grammar, each word in a sentence depends directly on another word, its head. The head determines the syntactic behavior of the dependent.
- The main benefits of dependency grammar are:
  - It avoids problems of constituency (what constitutes a phrase).
  - It reflects intuitive relationships between words.
  - It can yield simpler parsers.
- Some key concepts in dependency grammar are:
  - The relation between a head and its dependent is called a dependency.
  - The head of a dependency is the governor; the dependent is the subordinate.
  - Dependencies are directed; they have a head and a dependent.
- Example: The boy hit the ball.

![Dependency Grammar Example](https://www.aclweb.org/anthology/2020.bea-1.12/figures/bea-fig1.png)

- Advantages: Better reflects semantic relationships. Can avoid constituency problems. Simpler to learn and apply.
- Disadvantages: Loss of constituency information. Difficult to relate to phrase structure grammars.
- Applications: Shallow and broad-coverage parsing. Machine translation. Sentiment analysis. Automatic summarization.

- Mnemonics/Learning Tricks:
-- "Arrow points to the head" - The arrow in a dependency points from the dependent to the head.
-- " governor governs subordinate" - The head (governor) determines the behavior of the dependent (subordinate).