### Application of Pumping Lemma for the notes of the Unit 2 - Regular Expressions and Languages in the subject of Theory of Automata and Formal Languages

In the study of regular languages, the Pumping Lemma is a crucial tool for proving that a language is not regular. In this section, we will explore the application of the Pumping Lemma in detail.

#### What is the Pumping Lemma?

The Pumping Lemma is a technique used to prove that a language is not regular. It states that if a language L is regular, then there exists a constant n such that any string w in L with |w| ≥ n can be divided into three parts: w = xyz, where |y| > 0, |xy| ≤ n, and for all i ≥ 0, the string xy^iz is also in L.

#### How to apply the Pumping Lemma?

To apply the Pumping Lemma, follow these steps:

1. Assume that L is a regular language.
2. Choose a pumping length n for L.
3. Choose a string w in L such that |w| ≥ n.
4. Divide w into three parts: w = xyz, where |y| > 0, |xy| ≤ n.
5. Show that for all i ≥ 0, the string xy^iz is also in L.
6. If step 5 cannot be shown, then L is not a regular language.

#### Examples of applying the Pumping Lemma

Let's look at some examples of applying the Pumping Lemma to prove that a language is not regular:

1. L = {0^n1^n | n ≥ 0} (the language of all strings of 0's followed by an equal number of 1's)

Assume that L is a regular language. Choose a pumping length n for L. Choose the string w = 0^n1^n in L. Divide w into three parts: x = ε, y = 0, z = 0^n1^(n-1). Now, consider xy^2z = 0^1 0^(n-1) 1^n which is not in L since the number of 0's is not equal to the number of 1's. Thus, L is not a regular language.

2. L = {ww | w is a string over {0, 1}*}

Assume that L is a regular language. Choose a pumping length n for L. Choose the string w = 0^n1^n0^n1^n in L. Divide w into three parts: x = 0^a, y = 0^b1^n0^c, z = 1^n0^n1^n where a+b+c=n. Now, consider xy^2z = 0^(a+b) 1^n 0^(c+b) 1^n which is not in L since the first half of the string is not equal to the second half. Thus, L is not a regular language.

#### Conclusion

The Pumping Lemma is a powerful tool for proving that a language is not regular. By assuming that a language is regular and showing that it fails to satisfy the conditions of the Pumping Lemma, we can conclude that the language is not regular. It is an important concept to understand in the study of regular languages and automata theory.