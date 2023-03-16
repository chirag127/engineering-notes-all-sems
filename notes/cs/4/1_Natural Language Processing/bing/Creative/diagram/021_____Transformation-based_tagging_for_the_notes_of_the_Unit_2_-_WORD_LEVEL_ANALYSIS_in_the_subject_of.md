### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill.
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple initial tagging of the text, and then iteratively apply a set of rules that correct the errors in the tagging.
- The initial tagging can be based on the most frequent tag for each word, or a default tag (such as noun) for unknown words.
- The rules are learned from a tagged corpus, by finding the rule that reduces the most errors in each iteration.
- The rules are of the form: change tag a to tag b when condition c is met.
- For example, a rule could be: change tag NN (noun) to VB (verb) when the previous word is TO (to).
- The rules are ordered by the order of learning, and applied sequentially to the text.
- The advantages of transformation-based tagging are that it is fast, simple, and interpretable.
- The disadvantages are that it requires a large tagged corpus for learning, and that it may overfit the training data or miss some generalizations.