Shallow parsing, also known as chunking or light parsing, is a technique in natural language processing that identifies the constituent parts of sentences (such as nouns, verbs, adjectives, etc.) and then links them to higher order units that have discrete grammatical meanings (such as noun phrases, verb phrases, etc.) . Shallow parsing is different from deep parsing, which aims to produce a complete and detailed representation of the syntactic structure of a sentence. Shallow parsing is often used as a preliminary step for deeper analysis, or as a way to extract useful information from text without requiring full parsing .

The following diagram illustrates the basic architecture of a shallow parser using a memory-based learning approach. Memory-based learning is a machine learning technique that uses a large database of examples to classify new instances based on their similarity to the stored cases. A shallow parser can be constructed as a cascade of memory-based classifiers, each performing a specific subtask of the parsing process, such as part-of-speech tagging, chunking, and chunk linking. The output of each classifier is fed as input to the next one, until the final output is produced.

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Input text    +---->+  POS tagger    +---->+  Chunker       +---->+  Chunk linker  +---->+  Output text
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```

The output text is a representation of the shallow parse tree of the input text, where each word is annotated with its part-of-speech tag and its chunk type and role. For example, the sentence "He saw a man with a telescope" can be shallow parsed as:

```
[He/PRP/B-NP] [saw/VBD/B-VP] [a/DT/B-NP] [man/NN/I-NP] [with/IN/B-PP] [a/DT/B-NP] [telescope/NN/I-NP]
```

This means that "He" is a pronoun and the beginning of a noun phrase (B-NP), "saw" is a verb and the beginning of a verb phrase (B-VP), "a" is a determiner and the beginning of a noun phrase (B-NP), "man" is a noun and the continuation of a noun phrase (I-NP), "with" is a preposition and the beginning of a prepositional phrase (B-PP), and so on. The chunk types are NP (noun phrase), VP (verb phrase), PP (prepositional phrase), etc. The chunk roles are B (beginning), I (inside), or O (outside) of a chunk.