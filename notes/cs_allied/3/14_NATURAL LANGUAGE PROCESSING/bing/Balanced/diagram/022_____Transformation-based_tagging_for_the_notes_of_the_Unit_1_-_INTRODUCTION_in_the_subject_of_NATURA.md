### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple initial tagging of the text, and then iteratively apply a set of rules that correct the errors in the tagging .
- The rules are learned from a training corpus, where each rule has a trigger and an action. The trigger specifies a condition that must be met for the rule to apply, and the action specifies how to change the tag of a word .
- For example, a rule could be: if the current word is "to" and the next word is tagged as a verb, then change the tag of the current word to "TO" (preposition or infinitive marker) .
- The rules are ordered by their accuracy, and applied in sequence until no more rules can be applied or a predefined limit is reached .
- Transformation-based tagging has the advantage of being fast, simple, and interpretable. It also allows for incorporating linguistic knowledge in a readable form .
- However, it also has some limitations, such as relying on the quality of the initial tagging, being sensitive to the order of the rules, and having difficulty with long-distance dependencies and rare cases .