Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of context free grammar (CFG) for the notes of the unit 3 - regular and non-regular grammars in the subject of theory of automata and formal languages.

### Context Free Grammar (CFG)

- A context free grammar (CFG) is a set of rules that defines a language by specifying how any valid string can be derived from a special symbol called the start symbol.
- A CFG consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- Terminal symbols are the basic symbols that appear in the strings of the language. They cannot be further divided or replaced by any rules. For example, in the language of arithmetic expressions, the terminal symbols are digits, operators, and parentheses.
- Non-terminal symbols are placeholders that can be replaced by sequences of terminal and/or non-terminal symbols according to the production rules. They are usually denoted by uppercase letters. For example, in the language of arithmetic expressions, the non-terminal symbols are E (expression), T (term), and F (factor).
- The start symbol is a special non-terminal symbol that represents the whole language. It is usually denoted by S. The production rules define how the start symbol can be rewritten as a sequence of terminal and/or non-terminal symbols, and how the non-terminal symbols can be further rewritten until only terminal symbols remain. For example, in the language of arithmetic expressions, the production rules are:

  - S -> E
  - E -> E + T | E - T | T
  - T -> T * F | T / F | F
  - F -> (E) | digit

- A string is said to belong to the language defined by a CFG if it can be derived from the start symbol by applying the production rules repeatedly. For example, the string (2+3)*4 belongs to the language of arithmetic expressions because it can be derived as follows:

  - S -> E (by the rule S -> E)
  - E -> T (by the rule E -> T)
  - T -> T * F (by the rule T -> T * F)
  - T -> F * F (by the rule T -> F)
  - F -> (E) * F (by the rule F -> (E))
  - E -> E + T (by the rule E -> E + T)
  - E -> T + T (by the rule E -> T)
  - T -> F + F (by the rule T -> F)
  - F -> digit + F (by the rule F -> digit)
  - F -> 2 + F (by the rule digit -> 2)
  - F -> 2 + digit (by the rule F -> digit)
  - F -> 2 + 3 (by the rule digit -> 3)
  - F -> (2 + 3) * F (by the rule F -> (E))
  - F -> (2 + 3) * digit (by the rule F -> digit)
  - F -> (2 + 3) * 4 (by the rule digit -> 4)

- A CFG can be represented by a diagram called a parse tree, which shows the hierarchical structure of the derivation. The root of the tree is the start symbol, the leaves are the terminal symbols, and the internal nodes are the non-terminal symbols. The edges are labeled by the production rules. For example, the parse tree for the string (2+3)*4 is:

![Parse tree for (2+3)*4](https://i.imgur.com/6s0y6sO.png)

- A CFG is said to be ambiguous if there is more than one way to derive the same string from the start symbol, or equivalently, if there is more than one parse tree for the same string. For example, the string 2+3*4 is ambiguous in the language of arithmetic expressions because it can be derived in two different ways:

  - S -> E -> E + T -> T + T -> F + T -> digit + T -> 2 + T -> 2 + T * F -> 2 + F * F -> 2 + digit * F -> 2 + 3 * F -> 2 + 3 * digit -> 2 + 3 * 4
  - S -> E -> T -> T + F -> T * F + F -> F * F + F -> digit * F + F -> 2 * F + F -> 2 * digit + F -> 2 * 3 + F -> 2 * 3