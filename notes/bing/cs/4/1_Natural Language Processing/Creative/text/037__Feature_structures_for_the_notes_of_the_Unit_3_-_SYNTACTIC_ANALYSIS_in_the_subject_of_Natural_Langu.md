### Feature structures

- Feature structures are a way of representing complex linguistic information in a structured and hierarchical way.
- Feature structures consist of a set of attribute-value pairs, where the attribute is a feature name and the value is either an atomic value (such as a string or a number) or another feature structure.
- Feature structures can be used to encode various types of linguistic information, such as morphology, syntax, semantics, and pragmatics.
- Feature structures can be represented graphically as boxes with labeled slots, or textually as brackets with colons and commas.
- For example, the following feature structure represents some information about a noun phrase:

```
[CAT: NP
 NUM: SG
 HEAD: [CAT: N
        STEM: dog
        AGR: [NUM: SG
              PERS: 3]]]
```

- This feature structure has three attributes: CAT, NUM, and HEAD. The values of CAT and NUM are atomic, while the value of HEAD is another feature structure with three attributes: CAT, STEM, and AGR. The value of AGR is also another feature structure with two attributes: NUM and PERS.
- Feature structures can be nested and shared to capture complex and recursive linguistic phenomena, such as coordination, agreement, and anaphora.
- Feature structures can be unified to combine information from different sources, such as lexical entries, syntactic rules, and semantic constraints. Unification is an operation that takes two feature structures as input and returns a new feature structure as output, if the input structures are compatible. Otherwise, unification fails and returns a special value ⊥.
- Unification is compatible if the input structures have the same attribute names and values, or if the values can be further unified. Unification is incompatible if the input structures have different attribute names or values that cannot be unified.
- For example, the following feature structures can be unified:

```
[A: 1
 B: [C: 2
     D: 3]]

[A: 1
 B: [C: 2
     E: 4]]
```

- The result of unification is:

```
[A: 1
 B: [C: 2
     D: 3
     E: 4]]
```

- However, the following feature structures cannot be unified:

```
[A: 1
 B: [C: 2
     D: 3]]

[A: 1
 B: [C: 2
     D: 4]]
```

- The result of unification is ⊥, because the values of D are different and cannot be unified.