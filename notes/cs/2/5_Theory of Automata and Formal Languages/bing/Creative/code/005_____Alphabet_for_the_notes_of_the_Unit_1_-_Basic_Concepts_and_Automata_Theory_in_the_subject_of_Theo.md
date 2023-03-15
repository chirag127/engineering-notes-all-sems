Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Alphabet for the notes of the Unit 1 - Basic Concepts and Automata Theory in the subject of Theory of Automata and Formal Languages.

### Alphabet

- An alphabet is a finite, non-empty set of symbols, usually denoted by Σ.
- The symbols in an alphabet are called letters or characters.
- Examples of alphabets are:
  - Σ = {0, 1}, the binary alphabet
  - Σ = {a, b, c, ..., z}, the lowercase English alphabet
  - Σ = {a, b}, the alphabet of a simple language
- An alphabet can be used to form strings or words by concatenating the symbols in the alphabet.
- A string over an alphabet Σ is a finite sequence of symbols from Σ.
- Examples of strings are:
  - 0101, a string over the binary alphabet
  - hello, a string over the lowercase English alphabet
  - aba, a string over the alphabet {a, b}
- The length of a string is the number of symbols in the string, denoted by |w| for a string w.
- Examples of string lengths are:
  - |0101| = 4
  - |hello| = 5
  - |aba| = 3
- The empty string is the string of length zero, denoted by ε or λ.
- The empty string is a string over any alphabet.
- The set of all strings over an alphabet Σ is denoted by Σ*.
- Examples of Σ* are:
  - {0, 1}* = {ε, 0, 1, 00, 01, 10, 11, 000, 001, ...}
  - {a, b}* = {ε, a, b, aa, ab, ba, bb, aaa, aab, ...}
  - {a, b, c}* = {ε, a, b, c, aa, ab, ac, ba, bb, bc, ca, cb, cc, ...}
- A language over an alphabet Σ is a subset of Σ*, that is, a set of strings over Σ.
- Examples of languages are:
  - L = {0, 1, 00, 11, 000, 111, ...}, a language over the binary alphabet
  - L = {a, b, ab, ba, aab, baa, aba, ...}, a language over the alphabet {a, b}
  - L = {w | w is a palindrome}, a language over any alphabet
- A language can be finite or infinite, depending on the number of strings in the language.
- Examples of finite and infinite languages are:
  - L = {0, 1, 00, 11, 000, 111, ...} is an infinite language
  - L = {a, b, ab, ba, aab, baa, aba, ...} is an infinite language
  - L = {w | w is a palindrome and |w| ≤ 3} is a finite language
- A language can be defined by a rule, a grammar, a regular expression, or an automaton. These are different ways of specifying which strings belong to the language and which do not.