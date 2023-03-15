 Here is the content in Markdown format:

### Word Sense Disambiguation for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

Word Sense Disambiguation (WSD) is the process of identifying the correct sense of a word in a sentence depending upon the context. Ambiguity arises in natural language due to the presence of words that have multiple meanings (polysemy) or words that are identical in spelling but differ in meaning (homonymy).

For example:

1. The bank is located on the river bank. (polysemy)
2. He is going to the bank. (could refer to a river bank or a financial institution)

WSD tries to determine the correct sense of a word based on the context in which it appears. It has applications in areas like machine translation, information retrieval, speech recognition, etc.

Some approaches to WSD are:

1. Dictionary-based approaches: Refer to dictionary definitions and choose the sense that matches the context. Limitation is that dictionaries do not contain all senses of a word and senses may be incomplete or ambiguous.
2. Supervised learning approaches: Requires a corpus annotated with the correct sense of words. Machine learning algorithms are trained on this data to learn how to disambiguate senses in new contexts. Challenging to get a large corpus of word usages annotated with senses.
3. Unsupervised approaches: Do not require sense-annotated data. Cluster occurrences of a word based on contextual similarities to induce word senses. However, the resulting clusters do not necessarily correspond to traditional word senses.

Advantages of WSD include handling of lexical ambiguity and enabling various NLP applications. Limitations are the knowledge acquisition bottleneck, lack of sufficient context to determine sense in some cases, and difficulty of evaluating WSD systems.

[Include diagrams/images if helpful for learning]

[Additional points or examples can be added as needed]