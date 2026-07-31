# Dependency Grammar

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity.
- It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- Dependency grammar states that words of a sentence are dependent upon other words of the sentence.
- Dependency grammar is based on the concept that there is a direct link between every linguistic unit of a sentence.
- Dependency grammar uses dependency relations to indicate how words are related to each other in a sentence.
- Dependency relations are binary, asymmetric and labeled relations between a head and a dependent.
- A head is a word that governs the form and/or position of one or more dependents.
- A dependent is a word that is governed by a head and modifies or complements the head.
- For example, in the sentence "She likes the red car", the word "likes" is the head of the sentence and has three dependents: "She", "the" and "car". The word "car" is also a head and has one dependent: "red".
- Dependency grammar can be represented by dependency trees, which are directed graphs that show the dependency relations between words in a sentence.
- Dependency trees have a single root node, which is the head of the sentence, and each node has a label that indicates the type of dependency relation it has with its head.
- For example, the dependency tree for the sentence "She likes the red car" is:

```
  likes
 /  |  \
She |  car
    |  /
    | red
```

- The labels on the edges indicate the type of dependency relation between the head and the dependent. For example, "She" is a nominal subject (nsubj) of "likes", "the" is a determiner (det) of "car", and "red" is an adjectival modifier (amod) of "car".
- Dependency grammar can capture the syntactic and semantic structure of a sentence in a compact and intuitive way.
- Dependency grammar can also handle various linguistic phenomena, such as coordination, ellipsis, long-distance dependencies, and word order variation.
- Dependency grammar is widely used in natural language processing, especially for tasks such as dependency parsing, semantic role labeling, information extraction, and machine translation .