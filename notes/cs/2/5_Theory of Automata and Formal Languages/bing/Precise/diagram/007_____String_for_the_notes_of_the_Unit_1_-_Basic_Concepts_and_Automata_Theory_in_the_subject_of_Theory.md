### String

A string is a finite sequence of symbols chosen from a set called an alphabet. In the context of automata theory and formal languages, the alphabet is usually a finite set of symbols, such as {0,1} or {a,b,c,...,z}.

Some important concepts related to strings are:

- **Length of a string**: The number of symbols in a string. The length of a string `w` is denoted by `|w|`.
- **Empty string**: The string of length 0, denoted by `ε`.
- **Concatenation**: The operation of joining two strings together, end-to-end. For example, if `x = ab` and `y = cd`, then the concatenation of `x` and `y` is `xy = abcd`.
- **Reversal**: The operation of reversing the order of the symbols in a string. For example, the reversal of the string `abc` is `cba`.
- **Substring**: A string `u` is a substring of a string `v` if `v` can be written as `w1uw2` for some strings `w1` and `w2`.
- **Prefix**: A string `u` is a prefix of a string `v` if `v` can be written as `uw` for some string `w`.
- **Suffix**: A string `u` is a suffix of a string `v` if `v` can be written as `wu` for some string `w`.

These concepts are fundamental to the study of automata theory and formal languages. They are used to define and analyze formal languages, which are sets of strings over an alphabet. Formal languages are used to model and study various computational problems, such as pattern matching, parsing, and the recognition of regular and context-free languages.