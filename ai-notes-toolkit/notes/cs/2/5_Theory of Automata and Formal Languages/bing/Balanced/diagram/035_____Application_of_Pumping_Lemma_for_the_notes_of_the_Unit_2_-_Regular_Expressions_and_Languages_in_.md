### Application of Pumping Lemma

- The pumping lemma is a property of regular languages that states that any sufficiently long string in a regular language can be divided into three parts, such that the middle part can be repeated any number of times and the resulting string will still be in the language.
- The pumping lemma can be used to prove that certain languages are not regular, by showing that they do not satisfy the pumping lemma property.
- The pumping lemma can also be used to find the minimum number of states in a deterministic finite automaton (DFA) that recognizes a regular language, by finding the maximum length of a string that cannot be pumped.
- The pumping lemma can be formally stated as follows:

  - Let L be a regular language. Then there exists a positive integer n (called the pumping length) such that for any string w in L with |w| >= n, there exist strings x, y and z such that w = xyz, |xy| <= n, |y| > 0 and for all k >= 0, xy^kz is in L.

- The pumping lemma can be applied to show that a language is not regular by following these steps:

  - Assume that the language is regular and let n be the pumping length.
  - Choose a string w in the language with length at least n.
  - Divide w into x, y and z according to the pumping lemma conditions.
  - Show that for some k >= 0, xy^kz is not in the language, contradicting the pumping lemma.
  - Conclude that the language is not regular.

- For example, consider the language L = {a^nb^n | n >= 0} over the alphabet {a, b}. We can show that L is not regular by applying the pumping lemma as follows:

  - Assume that L is regular and let n be the pumping length.
  - Choose w = a^nb^n, which is in L and has length 2n >= n.
  - Divide w into x, y and z such that w = xyz, |xy| <= n, |y| > 0. Since |xy| <= n, xy must consist of only a's. Let x = a^i, y = a^j and z = a^(n-i-j)b^n, where i, j > 0 and i + j <= n.
  - Choose k = 2 and consider xy^2z = a^i(a^j)^2a^(n-i-j)b^n = a^(n+j)b^n. This string is not in L, because the number of a's and b's are not equal, contradicting the pumping lemma.
  - Conclude that L is not regular.