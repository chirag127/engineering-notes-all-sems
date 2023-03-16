### Feature Structures

Feature structures are used in syntactic analysis in natural language processing to represent the grammatical properties of words and phrases. They are a way to represent the hierarchical structure of a sentence and the relationships between its constituents.

1. **Definition:** A feature structure is a set of attribute-value pairs, where the attributes are the grammatical properties and the values are the possible values for those properties.
2. **Example:** For example, a noun phrase may have the attributes `number` and `gender`, with possible values `singular` or `plural` for `number` and `masculine`, `feminine`, or `neuter` for `gender`.
3. **Use:** Feature structures are used in unification-based grammars, where the grammatical rules specify the constraints on the feature structures of the constituents of a sentence.
4. **Unification:** Unification is the process of combining two feature structures by finding a common set of attribute-value pairs that satisfy the constraints of both structures.
5. **Parsing:** In syntactic analysis, feature structures are used to represent the possible parses of a sentence. The parser generates a set of feature structures for each constituent of the sentence, and then uses unification to combine them into a complete parse.
