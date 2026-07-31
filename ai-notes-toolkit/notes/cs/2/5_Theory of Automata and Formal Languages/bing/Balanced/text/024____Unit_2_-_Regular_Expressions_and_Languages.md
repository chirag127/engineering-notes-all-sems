## Unit 2 - Regular Expressions and Languages

- A **regular expression** is a concise way of describing a set of strings, using symbols and operators.
- A **regular language** is a set of strings that can be described by a regular expression, or equivalently, by a finite automaton.
- Regular expressions and languages are useful for specifying patterns of text, such as identifiers, keywords, or email addresses.
- Some basic symbols and operators for regular expressions are:

  - **∅**: the empty set, denoting no strings.
  - **ε**: the empty string, denoting a string of length zero.
  - **a**: a single character, denoting a string of length one.
  - **R₁ + R₂**: the union of two regular expressions, denoting the set of strings that belong to either R₁ or R₂.
  - **R₁R₂**: the concatenation of two regular expressions, denoting the set of strings that are formed by appending a string from R₁ to a string from R₂.
  - **R***: the Kleene star of a regular expression, denoting the set of strings that are formed by repeating a string from R zero or more times.
  - **(R)**: the parentheses, used to group regular expressions and override the precedence of operators.

- Some examples of regular expressions and the languages they describe are:

  - **a***: the set of strings that consist of zero or more a's, such as ε, a, aa, aaa, etc.
  - **a + b***: the set of strings that start with an a and end with zero or more b's, such as a, ab, abb, abbb, etc.
  - **(a + b)***: the set of strings that consist of zero or more a's or b's, such as ε, a, b, ab, ba, aa, bb, aba, bab, etc.
  - **a(b + c)***: the set of strings that start with an a and end with zero or more b's or c's, such as a, ab, ac, abb, abc, acc, etc.
  - **(a + b)(c + d)***: the set of strings that consist of an a or a b followed by a c or a d, such as ac, ad, bc, bd.