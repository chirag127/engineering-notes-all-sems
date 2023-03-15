### Closure properties of Regular Languages

- Closure properties on regular languages are defined as certain operations on a language, resulting in a new language that is of the same type as the original language, i.e., regular  .
- Regular languages are closed under the following operations  :
  - Union: If K and L are regular languages, then K ∪ L is also regular.
  - Intersection: If K and L are regular languages, then K ∩ L is also regular.
  - Complement: If L is a regular language, then L is also regular.
  - Difference: If K and L are regular languages, then K − L is also regular.
  - Concatenation: If K and L are regular languages, then KL is also regular.
  - Kleene star: If L is a regular language, then L* is also regular.
  - Kleene plus: If L is a regular language, then L+ is also regular.
  - Reversal: If L is a regular language, then LR is also regular, where LR is the language of all strings that are the reverse of some string in L.
  - Homomorphism: If L is a regular language and h is a homomorphism, then h(L) is also regular, where h(L) is the language of all strings that are the image of some string in L under h.
  - Inverse homomorphism: If L is a regular language and h is a homomorphism, then h-1(L) is also regular, where h-1(L) is the language of all strings that are the pre-image of some string in L under h.
- To prove that regular languages are closed under these operations, we can use any of its representations, such as regular expressions, finite automata, or regular grammars, and show that the operation can be performed on them in such a way that the result is also a regular expression, a finite automaton, or a regular grammar, respectively.