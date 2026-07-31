# Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple and general tagger, such as assigning the most frequent tag to each word, and then apply a series of rules that correct the errors made by the initial tagger .
- The rules are learned from a tagged corpus, using an error-driven algorithm that iteratively finds the rule that reduces the most errors on the training data .
- The rules are of the form: change the tag of the current word from X to Y, if condition Z is met .
- The condition Z can be based on the word itself, its surrounding words, its previous or following tags, or any combination of these features .
- The rules are applied in a fixed order, and each rule can override the previous ones .
- The advantages of transformation-based tagging are that it is fast, simple, and interpretable, and that it can incorporate linguistic knowledge in a readable form   .
- The disadvantages of transformation-based tagging are that it is sensitive to the order of the rules, that it can overfit the training data, and that it can be hard to generalize to new domains or languages .