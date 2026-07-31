# Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill.
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple initial tagging and then iteratively apply correction rules that improve the accuracy of the tagging.
- The initial tagging can be based on the most frequent tag for each word, or a default tag (such as noun) for unknown words.
- The correction rules are learned from a tagged corpus, using an error-driven learning algorithm that selects the rule that reduces the most errors at each step.
- The correction rules are of the form: change the tag of a word from X to Y, if condition Z is met.
- The condition Z can be based on the word itself, its surrounding words, or their tags.
- For example, a rule could be: change the tag of a word from noun to verb, if the previous word is "to".
- The advantage of transformation-based tagging is that it allows us to have linguistic knowledge in a readable form, and it can handle unknown words and ambiguity by using contextual information .
- The disadvantage of transformation-based tagging is that it can be slow, as it requires applying many rules sequentially, and it can be sensitive to the order of the rules.
- Transformation-based tagging can also be applied to other levels of textual analysis, such as chunking, which is the task of identifying non-recursive phrases (such as noun phrases) in a text.