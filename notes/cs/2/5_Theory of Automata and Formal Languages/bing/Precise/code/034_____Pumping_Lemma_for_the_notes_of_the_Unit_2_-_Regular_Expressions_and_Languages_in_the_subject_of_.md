### Pumping Lemma for Regular Languages

The Pumping Lemma for regular languages is a fundamental concept in the theory of formal languages. It is a property that all regular languages share and can be used to prove that certain languages are not regular.

The lemma states that for any regular language L, there exists a constant p (called the pumping length) such that any string s in L of length at least p can be divided into three substrings, s = xyz, satisfying the following conditions:

1. For every i ≥ 0, xy^iz ∈ L.
2. |y| > 0.
3. |xy| ≤ p.

The first condition means that we can "pump" the middle substring y any number of times, and the resulting string will still be in the language. The second condition ensures that the substring y is non-empty, and the third condition ensures that the substring y is within the first p characters of the string s.

The Pumping Lemma can be used to prove that certain languages are not regular by showing that no such division of a string in the language is possible. This is done by assuming that the language is regular, and then deriving a contradiction using the conditions of the lemma.

It is important to note that the Pumping Lemma is a necessary but not sufficient condition for a language to be regular. That is, if a language satisfies the conditions of the lemma, it does not necessarily mean that the language is regular. However, if a language does not satisfy the conditions of the lemma, it is guaranteed to be non-regular.