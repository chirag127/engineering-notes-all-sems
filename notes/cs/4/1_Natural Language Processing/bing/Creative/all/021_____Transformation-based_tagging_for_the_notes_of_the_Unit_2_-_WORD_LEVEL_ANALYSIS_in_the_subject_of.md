# Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text.
- It is also called Brill tagging, after its inventor Eric Brill .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that transforms one state to another state by using transformation rules  .
- The basic idea of transformation-based tagging is to start with a simple baseline tagger, such as assigning the most frequent tag to each word, and then apply a series of rules that correct the errors made by the baseline tagger  .
- The rules are learned from a tagged corpus, using an error-driven algorithm that iteratively selects the rule that reduces the most errors on the training data  .
- The rules are of the form: change the tag of a word from X to Y, if condition Z is met. For example, change the tag of a word from noun to verb, if the previous word is "to"  .
- The rules are ordered by their priority, and applied sequentially to the text. The order of the rules is determined by the order of their discovery, or by their accuracy  .
- Transformation-based tagging has the advantages of being fast, simple, and interpretable. It also allows for incorporating linguistic knowledge in a readable form   .
- Transformation-based tagging has the disadvantages of being dependent on the quality of the baseline tagger, the size and representativeness of the training data, and the complexity and coverage of the rules  .
- Transformation-based tagging can be applied to other tasks besides POS tagging, such as text chunking, named entity recognition, and semantic role labeling  .