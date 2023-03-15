### Programming problems based on the properties of CFGs for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

1. **Pumping Lemma for Context-Free Languages:** Given a context-free language L, the pumping lemma states that there exists a constant p (the pumping length) such that for any string s in L of length at least p, s can be divided into three substrings s = xyz, where |xy| ≤ p, |y| ≥ 1, and for all i ≥ 0, xy^iz ∈ L. This property can be used to prove that certain languages are not context-free.

2. **Closure Properties of Context-Free Languages:** Context-free languages are closed under the following operations: union, concatenation, Kleene star, reversal, homomorphism, and inverse homomorphism. These closure properties can be used to construct new context-free languages from existing ones.

3. **Decidability of Context-Free Languages:** The emptiness, finiteness, and membership problems for context-free languages are all decidable. This means that there exist algorithms to determine whether a given context-free language is empty, finite, or contains a given string.

4. **Chomsky Normal Form:** Every context-free grammar can be transformed into an equivalent grammar in Chomsky Normal Form, where all productions are of the form A → BC or A → a, where A, B, and C are non-terminal symbols and a is a terminal symbol. This normal form is useful for proving properties of context-free languages and for designing parsing algorithms.

5. **Pushdown Automata:** A pushdown automaton is a finite automaton equipped with a stack, which can be used to recognize context-free languages. The stack allows the automaton to keep track of an unbounded amount of information, which is necessary to recognize languages that are not regular.
