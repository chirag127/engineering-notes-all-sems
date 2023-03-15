Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of closure properties of regular languages for the unit 2 of the subject of theory of automata and formal languages.

### Closure properties of regular languages

- Closure properties on regular languages are defined as certain operations on regular language which are guaranteed to produce regular language  .
- Closure refers to some operation on a language, resulting in a new language that is of same “type” as originally operated on i.e., regular.
- Regular languages are closed under following operations  :

  - **Union**: If K and L are regular languages, then K ∪ L is also regular. This means that if we have two regular expressions R and S whose languages are K and L respectively, then R + S is a regular expression whose language is K ∪ L.
  - **Intersection**: If K and L are regular languages, then K ∩ L is also regular. This means that if we have two regular expressions R and S whose languages are K and L respectively, then RS is a regular expression whose language is K ∩ L.
  - **Complement**: If L is a regular language, then L is also regular. This means that if we have a regular expression R whose language is L, then R is a regular expression whose language is L.
  - **Difference**: If K and L are regular languages, then K − L is also regular. This means that if we have two regular expressions R and S whose languages are K and L respectively, then R − S is a regular expression whose language is K − L.
  - **Concatenation**: If K and L are regular languages, then KL is also regular. This means that if we have two regular expressions R and S whose languages are K and L respectively, then RS is a regular expression whose language is KL.
  - **Kleene star**: If L is a regular language, then L* is also regular. This means that if we have a regular expression R whose language is L, then R* is a regular expression whose language is L*.
  - **Positive closure**: If L is a regular language, then L+ is also regular. This means that if we have a regular expression R whose language is L, then R+ is a regular expression whose language is L+.
  - **Reversal**: If L is a regular language, then LR is also regular. This means that if we have a regular expression R whose language is L, then R is a regular expression whose language is LR.

- These closure properties can be proved using any of the representations of regular languages, such as regular expressions, finite automata, or regular grammars.
- These closure properties can be used to construct new regular languages from existing ones, or to show that some languages are not regular by using the contrapositive of the closure properties.