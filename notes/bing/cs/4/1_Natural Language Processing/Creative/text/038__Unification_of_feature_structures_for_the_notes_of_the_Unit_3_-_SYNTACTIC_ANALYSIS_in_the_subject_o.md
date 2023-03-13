### Unification of feature structures

- Feature structures are a way of representing partial information about some linguistic object or placing informational constraints on what the object can be  .
- A feature structure is a set of attribute-value pairs, where the attributes are symbolic labels and the values are either atomic symbols or other feature structures .
- For example, the feature structure for a noun phrase "the dog" can be written as:

```
[CAT: NP
 DET: [CAT: DET
       FORM: the]
 N: [CAT: N
     FORM: dog]]
```

- Unification is a (partial) operation on feature structures that combines two feature structures such that the new feature structure contains all the information of the original two, and nothing more .
- Unification can be seen as a way of merging the information in each feature structure, or describing objects that satisfy both sets of constraints.
- For example, the unification of two feature structures A and B can be written as A ⊕ B, and the result is a feature structure C that subsumes both A and B, meaning that C is more informative than or equal to A and B .
- If A and B are incompatible, meaning that they have conflicting values for some attribute, then the unification fails and the result is ⊥, which denotes the empty set .
- For example, the unification of the following feature structures fails:

```
A = [CAT: NP
     DET: [CAT: DET
           FORM: the]
     N: [CAT: N
         FORM: dog]]

B = [CAT: NP
     DET: [CAT: DET
           FORM: a]
     N: [CAT: N
         FORM: cat]]
```

- A ⊕ B = ⊥, because A and B have different values for the attributes DET.FORM and N.FORM .

- E-unification is a generalization of unification that allows for the presence of equations or constraints on the values of the attributes .
- E-unification of feature structures has, to the best of our knowledge, never been used in natural language processing (NLP), but it has potential applications in the domain of NLP .
- For example, E-unification can be used to model agreement phenomena, such as number and gender agreement between a noun and an adjective, or case marking on a verb and its arguments.
- E-unification can also be used to model lexical rules, such as derivation and inflection, or semantic interpretation, such as lambda abstraction and variable binding.
- E-unification is more expressive and powerful than structural unification, but it is also more complex and computationally expensive .
- E-unification is undecidable in general, but it can be tractable for some restricted classes of E-theories, such as linear, shallow, or regular E-theories .
- An E-theory is a set of equations or constraints that define the possible values of the attributes in a feature structure .
- For example, the following E-theory defines the possible values of the attribute NUM (number) for nouns and adjectives:

```
E = {NUM = sg | NUM = pl,
     N.NUM = A.NUM}
```

- The first equation in E states that the value of NUM can be either sg (singular) or pl (plural), and the second equation states that the value of NUM for a noun (N) and an adjective (A) must be the same.
- E-unification of feature structures with respect to an E-theory can be written as A ⊕E B, and the result is a feature structure C that subsumes both A and B and satisfies the equations in E .
- If A and B are incompatible with respect to E, then the E-unification fails and the result is ⊥ .
- For example, the E-unification of the following feature structures with respect to E succeeds:

```
A = [CAT: N
     NUM: sg
     FORM: dog]

B = [CAT: A
     NUM: ?
     FORM