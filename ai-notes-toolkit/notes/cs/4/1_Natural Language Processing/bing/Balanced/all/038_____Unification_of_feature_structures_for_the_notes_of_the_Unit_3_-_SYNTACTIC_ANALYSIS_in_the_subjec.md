# Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the attributes are symbols and the values are either symbols or other feature structures.
- For example, the feature structure for a noun phrase can be written as:

```
[CAT: NP
 NUM: SG
 CASE: NOM
 HEAD: [CAT: N
        NUM: SG
        STEM: dog]]
```

- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- For example, the unification of the feature structures `[CAT: NP NUM: SG]` and `[CAT: NP CASE: NOM]` is `[CAT: NP NUM: SG CASE: NOM]`.
- Unification can fail if the feature structures are incompatible, i.e., if they contain contradictory information. For example, the unification of `[CAT: NP NUM: SG]` and `[CAT: NP NUM: PL]` fails because the NUM feature has different values.
- Unification is widely used in natural language processing (NLP) for various tasks, such as parsing, generation, and semantic interpretation.
- Unification can be extended to E-unification, which allows the use of equations to express relations between feature values. E-unification of feature structures has, to the best of our knowledge, never been used in NLP, but it can be useful for capturing linguistic phenomena such as agreement, anaphora, and ellipsis .