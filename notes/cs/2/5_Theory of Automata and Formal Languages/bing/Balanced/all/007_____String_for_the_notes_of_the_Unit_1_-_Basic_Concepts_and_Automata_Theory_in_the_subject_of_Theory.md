# String

- A string is a finite sequence of symbols from a given alphabet.
- An alphabet is a finite set of symbols, such as {0, 1}, {a, b, c, ..., z}, or {+, -, x, /, (, )}.
- A string can be denoted by enclosing its symbols in double quotes, such as "0101", "hello", or "+(x/x)".
- The length of a string is the number of symbols in it, denoted by |s| for a string s.
- The empty string is the string with no symbols, denoted by ε or λ. It has length zero, i.e., |ε| = 0.
- A string s is a substring of another string t if s occurs as a consecutive sequence of symbols in t, such as "ell" is a substring of "hello".
- A string s is a prefix of another string t if s occurs at the beginning of t, such as "he" is a prefix of "hello".
- A string s is a suffix of another string t if s occurs at the end of t, such as "lo" is a suffix of "hello".
- A string s is a subsequence of another string t if s can be obtained from t by deleting some symbols, such as "hl" is a subsequence of "hello".
- The concatenation of two strings s and t is the string obtained by appending t to the end of s, denoted by s⋅t or simply st, such as "hello"⋅"world" = "helloworld".
- The reverse of a string s is the string obtained by reversing the order of its symbols, denoted by s^R, such as "hello"^R = "olleh".
- The power of a string s to the n-th exponent, denoted by s^n, is the string obtained by concatenating n copies of s, such as "ab"^3 = "ababab". The zero-th power of any string is the empty string, i.e., s^0 = ε.
- A language is a set of strings over a given alphabet, such as {0, 1}* is the language of all binary strings, or {a^n b^n | n ≥ 0} is the language of all strings with equal numbers of a's and b's.
- A language can be specified by a set of rules, such as a grammar, a regular expression, or an automaton, which define how to generate or recognize the strings in the language.