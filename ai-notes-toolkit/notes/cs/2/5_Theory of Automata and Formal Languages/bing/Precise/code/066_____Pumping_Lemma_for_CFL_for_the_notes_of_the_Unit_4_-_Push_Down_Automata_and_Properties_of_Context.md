### Pumping Lemma for CFL

The Pumping Lemma for Context-Free Languages (CFL) is a property that is used to prove that certain languages are not context-free. It states that for any context-free language L, there exists a constant n (which depends on L) such that for any string w in L of length at least n, w can be written as w = xyz such that:

1. |xy| ≤ n
2. |y| ≥ 1
3. For all i ≥ 0, xy^iz ∈ L

The constant n is called the pumping length of the language L. The idea behind the pumping lemma is that any sufficiently long string in a context-free language can be "pumped" by repeating a certain substring any number of times, and the resulting string will still be in the language.

The pumping lemma is often used to prove that a language is not context-free by showing that it does not satisfy the conditions of the lemma. This is done by assuming that the language is context-free, and then deriving a contradiction by showing that there exists a string in the language that cannot be pumped.

It is important to note that the pumping lemma is a necessary but not sufficient condition for a language to be context-free. That is, if a language satisfies the conditions of the pumping lemma, it does not necessarily mean that the language is context-free. However, if a language does not satisfy the conditions of the pumping lemma, it is guaranteed to not be context-free.