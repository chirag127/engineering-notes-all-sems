### Feature structures for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Natural Language Processing (NLP) is a branch of artificial intelligence that attempts to bridge the gap between what a machine recognizes as input and the human language.
- NLP combines artificial intelligence, computational linguistics and machine learning to enable computers and humans to communicate seamlessly.
- NLP can be divided into three main tasks: speech recognition, natural language understanding and natural language generation.
- Syntactic analysis is the process of analyzing the structure and meaning of sentences in natural language.
- Feature structures are a way of representing syntactic information in a hierarchical and modular way.
- Feature structures are composed of features and values, where features are atomic symbols and values can be atomic symbols, sets or other feature structures.
- Feature structures can be visualized as labeled graphs, where nodes are features and edges are values.
- For example, the following feature structure represents some information about a word:

```
[POS = N
 NUM = SG
 GND = FEM
 SEM = [CAT = ANIMAL
        NAME = 'Fido']]
```

- This feature structure can be graphically represented as:

```
    POS
     |
     N
    /|\
   / | \
  /  |  \
 /   |   \
NUM GND  SEM
 |   |    |
 SG FEM  [CAT = ANIMAL
          NAME = 'Fido']
```

- Feature structures can be manipulated by the operation of unification, which allows us to combine the information contained in two different feature structures.
- Unification is the process of finding the most general feature structure that is consistent with both of the input feature structures.
- Unification can fail if there is a contradiction between the input feature structures, such as different values for the same feature.
- For example, the unification of the following two feature structures:

```
[POS = N
 NUM = SG]
```

and

```
[POS = N
 GND = FEM]
```

results in the following feature structure:

```
[POS = N
 NUM = SG
 GND = FEM]
```

- However, the unification of the following two feature structures:

```
[POS = N
 NUM = SG]
```

and

```
[POS = V
 TNS = PRES]
```

fails because the values of the feature POS are different.