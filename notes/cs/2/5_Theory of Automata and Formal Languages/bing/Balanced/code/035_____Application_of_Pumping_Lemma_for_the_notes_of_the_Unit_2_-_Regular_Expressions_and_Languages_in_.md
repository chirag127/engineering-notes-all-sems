### Application of Pumping Lemma

- The pumping lemma is a property of regular languages that states that any sufficiently long string in a regular language can be divided into three parts, such that the middle part can be repeated any number of times and the resulting string will still be in the language  .
- The pumping lemma can be used to prove that certain languages are not regular, by showing a contradiction. If a language is regular, it must satisfy the pumping lemma, but if it does not satisfy the pumping lemma, it is not regular  .
- The pumping lemma can be applied as follows :
  - Choose a string in the language that is longer than the pumping length, which is a constant that depends on the language.
  - Divide the string into three parts, x, y, and z, such that |xy| <= n, |y| > 0, and xy^i z is in the language for all i >= 0, where ^ denotes repetition.
  - Show that there is no way to divide the string into such parts, or that there is a value of i for which xy^i z is not in the language.
  - Conclude that the language is not regular, since it violates the pumping lemma.
- For example, consider the language L = {a^b^c | n >= 0}, which is the set of strings that have n a's followed by n b's followed by n c's .
  - Suppose L is regular, and let n be the pumping length.
  - Choose the string s = a^n b^n c^n, which is in L and has length 3n > n.
  - Divide s into x, y, and z, such that |xy| <= n, |y| > 0, and xy^i z is in L for all i >= 0.
  - Since |xy| <= n, y must consist of only a's, say y = a^k, where 0 < k <= n.
  - Then, for any i >= 0, xy^i z = a^(n-k) a^(ki) b^n c^n = a^(n+(i-1)k) b^n c^n.
  - If i = 0, then xy^i z = a^(n-k) b^n c^n, which is not in L, since n-k != n.
  - If i > 1, then xy^i z = a^(n+(i-1)k) b^n c^n, which is not in L, since n+(i-1)k != n.
  - Therefore, there is no way to divide s into x, y, and z that satisfies the pumping lemma, and L is not regular.