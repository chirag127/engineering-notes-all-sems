### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Bootstrapping methods are a type of semi-supervised learning techniques that use a small set of labeled examples (seeds) and a large set of unlabeled examples to learn a mapping from input to output.
- Bootstrapping methods aim to enlarge the labeled set by iteratively selecting the most appropriate unlabeled examples and assigning them labels based on some criteria.
- Bootstrapping methods can be applied to various natural language processing tasks, such as relation extraction, semantic categorization, named entity recognition, information extraction, and subjectivity detection.
- Bootstrapping methods typically follow a general format:
  - Start with an empty list of things.
  - Initialize this list with carefully chosen seeds.
  - Repeat until a stopping criterion is met:
    - Use the current list to find new candidates from the unlabeled set.
    - Filter and rank the candidates based on some measure of confidence or similarity.
    - Add the best candidates to the list and assign them labels.
- Bootstrapping methods can be classified into different types based on the query strategy, the filtering and ranking criteria, and the stopping criterion.
- Some examples of bootstrapping methods are:
  - Snowball: a relation extraction method that uses extraction patterns to find new instances of a relation from the unlabeled set.
  - Basilisk: a semantic categorization method that uses selectional preferences to find new words that belong to a semantic category.
  - Nomen: a semantic categorization and named entity recognition method that uses morphological and syntactic features to find new words that belong to a semantic category or a named entity type .
  - AutoSlog-TS and SubSlog: subjectivity detection methods that use extraction patterns to find new subjective expressions from the unlabeled set .

- Some advantages of bootstrapping methods are:
  - They can reduce the cost and effort of manual annotation.
  - They can leverage the abundance of unlabeled data.
  - They can discover new knowledge that is not present in the seeds.
- Some disadvantages of bootstrapping methods are:
  - They can suffer from semantic drift, which is the loss of accuracy and consistency over iterations due to the propagation of errors or noise.
  - They can be sensitive to the choice of seeds, which can affect the coverage and diversity of the results.
  - They can be limited by the quality and quantity of the unlabeled data, which can affect the recall and precision of the results.

- Some mnemonics and learning tricks for bootstrapping methods are:
  - Remember the general format of bootstrapping methods as SLURP: Start with seeds, Loop until done, Use list to find candidates, Rank and filter candidates, Pick and label the best ones.
  - Remember the types of bootstrapping methods as RFS: Relation extraction, semantic categorization, and Subjectivity detection.
  - Remember the examples of bootstrapping methods as SNABS: Snowball, Nomen, AutoSlog-TS, Basilisk, and SubSlog.