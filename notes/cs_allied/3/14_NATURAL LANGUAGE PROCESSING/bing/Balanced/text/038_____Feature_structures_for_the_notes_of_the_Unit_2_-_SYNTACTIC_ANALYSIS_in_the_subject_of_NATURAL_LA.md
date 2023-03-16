### Feature structures for the notes of the Unit 2 - SYNTACTIC ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Feature structures are a way of representing linguistic information in a structured and hierarchical way.
- Feature structures consist of a set of attribute-value pairs, where the attributes are names of linguistic features and the values are either atomic symbols or other feature structures.
- Feature structures can be used to encode various aspects of linguistic analysis, such as morphology, syntax, semantics and pragmatics.
- Feature structures can be represented graphically as boxes with labeled slots, or textually as brackets with colons.
- For example, the following feature structure represents some information about the word "dog":

```
[POS: N
 NUMBER: SG
 GENDER: M
 SEM: [CLASS: ANIMAL
       SPECIES: DOG]]
```

- Feature structures can be nested, as shown by the SEM attribute, which has another feature structure as its value.
- Feature structures can also be shared, as shown by the coindexation of the two NP feature structures in the following example:

```
[S [NP NUM: PL
      PERS: 3
      GENDER: F]_i
   [VP [V FORM: PRES
          AGR: [NUM: PL
                PERS: 3]] 
      [NP NUM: PL
          PERS: 3
          GENDER: F]_i]]
```

- Feature structures can be manipulated by the operation of unification, which allows us to combine the information contained in two different feature structures.
- Unification is a process of finding the most general feature structure that is compatible with both input feature structures, or failing if there is no such feature structure.
- Unification is useful for implementing grammatical constraints, such as agreement, subcategorization and selectional restrictions.
- For example, the following unification of a verb and its subject results in a feature structure that represents the agreement information:

```
[V FORM: PRES
 AGR: [NUM: ?x
       PERS: ?y]] 
 unify
[NP NUM: SG
    PERS: 3
    GENDER: M]
 =
[V FORM: PRES
 AGR: [NUM: SG
       PERS: 3]] 
```

- Feature structures can be implemented and manipulated in NLTK using the `nltk.FeatStruct` class and its methods.
- NLTK also provides a parser for reading feature structures from strings, and a graphical interface for displaying feature structures.
- For example, the following code creates and displays a feature structure in NLTK:

```
>>> import nltk
>>> fs = nltk.FeatStruct('[POS: N, NUMBER: SG, GENDER: M, SEM: [CLASS: ANIMAL, SPECIES: DOG]]')
>>> print(fs)
[ GENDER = 'M'   POS = 'N'   NUMBER = 'SG'   SEM = [ CLASS = 'ANIMAL'   SPECIES = 'DOG' ] ]
>>> fs.draw()
```