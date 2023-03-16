### Transformation-based tagging

- Transformation-based tagging is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text.  
- It is also called Brill tagging, after its inventor Eric Brill.  
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that learns a series of transformation rules from data.   
- The basic idea of transformation-based tagging is to start with a simple baseline tagger, such as a unigram tagger, and then iteratively apply transformation rules that correct the errors made by the baseline tagger.  
- The transformation rules are learned from a tagged corpus using an error-driven learning algorithm, which selects the rule that reduces the most errors at each iteration.   
- The transformation rules have the form: change the tag of a word from X to Y if condition Z is met, where Z can be based on the surrounding words, tags, or other features.   
- For example, a possible transformation rule is: change the tag of a word from NN (singular noun) to NNS (plural noun) if the word ends with "s".  
- The advantage of transformation-based tagging is that it allows us to have linguistic knowledge in a readable form, and it can capture complex patterns that depend on multiple features.   
- The disadvantage of transformation-based tagging is that it can be slow to train and apply, and it can overfit the training data if the number of rules is too large.