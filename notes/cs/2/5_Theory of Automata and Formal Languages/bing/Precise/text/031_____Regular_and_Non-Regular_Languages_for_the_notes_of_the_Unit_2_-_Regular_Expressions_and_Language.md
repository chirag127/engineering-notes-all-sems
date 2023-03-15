### Regular and Non-Regular Languages

Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

1. A **regular language** is a formal language that can be expressed using a regular expression. It is a subset of the set of all possible strings over a given alphabet.
2. Regular languages can be recognized by a finite automaton, which is a computational model that can read and process a string of symbols one at a time.
3. A **non-regular language** is a formal language that cannot be expressed using a regular expression and cannot be recognized by a finite automaton.
4. The **pumping lemma** is a tool used to prove that a language is non-regular. It states that for any regular language, there exists a constant `p` such that any string in the language of length greater than or equal to `p` can be divided into three parts, `xyz`, such that `|xy| <= p`, `|y| > 0`, and `xy^iz` is in the language for all `i >= 0`.
5. An example of a regular language is the set of all strings over the alphabet `{0, 1}` that contain an even number of `0`s. This language can be expressed using the regular expression `(1*01*01*)*`.
6. An example of a non-regular language is the set of all strings over the alphabet `{0, 1}` where the number of `0`s is equal to the number of `1`s. This language cannot be expressed using a regular expression and cannot be recognized by a finite automaton.
