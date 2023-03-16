# Issues in PoS tagging

Part of Speech (PoS) tagging is a fundamental problem in Natural Language Processing (NLP). It is a disambiguation task where the goal is to find the right tag for a word given its context. A word can have multiple PoS tags, and the challenge is to assign the correct tag based on the context in which the word is used .

1. **Accuracy**: Most good PoS taggers report accuracy numbers of 97% and above on a per-word basis. However, some scholars have argued that per-token accuracy is not the best way to estimate the accuracy of the PoS engine. In their opinion, at the sentence level, the accuracy is much lower than the claimed 97% .

2. **Ambiguity**: The presence of ambiguity when tagging terms with different contextual meanings inside a sentence cannot be overlooked. This is one of the challenges that PoS tagging still faces in improving accuracy while reducing false-positive rates and in tagging unknown words .

3. **Errors in text and speech**: Misspelled or misused words can create problems for text analysis. Autocorrect and grammar correction applications can handle common mistakes, but they don’t always understand the writer’s intention .