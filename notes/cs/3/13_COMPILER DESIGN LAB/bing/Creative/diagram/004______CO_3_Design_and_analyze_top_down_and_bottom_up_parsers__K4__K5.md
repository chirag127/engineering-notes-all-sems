#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

- Top down and bottom up parsers are two types of parsing techniques that are used to construct the parse tree of a given input string based on the rules of grammar.
- A parse tree is a graphical representation of the syntactic structure of a sentence, where each node corresponds to a grammar symbol and each branch corresponds to a derivation step.
- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols of the language can be combined to form valid sentences.
- A parser is a program that takes an input string and checks if it belongs to the language defined by the grammar, and if so, produces the corresponding parse tree.

- Top down parsing is a parsing technique that starts from the root of the parse tree and works down to the leaves by using the rules of grammar in a forward direction.
- A top down parser tries to match the input string with the leftmost symbol of the start production, and then expands it recursively until it reaches the terminals or fails.
- A top down parser can be classified into two types: recursive descent parser and predictive parser.
- A recursive descent parser is a top down parser that uses a set of recursive procedures, one for each non-terminal, to parse the input string.
- A predictive parser is a top down parser that uses a parsing table, which is constructed from the grammar using the First and Follow sets, to determine which production to apply at each step.
- A top down parser can handle left factored grammars, i.e., grammars that do not have common prefixes in the right hand side of any production.
- A top down parser cannot handle left recursive grammars, i.e., grammars that have a production of the form A -> Aα, where A is a non-terminal and α is a string of symbols, because it will cause infinite recursion.

- Bottom up parsing is a parsing technique that starts from the leaves of the parse tree and works up to the root by using the rules of grammar in a reverse direction.
- A bottom up parser tries to reduce the input string to the start symbol by applying the productions in a backward order, i.e., replacing the right hand side of a production with the left hand side.
- A bottom up parser can be classified into two types: shift reduce parser and LR parser.
- A shift reduce parser is a bottom up parser that uses a stack and an input buffer to parse the input string. It performs two operations: shift and reduce.
- A shift operation moves the next input symbol from the input buffer to the top of the stack.
- A reduce operation applies a production to the topmost symbols on the stack that match the right hand side of the production, and replaces them with the left hand side of the production.
- A shift reduce parser uses a parsing table, which is constructed from the grammar using the First and Follow sets, to decide which operation to perform at each step.
- A shift reduce parser can handle any grammar that is free from ambiguity, i.e., grammars that have only one parse tree for each valid input string.
- A shift reduce parser cannot handle grammars that have shift reduce conflicts or reduce reduce conflicts, i.e., situations where the parser cannot decide which operation to perform based on the parsing table.
- An LR parser is a bottom up parser that is a special type of shift reduce parser that can handle a large class of grammars, including all deterministic context free grammars, i.e., grammars that have only one valid derivation for each valid input string.
- An LR parser uses a more sophisticated parsing table, which is constructed from the grammar using the canonical collection of LR(0) items, to decide which operation to perform at each step.
- An LR parser can handle grammars that have shift reduce conflicts, but not reduce reduce conflicts.
- An LR parser can be further classified into four types: LR(0) parser, SLR(1) parser, LR(1) parser and LALR(1) parser, depending on the amount of lookahead information used to resolve conflicts.