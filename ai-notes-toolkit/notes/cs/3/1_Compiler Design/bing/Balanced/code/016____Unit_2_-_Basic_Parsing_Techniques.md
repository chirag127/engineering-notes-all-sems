## Unit 2 - Basic Parsing Techniques

- Parsing is the process of analyzing the structure and meaning of a sentence or a program based on a given grammar.
- A grammar is a set of rules that define the syntax and semantics of a language.
- A parser is a program that implements a parsing algorithm for a given grammar.
- There are two main types of parsing techniques: top-down and bottom-up.
- Top-down parsing techniques start from the root or the start symbol of the grammar and try to match the input with the leftmost derivation of the grammar.
- Bottom-up parsing techniques start from the input and try to construct the rightmost derivation of the grammar by reducing the input to the root or the start symbol.
- Some common top-down parsing techniques are recursive descent parsing, predictive parsing, and LL parsing.
- Some common bottom-up parsing techniques are shift-reduce parsing, operator-precedence parsing, and LR parsing.
- Recursive descent parsing is a top-down parsing technique that uses a set of recursive procedures, one for each non-terminal symbol of the grammar, to parse the input.
- Predictive parsing is a top-down parsing technique that uses a parsing table, which maps each pair of a non-terminal symbol and an input symbol to a production rule, to parse the input.
- LL parsing is a top-down parsing technique that uses a stack and a parsing table to parse the input. LL stands for left-to-right scan and leftmost derivation.
- Shift-reduce parsing is a bottom-up parsing technique that uses a stack and a parsing table to parse the input. The parsing table maps each pair of a stack top symbol and an input symbol to an action, which can be shift, reduce, accept, or error.
- Operator-precedence parsing is a bottom-up parsing technique that uses a stack and a precedence table to parse the input. The precedence table defines the relative precedence and associativity of the operators in the grammar.
- LR parsing is a bottom-up parsing technique that uses a stack and a parsing table to parse the input. LR stands for left-to-right scan and rightmost derivation. The parsing table maps each pair of a stack state and an input symbol to an action, which can be shift, reduce, goto, accept, or error.