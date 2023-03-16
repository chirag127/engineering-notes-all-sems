# Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple initial tagging of the text, and then iteratively apply a set of rules that correct the errors in the tagging .
- The initial tagging can be based on the most frequent tag for each word, or a default tag (such as noun) for unknown words .
- The rules are learned from a tagged corpus, by finding the rule that reduces the most errors in each iteration .
- The rules are of the form: change the tag of the current word from X to Y, if condition Z is met .
- The condition Z can be based on the word itself, the previous or next word, the previous or next tag, or any combination of these features .
- For example, a rule could be: change the tag of the current word from noun to verb, if the previous word is "to" .
- The rules are applied in a fixed order, and the order can affect the accuracy of the tagging .
- The advantages of transformation-based tagging are that it is fast, simple, and interpretable .
- The disadvantages are that it can be sensitive to the order of the rules, and it can overfit the training data .
- Transformation-based tagging can also be applied to other natural language processing tasks, such as text chunking, named entity recognition, and semantic role labeling .