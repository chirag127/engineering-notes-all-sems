# Regular and Non-Regular Languages

- A **regular language** is a language that can be expressed with a **regular expression** or a **finite automaton**.
- A **regular expression** is a sequence of symbols that defines a **pattern** for matching strings.
- A **finite automaton** is a mathematical model of computation that has a finite number of **states** and can change its state based on the input symbols.
- A **non-regular language** is a language that **cannot** be expressed with a regular expression or a finite automaton.
- A non-regular language may require **infinite memory** or **unbounded counting** to recognize .
- Examples of regular languages are:
  - All strings of length 2 over {a, b}* i.e. L = {aa, ab, ba, bb}
  - All strings that start and end with the same symbol over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaa, bbb, ...}
  - All strings that contain an even number of 0s over {0, 1}* i.e. L = {1, 01, 10, 11, 001, 010, 100, 101, 110, 111, ...}
- Examples of non-regular languages are:
  - All strings that have equal number of a's and b's over {a, b}* i.e. L = {ab, ba, aabb, abab, baba, bbaa, ...}
  - All strings that are palindromes over {a, b}* i.e. L = {a, b, aa, bb, aba, bab, aaaa, bbbb, abba, baab, ...}
  - All strings of the form a^n b^n over {a, b}* i.e. L = {ab, aabb, aaabbb, aaaabbbb, ...}