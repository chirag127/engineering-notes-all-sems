 Here is the content in markdown format for the given topic:

### Issues in PoS tagging for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

The following are the major issues encountered in PoS tagging:

1. Ambiguity: The same word can have multiple PoS tags depending on the context. For example, "book" can be a noun or a verb. The PoS tagger has to determine the correct tag based on the context which is difficult.
2. Domain dependence: The linguistic patterns and distribution of words across PoS tags can vary across domains. A PoS tagger trained on one domain may not work well on text from another domain.
3. Complex words: Words like " guaranteer", "demilitarization" are complex and it is difficult to identify the correct tag. The suffix/prefix may not always determine the correct PoS.
4. Out of vocabulary (OOV) words: The PoS tagger may encounter new words that are not present in the training data. In such cases, it is difficult to predict the correct tag leading to errors.
5. Lack of adequate training data: The performance of a machine learning based PoS tagger depends on the amount and quality of training data. If the training data is less, the tagger may not learn the linguistic patterns and distributions properly leading to poor performance.

Some useful mnemonics for remembering the issues:

- A dog can book (ambiguity)
- Domain dance (domain dependence)
- Complex words are tough nuts to crack (complex words)
- Unknown words are out of luck (OOV words)
- Data drought impacts the clout (lack of training data)

The issues can be mitigated by using contextual information, domain adaptation techniques, morphological analysis of complex words, handling OOV words using dictionaries/word embeddings and collecting more annotated data.

Detailed examples and applications of PoS tagging along with advantages and disadvantages can be included if required. Please let me know if you would like me to elaborate on any part of the answer.