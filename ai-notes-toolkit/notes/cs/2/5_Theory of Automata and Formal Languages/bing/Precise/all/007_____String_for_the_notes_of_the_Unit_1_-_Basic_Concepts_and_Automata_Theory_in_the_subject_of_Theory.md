# Unit 1 - Basic Concepts and Automata Theory

## String

- A string is a finite sequence of symbols taken from a finite set called an alphabet.
- The length of a string is the number of symbols in the sequence.
- The empty string is the unique string of length 0, denoted by ε or λ.
- The set of all strings over an alphabet Σ is denoted by Σ*.
- The concatenation of two strings x and y is the string obtained by appending y to x, denoted by xy.
- The reverse of a string x is the string obtained by writing the symbols of x in reverse order, denoted by x^R.
- A string x is a prefix of a string y if there exists a string z such that y = xz.
- A string x is a suffix of a string y if there exists a string z such that y = zx.
- A string x is a substring of a string y if there exist strings u and v such that y = uxv.
- A string x is a subsequence of a string y if x can be obtained from y by deleting zero or more symbols.
- The set of all substrings of a string x is denoted by Sub(x).
- The set of all subsequences of a string x is denoted by Subseq(x).
- A language is a set of strings over an alphabet.
- The concatenation of two languages L and M is the language LM = {xy | x ∈ L and y ∈ M}.
- The Kleene closure of a language L is the language L* = {x1x2...xn | n ≥ 0 and xi ∈ L for all i}.
- The positive closure of a language L is the language L+ = {x1x2...xn | n ≥ 1 and xi ∈ L for all i}.