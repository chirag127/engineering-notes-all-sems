Unification of feature structures is a process of combining two or more feature structures that share some common attributes and values. Feature structures are sets of attribute-value pairs that provide morphological, syntactic or semantic information about linguistic units. Unification grammars are grammatical formalisms that use feature structures to represent linguistic categories and constraints.

A feature structure can be represented as a tree diagram, where each node is either an attribute or a value. An attribute is a label that identifies a property of a linguistic unit, such as number, gender, case, etc. A value is either an atomic symbol, such as singular, plural, masculine, feminine, etc., or another feature structure. A feature structure can also be represented as a bracketed expression, where each attribute-value pair is enclosed in square brackets and separated by a colon.

For example, the feature structure for the word "dog" can be represented as:

[cat: noun
 num: singular
 gen: common]

or as a tree diagram:

cat
 |
 noun
 / \
num gen
 | |
singular common

The feature structure for the word "dogs" can be represented as:

[cat: noun
 num: plural
 gen: common]

or as a tree diagram:

cat
 |
 noun
 / \
num gen
 | |
plural common

Unification of feature structures is a way of combining two or more feature structures that share some common attributes and values. For example, if we have a feature structure for a verb phrase (VP) that specifies that its head (H) is a verb (V) and its subject (SUBJ) is a noun phrase (NP), and a feature structure for a verb that specifies that its category (cat) is verb and its number (num) is singular, we can unify them to get a feature structure for a verb phrase with a singular verb:

[cat: VP
 H: [cat: V
     num: singular]
 SUBJ: [cat: NP]]

or as a tree diagram:

cat
 |
 VP
 / \
H SUBJ
 | |
cat cat
 | |
 V NP
 |
num
 |
singular

Unification of feature structures is a partial operation, meaning that it may fail if the feature structures are incompatible. For example, if we try to unify the feature structure for the verb phrase above with the feature structure for the word "dogs", we get a failure, because the number attribute of the verb and the noun do not match:

[cat: VP
 H: [cat: V
     num: singular]
 SUBJ: [cat: NP
        H: [cat: noun
            num: plural
            gen: common]]]

or as a tree diagram:

cat
 |
 VP
 / \
H SUBJ
 | |
cat cat
 | |
 V NP
 | / \
num H
 | | |
singular cat num gen
 | | | |
 noun plural common

Unification of feature structures is a useful tool for syntactic analysis, because it allows us to capture the agreement and selectional restrictions between different linguistic units. For example, we can use unification to check whether a verb phrase is compatible with a sentence, or whether a noun phrase is compatible with a verb, etc. Unification grammars use feature structures to represent the syntactic categories and rules of a language, and use unification to derive the well-formed structures of the language.