### Feature structures

- Feature structures are a way of representing linguistic information in a structured and hierarchical way.
- Feature structures consist of a set of attribute-value pairs, where the attribute is a feature name and the value is either an atomic value (such as a string or a number) or another feature structure.
- Feature structures can be used to encode various types of linguistic information, such as morphology, syntax, semantics, and pragmatics.
- Feature structures can be represented graphically as boxes with labeled slots, or textually as brackets with colon-separated pairs.
- For example, the feature structure for the word "cats" can be represented as:

```
[cats]
[CAT: N
 NUM: PL
 STEM: cat]
```

- Feature structures can be nested, meaning that the value of one attribute can be another feature structure. For example, the feature structure for the phrase "the cats" can be represented as:

```
[the cats]
[CAT: NP
 DET: [CAT: DET
       STEM: the]
 N: [CAT: N
     NUM: PL
     STEM: cat]]
```

- Feature structures can be unified, meaning that two feature structures can be combined into one by matching their attributes and values. Unification is a way of implementing agreement and selectional restrictions in grammar.
- Unification can fail if there is a mismatch between the attributes or values of the feature structures. For example, the feature structure for the word "is" cannot unify with the feature structure for the word "cats", because they have different values for the NUM attribute:

```
[is]
[CAT: V
 NUM: SG
 STEM: be]

[cats]
[CAT: N
 NUM: PL
 STEM: cat]
```

- Feature structures can be used to represent syntactic rules and lexical entries in a grammar. For example, the rule for forming a sentence (S) from a noun phrase (NP) and a verb phrase (VP) can be represented as:

```
[S] -> [NP] [VP]
[S] -> [CAT: S
        SUBJ: [CAT: NP]]
       [CAT: VP
        SUBJ: =SUBJ]
```

- The notation =SUBJ means that the value of the SUBJ attribute in the VP feature structure must be the same as the value of the SUBJ attribute in the S feature structure. This ensures that the subject of the sentence agrees with the subject of the verb phrase.
- The notation [CAT: X] means that the feature structure must have the value X for the CAT attribute. This ensures that the category of the phrase matches the expected category of the rule.
- The notation [STEM: Y] means that the feature structure must have the value Y for the STEM attribute. This ensures that the word matches the expected word of the lexical entry.