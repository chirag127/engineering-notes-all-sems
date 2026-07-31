### Application of Pumping Lemma for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages.

In the study of Theory of Automata and Formal Languages, the concept of Pumping Lemma is an important tool for proving that a given language is not regular. Here are some key points to understand the application of Pumping Lemma:

- Pumping Lemma is a technique that is used to prove that a language is not regular. It states that if a language is regular, then there exists a pumping length 'p' such that any string in the language that is longer than 'p' can be pumped, i.e., it can be divided into three parts - x, y, and z - such that y is non-empty and the string xy^iz is also in the language for all i ≥ 0.

- To apply the Pumping Lemma, we assume that the language L is regular and choose a string w in L that is longer than the pumping length 'p'. We then divide the string w into three parts - x, y, and z - such that |xy| ≤ p and |y| > 0. We can then pump the string by repeating y any number of times and showing that the resulting string is not in L, which contradicts our assumption that L is regular.

- It is important to note that the Pumping Lemma can only be used to prove that a language is not regular, but it cannot be used to prove that a language is regular. To prove that a language is regular, we need to construct a regular expression or a finite automaton that recognizes the language.

- The application of Pumping Lemma requires a good understanding of regular languages and their properties. It is important to be familiar with the basic operations on regular languages, such as concatenation, union, and Kleene star, and how they affect the regularity of a language.

- The Pumping Lemma can be used to prove that many languages are not regular, including the language {a^n b^n | n ≥ 0}, which is a classic example of a non-regular language. In fact, the Pumping Lemma is a powerful tool that has many applications in computer science and mathematics.

In conclusion, the Pumping Lemma is an important technique for proving that a language is not regular in the study of Theory of Automata and Formal Languages. It requires a good understanding of regular languages and their properties, and can be used to prove that many languages are not regular.