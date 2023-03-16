```markdown
### Shallow parsing

- Shallow parsing (also called chunking or light parsing) is an analysis of a sentence which first identifies constituent parts of sentences (nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (noun groups or phrases, verb groups, etc.).
- Shallow parsing is different from deep parsing, which aims to produce a complete and unambiguous representation of the syntactic structure of a sentence, such as a parse tree or a dependency graph.
- Shallow parsing is useful for many natural language processing applications that do not require full syntactic analysis, such as information extraction, named entity recognition, sentiment analysis, machine translation, etc.
- Shallow parsing can be performed using various methods, such as rule-based, statistical, or memory-based approaches. Some common techniques are:
  - Part-of-speech tagging: assigning a word class label (such as noun, verb, adjective, etc.) to each word in a sentence based on its morphology and context.
  - Chunking: identifying and labeling non-overlapping phrases or chunks in a sentence, such as noun phrases, verb phrases, prepositional phrases, etc.
  - Semantic role labeling: assigning a semantic role label (such as agent, patient, instrument, etc.) to each word or phrase in a sentence that indicates its function in the predicate-argument structure of the sentence.
- Shallow parsing can be evaluated using various metrics, such as precision, recall, F1-score, or accuracy, depending on the task and the level of granularity of the output. Some common evaluation datasets are:
  - CoNLL-2000: a corpus of Wall Street Journal articles annotated with part-of-speech tags and chunk labels.
  - CoNLL-2003: a corpus of news wire articles annotated with part-of-speech tags, chunk labels, and named entity labels.
  - CoNLL-2004: a corpus of news wire articles annotated with part-of-speech tags, chunk labels, and semantic role labels.
  - CoNLL-2005: a corpus of Wall Street Journal articles annotated with part-of-speech tags, chunk labels, and semantic role labels.
```