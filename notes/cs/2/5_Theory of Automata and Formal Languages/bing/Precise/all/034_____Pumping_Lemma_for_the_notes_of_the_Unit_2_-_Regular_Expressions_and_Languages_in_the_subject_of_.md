# Pumping Lemma for Regular Languages

The Pumping Lemma for regular languages is a fundamental result in the theory of formal languages. It provides a necessary condition for a language to be regular, and can be used to prove that certain languages are not regular.

The statement of the lemma is as follows:

Let L be a regular language. Then there exists a constant n (depending on L) such that for any string w in L of length at least n, w can be written as w = xyz, where:

1. |y| > 0
2. |xy| ≤ n
3. For all i ≥ 0, xy^iz ∈ L

The constant n is called the pumping length of the language L.

The Pumping Lemma can be used to prove that a language is not regular by showing that it does not satisfy the conditions of the lemma. This is done by assuming that the language is regular, and then deriving a contradiction by showing that there exists a string w in the language that cannot be pumped.

It is important to note that the Pumping Lemma provides only a necessary condition for a language to be regular, not a sufficient one. This means that there may exist non-regular languages that satisfy the conditions of the lemma. Therefore, the Pumping Lemma can only be used to prove that a language is not regular, but not to prove that it is regular.