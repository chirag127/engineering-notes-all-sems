### Shallow parsing for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Shallow parsing (also known as chunking or light parsing) is an analysis of a sentence which first identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.).
- Shallow parsing is a technique widely used in natural language processing. It is similar to the concept of lexical analysis for computer languages. It is also used as an explanation for why second language learners often fail to parse complex sentences correctly.
- Shallow parsing is useful for extracting information from text, such as named entities, keywords, relations, etc. It can also be used as a preprocessing step for deeper parsing or other NLP tasks.
- Shallow parsing can be done using rule-based methods, such as regular expressions or context-free grammars, or using machine learning methods, such as classifiers, topic modeling, etc. Machine learning methods can take contextual information into account and thus compose chunks in such a way that they better reflect the semantic relations between the basic constituents.
- Shallow parsing can be divided into two subtasks: part-of-speech (POS) tagging and chunking. POS tagging assigns a tag to each word in a sentence, indicating its grammatical category, such as noun, verb, adjective, etc. Chunking groups words into larger units, such as noun phrases, verb phrases, prepositional phrases, etc. Chunking can be done based on the POS tags or using other features, such as word shapes, capitalization, etc.
- An example of shallow parsing is shown below:

```
Sentence: He reckons the current account deficit will narrow to only # 1.8 billion in the third quarter.
POS tags: He/PRP reckons/VBZ the/DT current/JJ account/NN deficit/NN will/MD narrow/VB to/TO only/RB #/# 1.8/CD billion/CD in/IN the/DT third/JJ quarter/NN ./.
Chunks: [He/PRP] [reckons/VBZ] [the/DT current/JJ account/NN deficit/NN] [will/MD narrow/VB] [to/TO only/RB #/# 1.8/CD billion/CD] [in/IN the/DT third/JJ quarter/NN] ./.
```

- A mnemonic to remember the difference between shallow parsing and deep parsing is: shallow parsing is like peeling an onion, while deep parsing is like cutting it into pieces. Shallow parsing reveals the outer layers of the sentence structure, while deep parsing reveals the inner relations and dependencies.