Transformation-based tagging is a method of part-of-speech tagging that uses a set of rules to correct the initial tags assigned by a baseline tagger. The baseline tagger can be a simple rule-based tagger or a probabilistic tagger that assigns the most frequent tag for each word. The rules are learned from a tagged corpus by finding the most common errors and the best corrections for them. The rules are applied iteratively until no more errors can be corrected or a predefined limit is reached.

The following diagram illustrates the basic architecture of a transformation-based tagger:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Tagged corpus  |     |  Baseline tagger|     |  Rule learner   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +---------------------->|                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               |                       |
                               +---------------------->|                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       |                       |
                                                       +---------------------->|
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |
                                                                               |