### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text .
- It is also called Brill tagging, after its inventor Eric Brill .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns from a set of examples and a set of transformation rules .
- The basic idea of transformation-based tagging is to start with a baseline tagger that assigns a default tag to each word, and then iteratively apply transformation rules that correct the errors made by the baseline tagger .
- The transformation rules are of the form: change the tag of a word from X to Y if condition Z is met, where Z can be based on the word itself, its context, or its features .
- The transformation rules are learned from a training corpus by finding the rule that reduces the most errors at each iteration .
- The order of the rules is important, as each rule may affect the applicability of the subsequent rules .
- The advantages of transformation-based tagging are that it allows us to have linguistic knowledge in a readable form, it can handle unknown words by using contextual information, and it can achieve high accuracy with a relatively small number of rules  .
- The disadvantages of transformation-based tagging are that it is computationally expensive, it may overfit the training data, and it may produce inconsistent results depending on the order of the rules .