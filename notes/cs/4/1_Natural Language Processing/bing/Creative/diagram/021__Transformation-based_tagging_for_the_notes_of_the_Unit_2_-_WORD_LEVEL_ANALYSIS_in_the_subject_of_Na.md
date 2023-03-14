Transformation-based tagging is a method for part-of-speech tagging that assigns a tag to each word and changes it using a set of predefined rules. The rules are based on the context and the most frequent tag for each word. The following diagram illustrates the basic architecture of a transformation-based tagger:

```
Input: A sequence of words
Output: A sequence of tags

Step 1: Initialization
- For each word, assign the most frequent tag based on a dictionary or a lexical rule
- For unknown words, assign a default tag (e.g. noun)

Step 2: Transformation
- Apply a set of rules that change the tag of a word based on the surrounding words or tags
- Repeat until no more rules can apply or a threshold is reached

Example:

Input: They refuse to permit us to obtain the refuse permit
Initialization: They/PRP refuse/VBP to/TO permit/VB us/PRP to/TO obtain/VB the/DT refuse/NN permit/NN
Transformation: 
- Rule 1: NN -> VB if the previous tag is TO
- Rule 2: VB -> NN if the next word is permit
- Rule 3: NN -> VBP if the previous word is They
- Rule 4: VBP -> NN if the next tag is NN
- Rule 5: NN -> JJ if the previous tag is DT and the next tag is NN
Output: They/PRP refuse/NN to/TO permit/NN us/PRP to/TO obtain/VB the/DT refuse/JJ permit/NN
```