```markdown
### Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the values can be atomic symbols, variables, or other feature structures.
- For example, the feature structure for a noun phrase can be written as:

```
[CAT: NP
 NUM: sg
 CASE: nom
 HEAD: [CAT: N
        NUM: sg
        STEM: dog]]
```

- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- For example, the unification of the feature structures `[A: 1 B: 2]` and `[A: 1 C: 3]` is `[A: 1 B: 2 C: 3]`.
- Unification can fail if the feature structures are incompatible, i.e., if they assign different values to the same attribute. For example, the unification of `[A: 1 B: 2]` and `[A: 2 C: 3]` fails because they disagree on the value of `A`.
- Unification is used in natural language processing (NLP) for various tasks, such as parsing, generation, and semantic interpretation .
- Unification can handle various linguistic phenomena, such as agreement, subcategorization, and anaphora resolution.
- Unification can also be extended to E-unification, which allows the use of equations and constraints to express more complex relations between feature structures .
- E-unification can handle phenomena such as ellipsis, coordination, and word order variation.
```