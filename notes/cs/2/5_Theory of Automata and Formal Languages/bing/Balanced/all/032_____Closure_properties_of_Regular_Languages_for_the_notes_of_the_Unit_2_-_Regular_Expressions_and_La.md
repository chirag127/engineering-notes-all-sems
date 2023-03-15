# Closure properties of Regular Languages

- Closure properties on regular languages are defined as certain operations on a language, resulting in a new language that is of the same "type" as the original language, i.e., regular  .
- Regular languages are closed under the following operations  :
  - Union: If L1 and L2 are regular languages, then L1 ∪ L2 is also regular.
  - Intersection: If L1 and L2 are regular languages, then L1 ∩ L2 is also regular.
  - Complement: If L is a regular language, then L is also regular.
  - Difference: If L1 and L2 are regular languages, then L1 - L2 is also regular.
  - Concatenation: If L1 and L2 are regular languages, then L1L2 is also regular.
  - Kleene star: If L is a regular language, then L* is also regular.
  - Kleene plus: If L is a regular language, then L+ is also regular.
  - Reversal: If L is a regular language, then LR is also regular, where LR is the language obtained by reversing the strings of L.
  - Homomorphism: If L is a regular language and h is a homomorphism, then h(L) is also regular, where h(L) is the language obtained by applying h to each string of L.
  - Inverse homomorphism: If L is a regular language and h is a homomorphism, then h-1(L) is also regular, where h-1(L) is the language obtained by applying the inverse of h to each string of L.
- To prove the closure properties of regular languages, we can use any of its representations, such as regular expressions, finite automata, or regular grammars, and show that the operation on the languages can be performed using the corresponding representation.