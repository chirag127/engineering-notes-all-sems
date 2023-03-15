# Application of Pumping Lemma

- The pumping lemma is a property of regular languages that states that any sufficiently long string in a regular language can be divided into three parts, such that the middle part can be repeated any number of times and the resulting string will still belong to the language  .
- The pumping lemma can be used to prove that certain languages are not regular, by showing a contradiction. If a language is regular, it must satisfy the pumping lemma, but if it does not satisfy the pumping lemma, it is non-regular  .
- The pumping lemma can also be used to find the minimum number of states in a deterministic finite automaton (DFA) that recognizes a regular language, by using the pumping length as a lower bound.
- The pumping lemma can also be used to compare the expressive power of different classes of languages, such as context-free languages and context-sensitive languages, by showing that some languages that satisfy the pumping lemma for regular languages do not satisfy the pumping lemma for other classes of languages.

## Example of using the pumping lemma to prove a language is non-regular

- Consider the language L = {a^n b^n | n >= 0} over the alphabet {a, b}. We will show that L is not regular by using the pumping lemma.
- Suppose L is regular, then there exists a pumping length p such that any string in L of length at least p can be divided into three parts, x, y, and z, such that xy^i z is in L for any i >= 0, and |xy| <= p and |y| > 0.
- Let s = a^p b^p be a string in L of length 2p >= p. Then s can be divided into x, y, and z as described above. Since |xy| <= p, x and y must consist of only a's. Let x = a^k and y = a^l, where k + l <= p and l > 0. Then z = a^(p-k-l) b^p.
- Now consider the string xy^2 z, which is obtained by repeating y once. This string is equal to a^(k+2l) a^(p-k-l) b^p = a^(p+l) b^p. This string is not in L, because the number of a's and b's are not equal. This contradicts the pumping lemma, which says that xy^2 z should be in L.
- Therefore, we have shown that L does not satisfy the pumping lemma, and hence L is not regular.