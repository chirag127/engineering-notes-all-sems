## Unit 2 - Regular Expressions and Languages

- A regular expression is a concise way of describing a set of strings that share a common pattern.
- A regular expression can be used to specify the syntax of a language, to search for patterns in a text, or to validate user input.
- A regular expression consists of symbols that represent characters, sets of characters, or operations on sets of characters.
- The basic symbols of regular expressions are:

  - **Literals**: Any character that represents itself, such as `a`, `b`, `1`, `#`, etc.
  - **Wildcards**: A special character that matches any character, such as `.` (dot).
  - **Character classes**: A set of characters enclosed in square brackets that matches any character in the set, such as `[abc]`, `[0-9]`, `[A-Z]`, etc. A character class can also be negated by using a caret (`^`) as the first character, such as `[^abc]`, which matches any character except `a`, `b`, or `c`.
  - **Quantifiers**: Symbols that specify how many times a character or a group of characters can be repeated, such as `*` (zero or more times), `+` (one or more times), `?` (zero or one time), `{n}` (exactly n times), `{n,m}` (at least n and at most m times), etc.
  - **Grouping**: Parentheses that enclose a subexpression and treat it as a single unit, such as `(ab)+`, which matches one or more repetitions of `ab`.
  - **Alternation**: A vertical bar (`|`) that separates two or more alternatives, such as `a|b`, which matches either `a` or `b`.
  - **Anchors**: Symbols that indicate the position of a match, such as `^` (beginning of a line), `$` (end of a line), `\b` (word boundary), etc.

- A regular expression can be converted into a finite automaton, which is a mathematical model of computation that consists of a finite set of states, a finite set of input symbols, a transition function that maps a state and an input symbol to a new state, a start state, and a set of final states.
- A finite automaton can be either deterministic (DFA) or nondeterministic (NFA). A DFA has exactly one transition for each state and input symbol, while an NFA can have zero, one, or more transitions for each state and input symbol. An NFA can also have epsilon transitions, which are transitions that do not consume any input symbol.
- A DFA can recognize a regular language, which is a set of strings that can be described by a regular expression. A regular language can also be defined by using closure properties, such as union, concatenation, star, complement, intersection, etc.
- An NFA can also recognize a regular language, and every NFA can be converted into an equivalent DFA using the subset construction algorithm, which constructs a new state for each subset of states of the NFA, and defines the transitions and final states accordingly.
- A regular expression can also be converted into an NFA using the Thompson's construction algorithm, which constructs a new NFA for each symbol or operation of the regular expression, and combines them using epsilon transitions.