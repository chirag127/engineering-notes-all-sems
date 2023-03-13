### Feature structures for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Natural Language Processing (NLP) is a branch of artificial intelligence that attempts to bridge the gap between what a machine recognizes as input and the human language.
- Syntactic analysis is one of the main components of NLP, which deals with the structure and rules of natural language sentences.
- Feature structures are a way of representing syntactic information in a hierarchical and attribute-value form.
- A feature structure is a set of feature-value pairs, where a feature is a symbolic label and a value can be atomic (such as a string or a number) or complex (such as another feature structure).
- For example, the following feature structure represents some information about a word:

```
[  word  = 'dog'
   pos   = 'noun'
   num   = 'sg'
   sem   = [  class = 'animal'
              role  = 'patient' ] ]
```

- The feature structure has four features: word, pos, num, and sem. The values of word, pos, and num are atomic, while the value of sem is complex, containing another feature structure with two features: class and role.
- Feature structures can be nested arbitrarily deep, and can also share values using reentrancy, which is indicated by a numerical index. For example, the following feature structure represents a sentence with a subject and an object that refer to the same entity:

```
[  sent  = 'She likes herself'
   subj  = [  word  = 'she'
              index = 1 ]
   verb  = [  word  = 'likes'
              tense = 'pres' ]
   obj   = [  word  = 'herself'
              index = 1 ] ]
```

- The feature structure has three features: sent, subj, and obj. The values of sent and verb are atomic, while the values of subj and obj are complex, containing another feature structure with two features: word and index. The index feature indicates that the subj and obj have the same referent, which is marked by the same numerical value (1).
- Feature structures are useful for syntactic analysis because they can capture various kinds of linguistic information in a compact and flexible way. For example, feature structures can encode agreement, subcategorization, case, thematic roles, and semantic types.
- Feature structures can also be manipulated by operations such as unification, which allows us to combine the information contained in two different feature structures. Unification is the process of finding the most general feature structure that is consistent with both of the input feature structures. For example, unifying the following two feature structures:

```
[  pos  = 'noun'
   num  = 'pl' ]

[  pos  = 'noun'
   sem  = [  class = 'fruit' ] ]
```

- results in the following feature structure:

```
[  pos  = 'noun'
   num  = 'pl'
   sem  = [  class = 'fruit' ] ]
```

- Unification can be used to check the compatibility of feature structures, and to derive new feature structures from existing ones. For example, unification can be used to check the agreement between a subject and a verb, or to derive the feature structure of a phrase from the feature structures of its constituents.
- Feature structures can be represented graphically using boxes and arrows, where boxes correspond to feature structures, arrows correspond to features, and labels correspond to values. For example, the following graphical representation corresponds to the feature structure of the sentence 'She likes herself':

![feature structure graph](https://www.nltk.org/images/fs1.png)

- A mnemonic to remember the concept of feature structures is: **F**eatures **S**tructure **S**entences.