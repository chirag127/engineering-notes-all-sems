### Pumping Lemma for CFL

The Pumping Lemma for Context-Free Languages (CFL) is a property of context-free languages that is used to prove that certain languages are not context-free. It states that for any context-free language L, there exists a constant n (depending on L) such that for any string w in L of length at least n, w can be written as w = xyz, where:

1. |xy| ≤ n
2. |y| ≥ 1
3. For all i ≥ 0, xy^iz ∈ L

The constant n is called the pumping length of the language L. The lemma can be used to prove that a language is not context-free by showing that no such decomposition of a string w in the language exists, or that the condition 3 is not satisfied for some i.

This lemma is useful in the study of Push Down Automata and Properties of Context Free Languages, which is a topic in the subject of Theory of Automata and Formal Languages. It is an important concept to understand for students preparing for exams in this subject.