### Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the attributes are symbols and the values are either symbols or other feature structures.
- For example, the feature structure for a noun phrase "the dog" can be written as:

```
[CAT: NP
 DET: [CAT: DET
       FORM: the]
 N: [CAT: N
     FORM: dog]]
```

- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- For example, the unification of the feature structures `[A: 1 B: 2]` and `[A: 1 C: 3]` is `[A: 1 B: 2 C: 3]`.
- Unification can fail if the feature structures are incompatible, i.e., they have conflicting values for the same attribute. For example, the unification of `[A: 1 B: 2]` and `[A: 4 C: 3]` fails because they have different values for `A`.
- Unification is used in natural language processing (NLP) for various tasks, such as parsing, generation, and semantic interpretation.
- Unification can be extended to E-unification, which allows the use of equations to express relations between feature values.
- E-unification of feature structures has, to the best of our knowledge, never been used in NLP, but it has potential applications in areas such as anaphora resolution, lexical semantics, and discourse representation.
- E-unification can handle cases where structural unification is insufficient, such as when the feature values are not known or when they are related by some function.
- For example, the E-unification of `[A: x]` and `[A: f(y)]` with the equation `f(f(x)) = x` is `[A: f(y)]` with the substitution `{x/f(y)}`.
- E-unification is more expressive and powerful than structural unification, but also more complex and computationally expensive.
- E-unification is undecidable in general, but some subclasses of E-theories are decidable and tractable.
- A number of examples illustrate the usefulness of E-unification in the domain of NLP.