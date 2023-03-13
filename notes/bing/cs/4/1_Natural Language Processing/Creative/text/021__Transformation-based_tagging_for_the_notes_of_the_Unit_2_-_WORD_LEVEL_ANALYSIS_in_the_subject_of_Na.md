### Transformation-based tagging

- Transformation-based tagging is a method of part-of-speech tagging that uses a set of rules to correct the errors made by a baseline tagger.
- A baseline tagger is a simple tagger that assigns the most frequent tag for each word in the training corpus, or a default tag for unknown words.
- A rule is a pair of a condition and an action, such as "if the current word is 'to' and the next word is tagged as a noun, change the tag of the current word to a preposition".
- The rules are learned automatically from the training data, by applying the baseline tagger and finding the most frequent errors that can be corrected by a single rule.
- The rules are applied iteratively, starting from the most general and reliable ones, until no more errors can be corrected or a predefined limit is reached.
- The rules are stored in a rule file, which can be used to tag new sentences by applying the baseline tagger and then the rules in order.
- Transformation-based tagging is also known as Brill tagging, after its inventor Eric Brill.
- Transformation-based tagging is a fast and simple method that can achieve high accuracy with a small number of rules.
- Transformation-based tagging can also handle unknown words and morphological variations by using contextual information and word classes.