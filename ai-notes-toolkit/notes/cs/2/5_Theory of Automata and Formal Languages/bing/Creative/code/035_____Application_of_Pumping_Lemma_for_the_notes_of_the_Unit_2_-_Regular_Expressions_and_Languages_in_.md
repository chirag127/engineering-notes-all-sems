### Application of Pumping Lemma

- The pumping lemma is a property of regular languages that states that any sufficiently long string in a regular language can be divided into three parts, such that the middle part can be repeated any number of times and the resulting string will still be in the language.
- The pumping lemma can be used to prove that certain languages are not regular, by showing a contradiction. If a language is not regular, then there must exist some string in the language that does not satisfy the pumping lemma .
- The general steps to apply the pumping lemma are as follows:
  - Assume that the language is regular and let n be the pumping length given by the lemma.
  - Choose a string w in the language that is longer than n.
  - Divide w into three parts, x, y and z, such that |xy| <= n, |y| > 0 and xy^i z is in the language for all i >= 0.
  - Find a value of i such that xy^i z is not in the language, which contradicts the pumping lemma.
  - Conclude that the language is not regular.
- For example, consider the language L = {a^b^c^ | n >= 0} over the alphabet {a, b, c}. To prove that L is not regular, we can use the pumping lemma as follows:
  - Assume that L is regular and let n be the pumping length.
  - Choose w = a^n b^n c^n, which is in L and has length 3n > n.
  - Divide w into x, y and z, such that |xy| <= n, |y| > 0 and xy^i z is in L for all i >= 0. Since |xy| <= n, y must consist of only a's, say y = a^k, where 0 < k <= n.
  - Find a value of i such that xy^i z is not in L. We can choose i = 2, which gives xy^2 z = a^(n+k) b^n c^n, which is not in L because the number of a's, b's and c's are not equal.
  - This contradicts the pumping lemma, so L is not regular.