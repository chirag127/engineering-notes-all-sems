### Shallow parsing

- Shallow parsing (also called chunking or light parsing) is an analysis of a sentence which first identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.).
- Shallow parsing is different from deep parsing, which aims to produce a complete and detailed parse tree that represents the syntactic structure of a sentence according to a formal grammar.
- Shallow parsing is useful for many natural language processing applications that do not require full syntactic analysis, such as information extraction, named entity recognition, sentiment analysis, question answering, etc.
- Shallow parsing can be seen as a set of cascaded classification problems with separate classifiers for tagging, chunk boundary detection, chunk labeling, relation finding, etc.
- Shallow parsing can also be used to assign semantic roles to words or phrases in a sentence, such as that of an agent, goal, or result. This is also called semantic role labeling or slot-filling.
- Shallow parsing can be performed using various methods, such as rule-based systems, statistical models, machine learning algorithms, etc. Some popular tools for shallow parsing are NLTK, spaCy, Stanford CoreNLP, etc.