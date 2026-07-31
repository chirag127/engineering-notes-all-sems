### Regular and Non-Regular Languages

- A **regular language** is a language that can be expressed with a **regular expression** or a **deterministic** or **non-deterministic finite automaton** or state machine.
- A **language** is a set of strings which are made up of characters from a specified alphabet, or set of symbols.
- Regular languages are a subset of the set of all strings.
- Regular languages correspond to problems that can be solved with **finite memory**. Only need to remember one of finitely many things .
- Examples of regular languages are:
  - All strings of length = 2 over {a, b}* i.e. L = {aa, ab, ba, bb}.
  - All strings that start and end with the same symbol over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaa, bbb, ...}.
  - All strings that contain an even number of a's over {a, b}* i.e. L = {b, ab, ba, bb, aab, aba, baa, bba, ...}.
- A **non-regular language** is a language that **cannot** be expressed with a regular expression or a finite automaton .
- Non-regular languages correspond to problems that cannot be solved with finite memory. May need to remember one of infinitely many different things .
- Examples of non-regular languages are:
  - All strings that are palindromes over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaa, bbb, abba, baab, ...}.
  - All strings that have the same number of a's and b's over {a, b}* i.e. L = {ab, ba, aabb, abab, baba, bbaa, ...}.
  - All strings of the form a^n b^n over {a, b}* i.e. L = {ab, aabb, aaabbb, aaaabbbb, ...}.
- There are different methods to prove that a language is regular or non-regular, such as:
  - Using **closure properties** of regular languages, such as union, intersection, complement, concatenation, etc.
  - Using **pumping lemma** for regular languages, which states that any sufficiently long string in a regular language can be pumped, or repeated, without leaving the language.
  - Using **Myhill-Nerode theorem** for regular languages, which states that a language is regular if and only if it has a finite number of equivalence classes under a relation that preserves membership in the language.