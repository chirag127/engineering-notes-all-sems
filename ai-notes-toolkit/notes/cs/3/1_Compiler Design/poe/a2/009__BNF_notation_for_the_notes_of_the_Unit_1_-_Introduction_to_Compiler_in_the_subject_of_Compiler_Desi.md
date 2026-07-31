 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### BNF notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design:

1. BNF or Backus–Naur Form is a metasyntax used to express context-free grammars. It is used to define the syntax of programming languages.
2. A BNF specification consists of a set of rules. Each rule defines a symbol in terms of other symbols.
3. The basic components of a BNF rule are:
    - The symbol name on the left-hand side of the rule which is being defined.
    - The colon (:) separating the symbol name from the definition.
    - The definition on the right-hand side consisting of a sequence of symbols and/or terminals.
4. Terminals: These are the actual tokens in the language. They are enclosed within double quotes ("). For example, "id", ">=", etc.
5. Non-terminals: These are syntactic variables that denote sets of strings. They are the symbols not enclosed within double quotes. For example, stmt, expr, etc.
6. Alternation or choice: This is denoted by | (the vertical bar). It means that the symbol on the left can be replaced by any one of the alternatives on the right. For example, digit = "0" | "1" | ... | "9" specifies that a digit can be any one of the ten numerals.
7. Grouping: This is denoted by enclosing the group in parentheses (()). It is used to avoid ambiguity. For example, (expr) + (expr) clarifies that the entire expression on the right is rewritten, not just the first expr.
8. Repetition: This is denoted by * (for 0 or more occurrences), + (for 1 or more occurrences), or ? (for 0 or 1 occurrences). They specify the number of occurrences of the symbol on their left. For example, digit* means that the sequence of digits can be of any length including zero.