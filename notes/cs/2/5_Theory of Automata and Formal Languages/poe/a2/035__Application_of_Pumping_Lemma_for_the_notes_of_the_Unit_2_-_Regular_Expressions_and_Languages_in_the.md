 Here is the formal content in Markdown format without any emojis or external links on the given topic:

### Application of Pumping Lemma for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

1. Pumping Lemma states that for any regular language L, there exists a number p such that any string w in L with length at least p can be pumped to produce a new string of length greater than or equal to p.

2. The pumping length p depends only on the regular language L and not on the string w.

3. Pumping Lemma can be used to prove that a language is not regular. If we assume that a language L is regular and derive a contradiction by showing that L violates the Pumping Lemma, then L cannot be regular.

4. For example, consider the language L = {ww : w is a string of 0's and 1's with equal number of 0's and 1's}.

5. Assume that L is regular and let p be its pumping length.

6. Consider the string w = 0101. Since |w| = 4 >= p, w can be pumped to get a new string v = 0101010 of length greater than or equal to p.

7. However, v contains unequal number of 0's and 1's. This contradicts the definition of L.

8. Hence, the assumption that L is regular is incorrect. Therefore, L is not a regular language.

9. Thus, Pumping Lemma can be used to prove that a language is not regular by assuming it to be regular and arriving at a contradiction.