# Closure properties of Regular Languages

- Closure properties on regular languages are defined as certain operations on a language which are guaranteed to produce a regular language  .
- Closure refers to some operation on a language, resulting in a new language that is of same “type” as originally operated on i.e., regular.
- Regular languages are closed under following operations  :
  - Union: If L1 and L2 are regular languages, then L1 ∪ L2 is also a regular language.
  - Intersection: If L1 and L2 are regular languages, then L1 ∩ L2 is also a regular language.
  - Complement: If L is a regular language, then L is also a regular language.
  - Difference: If L1 and L2 are regular languages, then L1 - L2 is also a regular language.
  - Concatenation: If L1 and L2 are regular languages, then L1L2 is also a regular language.
  - Kleene star: If L is a regular language, then L* is also a regular language.
  - Kleene plus: If L is a regular language, then L+ is also a regular language.
  - Reversal: If L is a regular language, then LR is also a regular language, where LR is the language obtained by reversing the strings of L.
  - Homomorphism: If L is a regular language and h is a homomorphism, then h(L) is also a regular language.
  - Inverse homomorphism: If L is a regular language and h is a homomorphism, then h-1(L) is also a regular language.
  - Substitution: If L is a regular language and σ is a substitution, then σ(L) is also a regular language.
  - Prefix: If L is a regular language, then Pref(L) is also a regular language, where Pref(L) is the language of all prefixes of the strings of L.
  - Suffix: If L is a regular language, then Suff(L) is also a regular language, where Suff(L) is the language of all suffixes of the strings of L.
  - Substring: If L is a regular language, then Sub(L) is also a regular language, where Sub(L) is the language of all substrings of the strings of L.