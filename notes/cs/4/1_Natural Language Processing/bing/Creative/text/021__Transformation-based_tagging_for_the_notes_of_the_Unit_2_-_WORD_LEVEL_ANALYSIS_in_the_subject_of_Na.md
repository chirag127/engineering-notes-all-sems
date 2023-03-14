### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of part-of-speech (POS) to the given text  .
- It is also called Brill tagging, after its inventor Eric Brill.
- It is a form of supervised learning, which aims to minimize error by using annotated training data.
- It is a transformation-based process, in the sense that a tag is assigned to each word and changed using a set of predefined rules.
- The general idea is very simple: guess the tag of each word, then go back and fix the mistakes.
- The algorithm starts with initialization, which is the assignment of tags based on their probability for each word (for example, "dog" is more often a noun than a verb).
- Then "patches" are determined via rules that correct (probable) tagging errors made in the initialization phase.
- The rules are of the general form: tag1 → tag2 IF Condition, where the Condition tests the preceding and/or following word tokens, or their tags.
- The rules are applied iteratively, until a threshold is reached, or no more rules can apply.
- This approach ensures that valuable information such as the morphosyntactic construction of words is employed in an automatic tagging process.
- Transformation-based tagging has the advantages of being fast, accurate, and interpretable.
- It also has the disadvantages of being dependent on the quality of the initial tagger, the rule ordering, and the rule coverage.
- Transformation-based tagging can also be applied at a higher level of textual interpretation for locating chunks in the tagged text, such as non-recursive "baseNP" chunks.