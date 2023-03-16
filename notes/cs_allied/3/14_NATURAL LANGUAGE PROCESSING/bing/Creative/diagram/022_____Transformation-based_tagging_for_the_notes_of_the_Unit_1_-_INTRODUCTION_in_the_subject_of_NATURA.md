### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from examples and transforms one state to another state by using transformation rules .
- The basic idea of transformation-based tagging is to start with a simple and general tagging method, such as assigning the most frequent tag to each word, and then apply a series of rules that correct the errors in the initial tagging .
- The rules are learned from a tagged corpus, using an error-driven approach that iteratively finds the rule that reduces the most errors in the current tagging .
- The rules are of the form: change tag a to tag b when condition c is met, where condition c can be based on the word itself, the surrounding words, or the surrounding tags .
- The rules are applied in a fixed order, and each rule can only change one tag at a time .
- The advantages of transformation-based tagging are that it is fast, simple, and interpretable, and that it can incorporate linguistic knowledge in a readable form   .
- The disadvantages of transformation-based tagging are that it is sensitive to the order of the rules, that it can only correct one error at a time, and that it may overfit the training data .