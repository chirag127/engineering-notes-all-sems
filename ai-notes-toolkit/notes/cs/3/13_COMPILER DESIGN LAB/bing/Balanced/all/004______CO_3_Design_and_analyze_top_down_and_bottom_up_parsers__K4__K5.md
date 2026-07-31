#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

- Top down and bottom up parsers are two types of parsers that are used to construct parse trees from a given input string and a grammar.
- A parse tree is a graphical representation of the syntactic structure of a sentence according to a grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how words and symbols can be combined to form valid sentences.
- A parser is a program that takes an input string and a grammar as input and outputs a parse tree or an error message if the input string is not syntactically correct.

- Top down parsing
  - Top down parsing is a parsing technique that starts from the root of the parse tree and works down to the leaves by using the rules of the grammar.
  - Top down parsing is based on leftmost derivation, i.e., it expands the leftmost non-terminal symbol in each step until it reaches the input string.
  - Top down parsing can be implemented by two methods: recursive descent parsing and predictive parsing.
  - Recursive descent parsing is a method that uses a set of recursive procedures, one for each non-terminal symbol, to parse the input string. Each procedure tries to match the input string with the right hand side of the corresponding production rule. If it succeeds, it advances the input pointer and calls the procedures for the next symbols. If it fails, it backtracks and tries another alternative.
  - Predictive parsing is a method that uses a data structure called a parsing table to guide the parsing process. A parsing table is a two-dimensional array that maps each pair of a non-terminal symbol and an input symbol to a production rule or an error. A predictive parser uses a stack to store the symbols that need to be expanded and a pointer to scan the input string. It consults the parsing table to determine which production rule to apply or whether to report an error.
  - Advantages of top down parsing
    - It is easy to implement and understand.
    - It can handle left factored grammars, i.e., grammars that do not have common prefixes in the right hand sides of the production rules.
    - It can detect syntax errors early in the parsing process.
  - Disadvantages of top down parsing
    - It cannot handle left recursive grammars, i.e., grammars that have production rules of the form A -> Aα, where A is a non-terminal symbol and α is a string of symbols. Left recursive grammars cause infinite recursion in recursive descent parsing and parsing table entries in predictive parsing.
    - It may perform unnecessary backtracking, which is inefficient and time-consuming.

- Bottom up parsing
  - Bottom up parsing is a parsing technique that starts from the leaves of the parse tree and works up to the root by using the rules of the grammar.
  - Bottom up parsing is based on reverse rightmost derivation, i.e., it reduces the input string to the start symbol by applying the production rules in reverse order.
  - Bottom up parsing can be implemented by two methods: shift-reduce parsing and operator-precedence parsing.
  - Shift-reduce parsing is a method that uses a stack to store the symbols that have been processed and a pointer to scan the input string. It performs two operations: shift and reduce. A shift operation moves the input pointer to the next symbol and pushes it onto the stack. A reduce operation pops a string of symbols from the stack that matches the right hand side of a production rule and pushes the corresponding left hand side symbol onto the stack. The parsing process ends when the input string is exhausted and the stack contains only the start symbol.
  - Operator-precedence parsing is a method that uses a data structure called a precedence table to guide the parsing process. A precedence table is a two-dimensional array that maps each pair of symbols to a precedence relation: less than, equal to, greater than, or error. A precedence relation indicates the order of evaluation of the symbols. An operator-precedence parser uses a stack to store the symbols that have been processed and a pointer to scan the input string. It compares the top symbol of the stack and the current input symbol using the precedence table and performs one of the following actions: shift, reduce, accept, or error. A shift action moves the input pointer to the next symbol and pushes it onto the stack. A reduce action pops a string of symbols from the stack that forms an operand-operator-operand pattern and pushes the result of the operation onto the stack. An accept action indicates that the input string is successfully parsed. An error action indicates that the