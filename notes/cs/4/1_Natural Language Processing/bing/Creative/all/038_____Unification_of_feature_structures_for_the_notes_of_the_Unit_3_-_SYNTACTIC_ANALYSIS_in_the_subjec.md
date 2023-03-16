# Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be.
- A feature structure is a set of attribute-value pairs, where the attributes are symbols and the values are either symbols or other feature structures.
- For example, the feature structure for the word "dog" can be written as:

```
[CAT: N
 NUM: SG
 GND: M]
```

- This means that the word "dog" has the category N (noun), the number SG (singular), and the gender M (masculine).
- Unification is a (partial) operation on feature structures. Intuitively, it is the operation of combining two feature structures such that the new feature structure contains all the information of the original two, and nothing more.
- For example, let F1 be the feature structure:

```
[CAT: N
 NUM: SG]
```

- And let F2 be the feature structure:

```
[CAT: N
 GND: M]
```

- Then the unification of F1 and F2, written as F1 ⊓ F2, is the feature structure:

```
[CAT: N
 NUM: SG
 GND: M]
```

- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- Unification can also fail if the two feature structures are incompatible, meaning that they have conflicting values for some attribute. For example, F1 ⊓ F3 is undefined, where F3 is:

```
[CAT: V
 NUM: PL]
```

- Unification is useful in natural language processing (NLP) for various tasks, such as parsing, generation, and semantic interpretation.
- Unification can also be extended to E-unification, which allows for the use of equations or constraints on the values of the attributes.
- E-unification of feature structures has, to the best of our knowledge, never been used in NLP, but it has potential applications in areas such as anaphora resolution, lexical semantics, and discourse representation .
- E-unification can handle cases where the values of the attributes are not fixed, but depend on some other feature structures or variables. For example, let F4 be the feature structure:

```
[CAT: N
 NUM: X]
```

- And let F5 be the feature structure:

```
[CAT: N
 NUM: Y]
```

- And let E be the equation X = Y. Then the E-unification of F4 and F5 with respect to E, written as F4 ⊓E F5, is the feature structure:

```
[CAT: N
 NUM: X]
```

- Where X and Y are now unified to the same variable. This can capture the agreement between two nouns in number, for instance.