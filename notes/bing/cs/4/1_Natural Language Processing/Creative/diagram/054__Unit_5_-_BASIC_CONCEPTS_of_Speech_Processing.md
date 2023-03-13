## Unit 5 - BASIC CONCEPTS of Speech Processing

Speech processing is the study of how humans produce and perceive speech, as well as the methods and technologies for analyzing, synthesizing, and manipulating speech signals. Speech processing involves three major levels of processing: conceptualization, formulation, and articulation .

- Conceptualization is the process of determining what to say, based on the speaker's intention, knowledge, and context. This involves selecting the appropriate words, concepts, and structures to convey the intended meaning.
- Formulation is the process of encoding the conceptual representation into linguistic forms, such as phonological, morphological, syntactic, and prosodic structures. This involves applying the rules and constraints of the language to generate well-formed utterances.
- Articulation is the process of producing the speech sounds by the motor system using the vocal apparatus, such as the lungs, larynx, vocal cords, tongue, lips, and teeth. This involves coordinating the movements of various speech organs to create the desired acoustic signal.

The following diagram illustrates the basic architecture of a speech processing system using ASCII art:

```
+----------------+     +----------------+     +----------------+
| Conceptualizer | --> | Formulator     | --> | Articulator    |
+----------------+     +----------------+     +----------------+
    ^    |                  ^    |                  ^    |
    |    v                  |    v                  |    v
+----------------+     +----------------+     +----------------+
| Conceptual     |     | Linguistic     |     | Acoustic       |
| Representation |     | Representation |     | Representation |
+----------------+     +----------------+     +----------------+
```