# Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the attributes are symbolic labels and the values are either atomic symbols or other feature structures.
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
- For example, the unification of the feature structures `[A: 1 B: 2]` and `[A: 1 C: 3]` is `[A: 1 B: 2 C: 3]`.
- Unification can fail if the two feature structures are incompatible, i.e., they assign different values to the same attribute. For example, the unification of `[A: 1 B: 2]` and `[A: 2 C: 3]` fails because they disagree on the value of `A`.
- Unification is widely used in natural language processing (NLP) for various tasks, such as parsing, generation, grammar formalisms, and semantic interpretation.
- Unification can be extended to E-unification, which allows the use of equations to express additional constraints on the feature structures.
- E-unification of feature structures has, to the best of our knowledge, never been used in NLP, but it has potential applications in areas such as lexical semantics, anaphora resolution, and discourse analysis.
- E-unification is more expressive and powerful than structural unification, but also more complex and computationally expensive.
- A number of examples illustrate the usefulness of E-unification in the domain of NLP, such as handling synonymy, antonymy, hyponymy, and meronymy relations in lexical semantics.