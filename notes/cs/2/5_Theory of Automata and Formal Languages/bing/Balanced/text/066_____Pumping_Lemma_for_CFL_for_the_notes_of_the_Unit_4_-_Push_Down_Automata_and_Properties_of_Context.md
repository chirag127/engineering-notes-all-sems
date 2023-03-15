### Pumping Lemma for CFL

- The pumping lemma for context-free languages (CFL) is a tool to prove that a given language is not context-free.
- The idea is to assume that the language is context-free and derive a contradiction by showing that there exists a string in the language that cannot be pumped, i.e., repeated in a certain way, without leaving the language.
- The pumping lemma for CFLs states that if L is a context-free language, then there exists a constant n (called the pumping length) such that for any string w in L of length at least n, there exist strings u, v, x, y, and z such that:

  - w = uvxyz
  - |vxy| ≤ n
  - |vy| ≥ 1
  - uv<sup>i</sup>xy<sup>i</sup>z is in L for all i ≥ 0

- The intuition behind the pumping lemma is that any sufficiently long string in a CFL must have been derived by applying some production rule more than once, creating a loop in the derivation tree. This loop can be repeated or skipped, resulting in a different string that is still in the language.
- To use the pumping lemma to prove that a language is not context-free, we need to follow these steps:

  - Assume that the language is context-free and let n be the pumping length.
  - Choose a string w in the language that has length at least n. The choice of w may depend on n.
  - Show that for any possible decomposition of w into u, v, x, y, and z, there exists an i such that uv<sup>i</sup>xy<sup>i</sup>z is not in the language. This can be done by considering different cases based on the positions and lengths of v and y, and using some properties of the language to derive a contradiction.
  - Conclude that the language is not context-free by contradiction.