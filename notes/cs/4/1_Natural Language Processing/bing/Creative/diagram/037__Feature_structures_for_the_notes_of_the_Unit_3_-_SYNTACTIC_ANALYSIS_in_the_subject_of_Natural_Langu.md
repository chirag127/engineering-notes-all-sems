Feature structures are a way of representing grammatical information about words and phrases using dictionaries of features and values. They are often used in natural language processing to capture the syntactic and semantic properties of linguistic expressions. For example, the following feature structure represents a noun phrase with the orthography "Kim" and the referent "k":

[CAT: NP
 ORTH: Kim
 REF: k]

Feature structures can also be nested to represent complex structures, such as verb phrases or sentences. For example, the following feature structure represents a verb phrase with the orthography "chased", the relation "chase", the agent "sbj" and the patient "obj":

[CAT: VP
 ORTH: chased
 REL: chase
 AGT: sbj
 PAT: obj]

Feature structures can be combined using unification, a process that checks for compatibility and merges the information from two feature structures. For example, the following feature structure represents a sentence with the subject "Kim" and the verb phrase "chased Lee":

[CAT: S
 ORTH: Kim chased Lee
 REL: chase
 AGT: [CAT: NP
       ORTH: Kim
       REF: k]
 PAT: [CAT: NP
       ORTH: Lee
       REF: l]]

This feature structure is the result of unifying the feature structures for "Kim", "chased" and "Lee", and linking the agent and patient roles of the verb to the referents of the noun phrases.

Feature structures can be drawn as diagrams using boxes and arrows to show the features and values. The following diagram illustrates the feature structure for the sentence "Kim chased Lee":

+-----------------+
| CAT: S         |
| ORTH: Kim      |
|      chased Lee|
| REL: chase     |
| AGT: ----------+----+
| PAT: ----------+    |
+-----------------+    |
                      |
                      v
+-----------------+    +-----------------+
| CAT: NP        |    | CAT: VP        |
| ORTH: Kim      |    | ORTH: chased   |
| REF: k         |    | REL: chase     |
+-----------------+    | AGT: ----------+----+
                      | PAT: ----------+    |
                      +-----------------+    |
                                            |
                                            v
+-----------------+    +-----------------+
| CAT: NP        |    | CAT: NP        |
| ORTH: Lee      |    | ORTH: Kim      |
| REF: l         |    | REF: k         |
+-----------------+    +-----------------+