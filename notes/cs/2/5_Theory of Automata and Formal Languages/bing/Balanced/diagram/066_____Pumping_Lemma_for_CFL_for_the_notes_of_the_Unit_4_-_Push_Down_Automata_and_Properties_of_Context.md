### Pumping Lemma for CFL

- The pumping lemma for context-free languages (CFLs) is a tool to prove that a given language is not context-free.
- The idea is to assume that the language is context-free and derive a contradiction by showing that there exists a string in the language that cannot be pumped, i.e., repeated in a certain way, without leaving the language.
- The pumping lemma for CFLs states that if L is a context-free language, then there exists a constant n (called the pumping length) such that for any string w in L of length at least n, there exist strings u, v, x, y, and z such that:

  - w = uvxyz
  - |vxy| ≤ n
  - |vy| ≥ 1
  - uv<sup>i</sup>xy<sup>i</sup>z is in L for all i ≥ 0

- The intuition behind the pumping lemma is that any sufficiently long string in a CFL must have been derived by applying some production rule more than once, creating a loop in the derivation tree. This loop can be repeated or skipped, resulting in a pumped string that is still in the language.
- To use the pumping lemma to prove that a language is not context-free, we need to do the following steps:

  - Assume that the language is context-free and let n be the pumping length.
  - Choose a string w in the language that has length at least n and satisfies some additional property that makes it hard to pump.
  - Show that for any possible way of splitting w into u, v, x, y, and z, pumping v and y will either change the length of w, violate the property of w, or produce a string that is not in the language.
  - Conclude that the pumping lemma does not hold for w, and therefore the language is not context-free.

- For example, let us prove that the language L = {a<sup>n</sup>b<sup>n</sup>c<sup>n</sup> | n ≥ 1} is not context-free using the pumping lemma.

  - Assume that L is context-free and let n be the pumping length.
  - Choose w = a<sup>n</sup>b<sup>n</sup>c<sup>n</sup>, which is in L and has length 3n ≥ n. The property of w is that it has equal numbers of a's, b's, and c's.
  - Consider any possible way of splitting w into u, v, x, y, and z, such that |vxy| ≤ n and |vy| ≥ 1. There are three cases:

    - Case 1: vxy contains only one type of symbol, say a. Then pumping v and y will increase the number of a's in w, but not the number of b's or c's, resulting in a string that is not in L.
    - Case 2: vxy contains two types of symbols, say a and b. Then pumping v and y will either change the order of the symbols in w, or increase the number of a's and b's, but not the number of c's, resulting in a string that is not in L.
    - Case 3: vxy contains three types of symbols, say a, b, and c. Then pumping v and y will either change the order of the symbols in w, or increase the number of a's, b's, and c's, but not by the same amount, resulting in a string that is not in L.

  - In all cases, pumping v and y will produce a string that is not in L, contradicting the pumping lemma.
  - Therefore, L is not context-free.