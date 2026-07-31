### Pumping Lemma for Regular Languages

The pumping lemma for regular languages is a fundamental concept in the theory of formal languages. It is a property that all regular languages share and can be used to prove that certain languages are not regular.

The lemma states that for any regular language L, there exists a constant p (called the pumping length) such that any string s in L of length at least p can be divided into three substrings, s = xyz, satisfying the following conditions:

1. For every i ≥ 0, xy^iz ∈ L.
2. |y| > 0.
3. |xy| ≤ p.

The first condition states that we can "pump" the middle substring y any number of times, and the resulting string will still be in the language. The second condition ensures that the middle substring y is not empty. The third condition ensures that the pumped substring y lies within the first p characters of the string s.

The pumping lemma can be used to prove that certain languages are not regular by showing that no such division of a string in the language can satisfy the conditions of the lemma. This is done by assuming that the language is regular, and then deriving a contradiction using the pumping lemma.

For example, consider the language L = {a^nb^n | n ≥ 0}. We can use the pumping lemma to prove that this language is not regular. Suppose, for the sake of contradiction, that L is regular. Then, by the pumping lemma, there exists a constant p such that any string s in L of length at least p can be divided into three substrings s = xyz satisfying the conditions of the lemma.

Let s = a^pb^p be a string in L of length at least p. By the third condition of the lemma, the pumped substring y must lie within the first p characters of s, which are all a's. Thus, y must consist only of a's. By the first condition of the lemma, we can pump y any number of times and the resulting string will still be in L. However, if we pump y zero times, we obtain the string xy^0z = xz, which has fewer a's than b's and is therefore not in L. This contradicts the first condition of the lemma, and we conclude that L is not regular.

In summary, the pumping lemma for regular languages is a powerful tool for proving that certain languages are not regular. It is based on the idea that regular languages have a repetitive structure that can be "pumped" to generate new strings in the language. By showing that a language does not have this property, we can prove that it is not regular.