### Transformation-based tagging for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Transformation-based tagging, also known as Brill tagging, is a rule-based algorithm for automatic tagging of parts of speech (POS) to the given text  .
- It is an instance of transformation-based learning (TBL), which is a machine learning paradigm that transforms one state to another state by using transformation rules  .
- The basic idea of TBL is to start with a simple initial state, such as assigning the most frequent tag to each word, and then apply a series of rules that correct the errors in the previous state .
- The rules are learned from a tagged corpus by finding the rule that reduces the most errors in each iteration .
- The rules are of the form: Change tag a to tag b when condition c is met .
- For example, a rule could be: Change tag NN (noun) to VB (verb) when the previous word is TO (preposition) .
- The rules are applied in a fixed order, and the order is determined by the order of learning .
- The advantages of TBL are  :
  - It is fast and efficient, as it only requires one pass over the text to tag it.
  - It is interpretable and transparent, as the rules are human-readable and can capture linguistic knowledge.
  - It is adaptable and flexible, as it can learn rules for different domains, languages, and tasks.
  - It is robust and error-tolerant, as it can handle unknown words and noisy data.
- The disadvantages of TBL are :
  - It requires a large and representative tagged corpus for learning the rules.
  - It may overfit the training data and generalize poorly to new data.
  - It may produce conflicting or redundant rules that affect the tagging accuracy.
  - It may miss some complex or rare patterns that require higher-order n-grams or syntactic information.
- A possible mnemonic to remember the steps of TBL is: Start Simple, Correct Errors, Learn Rules, Apply Order .
- A possible application of TBL is text chunking, which is the task of identifying non-overlapping phrases or chunks in a text, such as noun phrases, verb phrases, etc.
- An example of text chunking using TBL is shown below:

|Word|Tag|Chunk|
|---|---|---|
|He|PRP|B-NP|
|reckons|VBZ|B-VP|
|the|DT|B-NP|
|current|JJ|I-NP|
|account|NN|I-NP|
|deficit|NN|I-NP|
|will|MD|B-VP|
|narrow|VB|I-VP|
|to|TO|B-PP|
|only|RB|B-NP|
|#|SYM|I-NP|
|1.8|CD|I-NP|
|billion|CD|I-NP|
|in|IN|B-PP|
|September|NNP|B-NP|
|.|.|O|

- B-NP means the beginning of a noun phrase, I-NP means the continuation of a noun phrase, B-VP means the beginning of a verb phrase, I-VP means the continuation of a verb phrase, B-PP means the beginning of a prepositional phrase, and O means outside of any chunk.
- The chunking process can be done by applying a set of rules that change the tag of a word based on its context, such as: Change tag B-NP to B-VP when the previous word is MD (modal verb).