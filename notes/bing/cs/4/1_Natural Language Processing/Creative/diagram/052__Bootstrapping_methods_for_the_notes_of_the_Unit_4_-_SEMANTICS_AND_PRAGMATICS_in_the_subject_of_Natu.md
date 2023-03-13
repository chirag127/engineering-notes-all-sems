Bootstrapping methods are a class of techniques that use a small amount of labeled data and a large amount of unlabeled data to learn a mapping from input to output in natural language processing. They typically follow a general format of:

1. Start with an empty list of things (such as words, phrases, relations, etc.).
2. Initialize this list with carefully chosen seeds (such as manually annotated examples, heuristics, rules, etc.).
3. Leverage the things in the list to find more things from the unlabeled data (such as using patterns, classifiers, similarity measures, etc.).
4. Add the new things to the list and repeat step 3 until a stopping criterion is met (such as a fixed number of iterations, a threshold on confidence, a convergence measure, etc.).

The following diagram illustrates the basic architecture of a bootstrapping method for natural language processing using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Labeled data   |     |  Unlabeled data |     |  Labeled data   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       ^
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Seed list      |---->|  Learner        |---->|  New list       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```