### Application of Pumping Lemma

- The pumping lemma is a property of regular languages that states that any sufficiently long string in a regular language can be divided into three parts, such that the middle part can be repeated any number of times and the resulting string will still be in the language.
- The pumping lemma can be used to prove that certain languages are not regular, by showing that they do not satisfy the pumping lemma property.
- The pumping lemma can also be used to find the minimum number of states in a deterministic finite automaton (DFA) that recognizes a regular language, by using the pumping length as a lower bound.
- The pumping lemma can be applied as follows:

  - Assume that the language L is regular and let n be the pumping length given by the lemma.
  - Choose a string w in L that is longer than n and divide it into three parts, w = xyz, such that |xy| <= n and |y| > 0.
  - Show that for some value of i, the string xy^iz is not in L, contradicting the pumping lemma property.
  - Conclude that L is not regular.

- For example, consider the language L = {a^nb^n | n >= 0} over the alphabet {a, b}. To prove that L is not regular, we can apply the pumping lemma as follows:

  - Assume that L is regular and let n be the pumping length.
  - Choose the string w = a^nb^n in L, where n is greater than the pumping length.
  - Divide w into three parts, w = xyz, such that |xy| <= n and |y| > 0. Since |xy| <= n, y must consist of only a's, say y = a^k, where k > 0.
  - Choose i = 2 and consider the string xy^2z = a^(n+k)b^n. This string is not in L, because it has more a's than b's, contradicting the pumping lemma property.
  - Therefore, L is not regular.