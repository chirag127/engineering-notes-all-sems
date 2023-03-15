## Unit 2 - Regular Expressions and Languages

Regular expressions and languages are fundamental concepts in computer science, particularly in the field of formal language theory. Here are some key points to remember:

1. A **regular expression** is a sequence of characters that defines a search pattern. These patterns are used to match character combinations in strings.

2. Regular expressions are used in many programming languages, including Perl, Python, and Java, as well as in text editors and utilities such as grep and sed.

3. A **regular language** is a formal language that can be expressed using a regular expression. Regular languages are a subset of the set of all formal languages.

4. Regular languages are closed under the operations of union, concatenation, and Kleene star. This means that if two languages are regular, then their union, concatenation, and Kleene closure are also regular.

5. The **finite automaton** is a computational model used to recognize regular languages. There are two types of finite automata: deterministic finite automata (DFA) and nondeterministic finite automata (NFA).

6. The **Pumping Lemma for regular languages** is a useful tool for proving that a language is not regular. It states that for any regular language, there exists a constant `p` such that any string in the language of length at least `p` can be divided into three substrings, `xyz`, such that `|xy| ≤ p`, `|y| ≥ 1`, and for all `i ≥ 0`, `xy^iz` is also in the language.
