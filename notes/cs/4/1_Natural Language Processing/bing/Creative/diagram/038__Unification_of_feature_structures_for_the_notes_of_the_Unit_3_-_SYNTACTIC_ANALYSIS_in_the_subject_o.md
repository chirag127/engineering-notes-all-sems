### Unification of feature structures for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

Unification is a (partial) operation on feature structures that combines two feature structures such that the new feature structure contains all the information of the original two, and nothing more. Feature structures are sets of attribute-value pairs that provide morphological, syntactic or semantic information about linguistic objects. Unification grammars are grammar formalisms that use feature structures and unification to describe linguistic phenomena.

A feature structure can be represented as a directed graph, where nodes are labeled with feature names and edges are labeled with values. A value can be either atomic (such as a string or a number) or complex (such as another feature structure). For example, the following feature structure describes a noun phrase with a determiner and a noun:

```
    [CAT: NP
     AGR: [NUM: sg
           PER: 3]
     DET: [CAT: DET
           AGR: [NUM: sg
                 PER: 3]
           FORM: the]
     N: [CAT: N
         AGR: [NUM: sg
               PER: 3]
         FORM: dog]]
```

The graph representation of this feature structure is:

```
    +-----------------+
    | CAT: NP         |
    | AGR: +--------+ |
    |      | NUM: sg| |
    |      | PER: 3 | |
    |      +--------+ |
    | DET: +--------+ |
    |      | CAT: DET| |
    |      | AGR: +--+--+
    |      | FORM: the| |
    |      +--------+ | |
    | N:   +--------+ | |
    |      | CAT: N  | | |
    |      | AGR: +--+ | |
    |      | FORM: dog| |
    |      +--------+ | |
    +-----------------+ |
           |            |
           +------------+
```

Unification of two feature structures is possible if and only if they do not contain any conflicting information. For example, the feature structures [NUM: sg] and [NUM: pl] cannot be unified, because they have different values for the same feature. However, the feature structures [NUM: sg] and [PER: 3] can be unified, because they have different features. The result of unification is the feature structure that contains all the features and values of both input feature structures. For example, the unification of [NUM: sg] and [PER: 3] is [NUM: sg PER: 3].

The graph representation of unification is the merging of the two graphs, where nodes with the same feature name are identified and edges with the same value are collapsed. For example, the unification of the following two feature structures:

```
    [CAT: NP
     AGR: [NUM: sg
           PER: 3]
     DET: [CAT: DET
           AGR: [NUM: sg
                 PER: 3]
           FORM: the]
     N: [CAT: N
         AGR: [NUM: sg
               PER: 3]
         FORM: dog]]

    [CAT: NP
     AGR: [NUM: sg
           PER: 3]
     DET: [CAT: DET
           AGR: [NUM: sg
                 PER: 3]
           FORM: a]
     N: [CAT: N
         AGR: [NUM: sg
               PER: 3]
         FORM: cat]]
```

is the following feature structure:

```
    [CAT: NP
     AGR: [NUM: sg
           PER: 3]
     DET: [CAT: DET
           AGR: [NUM: sg
                 PER: 3]
           FORM: the a]
     N: [CAT: N
         AGR: [NUM: sg
               PER: 3]
         FORM: dog cat]]
```

The graph representation of this feature structure is:

```
    +-----------------+
    | CAT: NP         |
    | AGR: +--------+ |
    |      | NUM: sg| |
    |      | PER: 3 | |
    |      +--------+ |
    | DET: +--------+ |
    |      | CAT: DET| |
    |      | AGR: +--+--+
    |      | FORM: the a